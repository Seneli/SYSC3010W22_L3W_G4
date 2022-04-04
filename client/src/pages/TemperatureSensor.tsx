import React from 'react';
import { realtimeDB } from '../firebase/initFirebase';
import { ref, onValue } from 'firebase/database';
import { useNavigate } from 'react-router-dom';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface TemperatureSensorProps {}

const TemperatureSensor: React.FunctionComponent<TemperatureSensorProps> = () => {
    const navigate = useNavigate();

    const temperatureValidation = () => {
        navigate('/Success');
    };

    const tempSenseState = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables/passedTempDetection');
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
                <Title>Temperature Sensor</Title>
                <Text>Stand still in front of the camera until the CSR logs your temperature</Text>
                <BoxContainer />
                <InputSubmit onClick={temperatureValidation} />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default TemperatureSensor;
