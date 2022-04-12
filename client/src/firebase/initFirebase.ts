import { initializeApp } from 'firebase/app';
import { getStorage, ref, deleteObject } from 'firebase/storage';
import { getDatabase } from 'firebase/database';

const config = {
    apiKey: process.env.REACT_APP_PUBLIC_FIREBASE_API_KEY,
    authDomain: `${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}.firebaseapp.com`,
    databaseURL: `https://${process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID}-default-rtdb.firebaseio.com`,
    storageBucket: `gs://covid-rapid-screener.appspot.com`,
    projectId: process.env.REACT_APP_PUBLIC_FIREBASE_PROJECT_ID
};

const app = initializeApp(config);
const realtimeDB = getDatabase(app);
const firebaseStorage = getStorage(app);

const systemStorageFolder = ref(firebaseStorage, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER);

const deleteImage = (refName: string) => {
    const imageRef = ref(firebaseStorage, process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER + '/' + refName);
    console.log(imageRef);

    deleteObject(imageRef)
        .then(() => {
            console.log('image deleted successfully!');
        })
        .catch((error) => {
            console.log('failed to delete image!', imageRef);
        });

    const processedImgRef = ref(firebaseStorage, `/${process.env.REACT_APP_PUBLIC_FIREBASE_SYSTEM_NUMBER}_processed_images/${refName}`);

    deleteObject(processedImgRef)
        .then(() => {
            console.log('image deleted successfully!');
        })
        .catch((error) => {
            console.log('failed to delete image!', processedImgRef);
        });
};

export { realtimeDB, firebaseStorage, systemStorageFolder, deleteImage };
