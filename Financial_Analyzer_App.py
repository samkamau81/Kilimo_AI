#streamlit app for the samart irrigation farm
#Framework supporting MLOps Apps
import streamlit as st 
import time
#Large Language Model Library
from langchain.llms import OpenAI
from decouple import config

openai_api_key=config('SECRET_KEY')


def generate_response(input_text):
    llm = OpenAI(temperature=0.3, openai_api_key=openai_api_key)
    output=llm(input_text)
    return output

def main():
    #Front-End
    with st.sidebar:
        st.markdown("<h1 style='text-align:center;font-family:Georgia'> 👨🏿‍🌾 Shamba Login </h1>",unsafe_allow_html=True)
        st.markdown("----")
        shamba = st.sidebar.text_input('Shamba ID')
        passwd = st.sidebar.text_input('Password',type='password')

        login_button=st.button("Login")

    # App framework
    st.markdown("<h1 style='text-align:center;font-family:Georgia'>💧OkoaMaji App </h1>",unsafe_allow_html=True)
    st.markdown("<h4 style='font-family:Georgia'>This app is designed to empower farmers with a user-friendly chatbot app that offers \n\
                    real-time guidance, personalized solutions, and valuable insights, enabling them to efficiently \n\
                    manage daily farming challenges and improve agricultural productivity. </h4>",unsafe_allow_html=True)
    st.markdown("-----")
    # User input field
    # Initialize chat history


    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "💧", "content": "Hey there, I'm your OkoaMaji Chatbot , here to advise you on \n\
                                        your agricultural needs. Ask literally anything 💧 "})
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            with st.spinner('Starting Bot ...'):
                st.markdown(message["content"])
        
    if (prompt := st.chat_input("What is up?")): 
    
        # Display user message in chat message container
        #user=👨🏿‍🌾
        with st.chat_message("👨🏿‍🌾"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "👨🏿‍🌾", "content": prompt})

        # Display assistant response in chat message container
        #assistant=💧
    # Display assistant response in chat message container
        with st.chat_message("💧"):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner('Wait for it...'):
                assistant_response = generate_response(prompt)

        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "💧", "content": full_response})


if __name__ == '__main__':
	main()