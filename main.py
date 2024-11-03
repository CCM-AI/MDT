import streamlit as st

# Sample responses for common questions
responses = {
    "What is your name?": "I am the AI assistant for the MDT team.",
    "What is the role of the MDT?": "The MDT team collaborates to provide comprehensive patient care.",
    "How can I contact a doctor?": "You can reach out to your doctor via the patient portal or contact the clinic directly.",
    "What should I do if I have a medical emergency?": "Please call emergency services or go to the nearest emergency room immediately."
}

st.title("MDT AI Assistant")
question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    answer = responses.get(question, "I'm sorry, I don't have an answer for that.")
    st.write(answer)
