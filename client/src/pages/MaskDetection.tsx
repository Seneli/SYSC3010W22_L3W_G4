import React, { useEffect, useState } from 'react';
import { realtimeDB, firebaseStorage, systemStorageFolder } from '../firebase/initFirebase';
import { getDownloadURL, listAll, ref as storageRef } from 'firebase/storage';
import { ref, onValue } from 'firebase/database';
import { useNavigate } from 'react-router-dom';
import { BoxImg, CenterContainer, Title, Text, InputSubmit, Vectors } from '../styles/styledComponents';
import vectorsImg from '../media/Vectors.png';

interface MaskDetectionProps {}

const MaskDetection: React.FunctionComponent<MaskDetectionProps> = () => {
    const navigate = useNavigate();
    const [lastImageRef, setLastImageRef] = useState('https://example.com/');

    useEffect(() => {
        let errorIMG = storageRef(systemStorageFolder, '/loading.jpg');

        const processed_img_ref = storageRef(firebaseStorage, `/${process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER}_processed_images`);
        console.log(processed_img_ref);

        setInterval(() => {
            listAll(processed_img_ref)
                .then((res) => {
                    getDownloadURL(res.items[res.items.length - 1])
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

    const maskDetectionState = ref(realtimeDB, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/System_Variables/passedMaskDetection');
    onValue(maskDetectionState, (snapshot) => {
        const data = snapshot.val();
        if (data === 'true') {
            navigate('/Temperature');
        } else if (data === 'false') {
            navigate('/Error');
        }
    });

    return (
        <>
            <CenterContainer placement="15%">
                <Title>Mask Detection</Title>
                <Text>Stand still in front of the camera until the CSR detects your mask</Text>
                <BoxImg src={lastImageRef} alt="image still loading" />
            </CenterContainer>
            <Vectors src={vectorsImg} />
        </>
    );
};

export default MaskDetection;
