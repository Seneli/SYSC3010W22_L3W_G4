import styled from 'styled-components';

const colourPalette = {
    mainDarkGreen: "224957", 
    secondaryMintGreen: "#20DF7F",  
    thirdGreyGreen: "4E6D79", 
    white: "FFFFFF"
}

// const imports = styled.h1`
//     @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');
// `; 

const CenterContainer = styled.div`
    text-align: center;
    margin: auto;
`; 

const Title = styled.h1`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    color: #224957;
    font-family: 'Lexend Deca', sans-serif;
`; 

const Text = styled.p`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    color: #224957;
    font-family: 'Lexend Deca', sans-serif;
`; 

const InputText = styled.input.attrs({
    type: 'text'
})`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    display: block;  
    font-family: 'Lexend Deca', sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 20px;
    /* identical to box height, or 143% */
    padding: 10px 15px;
    color: #FFFFFF;

    background: #224957;
    border-radius: 10px;
    
    ::placeholder {
        color: #FFFFFF;
    }
`; 

const InputSubmit = styled.input.attrs({
    type: 'submit'
})`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    font-family: 'Lexend Deca', sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    line-height: 20px;
    /* identical to box height, or 125% */
    text-align: center;
    text-transform: capitalize;
    color: #224957;


    background: #20DF7F;
    border: none; 
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.3);
    border-radius: 10px;
    padding: 10px 50px; 
    
`; 

const Vectors = styled.img`
    position: absolute;
    bottom: 0px;
    width: 100%;
`; 

export { CenterContainer, Title, Text, InputText, InputSubmit, Vectors}; 