import React from 'react';
import { CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface MaskDetectionProps {
    
}
 
const MaskDetection: React.FunctionComponent<MaskDetectionProps> = () => {
    return ( 
        <>
            <CenterContainer>
                <Title>Mask Detection</Title>
                <Text>Stand still in front of the camera until the CSR detects your mask</Text>
                <div>BLACK BOX THINGY GOES HERE KEKW</div>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default MaskDetection;