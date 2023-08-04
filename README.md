# project_1

The purpose of Project 1 was to create a remote backup automation application which can be used remotely via HTTP. 
As part of this, a table was created to record the logs using MySQL.

The following briefly outlines the architecture:
  Curl commands make a HTTP request to Flask, which provides the HTTP response
  Flask then invokes the code within app.py and the Python commands run
  app.py then executes the backup via Linux
  The log is actioned and recorded within the MySQL database

  The following was used to prepare the log table:
          CREATE TABLE log(
          id        INT PRIMARY KEY AUTO_INCREMENT,
          date      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          action    VARCHAR(100),
          parameter VARCHAR(1000),
          status    VARCHAR(100)
        );

    The curl commands used were as follows:

              python app.py
          
          # Using Curl
          
          # Backup example
          curl -X POST http://localhost:5000 -H "Content-Type: application/json" -d '{"path":"G:\hello"}' 
          
          # Get Log
          curl localhost:5000/log?start=2023-06-01&end=2023-08-31
          
          # Get Log
          curl localhost:5000/stat

# project_2

After completing project 1, the next step was to use automation to run the application app.py
The first step to was to use a Trello board to outline all key objectives of this project
Then, it was important to configure Nexus for docker. Two repositories were created (proxy and hosted)
The virtual machines provided by QA were then configured using docker commands in the CMD 
Using Jenkins, a freestyle project was set up which ran Bash commands to connect to the local git repository storing the code
A pipeline was also created using Jenkins which allowed me to automate the entire process and running of app.py
Configuration of Jenkins included linking this to Nexus and the git repositories to enable it to access these 
A Jenkins file was also created and stored on the Git repo, allowing Docker to build images and store within the containers 


