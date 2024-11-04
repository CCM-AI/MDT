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

{"question": "What is diabetes?", "answer": "Diabetes is a chronic condition characterized by high blood sugar levels due to insulin production or use issues."},
        {"question": "What are the different types of diabetes?", "answer": "The main types are Type 1 diabetes, Type 2 diabetes, and gestational diabetes."},
        {"question": "What are the symptoms of diabetes?", "answer": "Symptoms include increased thirst, frequent urination, extreme fatigue, blurred vision, and slow-healing sores."},
        {"question": "How is diabetes diagnosed?", "answer": "Diabetes is diagnosed through blood tests, including fasting blood sugar, oral glucose tolerance test, or HbA1c test."},
        {"question": "What are the long-term complications of diabetes?", "answer": "Complications can include heart disease, kidney damage, neuropathy, and eye problems."},
        {"question": "How can I manage my diabetes?", "answer": "Management includes monitoring blood sugar levels, healthy eating, regular exercise, and medication as prescribed."},
        {"question": "What is the role of insulin in diabetes?", "answer": "Insulin is a hormone that helps cells absorb glucose; in diabetes, insulin function or production is impaired."},
        {"question": "How does diet impact diabetes management?", "answer": "A balanced diet that controls carbohydrate intake is crucial for managing blood sugar levels."},
        {"question": "What is the significance of blood sugar monitoring?", "answer": "Regular monitoring helps track blood sugar levels and manage diabetes effectively."},
        {"question": "What lifestyle changes can help prevent Type 2 diabetes?", "answer": "Healthy eating, regular physical activity, and maintaining a healthy weight can reduce the risk."},
        {"question": "What are the risks associated with uncontrolled diabetes?", "answer": "Uncontrolled diabetes can lead to serious health complications such as heart disease, nerve damage, and kidney failure."},
        {"question": "How often should I check my blood sugar?", "answer": "The frequency depends on your treatment plan; those on insulin may need to check several times a day."},
        {"question": "What is the glycemic index?", "answer": "The glycemic index ranks foods based on their effect on blood sugar levels; low GI foods are preferred for diabetes management."},
        {"question": "Can diabetes be reversed?", "answer": "Type 2 diabetes can sometimes be reversed through significant lifestyle changes, while Type 1 is managed, not reversed."},
        {"question": "What medications are commonly used to treat diabetes?", "answer": "Medications include metformin, insulin, sulfonylureas, and GLP-1 receptor agonists."},
        {"question": "What should I do if my blood sugar is too low?", "answer": "Consume fast-acting carbohydrates like glucose tablets or fruit juice and seek medical attention if symptoms persist."},
        {"question": "How does physical activity affect blood sugar levels?", "answer": "Regular exercise helps lower blood sugar levels and increases insulin sensitivity."},
        {"question": "What are some common myths about diabetes?", "answer": "Common myths include that diabetes is caused by eating too much sugar and that people with diabetes cannot eat carbohydrates."},
        {"question": "What is diabetic neuropathy?", "answer": "Diabetic neuropathy is nerve damage caused by high blood sugar, leading to pain, numbness, or weakness."},
        {"question": "How does stress affect diabetes?", "answer": "Stress can raise blood sugar levels, making it essential to manage stress effectively."},
        {"question": "What is the role of carbohydrates in diabetes?", "answer": "Carbohydrates affect blood sugar levels; it's important to monitor and manage carb intake."},
        {"question": "Can I drink alcohol if I have diabetes?", "answer": "Moderate alcohol consumption may be safe for some people with diabetes, but it can affect blood sugar levels."},
        {"question": "What are the signs of high blood sugar?", "answer": "Signs include increased thirst, frequent urination, fatigue, and blurred vision."},
        {"question": "What is the importance of foot care for diabetics?", "answer": "Proper foot care is crucial to prevent infections and complications, as diabetes can impair circulation and sensation."},
        {"question": "How can I educate my family about diabetes?", "answer": "Share reliable resources and involve them in your management plan to enhance their understanding."},
        {"question": "What is the importance of regular check-ups for diabetes?", "answer": "Regular check-ups help monitor blood sugar levels and assess for potential complications."},
        {"question": "What are some effective weight management strategies for diabetics?", "answer": "Strategies include portion control, regular exercise, and balanced meal planning."},
        {"question": "Can diabetes lead to heart disease?", "answer": "Yes, diabetes significantly increases the risk of developing heart disease."},
        {"question": "What is the role of fiber in diabetes management?", "answer": "Dietary fiber helps regulate blood sugar levels and improves digestive health."},
        {"question": "What is gestational diabetes?", "answer": "Gestational diabetes is a type of diabetes that develops during pregnancy and usually resolves after childbirth."},
        {"question": "How can I prevent diabetes complications?", "answer": "Control blood sugar levels, maintain a healthy lifestyle, and attend regular medical check-ups."},
        {"question": "What are the signs of low blood sugar?", "answer": "Signs include shakiness, sweating, confusion, irritability, and dizziness."},
        {"question": "How can I stay motivated to manage my diabetes?", "answer": "Setting realistic goals, tracking progress, and seeking support from healthcare providers and peers can help."},
        {"question": "Can I have a normal pregnancy with diabetes?", "answer": "Yes, with careful management and monitoring, many women with diabetes can have healthy pregnancies."},
        {"question": "What is the connection between diabetes and vision problems?", "answer": "Diabetes can lead to diabetic retinopathy, which can cause vision loss."},
        {"question": "How can I incorporate exercise into my daily routine?", "answer": "Find activities you enjoy, set a regular schedule, and start gradually to make exercise a habit."},
        {"question": "What are some healthy snack options for diabetics?", "answer": "Healthy snacks include nuts, yogurt, fruit, and raw vegetables."},
        {"question": "What are the differences between Type 1 and Type 2 diabetes?", "answer": "Type 1 diabetes is an autoimmune condition with no insulin production, while Type 2 involves insulin resistance."},
        {"question": "What should I include in my diabetes management plan?", "answer": "A management plan should include medication, diet, exercise, and regular monitoring of blood sugar."},
        {"question": "How does diabetes affect mental health?", "answer": "Living with diabetes can lead to stress, anxiety, and depression due to the challenges of managing the condition."},
        {"question": "What are some tips for dining out with diabetes?", "answer": "Review the menu ahead of time, choose healthier options, and consider portion sizes when ordering."},
        {"question": "How can I manage diabetes while traveling?", "answer": "Plan ahead by packing snacks, monitoring blood sugar regularly, and maintaining your medication schedule."},
        {"question": "What is continuous glucose monitoring?", "answer": "Continuous glucose monitoring involves using a device to track blood sugar levels throughout the day and night."},
        {"question": "What should I know about diabetes medications?", "answer": "Understand how each medication works, its side effects, and how it fits into your overall management plan."},
        {"question": "How can I support a loved one with diabetes?", "answer": "Be supportive, offer to help with meal planning, encourage regular check-ups, and listen to their concerns."},
        {"question": "What role does technology play in diabetes management?", "answer": "Technology like apps, continuous glucose monitors, and insulin pens can help track and manage diabetes more effectively."},
        {"question": "What is the importance of hydration for diabetics?", "answer": "Staying hydrated helps regulate blood sugar levels and supports overall health."},
        {"question": "What are the potential side effects of diabetes medications?", "answer": "Side effects vary by medication but may include nausea, weight gain, or low blood sugar."},
        {"question": "What should I do if I miss a dose of my diabetes medication?", "answer": "Take the missed dose as soon as you remember, but skip it if it's almost time for the next dose."},
        {"question": "How can I help my children understand diabetes?", "answer": "Use age-appropriate resources and involve them in your management plan to foster understanding."},
        {"question": "What resources are available for diabetes education?", "answer": "Diabetes education programs, online resources, and support groups can provide valuable information and support."},
    ]
    
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
    "how does diabetes affect heart health": "Diabetes increases the risk of heart disease due to associated factors like high blood pressure and cholesterol.",
    "what is coronary artery disease": "Coronary artery disease occurs when the coronary arteries become narrowed or blocked, leading to reduced blood flow to the heart.",
    "how can I monitor my heart health at home": "You can track your blood pressure, heart rate, and maintain a healthy lifestyle.",
    "what is the importance of regular check-ups for heart health": "Regular check-ups help monitor risk factors and catch issues early.",
    
    # Asthma
    "what is asthma": "Asthma is a chronic condition that affects the airways, causing wheezing, shortness of breath, and coughing.",
    "what triggers asthma attacks": "Common triggers include allergens, smoke, exercise, cold air, and respiratory infections.",
    "how is asthma diagnosed": "Asthma is diagnosed based on medical history, symptoms, and tests like lung function tests.",
    "what are the symptoms of asthma": "Symptoms include wheezing, coughing, chest tightness, and difficulty breathing.",
    "how can I manage asthma symptoms": "Management includes avoiding triggers, using medications like inhalers, and following an asthma action plan.",
    "what types of medications are used to treat asthma": "Medications include quick-relief inhalers for immediate symptoms and long-term control medications.",
    "what is an asthma action plan": "An asthma action plan outlines how to manage asthma symptoms, including when to use medications and seek help.",
    "how can I avoid asthma triggers": "Identify and minimize exposure to known triggers, such as allergens and irritants.",
    "what should I do during an asthma attack": "Use your quick-relief inhaler and seek medical help if symptoms do not improve.",
    "how does exercise affect asthma": "Exercise can benefit asthma control if managed carefully; warm up properly and avoid triggers.",
    "what are the long-term effects of uncontrolled asthma": "Uncontrolled asthma can lead to permanent changes in lung function and increased risk of severe attacks.",
    "how can I tell if my asthma is well-controlled": "Well-controlled asthma means fewer symptoms, no nighttime awakenings, and no limitations on activities.",
    "what is the role of allergy testing in asthma management": "Allergy testing can help identify triggers and guide management strategies.",
    "how often should I see my doctor for asthma management": "Regular follow-ups with your healthcare provider are important for managing asthma effectively.",
    "what is the difference between asthma and COPD": "Asthma is usually reversible and often triggered by allergens, while COPD is a progressive disease typically linked to smoking.",
    "what lifestyle changes can help manage asthma": "Avoiding smoking, maintaining a healthy weight, and managing allergies can help.",
    "how does weather affect asthma": "Extreme weather conditions can trigger asthma symptoms; cold air and humidity are common triggers.",
    "what is peak flow monitoring": "Peak flow monitoring measures how well air moves out of your lungs, helping to manage asthma.",
    
    "how often should I review my asthma management plan with my doctor": 
        "You should review your asthma management plan at least once a year or whenever there are changes in your symptoms or medication.",
    
    "can environmental changes improve my asthma": 
        "Yes, moving to a location with less pollution or allergens can improve asthma symptoms for some individuals.",
    
    "what is a spacer, and how does it help with inhalers": 
        "A spacer is a device that attaches to inhalers, helping to deliver medication more effectively to the lungs.",
    
    "how can I prepare for asthma triggers during seasonal changes": 
        "Prepare by monitoring pollen counts, adjusting your medication as needed, and minimizing outdoor activities during high-risk times.",
    
    "can obesity affect my asthma control": 
        "Yes, obesity can make asthma symptoms worse and complicate treatment, so weight management is important.",
    
    "are there any new treatments for asthma": 
        "New treatments such as biologics target specific asthma pathways and can be effective for severe asthma cases.",
    
    "what role does the immune system play in asthma": 
        "In asthma, the immune system overreacts to allergens, causing inflammation and airway constriction.",
    
    "can I use essential oils to manage asthma symptoms": 
        "While some people find essential oils helpful, they may trigger symptoms in others, so consult your doctor before use.",
    
    "what should I include in my asthma emergency kit": 
        "Include your rescue inhaler, spacer, a copy of your asthma action plan, and any other necessary medications.",
    
    "what impact does sleep have on asthma": 
        "Poor sleep can exacerbate asthma symptoms and reduce overall health, so maintaining good sleep hygiene is important.",
    
    "how can I help my child manage their asthma": 
        "Educate them about asthma, help create a management plan, and work with their school to ensure a safe environment.",
    
    "what is the link between asthma and sinus infections": 
        "Sinus infections can exacerbate asthma symptoms due to increased mucus production and inflammation.",
    
    "how can I improve indoor air quality for my asthma": 
        "Use air purifiers, avoid smoking indoors, regularly clean to reduce dust, and maintain humidity levels.",
    
    "can I have both asthma and COPD": 
        "Yes, having both conditions is possible, and it is referred to as asthma-COPD overlap syndrome.",
    
    "how can I recognize if my child has asthma": 
        "Look for symptoms such as wheezing, frequent coughing, and difficulty breathing during physical activity.",
    
    "what are some tips for managing asthma during cold and flu season": 
        "Get vaccinated, wash hands frequently, avoid close contact with sick individuals, and follow your asthma action plan.",
    
    "can I eat anything specific to help with asthma": 
        "Eating a diet rich in fruits, vegetables, and omega-3 fatty acids may help reduce inflammation and improve lung health.",
    
    "what should I do if I forget to take my asthma medication": 
        "Take the missed dose as soon as you remember unless it’s close to the next dose; in that case, skip the missed dose and continue with your schedule.",
    
    "what is the role of allergists in asthma management": 
        "Allergists specialize in diagnosing and managing allergies that may trigger asthma symptoms and can provide targeted treatments.",
    
    "can stress management techniques help control asthma": 
        "Yes, techniques such as deep breathing, meditation, and yoga can help reduce stress, which may improve asthma control.",
    
    "how can I encourage someone with asthma to adhere to their treatment plan": 
        "Offer support, educate them about the importance of their medication, and help them track their symptoms and medication use.",
    
    "can I travel internationally with asthma": 
        "Yes, but be sure to carry your medications, understand the air quality at your destination, and have a plan in case of an emergency.",
    
    "how do changes in altitude affect asthma": 
        "Higher altitudes can sometimes exacerbate asthma symptoms due to lower oxygen levels; consult your doctor before traveling to high altitudes.",
    
    "can I still have a normal life with asthma": 
        "Yes, with proper management, most people with asthma can lead normal, active lives.",
    
    "what are the best ways to stay active with asthma": 
        "Choose low-impact activities, warm up before exercising, and use a rescue inhaler before exercise if necessary.",
    
    "how does humidity affect asthma": 
        "High humidity can increase the risk of mold and dust mites, while low humidity can dry out the airways, both potentially triggering symptoms.",
    
    "what is the importance of hydration for asthma management": 
        "Staying hydrated helps keep mucus thin and easier to expel, reducing the likelihood of airway blockage.",
    
    "can you outgrow asthma": 
        "Some children may outgrow asthma, but for others, it can persist into adulthood.",
    
    "how do I know if my asthma medication is working": 
        "You should experience fewer symptoms, less need for rescue inhalers, and improved peak flow readings.",
    
    "what should I do if I experience side effects from my asthma medication": 
        "Report any side effects to your healthcare provider, who may adjust your treatment plan accordingly.",
   # COPD 
    "what is your COPD": "Chronic Obstructive Pulmonary Disease is a lung disease that blocks airflow and makes breathing difficult.",
    "what are the symptoms of COPD": "Symptoms include chronic cough, shortness of breath, and frequent respiratory infections.",
    "how is COPD diagnosed": "COPD is diagnosed through lung function tests, imaging, and a review of symptoms.",
    "what are the stages of COPD": "COPD is staged from mild to very severe based on symptoms and lung function tests.",
    "what treatments are available for COPD": "Treatment may include bronchodilators, steroids, oxygen therapy, and pulmonary rehabilitation.",
    "how can I manage my COPD symptoms": "Avoid smoking, follow treatment plans, and engage in regular physical activity to help manage symptoms.",
    "what lifestyle changes can help with COPD": "Healthy eating, staying active, and avoiding pollutants can improve quality of life.",
    "how does smoking affect COPD": "Smoking is the leading cause of COPD; quitting can slow disease progression and improve symptoms.",
    "what should I do if I have difficulty breathing": "Seek medical help immediately if you're having severe difficulty breathing or a sudden worsening of symptoms.",
    "how can pulmonary rehabilitation help me": "Pulmonary rehabilitation provides education, exercise training, and support to help manage COPD.",
    "what role does oxygen therapy play in COPD treatment": "Oxygen therapy can help those with low oxygen levels breathe more easily and improve quality of life.",
    "what are the complications of COPD": "Complications can include heart disease, lung infections, and pulmonary hypertension.",
    "how can I tell if my COPD is getting worse": "Increased shortness of breath, more frequent exacerbations, and changes in sputum can indicate worsening COPD.",
    "what is a COPD action plan": "A COPD action plan outlines steps to take during exacerbations and daily management strategies.",
    "how can I recognize an exacerbation of COPD": "Symptoms may include increased cough, wheezing, and difficulty breathing that worsen over a few days.",
    "what is the importance of vaccinations for people with COPD": "Vaccinations can help prevent respiratory infections that can worsen COPD symptoms.",
    "how does air pollution affect COPD": "Air pollution can irritate the lungs and worsen symptoms in people with COPD.",
    "what are some tips for managing COPD at home": "Create a clean air environment, follow your medication plan, and stay active within your limits.",

}

def find_best_match(user_input):
    # Find the best match for the user input from the responses dictionary
    best_match = process.extractOne(user_input, responses.keys())
    return best_match[0] if best_match[1] > 60 else None  # Only return if confidence > 60%

def main():
    st.title("Health Inquiry Assistant")
    st.write("Ask your health-related questions and receive accurate information.")

    user_input = st.text_input("Type your question here:")

    if st.button("Get Answer"):
        if user_input:
            best_match = find_best_match(user_input.lower())
            if best_match:
                response = responses[best_match]
                st.success(response)
            else:
                st.warning("Sorry, I don't have an answer for that question. Please try asking something else.")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
