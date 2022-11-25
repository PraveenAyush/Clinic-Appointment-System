import pandas as pd
import streamlit as st

from database import add_doctor, delete_doctor, show_all_doctors, add_clinic, delete_clinic, show_all_clinics, get_all_CID, get_all_DID, assign_doctor_to_clinic, delete_assigned_doctor, update_doctor_timing

# doctor section
def add_doc():
    name = st.text_input("Doctor Name:")
    gender = st.selectbox("Gender:", ["Male", "Female"])
    experience = st.number_input("Experience in Years:")
    specialization = st.text_input("Specialization:")
    phone = st.text_input("Phone_No")

    if st.button("Submit"):
        add_doctor(name, gender, experience, specialization, phone)
        st.success(f"Successfully added Doctor {name}")


def delete_doc():
    did = st.number_input("DID:")

    if st.button("Delete"):
        delete_doctor(did)
        st.success(f"Doctor DID {did} successfully deleted")


def show_doctors():
    data = show_all_doctors()

    df = pd.DataFrame(data, columns=[
                      'DID', 'Name', 'Gender', 'Experience', 'Specialization', 'Phone No.', 'Start Date'])
    st.dataframe(df)


# clinic section
def add_cli():
    name = st.text_input("Clinic Name:")
    adr1 = st.text_input("Address Line 1:")
    adr2 = st.text_input("Address Line 2:")
    city = st.text_input("City:")
    state = st.text_input("State:")
    phone = st.text_input("Phone_No")

    if st.button("Submit"):
        add_clinic(name, adr1, adr2, city, state, phone)
        st.success(f"Successfully added Clinic {name}")


def delete_cli():
    cid = st.number_input("CID:")

    if st.button("Delete"):
        delete_clinic(cid)
        st.success(f"Clinic CID {cid} successfully deleted")


def show_clinics():
    data = show_all_clinics()

    df = pd.DataFrame(data, columns=[
                      'CID', 'Name', 'Address Line 1', 'Address Line 2', 'City', 'State', 'Phone No.'])
    st.dataframe(df)


# availability menu
def assign_to_clinic():
    availableCID = [i[0] for i in get_all_CID()]
    cid = st.selectbox("CID:", availableCID)

    availableDID = [i[0] for i in get_all_DID()]
    did = st.selectbox("DID:", availableDID)
    day = st.text_input("Day:")
    start = st.time_input("Start Time:")
    end = st.time_input("End Time:")

    if st.button("Submit"):
        assign_doctor_to_clinic(cid, did, day, start, end)
        st.success("Doctor Assigned successfully")
    
def delete_from_clinic():
    availableCID = [i[0] for i in get_all_CID()]
    cid = st.selectbox("CID:", availableCID)

    availableDID = [i[0] for i in get_all_DID()]
    did = st.selectbox("DID:", availableDID)

    if st.button("Delete"):
        delete_assigned_doctor(cid, did)
        st.success("Record deleted successfully")

def update_availability():
    availableCID = [i[0] for i in get_all_CID()]
    cid = st.selectbox("CID:", availableCID)

    availableDID = [i[0] for i in get_all_DID()]
    did = st.selectbox("DID:", availableDID)
    new_day = st.text_input("Day:")
    new_start = st.time_input("Start Time:")
    new_end = st.time_input("End Time:")

    if st.button("Submit"):
        update_doctor_timing(cid, did, new_day, new_start,new_end)
        st.success("Record Updated successfully")
