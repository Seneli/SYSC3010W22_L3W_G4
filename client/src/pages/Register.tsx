import React from 'react';
import { CenterContainer, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface RegisterProps {
    
}
 
const Register: React.FunctionComponent<RegisterProps> = () => {
    return ( 
        <>
            <CenterContainer>
                <Title>Register</Title>
                <Text>Sign in to the Covid Rapid Screener to enter the building</Text>
                <form action="">
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