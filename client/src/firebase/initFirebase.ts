//import firebase from "firebase/app";
import { initializeApp } from 'firebase/app';
import { getStorage, ref, deleteObject } from 'firebase/storage';
//import "firebase/auth"; //if we want auth we need this
import { getDatabase } from 'firebase/database';

const config = {
    apiKey: process.env.REACT_APP_PUBLIC_FIREBASE_API_KEY,
    authDomain: `${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}.firebaseapp.com`,
    databaseURL: `https://${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}-default-rtdb.firebaseio.com`,
    storageBucket: `gs://covid-rapid-screener.appspot.com`,
    projectId: process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID
};

const storageConfig = {
    apiKey: process.env.REACT_APP_PUBLIC_FIREBASE_API_KEY,
    authDomain: `${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}.firebaseapp.com`,
    databaseURL: `https://${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}-default-rtdb.firebaseio.com`,
    storageBucket: `gs://covid-rapid-screener.appspot.com`
};

const app = initializeApp(config);
//const storageApp = initializeApp(storageConfig);
const realtimeDB = getDatabase(app);

const firebaseStorage = getStorage(app);
//const firebaseStorage = getStorage(storageApp);

const deleteImage = (refName: string) => {
    const imageRef = ref(firebaseStorage, process.env.REACT_APP_SYSTEM_NUMBER + '/' + refName);
    console.log(imageRef);

    deleteObject(imageRef)
        .then(() => {
            console.log('image deleted successfully!');
        })
        .catch((error) => {
            console.log('failed to delete image!', imageRef);
        });
};

export { realtimeDB, firebaseStorage, deleteImage };
