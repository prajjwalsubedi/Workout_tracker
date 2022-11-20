import os
import datetime
import requests

GENDER = "male"
WEIGHT_KG = 59.9
HEIGHT_CM = 169.7
AGE = 26
sheety_headers_token = os.environ["SHEETY_TOKEN"]
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_api_endpoint = "https://api.sheety.co/1d0822a1e0c9641c4bb7a9f139ee69bf/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_params = {
    "query": input("Tell me which exercises you did:  "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
results = response.json()

sheety_headers = {
    "Authorization": f"Bearer {sheety_headers_token}"
}


for result in results["exercises"]:
    post_json = {
        "workout":
            {"date": str(datetime.datetime.now().date().strftime("%d/%m/%Y")),
             "time": str(datetime.datetime.now().time().strftime("%X")),
             "exercise": result["name"].title(),
             "duration": result["duration_min"],
             "calories": result["nf_calories"]
             }
    }

    response = requests.post(url=sheet_api_endpoint, json=post_json, headers=sheety_headers)
