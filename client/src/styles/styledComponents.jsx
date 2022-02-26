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

const BoxContainer = styled.div`
    margin: auto;
    width: 80vw;
    height: 40vh;
    background: ${props => props.background|| "#23667E"}; 
    border: 5px solid #093545;
    box-sizing: border-box;
    box-shadow: 4px 10px 4px rgba(0, 0, 0, 0.15);
    border-radius: 25px;
`;

const CenterContainer = styled.div`
    text-align: center;
    margin: auto;
    position: absolute; 
    top: 30%;
    /* left: 20%;  */
    /* display: flex; */
    /* justify-content: center; */
    align-items: center;
    height: 200px;
`; 

const Header = styled.div`
    text-align: center;
    margin: auto;
    padding: 5vh; 
    //color: #FFFFFF;
    background-color: #224957;
`; 

const Title = styled.h1`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');
    
    color: ${props => props.color || "#224957"}; 
    font-family: 'Lexend Deca', sans-serif;
`; 

const Text = styled.p`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    color: ${props => props.color || "#224957"}; 
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
    border: none;
    
    ::placeholder {
        color: #FFFFFF;
    }
`; 

const buttonStyles = `
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

export { BoxContainer, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors }; 