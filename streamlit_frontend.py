import streamlit as st
import requests

# Set the FastAPI backend URL
API_URL = "https://twingenapi-bggtahasg9b2gqck.centralindia-01.azurewebsites.net/messages/rag/"  # Change this if the backend URL is different
CLEAN_SESSION_URL = "https://twingenapi-bggtahasg9b2gqck.centralindia-01.azurewebsites.net/messages/clean_session/"  # URL for cleaning the session

st.title("Personalized Chatbot")

# User input
user_id = st.text_input("Enter your user ID:")
user_message = st.text_area("Type your message here:")

if st.button("Send"):
    if user_id and user_message:
        # Send the message to the backend
        response = requests.post(API_URL, json={"user_id": int(user_id), "content": user_message})
        
        if response.status_code == 200:
            reply = response.json().get("response")
            st.success(f"Bot: {reply}")
        else:
            st.error("Failed to get a response from the bot.")
    else:
        st.warning("Please enter both User ID and message.")

# Button to clean the Redis session
if st.button("Start New Session"):
    if user_id:
        # Clean the session by sending a DELETE request
        clean_response = requests.delete(f"{CLEAN_SESSION_URL}{user_id}")
        
        if clean_response.status_code == 200:
            st.success("Short-term memory cleared. You can start a new session.")
        else:
            st.error("Failed to clear short-term memory. It may not exist.")
    else:
        st.warning("Please enter your User ID to clean the session.")
