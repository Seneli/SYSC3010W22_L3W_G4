import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import firebaseDB from '../firebase/initFirebase';
import { ref, set, onValue} from "firebase/database";
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 


interface ErrorProps {
    
}
 
const Error: React.FunctionComponent<ErrorProps> = () => {
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

    const tempSenseState = ref(firebaseDB, 'System_variables/' + "passedTempDetection");
    onValue(tempSenseState, (snapshot) => {
        const data = snapshot.val();
        console.log(data);
        if (data === "true"){
            navigate("/Success");
        } else if (data === "false"){
            navigate("/Error");
        }
    });

    return ( 
        <>
            <CenterContainer>
                <BoxContainer background="#23667E">
                    <CenterContainer>
                        <Title color="#fff">Error Page</Title>
                        <Text color="#fff">If you have reached this page it means you hit an error</Text>
                    </CenterContainer>
                </BoxContainer>
                <InputSubmit value="Return to Sign In Page" onClick={(e:any) => handleSubmit(e)}/>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Error;