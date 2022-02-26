import React from 'react';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

 
const Success = () => {
    return ( 
        <>
            <CenterContainer>
                <BoxContainer background="#B8F8D8">
                    <Title color="#fff">Thank you for using CRS</Title>
                    <Text color="#fff">Proceed to the doors to enter the establishment</Text>
                </BoxContainer>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Success;