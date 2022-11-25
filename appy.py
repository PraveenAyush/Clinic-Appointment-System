from database import authenticate_admin
import streamlit as st

# from admin import login_admin

headerSection = st.container()
loginSection = st.container()


def login_admin():
    with loginSection:
        uName = st.text_input("Username:")
        pwd = st.text_input("Password:")

        if st.button("Login"):
            if authenticate_admin(uName, pwd):
                st.success(f"Login Successful for {uName}")

def main():
    with headerSection:
        st.title("Clinic Appointment System")
        st.subheader("Login to get a Consultation")
        if st.button("Patient Login"):
            pass
        if st.button("Admin Login"):
            login_admin()



if __name__ == '__main__':
    main()
