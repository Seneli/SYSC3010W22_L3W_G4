//import firebase from "firebase/app";
import { initializeApp } from "firebase/app";
//import "firebase/auth"; //if we want auth we need this 
import { getDatabase } from "firebase/database";
//require('dotenv').config();
// import "dotenv/config"; 

const config = {
    apiKey: process.env.REACT_APP_PUBLIC_FIREBASE_API_KEY,
    authDomain: `${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}.firebaseapp.com`,
    databaseURL: `https://${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}-default-rtdb.firebaseio.com`,
    projectId: process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID
};

const app = initializeApp(config);
const database = getDatabase(app);

export default database ; 