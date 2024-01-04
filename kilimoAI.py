#HomePage
import streamlit as st 

def button_click(url):
     



     
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


if __name__ == '__main__':
	main()