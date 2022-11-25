import streamlit as st

from patient_functions import *

st.subheader("Welcome User")

menu = ["Book Appointment", "Show Appointments", "Cancel Appointment"]
choice = st.sidebar.selectbox("Appointments", menu)

if choice == "Book Appointment":
    st.subheader("Book Appointment")
    book_appointment()

elif choice == "Show Appointments":
    st.subheader("Appointments History")

elif choice == "Cancel Appointment":
    st.subheader("Cancel Appointment")
