import React from 'react';
import { realtimeDB } from '../firebase/initFirebase';
import { ref, onValue } from 'firebase/database';
import { useNavigate } from 'react-router-dom';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface MaskDetectionProps {}

const MaskDetection: React.FunctionComponent<MaskDetectionProps> = () => {
    const navigate = useNavigate();

    const maskValidation = () => {
        navigate('/Temperature');
    };

    const maskDetectionState = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables/passedMaskDetection');
    onValue(maskDetectionState, (snapshot) => {
        const data = snapshot.val();
        console.log(data);
        if (data === 'true') {
            navigate('/Temperature');
        } else if (data === 'false') {
            navigate('/Error');
        }
    });

    return (
        <>
            <CenterContainer>
                <Title>Mask Detection</Title>
                <Text>Stand still in front of the camera until the CSR detects your mask</Text>
                <BoxContainer />
                <InputSubmit onClick={maskValidation} />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default MaskDetection;
