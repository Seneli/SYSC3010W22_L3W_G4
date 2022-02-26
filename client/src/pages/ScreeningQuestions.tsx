import React from 'react';
import { CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface ScreeningQuestionsProps {
    
}
 
const ScreeningQuestions: React.FunctionComponent<ScreeningQuestionsProps> = () => {
    return ( 
        <>
            <Header>
                <Title color="#fff">Screening Questions</Title>
            </Header>
            <CenterContainer>
                <Text>Answer the following screening questions to proceed</Text>
                <form action="">
                    {/* for every question in this json file - have a text + "Yes"/"No" */}
                    <InputSubmit value="Submit"/>
                </form>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default ScreeningQuestions;