import React from 'react';
import { useNavigate } from "react-router-dom";
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface MaskDetectionProps {
    
}
 
const MaskDetection: React.FunctionComponent<MaskDetectionProps> = () => {

    const navigate = useNavigate();

    const maskValidation = () => {
        // await sending stuff to the back end and validating 
        // depending on validaiton move to screening -
        // else return some form of error messaging
        //window.location.replace('http://localhost:3000/Register');
        navigate("/Temperature");
    }

    return ( 
        <>
            <CenterContainer>
                <Title>Mask Detection</Title>
                <Text>Stand still in front of the camera until the CSR detects your mask</Text>
                <BoxContainer/>
                <InputSubmit/>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default MaskDetection;