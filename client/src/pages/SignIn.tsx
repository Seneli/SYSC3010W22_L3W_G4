import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { CenterContainer, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

import firebaseDB from '../firebase/initFirebase';
import { ref, set } from "firebase/database";


type SignInProps = string; 
 
const SignIn: React.FunctionComponent<SignInProps> = () => {
    const [userName, setUserName] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e: any) => {
        e.preventDefault();
        console.log(firebaseDB);

        set(ref(firebaseDB, 'System_variables'), {
            currentUser: userName,
            passedMaskDetection: "null",
            passedTempDetection: "null",
            runDetection: "true",
        });
        navigate("/Mask");
    }

    const handleChange = (e: any) => {
        setUserName(e.target.value);
    }

    return ( 
        <>
            <CenterContainer>
                <Title>Sign In</Title>
                <Text>Enter your student number below to begin the Rapid Screening process.</Text>
                <form onSubmit={(e) => handleSubmit(e)} action="">
                    <InputText placeholder="Student Number" onChange={handleChange}/>
                    <InputText placeholder="Password"/>
                    <InputSubmit value="Login"/>
                </form>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
     );
}
 
export default SignIn;