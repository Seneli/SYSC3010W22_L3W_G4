import React from 'react';

interface SignInProps {
    
}
 
const SignIn: React.FunctionComponent<SignInProps> = () => {
    return ( 
        <>
            <div>
                <h1>Sign In</h1>
                <p>Sign in to the Covid Rapid Screener to enter the building</p>
                <form>
                    <input type="text" placeholder="Login"/>
                    <input type="text" placeholder="Password"/>
                    <input type="submit" value="Login"/>
                </form>
            </div>
            <div>
                vectors go here!
            </div>
        </>
     );
}
 
export default SignIn;