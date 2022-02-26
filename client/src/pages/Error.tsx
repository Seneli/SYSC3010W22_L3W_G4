import React from 'react';
import { CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 


interface ErrorProps {
    
}
 
const Error: React.FunctionComponent<ErrorProps> = () => {
    return ( 
        <>
            <CenterContainer>
                <Title>Error: page _ props _ </Title>
                <Text>asdasdasd</Text>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Error;