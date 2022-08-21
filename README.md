# Machine_Learning_Project
This is my first machine learning project..

### Start Machine Learning Project

### Software and account requirement
1. Github account
2. Heroku account
3. VS Code IDE
4. Git

Creating conda Environment

...

conda create -p venv python==3.7 -y

...


conda activate venv/

...

pip install -r requirements.txt

...

To add files to git

...

git add .

...

or

...

git add (file_name)

...

Note: To ignore file or folder from git we  we can write name of folder/file in 
.gitignore file

...

To check git status

....

git status

...

To check all version maintained by git

...

git log

...

To create version/commit all changes by git

...

git commit -m "message"

...

To send version/changes to github

...

git push origin main

...

To check remote url

...

git remote -v

....


To check branch name

...

git branch

...

To setup CI/CD pipeline in heroku we need 3 informations

1. HEROKU_EMAIL = moreshwar.22kar@gmail.com
2. HEROKU_API_KEY = 81d1f093-d4e2-45a3-b586-91e6f645cde1
3. HEROKU_APP_NAME = myfirstml-app
...

BUILD DOCKER IMAGE

...

docker build -t <image_name>:<tagname> .

...

note - image name for docker must be lower case

...

TO LIST DOCKER IMAGE

... 

docker image

...

Run docker image

...

docker run -p 5000:5000 -e PORT=5000 aedf133308e0

...

To check runnig container in docker

...

docker ps

....

To stop docker container

...

docker stop <container_id>

...




