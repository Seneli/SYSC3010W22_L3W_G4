import React from 'react';
import { CenterContainer, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface SignInProps {
    
}
 
const SignIn: React.FunctionComponent<SignInProps> = () => {
    return ( 
        <>
            <CenterContainer>
                <Title>Sign In</Title>
                <Text>Sign in to the Covid Rapid Screener to enter the building</Text>
                <form>
                    <InputText placeholder="Login"/>
                    <InputText placeholder="Password"/>
                    <InputSubmit value="Login"/>
                </form>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
     );
}
 
export default SignIn;