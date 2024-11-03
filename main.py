import streamlit as st
from fuzzywuzzy import process

# Comprehensive responses for common questions across conditions
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
    "how often should I check my blood pressure": "It's recommended to check your blood pressure regularly, as advised by your healthcare provider.",
    "what foods should I avoid with hypertension": "Avoid foods high in salt, saturated fats, and added sugars. Focus on fruits, vegetables, whole grains, and lean proteins.",
    "what is a normal blood pressure reading": "A normal blood pressure reading is typically around 120/80 mmHg.",
    "can stress affect my blood pressure": "Yes, stress can temporarily raise blood pressure, so managing stress is important.",
    "how does alcohol consumption affect blood pressure": "Excessive alcohol intake can raise blood pressure; moderation is key.",
    "what exercises are best for lowering blood pressure": "Aerobic exercises like walking, cycling, and swimming are beneficial for heart health.",
    "how can I reduce salt intake": "Read nutrition labels, avoid processed foods, and use herbs and spices for flavor instead of salt.",
    "what is the DASH diet": "The DASH diet (Dietary Approaches to Stop Hypertension) emphasizes fruits, vegetables, whole grains, and low-fat dairy.",
    "how does smoking affect blood pressure": "Smoking raises blood pressure and damages blood vessels, increasing heart disease risk.",
    "what role does potassium play in blood pressure management": "Potassium helps balance sodium levels and can help lower blood pressure.",
    "how can I tell if my blood pressure medication is working": "Regular monitoring and follow-up with your healthcare provider can help assess effectiveness.",
    "what should I do if I miss a dose of my blood pressure medication": "Take the missed dose as soon as you remember, but skip it if it's almost time for the next dose. Never double up.",
    "can high blood pressure be cured": "While high blood pressure can often be managed effectively, it may not be curable. Long-term management is important.",
    
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
    "how often should I check my blood sugar levels": "Check your blood sugar as recommended by your healthcare provider, often several times a day.",
    "what foods should I eat to manage diabetes": "Focus on whole grains, lean proteins, healthy fats, fruits, and non-starchy vegetables.",
    "how does exercise affect blood sugar levels": "Physical activity helps lower blood sugar by increasing insulin sensitivity and glucose uptake in muscles.",
    "what is the glycemic index": "The glycemic index ranks foods based on their effect on blood sugar levels; low-GI foods are better for blood sugar control.",
    "how can I prevent diabetes complications": "Control your blood sugar, maintain a healthy weight, and have regular check-ups with your healthcare provider.",
    "what is the role of carbohydrates in my diet": "Carbohydrates can raise blood sugar, so managing portion sizes and choosing complex carbs is important.",
    "how can I cope with the emotional aspects of diabetes": "Seek support from friends, family, or a counselor, and consider joining a diabetes support group.",
    "what should I know about diabetes medications": "Different medications work in various ways; follow your healthcare provider’s guidance on taking them.",
    "how can I create a meal plan for diabetes": "Work with a dietitian to develop a meal plan that fits your preferences and helps manage blood sugar levels.",
    "what is the importance of foot care in diabetes management": "Proper foot care can prevent serious complications like infections and amputations.",
    "how does stress affect diabetes management": "Stress can raise blood sugar levels, so finding effective stress management techniques is important.",
    "what should I do if I experience low blood sugar": "Eat or drink something with fast-acting carbohydrates, like juice or candy, and monitor your blood sugar levels.",
    
    # Cardiovascular Diseases
    "what is cardiovascular disease": "Cardiovascular disease refers to a group of disorders that affect the heart and blood vessels.",
    "what are the symptoms of heart disease": "Symptoms may include chest pain, shortness of breath, and fatigue.",
    "how is cardiovascular disease diagnosed": "Diagnosis can include physical exams, blood tests, and imaging tests like an ECG or echocardiogram.",
    "what lifestyle changes can reduce my risk of heart disease": "Eating a healthy diet, exercising regularly, quitting smoking, and managing stress can help reduce risk.",
    "what treatments are available for cardiovascular disease": "Treatment options may include medications, lifestyle changes, and possibly procedures like angioplasty or surgery.",
    "what are the signs of a stroke": "Signs include sudden numbness, confusion, trouble speaking, and severe headache. Seek immediate help if you notice these symptoms.",
    "how can I lower my cholesterol levels": "Eat a heart-healthy diet, exercise, and take medications if prescribed by your healthcare provider.",
    "what role does exercise play in heart health": "Regular exercise strengthens the heart muscle, improves circulation, and helps maintain a healthy weight.",
    "what should I do if I have chest pain": "Seek emergency medical help immediately if you experience chest pain, especially if it's severe or accompanied by other symptoms.",
    "how can I manage stress to protect my heart health": "Practice relaxation techniques, engage in hobbies, and maintain a strong support network.",
    "what is a healthy blood pressure range": "A normal blood pressure reading is typically around 120/80 mmHg.",
    "how does smoking affect cardiovascular health": "Smoking damages blood vessels and increases the risk of heart disease and stroke.",
    "what is the impact of obesity on heart health": "Obesity increases the risk of high blood pressure, diabetes, and other heart-related conditions.",
    "how often should I get my cholesterol checked": "Discuss with your healthcare provider; it's generally recommended to check cholesterol every 4-6 years for adults.",
    "what are the benefits of a heart-healthy diet": "A heart-healthy diet can lower cholesterol, blood pressure, and reduce the risk of heart disease.",
    "how can I recognize the signs of heart failure": "Signs may include shortness of breath, fatigue, and swelling in the legs and ankles.",
    "what is atrial fibrillation": "Atrial fibrillation is an irregular heartbeat that can increase the risk of stroke and heart-related complications.",
    "what role does hydration play in heart health": "Staying hydrated supports overall cardiovascular function and helps regulate blood pressure.",
    "how can I prevent heart disease if I have a family history": "Focus on a healthy lifestyle, including diet and exercise, and follow your healthcare provider's recommendations.",
    
    # COPD
    "what is COPD": "Chronic Obstructive Pulmonary Disease (COPD) is a lung disease that makes it hard to breathe.",
    "what are the symptoms of COPD": "Symptoms include chronic cough, shortness of breath, and wheezing.",
    "how is COPD diagnosed": "Diagnosis involves a physical exam, lung function tests, and imaging tests like X-rays.",
    "what treatments are available for COPD": "Treatment may include medications, pulmonary rehabilitation, and oxygen therapy.",
    "how can I manage my COPD symptoms": "Avoid triggers, use prescribed medications, and practice breathing exercises to manage symptoms.",
    "what role does smoking cessation play in COPD management": "Quitting smoking is crucial as it can slow the progression of the disease and improve lung function.",
    "what are the long-term effects of COPD": "COPD can lead to worsening lung function, respiratory infections, and complications like heart disease.",
    "how can I improve my lung health with COPD": "Engage in pulmonary rehabilitation, stay active within limits, and follow your treatment plan.",
    "what should I do during a COPD flare-up": "Use your rescue inhaler and follow your action plan; seek medical help if symptoms worsen.",
    "how can I recognize early signs of COPD": "Watch for persistent cough, increased mucus production, and increasing shortness of breath.",
    "what lifestyle changes can help with COPD": "Avoid smoking, exercise as tolerated, eat a healthy diet, and maintain good indoor air quality.",
    "how does air quality affect COPD symptoms": "Poor air quality can worsen symptoms, so limit exposure to pollutants and allergens.",
    "what is pulmonary rehabilitation": "A structured program that includes exercise training, education, and support for individuals with lung diseases.",
    "how can I use an inhaler effectively": "Follow instructions from your healthcare provider; use a spacer if recommended for better medication delivery.",
    "what should I know about oxygen therapy": "Oxygen therapy can help maintain adequate oxygen levels; follow your provider’s instructions for use.",
    "how can I prevent respiratory infections with COPD": "Practice good hygiene, get vaccinated, and avoid close contact with sick individuals.",
    "what are the benefits of using a humidifier for COPD": "A humidifier can help keep airways moist, making it easier to breathe.",
    "how often should I see my healthcare provider for COPD management": "Regular follow-up appointments are essential for monitoring and adjusting your treatment plan.",
    "what role does nutrition play in COPD management": "A balanced diet can support overall health and help maintain a healthy weight, reducing the burden on your lungs.",
    
    # General chronic conditions
    "how can I effectively communicate with my healthcare team": "Be honest about your symptoms, ask questions, and express any concerns during your appointments.",
    "what role does nutrition play in managing my health condition": "Good nutrition supports overall health and helps manage conditions like hypertension, diabetes, and heart disease.",
    "how can I stay motivated to manage my health": "Set small, achievable goals, track your progress, and seek support from family, friends, or support groups.",
    "what are the benefits of physical activity for my condition": "Regular physical activity helps control weight, lowers blood pressure, improves heart health, and boosts mood.",
    "what should I know about my family history and its impact on my health": "Family history can influence your risk for certain conditions. Share this information with your healthcare provider for tailored advice.",
    "what resources are available for learning about my condition": "Many organizations provide educational materials, online resources, and support groups tailored to specific conditions.",
    "how can I balance managing my condition with everyday life": "Incorporate healthy habits into your daily routine, like meal prepping and scheduling medication reminders.",
    "what is an action plan for managing my condition": "An action plan outlines steps to take in daily management and what to do in case of emergencies.",
    "what should I do if I feel unwell or have new symptoms": "Contact your healthcare provider for guidance on how to proceed.",
    "how can I prepare for a doctor's appointment": "Make a list of questions, symptoms, and medications to discuss with your provider.",
    "what are some strategies for stress management": "Consider mindfulness, relaxation techniques, and engaging in hobbies you enjoy.",
    "how can I involve my family in my health management": "Share your goals and plans with family members and ask for their support in achieving them.",
    "what should I know about medication adherence": "Taking medications as prescribed is crucial for managing your condition and preventing complications.",
    "how often should I schedule follow-up appointments": "Follow your healthcare provider's recommendations for regular check-ups based on your condition.",
    "what is the importance of monitoring my symptoms": "Monitoring helps track your condition's progress and informs your healthcare provider about necessary adjustments.",
    "how can I find a support group for my condition": "Check with local hospitals, community centers, or online resources for support group listings.",
    "what should I know about advanced care planning": "Advanced care planning involves making decisions about future healthcare preferences and communicating them to your loved ones.",
    "how can I prevent complications from my condition": "Follow your treatment plan, make healthy lifestyle choices, and stay in communication with your healthcare provider.",
    "what role does hydration play in managing my health": "Staying hydrated is essential for overall health and can help manage certain conditions effectively.",
    "how can I set realistic goals for my health management": "Consider your current situation and break larger goals into smaller, manageable steps.",
    "what is the importance of sleep in managing chronic conditions": "Good sleep supports overall health, helps with recovery, and improves mood and energy levels.",
    "how can I track my progress in managing my condition": "Use a journal or an app to record symptoms, medication adherence, and lifestyle changes.",
}

# Function to get answer based on keywords and fuzzy matching
def get_answer(question):
    # Normalize the input
    question = question.strip().lower()
    
    # Use fuzzy matching to find the best response
    matched_question, score = process.extractOne(question, responses.keys())
    
    # Set a threshold for a match
    if score >= 80:  # You can adjust the threshold as needed
        return responses[matched_question]
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
