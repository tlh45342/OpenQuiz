# INTRODUCTION

OpenQuiz is a simple example flask app that can be used to host a Quiz.  This is designed to be "section" aware so that questions can be drawn from a pool.
This is designed to be quiz and test friendly.

## PRESUMPTION

- python is installed
- pip is installed
- gunicorn is installed

## INSTALLATION

```bash
cd /opt
git clone https://github.com/tlh45342/OpenQuiz.git
cd OpenQuiz
pip install -r requirements.txt
python server.py
```

## DOCKER

If wanting to create as a docker image the following command can be used.

```bash
git clone https://github.com/tlh45342/flask-example4.git
cd flask-example4
docker-compose up -d
```

*One line command to build docker image.*
```bash
docker build github.com/tlh45342/flask-example4#main 
```
Please note:  After October 1, 2020 github changed the default branch from **MASTER** to **MAIN**.  
So please remember to put #main at the end of the request - or rename your branch in github to master.  
As of this writing "docker build github..." uses **MASTER** as the default.

The result might be

```bash
docker run -it -d -p 443:443 dca6
```

# Quick note about docker image clean up.
PLEASE REVIEW THIS CAREFFULLY BEFORE USING.
This would delete containers and images that aren't running.
Only use this if this what you intend.
```bash
docker container prune -f
docker image prune -a -f
```

## SIDEBAR: Notes for creating a service for Linux based distributions

I am putting my notes here now - because I will use them.  Consider these notes used to implement the Flask APP as a service.

To create a service entry cd /etc/systemd/system
Create a file that looks something like is found in the following block.
As much as I hate assumptions - you will need to edit this to your tastes and for your environment.

```bash
cat <<EOF | sudo tee /etc/systemd/system/flask-example4.service
[Unit]
Description=flask-example4

[Service]
WorkingDirectory=/mnt/opt/flask-example4/
ExecStart=/usr/local/bin/gunicorn --certfile=cert.pem --keyfile=key.pem --bind 0.0.0.0:443 server:app

[Install]
WantedBy=multi-user.target
EOF
```

The key commands for reference are: 

```bash
sudo systemctl daemon-reload
sudo systemctl start flask4.service
sudo systemctl restart flask4.service
sudo systemctl stop flask4.service
```

## STRUCTURE

    ├── README.md                   This document
    ├── requirements.txt            3rd libraries
    ├── server.py                   Wsgi app
    └── app
       ├── __init__.py
       ├── app.py                   Main App
       ├── user
       ├── api
       ├── static                   Static files
       │   ├── css
       └── templates                Jinja2 templates
           ├── errors
           ├── frontend
           └── index.html
 
## Version

(01/9/2023) - This is a work in progress and will be clobered toghether from existing Flask and Datbase projects.

## LICENSE

flask-example4 is licensed under the Apache License, Version 2.0. See LICENSE for the full license text.

## ACKNOWLEDGEMENTS

Many thanks to Python, Flask and other good stacks.  
