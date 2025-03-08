# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 16:25:33 2025

@author: Admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Load saved models
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))
lungs_disease_model = pickle.load(open("lungs_disease_model.sav", 'rb'))
thyroid_model = pickle.load(open("Thyroid_model.sav", 'rb'))


# Function to set background image
def set_bg_image(image_url):
    """Set the full-screen background image for all prediction pages."""
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center fixed;
            background-size: cover;
        }}
        /* Text color fix for visibility */
        h1, h2, h3, h4, h5, h6, p, label, div, span, .stTextInput, .stSelectbox, .stNumberInput {{
            color: black !important;
        }}
        /* Button styling */
        .stButton>button {{
            color: black !important; 
            background-color: white !important;
            border: 2px solid black !important;
            font-weight: bold !important;
            padding: 10px !important;
            border-radius: 5px !important;
        }}
        .stButton>button:hover {{
            background-color: #f0f0f0 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Login Page Function
def login():
    """Login function with background image and authentication."""
    set_bg_image('https://i.ibb.co/mrRDr84Y/DALL-E-2025-03-08-15-20-10-A-high-definition-light-colored-background-image-designed-for-a-medical-d.webp')  # Login Page Background

    st.title("Login to Continue")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "Rakshitha" and password == "password123":  # Change credentials as needed
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid username or password")


# Initialize authentication session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Show login page if not authenticated
if not st.session_state["authenticated"]:
    login()
    st.stop()  # Stops execution until login is successful

else:
    # Apply Background for all prediction pages
    set_bg_image("https://i.ibb.co/TxvqGwfk/DALL-E-2025-03-08-16-43-26-A-modern-high-definition-medical-background-image-with-a-light-colored-th.webp")  # background image

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            'Multiple Disease Prediction System 🩺 ',
            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction', 'Lungs Disease Prediction', 'Thyroid Prediction'],
            icons=['activity', 'heart', 'person', 'lungs', 'capsule'],
            default_index=0
        )

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    # User input fields
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
    glucose = st.number_input('Glucose Level')
    blood_pressure = st.number_input('Blood Pressure Value')
    skin_thickness = st.number_input('Skin Thickness Value')
    insulin = st.number_input('Insulin Value')
    bmi = st.number_input('BMI Value')
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function Value')
    age = st.number_input('Age of the Person', min_value=1, step=1)

    if st.button('Diabetes Test Result'):
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                                insulin, bmi, diabetes_pedigree_function, age]])
        prediction = diabetes_model.predict(input_data)

        if prediction[0] == 1:
            st.warning("The person is Diabetic")
            
            # Health recommendations for diabetes
            st.subheader("Health Recommendations 🩺")
            st.info("✅ Follow a low-carb, high-fiber diet (avoid sugar & processed foods)")
            st.info("✅ Engage in at least 30 minutes of physical activity daily")
            st.info("✅ Monitor blood sugar levels regularly")
            st.info("✅ Stay hydrated and reduce stress")
            st.info("✅ Consult a doctor for medication & lifestyle guidance")

        else:
            st.success("The person is not Diabetic")

            # General diabetes prevention tips
            st.subheader("Diabetes Prevention Tips 🥗")
            st.info("✅ Maintain a healthy weight and exercise regularly")
            st.info("✅ Avoid sugary drinks and processed foods")
            st.info("✅ Include whole grains, vegetables, and lean proteins in your diet")
            st.info("✅ Get regular health check-ups and manage stress levels")

# ---------------- Heart Disease Prediction ----------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')

    age = st.text_input('Age')
    sex = st.text_input('Sex (0=Female, 1=Male)')
    cp = st.text_input('Chest Pain Type (0-3)')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholesterol in mg/dL')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL (0=No, 1=Yes)')
    restecg = st.text_input('Resting Electrocardiographic results (0-2)')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina (0=No, 1=Yes)')
    oldpeak = st.text_input('ST Depression induced by Exercise')
    slope = st.text_input('Slope of the Peak Exercise ST Segment (0-2)')
    ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (0-4)')
    thal = st.text_input('Thalassemia (1=Normal, 2=Fixed Defect, 3=Reversible Defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            input_data = np.array([
                int(float(age)), int(float(sex)), int(float(cp)), int(float(trestbps)), 
                int(float(chol)), int(float(fbs)), int(float(restecg)), int(float(thalach)), 
                int(float(exang)), float(oldpeak), int(float(slope)), int(float(ca)), int(float(thal))
            ]).reshape(1, -1)

            heart_prediction = heart_disease_model.predict(input_data)
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
                st.warning(heart_diagnosis)

                # Health Recommendations for Heart Disease
                st.subheader("Health Recommendations ❤️")
                st.info("✅ Maintain a heart-healthy diet (low salt, low fat, more vegetables)")
                st.info("✅ Exercise regularly (30 minutes of moderate activity per day)")
                st.info("✅ Manage stress with relaxation techniques like meditation")
                st.info("✅ Monitor blood pressure and cholesterol levels")
                st.info("✅ Avoid smoking and excessive alcohol consumption")
                st.info("✅ Consult a cardiologist for further evaluation")

            else:
                heart_diagnosis = 'The person does not have heart disease'
                st.success(heart_diagnosis)

                # General Heart Health Tips
                st.subheader("Heart Health Tips 🏃‍♂️")
                st.info("✅ Eat a balanced diet with healthy fats")
                st.info("✅ Stay physically active and maintain a healthy weight")
                st.info("✅ Get regular check-ups to monitor heart health")
                st.info("✅ Stay hydrated and manage stress effectively")

        except ValueError:
            st.error("⚠ Please enter valid numerical values.")

    st.success(heart_diagnosis)


