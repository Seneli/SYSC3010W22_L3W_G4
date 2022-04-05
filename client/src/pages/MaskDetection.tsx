import React, { useEffect, useState } from 'react';
import { realtimeDB, systemStorageFolder } from '../firebase/initFirebase';
import { StorageReference, getDownloadURL, listAll, ref as storageRef } from 'firebase/storage';
import { ref, onValue } from 'firebase/database';
import { useNavigate } from 'react-router-dom';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface MaskDetectionProps {}

const MaskDetection: React.FunctionComponent<MaskDetectionProps> = () => {
    const navigate = useNavigate();
    const [lastImageRef, setLastImageRef] = useState('https://example.com/');

    useEffect(() => {
        let errorIMG = storageRef(systemStorageFolder, '/error.jpeg');

        setInterval(() => {
            listAll(systemStorageFolder)
                .then((res) => {
                    getDownloadURL(res.items[res.items.length - 2])
                        .then((url) => {
                            setLastImageRef(url);
                        })
                        .catch((error) => {
                            console.log(error);
                        });
                })
                .catch((error) => {
                    getDownloadURL(errorIMG)
                        .then((url) => {
                            setLastImageRef(url);
                        })
                        .catch((error) => {
                            console.log(error);
                        });
                });
        }, 1000);
    }, []);

    const maskValidation = () => {
        navigate('/Temperature');
    };

    const maskDetectionState = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables/passedMaskDetection');
    onValue(maskDetectionState, (snapshot) => {
        const data = snapshot.val();
        //console.log(data);
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
                <BoxContainer src={lastImageRef} />
                <InputSubmit onClick={maskValidation} />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default MaskDetection;
