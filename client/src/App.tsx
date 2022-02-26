import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'; 
import SignIn from './pages/SignIn';
import Register from './pages/Register';

interface AppProps {
    
}
 
const App : React.FunctionComponent<AppProps> = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<SignIn/>}/>
                <Route path="/Register" element={<Register/>}/>
            </Routes>
        </BrowserRouter>
    )
}
 
export default App ;
