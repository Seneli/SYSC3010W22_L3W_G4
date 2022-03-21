package project_files;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class ElevatorSubsystem extends Thread{

	ArrayList<Integer> stops = new ArrayList<Integer>();
	ArrayList<Integer> postStops = new ArrayList<Integer>();
	
	private int portNum;
	private int schedPort = 126;
	
	DatagramPacket receivePacket, reqPacket;
	DatagramSocket receiveReplySocket;
	Elevator elev;
	
	private int floorNum = 0;
	private int direction = 2;

	public ElevatorSubsystem(int portNum){
		
		this.portNum = portNum;
		try {
			this.receiveReplySocket = new DatagramSocket(this.portNum); //Instantiate DatagramSocket
		} catch (SocketException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		elev = new Elevator();
		elev.subscribe(this);
	}
	
	public int getPortNum() {
		return portNum;
	}
	
	public void receiveAndProcess() {
		
		byte data[] = new byte[100];
		while(true) {
			
			//Wait for scheduler info request
	        byte[] reqMsg = {0};
	        reqPacket = new DatagramPacket(reqMsg,reqMsg.length);
	        
	        try {
				receiveReplySocket.receive(reqPacket);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	        
	        
	        //Make packet and sent to scheduler
	        ByteArrayOutputStream bos = new ByteArrayOutputStream();
	        int retPort = reqPacket.getPort();

	        bos.write(floorNum);
	        bos.write((int) direction);
	        
	        reqMsg = bos.toByteArray();
	        
	        try {
				reqPacket = new DatagramPacket(reqMsg,reqMsg.length,InetAddress.getLocalHost(), schedPort);
			} catch (UnknownHostException e2) {
				// TODO Auto-generated catch block
				e2.printStackTrace();
			}
	        
	        try {
				receiveReplySocket.send(reqPacket);
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}

	        
	        data = new byte[4];
			receivePacket = new DatagramPacket(data, data.length); //Create receive packet
			
			System.out.println("Elev_Sub: Waiting for packet...");
			
			//Receiving datagramPacket from Scheduler
			try {
				receiveReplySocket.receive(receivePacket);
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			byte[] cancelCode = {8,8,8,8};
			
			if (receivePacket.getData().equals(cancelCode)) {
				continue;
			}

			System.out.println("Elev_Sub: Received Packet From Scheduler (" + receivePacket.getAddress() + ")");
			
	        System.out.println("Elev_Sub: Scheduler at port " + receivePacket.getPort());
	        int len = receivePacket.getLength();
	        System.out.println("Elev_Sub: Length of " + len);
	        System.out.print("Elev_Sub: Containing Bytes [");
	        for (byte b: receivePacket.getData()){
	            System.out.print(b);
	        }
	        System.out.print("]\n");
	        
	        byte[] recData = new byte[len];
	        
	        for (int i = 0; i < len; i++) {
	        	recData[i] = receivePacket.getData()[i];
	        }

	        int requestFloor = recData[0];
	        int destination = recData[1];
	        
	        addStops(requestFloor);
	        addStops(destination);
	        
	        moveTo(stops.get(0));
		}
	}
	
	
	public void addStops(int i) {

		if(direction == 2 && stops.isEmpty()) {
			stops.add(i);
			if (stops.get(0) > floorNum) {
				direction = 1;
			} else if (stops.get(0) < floorNum) {
				direction = 0;
			}
		}else if (stops.isEmpty() && !postStops.isEmpty()) {
			stops.add(i);
			if (stops.get(0) > floorNum) {
				direction = 1;
			} else if (stops.get(0) < floorNum) {
				direction = 0;
			}
		}
		
		else if (direction == 1 && i > stops.get(0)) {
			stops.add(i);
			Collections.sort(stops);
			
		}else if(direction == 0 && i < stops.get(0)) {
			stops.add(i);
			Collections.sort(stops, Collections.reverseOrder());
			
		}else if(direction == 1 && i < stops.get(0)) {
			postStops.add(i);
			Collections.sort(postStops, Collections.reverseOrder());
			
		}else if(direction == 0 && i > stops.get(0)) {
			postStops.add(i);
			Collections.sort(postStops);
			
		}else if (stops.get(0) == i) {
			//Do nothing
		}
		
	}
	
	public void moveTo(int destinationFloor) { 

		System.out.println("Elevator Subsystem: moving elevator to floor " + destinationFloor);

		int timeDelay = calculateTimeBetweenFloors(floorNum, destinationFloor); 
		
		System.out.println("Elevator Subsystem: It will take approximately " + (timeDelay/1000) + " seconds for the elevator to arrive");
		
		elev.Move(destinationFloor ,direction, timeDelay); //Send data to Elevator;
		
		elev.doors();
		
		floorNum = destinationFloor;
		
		System.out.println("Elevator Subsystem: Elevator Arrived at floor " + floorNum);
		System.out.println("STOPS: " + stops.toString());
		System.out.println("POSTSTOPS: " +postStops.toString());
		if (!stops.isEmpty()) {
			stops.remove(0);
		}
		receiveAndProcess();
		if (!stops.isEmpty()) {
			receiveAndProcess();
		}else if(stops.isEmpty() && !postStops.isEmpty()) {
			if (direction == 1) {
				direction = 0;
			}else {
				direction = 1;
			}
			stops = postStops;
			postStops = new ArrayList<Integer>();
			receiveAndProcess();
			}else if (postStops.isEmpty()) {
				direction = 2;
				System.out.println("Elevator Subsystem: Elevator stopped at floor " + floorNum);
				receiveAndProcess();
			}
		}
	
	public int calculateTimeBetweenFloors(int currentFloor, int destinationFloor) {
		double time = 0; 
		int timeToMoveOneFloor = 12000;
		int timeToStartandGo = 18000;
		int timeToClearFloorAtVelocity = 9000;
		
		int differenceBetweenFloors = Math.abs(destinationFloor-currentFloor); 
		
		if (differenceBetweenFloors < 1) {
			time = 0;
		}
		else if (differenceBetweenFloors == 1) { 
			time = timeToMoveOneFloor;  //in milliseconds
		}
		else if (differenceBetweenFloors == 2) {
			time = timeToStartandGo; 
		} 
		else { 
			time = timeToStartandGo + timeToClearFloorAtVelocity * (differenceBetweenFloors - 2); 
		}
		return (int) time ; 
	}
	
	public static void main(String args[]) {
		
		ElevatorSubsystem es1 = new ElevatorSubsystem(12);
		//ElevatorSubsystem es2 = new ElevatorSubsystem(13);
		//ElevatorSubsystem es3 = new ElevatorSubsystem(14);
		es1.receiveAndProcess();
		//es2.receiveAndProcess();
		//es3.receiveAndProcess();

	}
}

