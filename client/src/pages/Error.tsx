import React from 'react';
import { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 


interface ErrorProps {
    
}
 
const Error: React.FunctionComponent<ErrorProps> = () => {
    return ( 
        <>
            <CenterContainer>
                <BoxContainer background="#23667E">
                    <CenterContainer>
                        <Title color="#fff">Error: [Page Name]</Title>
                        <Text color="#fff">[explanation for how they failed]</Text>
                    </CenterContainer>
                </BoxContainer>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default Error;