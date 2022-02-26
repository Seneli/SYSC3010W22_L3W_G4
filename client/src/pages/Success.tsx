import React from 'react';
import { CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

 
const Success = () => {
    return ( 
        <>
            <CenterContainer>
                <Title>Success!</Title>
                <Text>asdasdasd</Text>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Success;