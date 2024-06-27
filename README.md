# Welcome to my Recipe and Meal Planner App!

## About

API: [EDAMAM API](https://developer.edamam.com/edamam-docs-recipe-api)

Description: Develop a recipe and meal planning application that helps users find recipes and plan meals.

# Search for a recipe

You can search by food, cuisine, diet, intolerances, and type.

## Developement Setup

### Set up virtual environment

1. Install the virtual environment `virtualenv -p python3 .env`
2. Activate the environment in your shell `source .env/bin/activate`
3. Install dependencies `pip3 install -r requirements.txt`
4. Select the python interpreter for the virtual environment

## Setting up GCP project

1. create a new project
2. enable Compute Engine, Cloud Build, and Secret Manager
3. visit the Datastore console and CREATE DATABASE
   - enable Datastore mode
   - enable Region `us-west1 (Oregon)`
   - CREATE DATABASE
4. visit IAM console and add secret manager to Compute Engine account
   - `Role: Secret Manager Secret Accessor`
5. create a service account called `mealplanner` and add the following roles
   - `Role: Cloud Datastore User`
   - `Role: Storeage Admin`
6. open a cloud shell session and clone the git repository
   - `git clone git@github.com:FemputerTech/MealPlanner.git`
7. cd into MealPlanner

## Build container

1. Cloud Run prefers to run images from Artifact Registry. Building and pushing the Docker image in Cloud Build and storing it in gcr.io can be done with a single command
2. Run the command in Cloud Shell in the same directory as the Dockerfile to build the container
   `gcloud builds submit --tag gcr.io/cloud-mealplanner-leicht/mealplanner-image`
3. Check that the image was created in Artifact Registry
4. to rebuild the image, just pull the latest repo and run the same function

### Set up the secret API KEY

1. Go to Secret Manager Web Console and Create Secret (one for app_id and one for app_key)
   - Name: `app_id`
   - Secret value: `<the app id>`
   - Create Secret
   - Name: `app_key`
   - Secret value: `<the api key>`
   - Create Secret

### Deploy with Cloud Run

1. Run the following command in Cloud Shell
2. This will Deploy and add an Environment Variable for the secret app_id and app_key

```
gcloud run deploy mealplanner \
  --image gcr.io/cloud-mealplanner-leicht/mealplanner-image:latest \
  --platform=managed --region=us-west1 --allow-unauthenticated \
  --update-secrets=APP_ID=app_id:latest \
  --update-secrets=APP_KEY=app_key:latest \
  --region=us-west1
```

2. To redeploy, just run the same function

### Running the application locally

1. create a local environment variable for APP_ID and APP_KEY
   `export APP_ID=<the app id>`
   `export APP_KEY=<the api key>`
2. create a local environment variable for GOOGLE_APPLICATION_CREDENTIALS
   `export GOOGLE_APPLICATION_CREDENTIALS=<gcp-project-key.json>`
3. run the with python `python3 app.py`
