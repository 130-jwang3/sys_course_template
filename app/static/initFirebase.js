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
    apiKey: "AIzaSyCcw7Hox9WU7hbaEXaSL1Vd9ohlAnWHw0g",
    authDomain: "syscourse.firebaseapp.com",
    projectId: "syscourse",
    storageBucket: "syscourse.appspot.com",
    messagingSenderId: "401064857156",
    appId: "1:401064857156:web:891ccddf0bd80fc93f3611",
    measurementId: "G-7K29T3VDDD"
  };


// Initialize Firebase
const app = initializeApp(firebaseConfig);

export { app };