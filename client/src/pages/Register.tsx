import React from 'react';
import { useNavigate } from "react-router-dom";
import { CenterContainer, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface RegisterProps {
    
}
 
const Register: React.FunctionComponent<RegisterProps> = () => {

    const navigate = useNavigate();

    const handleSubmit = () => {
        // await sending stuff to the back end and validating 
        // depending on validaiton move to screening -
        // else return some form of error messaging
        //window.location.replace('http://localhost:3000/Register');
        navigate("/Screening");
    }

    return ( 
        <>
            <CenterContainer>
                <Title>Register</Title>
                <Text>Sign in to the Covid Rapid Screener to enter the building</Text>
                <form onSubmit={handleSubmit} action="">
                    <InputText placeholder="Login"/>
                    <InputText placeholder="Password"/>
                    <InputSubmit value="Login"/>
                </form>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Register;