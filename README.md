**devops_assignment2_part1**

**Step 1**

**Command:** http://127.0.0.1:8000/

**Output:** 

{
  "message": "Hello World"
}

**Step 2**

**Command:**

db defined in docker compose

**Output:** 

db accessible in mongodb compass: mongodb://127.0.0.1:27017


**Step 3**

**Command:**

db defined in docker compose

**Output:** 

db accessible in mongodb compass: mongodb://127.0.0.1:27017
in the application db will be accesibke using "mongodb://db:27017"

**Step 4**


**Output:** 

application is accessible at: http://127.0.0.1:8000/
db accessible in mongodb compass: mongodb://127.0.0.1:27017

**Step 5**

new feature of adding your name, age and location to the database added and in return it gives a hello {name} message 

**Output:** 

application is accessible at: http://127.0.0.1:8000/
db accessible in mongodb compass: mongodb://127.0.0.1:27017

**Step 6**

added volume db_data to the docker compose

**Output:** 

after deleting the image and containers , recomposed the services and data is restored


**Step 7**

**Command:**

docker-compose up -d --scale web=3e

**Output:** 

 - Network devops_assignment2_part2_default  Created                                                               0.1s
 - Container devops_assignment2_part2-web-3  Started                                                               1.8s
 - Container devops_assignment2_part2-web-1  Started                                                               1.4s
 - Container devops_assignment2_part2-db-1   Started                                                               0.7s
 - Container devops_assignment2_part2-web-2  Started                                                               0.9s

**Command:**

docker-compose ps


**Output:** 

NAME                             IMAGE                          COMMAND                  SERVICE             CREATED              STATUS              PORTS
devops_assignment2_part2-db-1    bitnami/mongodb:latest         "/opt/bitnami/script…"   db                  About a minute ago   Up About a minute   0.0.0.0:27017->27017/tcp
devops_assignment2_part2-web-1   devops_assignment2_part2-web   "/bin/sh -c 'uvicorn…"   web                 About a minute ago   Up About a minute   0.0.0.0:53275->8000/tcp
devops_assignment2_part2-web-2   devops_assignment2_part2-web   "/bin/sh -c 'uvicorn…"   web                 About a minute ago   Up About a minute   0.0.0.0:53272->8000/tcp
devops_assignment2_part2-web-3   devops_assignment2_part2-web   "/bin/sh -c 'uvicorn…"   web                 About a minute ago   Up About a minute   0.0.0.0:53276->8000/tcp


***All three containers are accessible on localhost with their ports***

**Step 8**

**Command:**

docker-compose up -d --scale web=3e

**Output:** 
