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
    apiKey: "AIzaSyCo0E0jVQswQ9b6rSdBqjQPAu-buR1KH28",
    authDomain: "syscourse-474.firebaseapp.com",
    databaseURL: "https://syscourse-474-default-rtdb.firebaseio.com",
    projectId: "syscourse-474",
    storageBucket: "syscourse-474.appspot.com",
    messagingSenderId: "378158361477",
    appId: "1:378158361477:web:4cbeb1f23610818baf32ec",
    measurementId: "G-5HYZF1820S"
  };  


// Initialize Firebase
const app = initializeApp(firebaseConfig);

export { app };