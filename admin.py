import streamlit as st

from admin_functions import *

# def admin():
st.subheader("Welcome Admin")
# doc_menu = ["Add Doctor", "Delete Doctor", "View all Doctors"]
# doc_choice = st.sidebar.selectbox("Doctor", doc_menu)

# cli_menu = ["Add Clinic", "Delete Clinic", "View all Clinics"]
# cli_choice = st.sidebar.selectbox("Clinic", cli_menu)

avail_menu = ["Assign Doctor to Clinic", "Delete Doctor From Clinic", "Update Doctor Timings"]
avail_choice = st.sidebar.selectbox("Clinic", avail_menu)

# doctor menu
# if doc_choice == "Add Doctor":
#     st.subheader("Enter Doctor Details")
#     add_doc()
# elif doc_choice == "Delete Doctor":
#     st.subheader("Enter DID of Doctor")
#     delete_doc()
# elif doc_choice == "View all Doctors":
#     st.subheader("Registered Doctors")
#     show_doctors()

# clinic menu
# if cli_choice == "Add Clinic":
#     st.subheader("Enter Clinic Details")
#     add_cli()

# elif cli_choice == "Delete Clinic":
#     st.subheader("Enter CID of Clinic")
#     delete_cli()

# elif cli_choice == "View all Clinics":
#     st.subheader("Registered Clinics")
#     show_clinics()

# availability menu
if avail_choice == "Assign Doctor to Clinic":
    st.subheader("Assign Doctor to Clinic")
    assign_to_clinic()

elif avail_choice == "Delete Doctor From Clinic":
    st.subheader("Delete Doctor From Clinic")
    delete_from_clinic()

elif avail_choice == "Update Doctor Timings":
    st.subheader("Update Doctor Timings")
    update_availability()
