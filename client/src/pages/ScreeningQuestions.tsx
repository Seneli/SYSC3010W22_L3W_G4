import React from 'react';
import { useNavigate } from "react-router-dom";
import { CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors } from '../styles/styledComponents'; 
import vectorsImg from '../media/Vectors.png'; 

interface ScreeningQuestionsProps {
    
}
 
const ScreeningQuestions: React.FunctionComponent<ScreeningQuestionsProps> = () => {

    const navigate = useNavigate();

    const handleSubmit = () => {
        // await sending stuff to the back end and validating 
        // depending on validaiton move to screening -
        // else return some form of error messaging
        //window.location.replace('http://localhost:3000/Register');
        navigate("/Mask");
    }

    return ( 
        <>
            <Header>
                <Title color="#fff">Screening Questions</Title>
            </Header>
            <CenterContainer>
                <Text>Answer the following screening questions to proceed</Text>
                <form onSubmit={handleSubmit} action="">
                    {/* for every question in this json file - have a text + "Yes"/"No" */}
                    <InputSubmit value="Submit"/>
                </form>
            </CenterContainer>
            <Vectors src={vectorsImg}/>
        </>
    );
}
 
export default ScreeningQuestions;