#! /usr/bin/python3
import time,board,busio
import numpy as np
import adafruit_mlx90640
from scipy import ndimage

class ThermalCam:
    
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
        self.mlx = adafruit_mlx90640.MLX90640(self.i2c) # begin MLX90640 with I2C comm
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate
        self.mlx_shape = (24,32) # mlx90640 shape
        self.frame = np.zeros(self.mlx_shape[0]*self.mlx_shape[1]) # 768 pts
        
    def get_temp(self):
        print("Getting temp from frame")
        self.mlx.getFrame(self.frame) # read mlx90640
        
        highest = -200
        for i in self.frame:
            if(i > highest):
                highest = i
        
        return highest
            
    def get_avg_temp(self):
        wait = 0
        highest_temp =[]
        while (wait < 11):
            try:
                highest_temp.append(self.get_temp())
            except:
                continue
            time.sleep(1)
            wait += 1
        print("getting avg")
        list_sum = sum(highest_temp)
        avg = list_sum/(len(highest_temp))
        print("Average of highest temperature: ", avg) #get the average of all the higest temp of each update
        if (avg > 38):
            print("Higher than norm for fever")
        else:
            print("Lower than norm for fever")
        return round(avg, 2)
