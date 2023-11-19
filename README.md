# Reflex authentification with firebase demo - WIP


## Getting Started

This project tries to demonstrate how to use reflex with firebase authentification.

## Prerequisites

You need to :
- Have a firebase project link to your GCP account. Go to https://console.firebase.google.com/ and create a new project and select the GCP project you want to link it to.
- Create a web app in your firebase project.
- Create a json key from the firebase service account that was automatically created when you linked your firebase project to your GCP account.
- Duplicate the `.env.template` file and rename it `.env`.
- Add the json key to the `secrets/`folder and update the `GOOGLE_APPLICATION_CREDENTIALS` in the .env file with the name of the json key file.
- Go to the firebase console --> "Project parameters" --> "Web API KEY" and copy the key in the .env file.

## Run the project

Create a new env, for example with conda:
```
conda create -n reflex-firebase python=3.10
```

Install requirements:
```
pip install -r requirements.txt
```

Run the project:
```
reflex run
```
