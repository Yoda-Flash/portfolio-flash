# Portfolio Flash
Welcome to Portfolio Flash, our project for the hackathon HackYourPortfolio 2023!

Portfolio Flash is an app that generates portfolios in a flash! It is based on user input on both portfolio information and formatting choices, so all portfolios generated are fully customized and personal!

## Github Pages - https://yoda-flash.github.io/portfolio-flash/
Ideally, this github page acts as a landing site, which allows the Auth0 to authenticate the user before entering the actual app.

## Streamlit Page - https://yoda-flash-portfolio-flash-app-socrsu.streamlit.app/
Ideally, this streamlit page will take in user input, and after pressing a button, it will generate a PDF portfolio. 

## Code Directory
### Backend folder
Initial draft of backend using Appwrite and JS, which we ended up not using because it didn't fit the needs of our app.

### Frontend folder
Code for Auth0 user authentication

### Templates
Templates for Auth0 authentication

### App.py
Code for the streamlit application that takes in user input and contains a (commented out) button to generate PDF files

### Index.html
Code for the Github Pages landing page, which includes a link to the streamlit application
Ideally, this link will be to the Auth0 site for authentication, but we couldn't connect it to Auth0 yet, so it is currently a redirect to the streamlit app.

### PDF.py
Commented out code for generating PDFs based on App.py's user input
Commented out because of failed integrations with Streamlit, and we needed to be able to present something on our app in time for the deadline

### Style.css
Styling for index.html, the Github landing page.
