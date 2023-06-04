import { Client } from 'appwrite';
const express = require('express');


const client = new Client();

const app = express()

// Pretty indenting
app.set("json spaces", 2)

app.get('/', (req, res) => res.send("Portfolio-Flash!"))

app.get('/createUser', (req,res) => {
    
client
.setEndpoint('https://cloud.appwrite.io/v1')
.setProject('647a9e045ef4f5948a16');

})