# Author: JEAN CARLLO JARDIM COSTA

# strider-posterr-backend

This is an API Rest built on python using flask for server side and SQLALchemy as an object relacional mapper. 

# run the project
To run the project you can type on terminal inside the root folder of the project

- docker compose up -d db   

After that you have to run:

- docker compose up --build posterrapp

So, using a browser you can access http://127.0.0.1:5000/docs to see ant test all the endpoints.
With the page \docs opened you can expand default, expand POST /initdb, than click on the button "Try it out" and finally click on "Execute" to criate the tables of the database.

You can use the previous step to test every route.
