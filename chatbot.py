import streamlit as st 

st.title('chatbot ai')

st.chat_input('enter your message')

with st.sidebar :
    st.write ('this is sidebar')
    st.button ('sidebar')

import streamlit as st

st.title("My Chatbot 🤖")

# User input
user_message = st.text_input("You:", "")

# Simple chatbot responses
if user_message:
    if "hello" in user_message.lower():
        response = "Hi! How can I help you?"
    elif "how are you" in user_message.lower():
        response = "I am doing well. Thanks for asking!"
    elif "bye" in user_message.lower():
        response = "Goodbye! Have a great day."
    else:
        response = f"You said: {user_message}"

    st.write("🤖 Bot:", response)
