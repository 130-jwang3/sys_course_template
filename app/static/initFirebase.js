// Copyright 2018 Google LLC.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Script for configuring Firebase.
// See https://firebase.google.com/docs/web/setup for more information.

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyA0NufVO3H5QMk0PS1zpzRWqic93_2YsEU",
    authDomain: "project-syscourse.firebaseapp.com",
    databaseURL: "https://project-syscourse-default-rtdb.firebaseio.com",
    projectId: "project-syscourse",
    storageBucket: "project-syscourse.appspot.com",
    messagingSenderId: "131114168104",
    appId: "1:131114168104:web:057d30fc64cc3fe9e32a1d",
    measurementId: "G-T1WM8E7FSG"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);

export { app };