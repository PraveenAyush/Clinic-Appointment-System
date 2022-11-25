import streamlit as st

from admin import admin
from database import authenticate_user

headerSection = st.container()
loginSelection = st.container()
mainSection = st.container()


def login_clicked(uName, pwd):
    uType= authenticate_user(uName, pwd)[0][0]
    if uType is not None:
        st.session_state['loggedIn'] = True
        st.session_state['user_type'] = uType
        st.success(f"Login Successful for {uType}")
    else:
        st.session_state['loggedIn'] = False


def show_login():
    with loginSelection:
        if st.session_state['loggedIn'] == False:
            uName = st.text_input("Username:")
            pwd = st.text_input("Password:")

            st.button('Login', on_click=login_clicked, args=(uName, pwd))
            # return authenticate_user(uName, pwd)[0][0]

def main():
    with headerSection:
        st.title("Clinic Appointment System")
        if 'loggedIn' not in st.session_state:
            st.session_state['user_type'] = None
            st.session_state['loggedIn'] = False
            st.subheader("Login")
            show_login()
        else:
            if st.session_state['loggedIn']:
                main_page(st.session_state['user_type'])
            else:
                st.subheader("Login")
                show_login()
    
def main_page(uType):
    with mainSection:
        if uType == 'Admin':
            st.subheader("Welcome Admin")
            admin()

if __name__ == '__main__':
    main()
