import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import firebaseDB from '../firebase/initFirebase';
import { ref, set } from "firebase/database";
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

 
const Success = () => {
    const [userName, setUserName] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e: any) => {
        e.preventDefault();
        console.log(firebaseDB);

        //const systemVariablesRef = firebaseDB.ref("Sy")
        
        set(ref(firebaseDB, 'System_variables'), {
            currentUser: userName,
            passedMaskDetection: "null",
            passedTempDetection: "null",
            runDetection: "false",
        });
        console.log(userName);
        navigate("/");
    }

    return ( 
        <>
            <CenterContainer>
                <BoxContainer background="#B8F8D8">
                    <Title color="#fff">Thank you for using CRS</Title>
                    <Text color="#fff">Proceed to the doors to enter the establishment</Text>
                </BoxContainer>
                <InputSubmit value="Screen New User" onClick={(e:any) => handleSubmit(e)}/>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Success;