import streamlit as st
import pandas as pd

from database import get_all_clinics, get_clinicID, get_doctors

def book_appointment():
    avail_clinics = [i[0] for i in get_all_clinics()]
    clinic = st.selectbox("Select Clinic:", avail_clinics)

    cid = get_clinicID(clinic)[0][0]
    avail_doctors = get_doctors(cid)
    avail_doctors_df = pd.DataFrame(avail_doctors, columns=['Doctor Name', 'Start Time', 'End Time'])

    with st.expander("Available Doctors"):
        st.dataframe(avail_doctors_df)
    
    doctor = st.selectbox("Select Doctor:", avail_doctors_df['Doctor Name'])
    appointment_date = st.date_input("Select Appointment Date:")

    if st.button("Book Appointment"):
        st.success("Appointment Booked Successfully")

def show_all_appointments():
    pass

def cancel_appointment():
    pass
# TODO : Take all appointments from show_all_appointments and let user select CID and DID only from the available ones

