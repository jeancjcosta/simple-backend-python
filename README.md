# Author: JEAN CARLLO JARDIM COSTA

# strider-posterr-backend

This is an API Rest built on python using flask for server side and SQLALchemy as an object relational mapper. 

# run the project
To run the project you need to install docker (https://docs.docker.com/get-docker/) in your mnachine. After that you have to type on terminal inside the root folder of the project.
```
- docker compose up -d db   
```
After that you have to run:
```
- docker compose up --build posterrapp
```
So, using a browser you can access localhost:8080/docs to see a swagger UI to test all the endpoints.
With the page \docs opened you can expand default, expand POST /initdb, than click on the button "Try it out" and finally click on "Execute" to create the tables of the database.

You can use the previous step to test every route.

# Database diagram
- The database diagram is in root folder in the file ER-Diagram.png

# Payload examples
# For route /homepage method POST
- POST
```
{
  "content": "This is a post",
  "created_at": "2022-01-07",
  "post_type": "POST",
  "user_id": 1
}
```

- REPOST
```
{
  "content": "This is a post",
  "created_at": "2022-01-07",
  "post_type": "REPOST",
  "user_id": 1,
  "post_id": 1
}
```
- QUOTE POST
```
{
  "content": "This is a quote post",
  "created_at": "2022-01-07",
  "post_type": "QUOTE_POST",
  "user_id": 1,
  "post_id": 1
}
```

# SQL to insert user on database
```
insert into public.user (id, name, date_joined) values (1, 'Jhon', '2022-01-10');

insert into public.user (id, name, date_joined) values (2, 'Mary', '2022-07-01');

insert into public.user (id, name, date_joined) values (3, 'Albert', '2021-11-13');

insert into public.user (id, name, date_joined) values (4, 'Alice', '2020-10-31');
```

# CRITIQUE
- This project was implemented to be a prototype, so several improvements have to be done to prepare this project to production.
- One of the improvements is related to the database. The best wey to handle the changes, including the initial setup, is using some tool for migrations.
- Related to security, it is important to implement authentication and other layers of security. Several of then available in services like Azure or AWS. 
- To be right that the software works as planned is important to implement, unit tests, integration tests, security tests, performance tests, and so on.
In any project, it is always a challenge to get the code perfectly how you'd want it. Here is what you need to do for this section:

About the scaling is import highlight some points:
- if this software were to grow and have many users some steps is important to avoid failures:
    - Define the policy of development, including git practices like gitflow, project patterns, code organization and documentation;
    - Use microservices for modules to avoid problems in the entire software and to facilitate maintenance;
    - Use a service like rancher to manage docker, kubernetes, and deploys. Its important to easily scale the software by demand, even in a temporary demand.  
