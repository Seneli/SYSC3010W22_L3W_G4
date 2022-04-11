import styled from 'styled-components';

const BoxImg = styled.img`
    margin: auto;
    display: block;
    height: 200px;
    width: auto;
    background: ${(props) => props.background || '#23667E'};
    border: 5px solid #093545;
    box-sizing: border-box;
    box-shadow: 4px 10px 4px rgba(0, 0, 0, 0.15);
    border-radius: 25px;
`;

const BoxContainer = styled.div`
    margin: auto;
    width: 100%;
    height: 100%;
    background: ${(props) => props.background || '#23667E'};
    border: 5px solid #093545;
    box-sizing: border-box;
    box-shadow: 4px 10px 4px rgba(0, 0, 0, 0.15);
    border-radius: 25px;
    vertical-align: middle;
`;

const CenterContainer = styled.div`
    text-align: center;
    margin: auto;
    position: absolute;
    left: 20%;
    width: 60%;
    top: ${(props) => props.placement || '30%'};
    align-items: center;
    height: 200px;
`;

const Header = styled.div`
    text-align: center;
    margin: auto;
    padding: 5vh;
    background-color: #224957;
`;

const Title = styled.h1`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    display: ${(props) => props.display || 'block'};
    padding-top: ${(props) => props.top || '0px'};
    margin: 10px auto;
    color: ${(props) => props.color || '#224957'};
    font-family: 'Lexend Deca', sans-serif;
`;

const Text = styled.p`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    margin: 20px 20px auto;
    color: ${(props) => props.color || '#224957'};
    font-family: 'Lexend Deca', sans-serif;
`;

const InputText = styled.input.attrs({
    type: 'text'
})`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    margin: 20px auto;

    display: block;
    font-family: 'Lexend Deca', sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 20px;
    padding: 10px 15px;
    color: #ffffff;

    background: #224957;
    border-radius: 10px;
    border: none;
    text-align: center;
    margin: auto;

    ::placeholder {
        color: #ffffff;
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
    text-align: center;
    text-transform: capitalize;
    color: #224957;

    background: #20df7f;
    border: none;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.3);
    border-radius: 10px;
    padding: 10px 50px;
    margin: 20px auto;
`;

const Button = styled.button`
    @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400&display=swap');

    font-family: 'Lexend Deca', sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    line-height: 20px;
    text-align: center;
    text-transform: capitalize;
    color: #224957;

    background: #20df7f;
    border: none;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.3);
    border-radius: 10px;
    padding: 10px 50px;
    display: block;
    margin: 20px auto;
`;

const Vectors = styled.img`
    position: absolute;
    bottom: 0px;
    width: 100%;
`;

export { BoxContainer, BoxImg, Button, CenterContainer, Header, Title, Text, InputText, InputSubmit, Vectors };
