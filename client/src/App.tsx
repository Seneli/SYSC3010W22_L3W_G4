import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'; 
import { SignIn, Register, Screening, Mask, Temperature, Success, Error } from "./pages"; 

interface AppProps {
}
 
const App : React.FunctionComponent<AppProps> = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<SignIn/>}/>
                <Route path="/Register" element={<Register/>}/>
                <Route path="/Screening" element={<Screening/>}/>
                <Route path="/Mask" element={<Mask/>}/>
                <Route path="/Temperature" element={<Temperature/>}/>
                <Route path="/Success" element={<Success/>}/>
                <Route path="/Error" element={<Error/>}/>
            </Routes>
        </BrowserRouter>
    )
}
 
export default App ;
