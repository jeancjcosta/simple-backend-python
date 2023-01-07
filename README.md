# Author: JEAN CARLLO JARDIM COSTA

# strider-posterr-backend

This is an API Rest built on python using flask for server side and SQLALchemy as an object relacional mapper. 

# run the project
To run the project you need to install docker in your mnachine. After that you have to type on terminal inside the root folder of the project.

- docker compose up -d db   

After that you have to run:

- docker compose up --build posterrapp

So, using a browser you can access localhost:8080/docs to see ant test all the endpoints.
With the page \docs opened you can expand default, expand POST /initdb, than click on the button "Try it out" and finally click on "Execute" to create the tables of the database.

You can use the previous step to test every route.
