# Welcome to my Recipe and Meal Planner App!

## About

API: [Spoonacular API](https://spoonacular.com/food-api/docs)

Description: Develop a recipe and meal planning application that helps users find recipes and plan meals.

# Search for a recipe

You can search by food, cuisine, diet, intolerances, and type.

## Developement Setup

### Initial commit

1. mkdir final
2. touch final/Dockerfile
3. touch final/app.py
4. touch final/project_url.txt
5. touch final/screencast_url.txt
6. git add final
7. git commit -m "initial commit for final"
8. git push

### Set up virtual environment

1. Install the virtual environment `virtualenv -p python3 env`
2. Activate the environment in your shell `source env/bin/activate`
3. Install dependencies `pip3 install -Ur requirements.txt`
4. Select the python interpreter for the virtual environment

### Set up for Container Registry

1. Cloud Run prefers to run images from Container Registry. Building and pushing the Docker image in Cloud Build and storing it in gcr.io can be done with a single command
2. Go to Cloud Shell and go to the final directory
   `git clone git@gitlab.com:mleicht/cloud-leicht-mleicht.git`
   `cd cloud-leicht-mleicht/final`
3. Run the command in Cloud Shell in the same directory as the Dockerfile to build the container
   `gcloud builds submit --tag gcr.io/cloud-leicht-mleicht/mealplanner-image`
4. Check that the image was created in Container Registry
5. to redeploy, just run the same function

### Set up the secret API KEY

1. Go to Secret Manager Web Console and Create Secret
2. Name: `mealplanner-api-key`
3. Secret value: `<the api key>`
4. Create Secret
5. Visit the IAM console, find the service account for google cloud projects, and make sure the service role of Secret Manager Secret Accessor is added

### Deploy with Cloud Run

1. Run the following command in Cloud Shell
2. This will Deploy and add an Environment Variable for the secret api key

```
gcloud run deploy recipes \
  --image gcr.io/cloud-leicht-mleicht/mealplanner-image:latest \
  --platform=managed --region=us-west1 --allow-unauthenticated \
  --update-secrets=API_KEY=mealplanner-api-key:latest \
  --region=us-west1
```

2. To redeploy, just run the same function

### Running the application locally

1. create a local environment variable for API_KEY
   `export API_KEY=<the api key>`
2. create a local environment variable for GOOGLE_APPLICATION_CREDENTIALS
   `export GOOGLE_APPLICATION_CREDENTIALS="cloud-leicht-mleicht-key.json"`
3. run the with python `python3 app.py`
