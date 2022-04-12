import React from 'react';
import { useNavigate } from 'react-router-dom';
import { realtimeDB, deleteImage } from '../firebase/initFirebase';
import { ref, update, onValue } from 'firebase/database';
import { BoxContainer, CenterContainer, Title, Text, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface ErrorProps {}

const Error: React.FunctionComponent<ErrorProps> = () => {
    const navigate = useNavigate();

    const resetForNewUser = (e: any) => {
        e.preventDefault();
        console.log(realtimeDB);

        update(ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables'), {
            currentUser: '',
            detectedTemp: 'null',
            passedMaskDetection: 'null',
            passedTempDetection: 'null',
            runDetection: 'false'
        });

        for (let i = 0; i < 10; i++) {
            deleteImage(i + '.jpg');
        }

        navigate('/');
    };

    return (
        <>
            <CenterContainer>
                <BoxContainer background="#23667E">
                    <Title color="#fff" top="5%">
                        Screening Failed
                    </Title>
                    <Text color="#fff">
                        If you have reached this page it means you have failed the mask or temperature screening. The system admin has been contacted and will be there to assist you shortly.
                    </Text>
                </BoxContainer>
                <InputSubmit value="Return to Sign In Page" onClick={(e: any) => resetForNewUser(e)} />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default Error;
