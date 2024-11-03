import streamlit as st

# Sample responses for common questions
responses = {
    # General questions
    "what is your name": "I am the AI assistant for the MDT team.",
    "what is the role of the mdt": "The MDT team collaborates to provide comprehensive patient care.",
    "how can I contact a doctor": "You can reach out to your doctor via the patient portal or contact the clinic directly.",
    "what should I do if I have a medical emergency": "Please call emergency services or go to the nearest emergency room immediately.",
    "what are the symptoms of flu": "Common flu symptoms include fever, cough, sore throat, body aches, and fatigue.",
    
    # Hypertension
    "what is hypertension": "Hypertension, or high blood pressure, is a condition where the force of the blood against the artery walls is too high.",
    "what are the symptoms of hypertension": "Many people with hypertension have no symptoms, but it can lead to headaches, shortness of breath, or nosebleeds.",
    "how is hypertension diagnosed": "Hypertension is diagnosed using a blood pressure cuff to measure your blood pressure readings.",
    "how is hypertension treated": "Treatment can include lifestyle changes like diet and exercise, and medications such as diuretics or ACE inhibitors.",
    "what lifestyle changes can help lower blood pressure": "Eating a balanced diet, reducing salt intake, exercising regularly, and avoiding alcohol and tobacco can help.",
    "what are the potential complications of untreated hypertension": "Untreated hypertension can lead to serious issues like heart disease, stroke, and kidney damage.",
    "how can I monitor my blood pressure at home": "You can use a digital blood pressure monitor and keep a log of your readings to discuss with your doctor.",
    "what should I do if my blood pressure is too high": "If your blood pressure is significantly high or if you have symptoms, contact your healthcare provider immediately.",
    "what is the difference between primary and secondary hypertension": "Primary hypertension has no identifiable cause, while secondary hypertension is caused by another medical condition.",
    
    # Diabetes
    "what is diabetes": "Diabetes is a chronic condition that occurs when the body cannot properly process food for use as energy.",
    "what are the types of diabetes": "The main types are Type 1 diabetes, Type 2 diabetes, and gestational diabetes.",
    "what are the symptoms of diabetes": "Common symptoms include increased thirst, frequent urination, extreme fatigue, and blurred vision.",
    "how is diabetes diagnosed": "Diabetes is diagnosed through blood tests that check glucose levels.",
    "what are the treatment options for diabetes": "Treatment may include lifestyle changes, insulin therapy, and medications to help control blood sugar levels.",
    "how can I manage my blood sugar levels": "Regular monitoring, a balanced diet, exercise, and taking medications as prescribed can help manage your blood sugar.",
    "what should I know about insulin therapy": "Insulin therapy involves injecting insulin to help control blood sugar levels, and your healthcare provider will guide you on how to use it.",
    "what are the complications of diabetes": "Complications can include heart disease, nerve damage, kidney disease, and vision problems.",
    "what is prediabetes": "Prediabetes is a condition where blood sugar levels are higher than normal but not high enough to be classified as diabetes.",
    
    # Cardiovascular Diseases
    "what is cardiovascular disease": "Cardiovascular disease refers to a group of disorders that affect the heart and blood vessels.",
    "what are the symptoms of heart disease": "Symptoms may include chest pain, shortness of breath, and fatigue.",
    "how is cardiovascular disease diagnosed": "Diagnosis can include physical exams, blood tests, and imaging tests like an ECG or echocardiogram.",
    "what lifestyle changes can reduce my risk of heart disease": "Eating a healthy diet, exercising regularly, quitting smoking, and managing stress can help reduce risk.",
    "what treatments are available for cardiovascular disease": "Treatment options may include medications, lifestyle changes, and possibly procedures like angioplasty or surgery.",
    "what are the signs of a stroke": "Signs include sudden numbness, confusion, trouble speaking, and severe headache. Seek immediate help if you notice these symptoms.",
    
    # COPD
    "what is COPD": "Chronic Obstructive Pulmonary Disease (COPD) is a lung disease that makes it hard to breathe.",
    "what are the symptoms of COPD": "Symptoms include chronic cough, shortness of breath, and wheezing.",
    "how is COPD diagnosed": "Diagnosis involves a physical exam, lung function tests, and imaging tests like X-rays.",
    "what treatments are available for COPD": "Treatment may include medications, pulmonary rehabilitation, and oxygen therapy.",
    "how can I manage my COPD symptoms": "Avoid triggers, use prescribed medications, and practice breathing exercises to manage symptoms.",
    "what role does smoking cessation play in COPD management": "Quitting smoking is crucial as it can slow the progression of the disease and improve lung function.",
    
    # Asthma
    "what is asthma": "Asthma is a chronic condition that affects the airways, causing them to become inflamed and narrow.",
    "what are the symptoms of asthma": "Symptoms include wheezing, coughing, chest tightness, and shortness of breath.",
    "how is asthma diagnosed": "Asthma is diagnosed through medical history, physical examination, and tests like spirometry.",
    "what are common asthma triggers": "Triggers can include allergens, smoke, exercise, and cold air.",
    "how can I manage my asthma": "Use medications as prescribed, avoid triggers, and create an asthma action plan with your healthcare provider.",
    "what should I do during an asthma attack": "Use your rescue inhaler immediately, try to stay calm, and seek emergency help if symptoms do not improve.",
    
    # General chronic conditions
    "how can I effectively communicate with my healthcare team": "Be honest about your symptoms, ask questions, and express any concerns during your appointments.",
    "what role does nutrition play in managing my health condition": "Good nutrition supports overall health and helps manage conditions like hypertension, diabetes, and heart disease.",
    "how can I stay motivated to manage my health": "Set small, achievable goals, track your progress, and seek support from family, friends, or support groups.",
    "what are the benefits of physical activity for my condition": "Regular physical activity helps control weight, lowers blood pressure, improves heart health, and boosts mood.",
    "what should I know about my family history and its impact on my health": "Family history can influence your risk for certain conditions. Share this information with your healthcare provider for tailored advice.",
    "what resources are available for learning about my condition": "Many organizations provide educational materials, online resources, and support groups tailored to specific conditions.",
    "how can I balance managing my condition with everyday life": "Incorporate healthy habits into your daily routine, like meal prepping and scheduling medication reminders.",
}

# Function to get answer based on keywords
def get_answer(question):
    # Normalize the input
    question = question.strip().lower()
    for key in responses:
        if key in question:
            return responses[key]
    return "I'm sorry, I don't have an answer for that."

# Set the title of the app
st.title("MDT AI Medical Assistant")

# Provide guidance on questions
st.write("You can ask any medical question:")

# Get user input
question = st.text_input("Ask your question:")

# Respond to user input
if st.button("Get Answer"):
    answer = get_answer(question)
    st.write(answer)
