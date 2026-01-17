import requests

url = 'http://localhost:9696/predict'

person = {  "menstrual_irregularity": 1,
  "chronic_pain_level": 3.43688,
  "hormone_level_abnormality": 1,
  "infertility": 0,
  "bmi": 27.237861,
  "physical_activity": "rarely"}

response = requests.post(url, json = person)
diagnosis = response.json() 

print('Response', diagnosis)

if diagnosis['diagnosis'] >= 0.5:
    print('Risk of endometriosis')
else:
    print('Healthy')