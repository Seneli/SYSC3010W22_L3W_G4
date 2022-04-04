import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { realtimeDB, deleteImage } from '../firebase/initFirebase';
import { ref, update } from 'firebase/database';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';
import { getStorage, deleteObject } from 'firebase/storage';

const Success = () => {
    const [userName, setUserName] = useState('');
    const navigate = useNavigate();
    const storage = getStorage();

    const handleSubmit = (e: any) => {
        e.preventDefault();

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
                <BoxContainer background="#B8F8D8">
                    <Title color="#fff">Thank you for using CRS</Title>
                    <Text color="#fff">Proceed to the doors to enter the establishment</Text>
                </BoxContainer>
                <InputSubmit value="Screen New User" onClick={(e: any) => handleSubmit(e)} />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default Success;
