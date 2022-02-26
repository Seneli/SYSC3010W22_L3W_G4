import React from 'react';
import { useNavigate } from "react-router-dom";
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface TemperatureSensorProps {
    
}
 
const TemperatureSensor: React.FunctionComponent<TemperatureSensorProps> = () => {

    const navigate = useNavigate();

    const temperatureValidation = () => {
        // await sending stuff to the back end and validating 
        // depending on validaiton move to screening -
        // else return some form of error messaging
        //window.location.replace('http://localhost:3000/Register');
        navigate("/Success");
    }

    return ( 
        <>
            <CenterContainer>
                <Title>Temperature Sensor</Title>
                <Text>Stand still in front of the camera until the CSR logs your  temperature</Text>
                <BoxContainer/>
                <InputSubmit onClick={temperatureValidation}/>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default TemperatureSensor;