import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { realtimeDB } from '../firebase/initFirebase';
import { ref, update, onValue } from 'firebase/database';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface ErrorProps {}

const Error: React.FunctionComponent<ErrorProps> = () => {
    const navigate = useNavigate();

    const handleSubmit = (e: any) => {
        e.preventDefault();
        console.log(realtimeDB);

        update(ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables'), {
            currentUser: '',
            detectedTemp: 'null',
            passedMaskDetection: 'null',
            passedTempDetection: 'null',
            runDetection: 'false'
        });
        navigate('/');
    };

    const tempSenseState = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + 'System_Variables/' + 'passedTempDetection');
    onValue(tempSenseState, (snapshot) => {
        const data = snapshot.val();
        console.log(data);
        if (data === 'true') {
            navigate('/Success');
        } else if (data === 'false') {
            navigate('/Error');
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
                <InputSubmit value="Return to Sign In Page" onClick={(e: any) => handleSubmit(e)} />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default Error;
