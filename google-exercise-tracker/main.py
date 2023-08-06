import requests

exercise_details = input("Tell me which exercise you did: ")

GENDER = 'female'
WEIGHT_KG = 53.2
HEIGHT_CM = 5.5
AGE = 40

APP_ID = 'd92c81c4'
API_KEY = '5e2b89910ac8464f4c3597c7b59e659b'

url_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

url_config = {
    "query":exercise_details,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

respone = requests.post(url=url_endpoint, json=url_config, headers=headers )
print(respone.text)