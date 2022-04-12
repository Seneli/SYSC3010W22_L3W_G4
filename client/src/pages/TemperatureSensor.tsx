import React, { useEffect, useState } from 'react';
import { realtimeDB } from '../firebase/initFirebase';
import { ref, onValue } from 'firebase/database';
import { useNavigate } from 'react-router-dom';
import { BoxContainer, CenterContainer, Title, Text, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface TemperatureSensorProps {}

const TemperatureSensor: React.FunctionComponent<TemperatureSensorProps> = () => {
    const navigate = useNavigate();
    const [detectedTemp, setDetectedTemp] = useState('getting temperature...');
    const [displayCountdown, setDisplayCountdown] = useState('none');

    const temperatureValidation = () => {
        navigate('/Success');
    };

    const tempFail = () => {
        navigate('/Error');
    };

    useEffect(() => {
        const tempSenseState = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables/passedTempDetection');
        onValue(tempSenseState, (snapshot) => {
            const data = snapshot.val();
            console.log(data);
            if (data === 'true') {
                setDisplayCountdown('block');
                setTimeout(temperatureValidation, 3000);
            } else if (data === 'false') {
                setDisplayCountdown('block');
                setTimeout(tempFail, 3000);
            }
        });

        const firebaseTemp = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables/detectedTemp');
        onValue(firebaseTemp, (snapshot) => {
            const data = snapshot.val();
            console.log(data);
            setDetectedTemp(data);
        });
    });

    return (
        <>
            <CenterContainer placement="20%">
                <Title>Temperature Sensor</Title>
                <Text>Stand still in front of the camera until the CSR logs your temperature</Text>
                <BoxContainer>
                    <Title top="40px" color="#FFF">
                        {detectedTemp}
                    </Title>
                    <Title color="#FFF" display={displayCountdown}>
                        Moving to next page in 3 seconds
                    </Title>
                </BoxContainer>
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default TemperatureSensor;