# ---------------- Parkinson's Disease Prediction ----------------
if selected == 'Parkinsons Disease Prediction':
    st.title('Parkinson’s Disease Prediction Using ML')

    # User input fields for Parkinson's prediction
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    jitter_percent = st.text_input('MDVP:Jitter(%)')
    jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    rap = st.text_input('MDVP:RAP')
    ppq = st.text_input('MDVP:PPQ')
    ddp = st.text_input('Jitter:DDP')
    shimmer = st.text_input('MDVP:Shimmer')
    shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    shimmer_apq3 = st.text_input('Shimmer:APQ3')
    shimmer_apq5 = st.text_input('Shimmer:APQ5')
    apq = st.text_input('MDVP:APQ')
    shimmer_dda = st.text_input('Shimmer:DDA')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    rpde = st.text_input('RPDE')
    dfa = st.text_input('DFA')
    spread1 = st.text_input('Spread1')
    spread2 = st.text_input('Spread2')
    d2 = st.text_input('D2')
    ppe = st.text_input('PPE')
    
    #parkinsons disease prediction

    if st.button('Parkinson’s Disease Test Result'):
        try:
            input_data = np.array([[
                float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs), 
                float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db), 
                float(shimmer_apq3), float(shimmer_apq5), float(apq), float(shimmer_dda), 
                float(nhr), float(hnr), float(rpde), float(dfa), float(spread1), float(spread2), 
                float(d2), float(ppe)
            ]]).reshape(1, -1)

            parkinsons_prediction = parkinsons_model.predict(input_data)

            if parkinsons_prediction[0] == 1:
                st.warning("The person has Parkinson’s disease")

                # Health recommendations for Parkinson’s
                st.subheader("Health Recommendations 🏥")
                st.info("✅ Engage in regular exercise like walking, swimming, or yoga")
                st.info("✅ Maintain a healthy diet rich in antioxidants (e.g., berries, nuts, green vegetables)")
                st.info("✅ Consider physical therapy for mobility and balance improvement")
                st.info("✅ Manage stress through relaxation techniques")
                st.info("✅ Consult a neurologist for appropriate medication and therapies")

            else:
                st.success("The person does not have Parkinson’s disease")

                # General tips for nervous system health
                st.subheader("Brain Health Tips 🧠")
                st.info("✅ Stay physically and mentally active (puzzles, reading, learning new skills)")
                st.info("✅ Maintain a balanced diet with Omega-3 fatty acids")
                st.info("✅ Get enough sleep and reduce stress")
                st.info("✅ Avoid smoking and excessive alcohol consumption")
                st.info("✅ Regularly consult a doctor for neurological check-ups")

        except ValueError:
            st.error("⚠ Please enter valid numerical values.")

