import React from 'react';
import { Title, InputText, InputSubmit } from '../styles/styledComponents'; 

interface SignInProps {
    
}
 
const SignIn: React.FunctionComponent<SignInProps> = () => {
    return ( 
        <>
            <div>
                <Title>Sign In</Title>
                <p>Sign in to the Covid Rapid Screener to enter the building</p>
                <form>
                    <InputText placeholder="Login"/>
                    <InputText placeholder="Password"/>
                    <InputSubmit value="Login"/>
                </form>
            </div>
            <div>
                vectors go here!
            </div>
        </>
     );
}
 
export default SignIn;