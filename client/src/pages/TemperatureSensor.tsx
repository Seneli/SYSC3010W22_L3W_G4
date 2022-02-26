import React from 'react';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface TemperatureSensorProps {
    
}
 
const TemperatureSensor: React.FunctionComponent<TemperatureSensorProps> = () => {
    return ( 
        <>
            <CenterContainer>
                <Title>Temperature Sensor</Title>
                <Text>Stand still in front of the camera until the CSR logs your  temperature</Text>
                <BoxContainer/>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default TemperatureSensor;