# ---------------- Lungs Disease Prediction ----------------
if selected == 'Lungs Disease Prediction':
    st.title('Lung Disease Prediction Using ML')

    # User input fields for Lung Disease prediction
    gender = st.text_input('Gender (0=Female, 1=Male)')
    age = st.text_input('Age')
    smoking = st.text_input('Smoking (1=Yes, 2=No)')
    yellow_fingers = st.text_input('Yellow Fingers (1=Yes, 2=No)')
    anxiety = st.text_input('Anxiety (1=Yes, 2=No)')
    peer_pressure = st.text_input('Peer Pressure (1=Yes, 2=No)')
    chronic_disease = st.text_input('Chronic Disease (1=Yes, 2=No)')
    fatigue = st.text_input('Fatigue (1=Yes, 2=No)')
    allergy = st.text_input('Allergy (1=Yes, 2=No)')
    wheezing = st.text_input('Wheezing (1=Yes, 2=No)')
    alcohol_consuming = st.text_input('Alcohol Consuming (1=Yes, 2=No)')
    coughing = st.text_input('Coughing (1=Yes, 2=No)')
    shortness_of_breath = st.text_input('Shortness of Breath (1=Yes, 2=No)')
    swallowing_difficulty = st.text_input('Swallowing Difficulty (1=Yes, 2=No)')
    chest_pain = st.text_input('Chest Pain (1=Yes, 2=No)')

    if st.button('Lungs Disease Test Result'):
        try:
            input_data = np.array([[
                int(float(gender)), int(float(age)), int(float(smoking)), int(float(yellow_fingers)), 
                int(float(anxiety)), int(float(peer_pressure)), int(float(chronic_disease)), int(float(fatigue)), 
                int(float(allergy)), int(float(wheezing)), int(float(alcohol_consuming)), int(float(coughing)), 
                int(float(shortness_of_breath)), int(float(swallowing_difficulty)), int(float(chest_pain))
            ]]).reshape(1, -1)

            lungs_disease_prediction = lungs_disease_model.predict(input_data)

            if lungs_disease_prediction[0] == 1:
                st.warning("The Person has Lung Disease")

                # Health recommendations for lung disease
                st.subheader("Health Recommendations 🏥")
                st.info("✅ Quit smoking and avoid second-hand smoke exposure 🚭")
                st.info("✅ Perform breathing exercises and lung rehabilitation 🏃‍♂️")
                st.info("✅ Stay hydrated and consume a diet rich in vitamins 🍎")
                st.info("✅ Use air purifiers to reduce allergens and pollutants 🌬️")
                st.info("✅ Seek medical attention for persistent symptoms or breathing difficulties 👨‍⚕️")

            else:
                st.success("The Person does not have Lung Disease")

                # General lung health tips
                st.subheader("Lung Health Tips 🫁")
                st.info("✅ Exercise regularly to strengthen lung capacity 🏋️")
                st.info("✅ Maintain proper posture to support deep breathing 📏")
                st.info("✅ Get vaccinations like flu shots to prevent respiratory infections 💉")
                st.info("✅ Practice deep breathing exercises for lung expansion 🧘")
                st.info("✅ Avoid exposure to pollutants and chemicals 🚧")

        except ValueError:
            st.error("⚠ Please enter valid numerical values.")


# ---------------- Thyroid Prediction ----------------
if selected == 'Thyroid Prediction':
    st.title('Thyroid Disease Prediction Using ML')

    # User input fields for Thyroid prediction
    age = st.text_input('Age')
    sex = st.text_input('Sex (0=Female, 1=Male)')
    on_thyroxine = st.text_input('On Thyroxine (0=No, 1=Yes)')
    tsh = st.text_input('TSH (Thyroid-Stimulating Hormone Level)')
    t3_measured = st.text_input('T3 Measured (0=No, 1=Yes)')
    t3 = st.text_input('T3 (Triiodothyronine Level)')
    tt4 = st.text_input('TT4 (Total Thyroxine Level)')

    if st.button('Thyroid Test Result'):
        try:
            input_data = np.array([[
                int(float(age)), int(float(sex)), int(float(on_thyroxine)), float(tsh), 
                int(float(t3_measured)), float(t3), float(tt4)
            ]]).reshape(1, -1)

            thyroid_prediction = thyroid_model.predict(input_data)

            if thyroid_prediction[0] == 1:
                st.warning("The Person has Thyroid Disease")

                # Health recommendations for thyroid disease
                st.subheader("Health Recommendations 🏥")
                st.info("✅ Follow a balanced diet rich in iodine and selenium 🍎")
                st.info("✅ Take prescribed thyroid medications as directed 💊")
                st.info("✅ Monitor your thyroid hormone levels regularly 📊")
                st.info("✅ Reduce stress through yoga or meditation 🧘")
                st.info("✅ Stay physically active and maintain a healthy weight 🏃‍♂️")

            else:
                st.success("The Person does not have Thyroid Disease")

                # General thyroid health tips
                st.subheader("Thyroid Health Tips 🦋")
                st.info("✅ Eat iodine-rich foods like fish, dairy, and eggs 🐟")
                st.info("✅ Limit processed foods and excessive soy intake ❌")
                st.info("✅ Stay hydrated and maintain proper nutrition 🥗")
                st.info("✅ Get enough sleep to regulate hormone balance 😴")
                st.info("✅ Avoid excessive stress, as it can impact thyroid function 🧘‍♀️")

        except ValueError:
            st.error("⚠ Please enter valid numerical values.")


    