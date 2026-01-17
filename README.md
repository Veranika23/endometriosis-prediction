# Problem description

Endometriosis is a chronic gynecological condition characterized by the growth of endometrial-like tissue outside the uterus, leading to symptoms such as pelvic pain, infertility, and reduced quality of life. Despite affecting an estimated 10% of women of reproductive age worldwide, endometriosis is often underdiagnosed or diagnosed after significant delays, primarily due to the non-specific nature of its symptoms and the need for invasive procedures like laparoscopy for definitive diagnosis. Early and accurate prediction of endometriosis is crucial for timely intervention, improved patient outcomes, and reduced healthcare costs. 


Leveraging machine learning (ML) techniques to predict endometriosis based on clinical and demographic data offers the potential to enhance diagnostic accuracy, minimize invasive procedures, and support personalized treatment strategies.

# Dataset description




```
curl -X 'POST' \
  'http://localhost:9696/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "menstrual_irregularity": 1,
  "chronic_pain_level": 3.43688,
  "hormone_level_abnormality": 1,
  "infertility": 0,
  "bmi": 27.237861,
  "physical_activity": "rarely"
}'
```