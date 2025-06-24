import streamlit as st
import pickle
import numpy as np

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# App title
st.title("📧 Spam Message Detector")

# Input field
user_input = st.text_area("Enter a message to check:", height=150)

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Preprocess and predict
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        prob = np.max(model.predict_proba(input_vector)) * 100

        # Display result
        if prediction == 1:
            st.error(f"🚫 This is **Spam** ({prob:.2f}% confidence)")
        else:
            st.success(f"✅ This is **Ham** ({prob:.2f}% confidence)")
