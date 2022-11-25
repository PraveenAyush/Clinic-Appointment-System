import mariadb
from datetime import date, datetime

mydb = mariadb.connect(
    host="localhost",
    user="root",
    database="appointment_booking"
)
cur = mydb.cursor()


# login portion
def authenticate_patient(uName, pwd):
    cur.execute(f"SELECT Name FROM patient WHERE Username = '{uName}' and Password = '{pwd}'")
    data = cur.fetchall()
    return data[0][0]

def authenticate_admin(uName, pwd):
    cur.execute(f"SELECT Username FROM admin WHERE Username = '{uName}' and Password = '{pwd}'")
    data = cur.fetchall()
    return data[0][0]


# admin-doctor portion
def add_doctor(name, gender, experience, specialization, phone):
    cur.execute(f"INSERT INTO doctors (Name, Gender, Experience, Specialisation, Phone_No, Start_Date) VALUES ('{name}','{gender}',{experience},'{specialization}','{phone}','{date.today()}')")
    mydb.commit()

def delete_doctor(d_id):
    cur.execute(f"DELETE FROM doctors WHERE DID = {d_id}")
    mydb.commit()

def show_all_doctors():
    cur.execute("SELECT * FROM doctors")
    data = cur.fetchall()
    return data


# admin-clinic portion
def add_clinic(name, adr_1, adr_2, city, state, phone):
    cur.execute(
        f"INSERT INTO clinic (Name, Address_Line_1, Address_Line_2, City, State, Phone_No) VALUES ('{name}','{adr_1}','{adr_2}','{city}','{state}','{phone}')")
    mydb.commit()

def delete_clinic(c_id):
    cur.execute(f"DELETE FROM clinic WHERE CID = {c_id}")
    mydb.commit()

def show_all_clinics():
    cur.execute("SELECT * FROM clinic")
    data = cur.fetchall()
    return data


# admin-availibility portion
def get_all_CID():
    cur.execute("SELECT CID FROM clinic")
    data = cur.fetchall()
    return data

def get_all_DID():
    cur.execute("SELECT DID FROM doctors")
    data = cur.fetchall()
    return data

def assign_doctor_to_clinic(c_id, d_id, day, start, end):
    cur.execute(f"INSERT INTO doctor_available (CID, DID, Day, Start_Time, End_Time) VALUES ({c_id}, {d_id}, '{day}', '{start}', '{end}')")
    mydb.commit()

def delete_assigned_doctor(c_id, d_id):
    cur.execute(f"DELETE FROM doctor_available WHERE CID = {c_id} AND DID = {d_id}")
    mydb.commit()

def update_doctor_timing(c_id, d_id, new_day, new_start, new_end):
    cur.execute(f"UPDATE doctor_available SET Day = '{new_day}', Start_Time = '{new_start}', End_Time = '{new_end}' WHERE CID = {c_id} AND DID = {d_id}")
    mydb.commit()


# patient portion
def get_all_clinics():
    cur.execute("SELECT Name FROM clinic")
    data = cur.fetchall()
    return data

def get_clinicID(c_name):
    cur.execute(f"SELECT CID FROM clinic WHERE Name = '{c_name}'")
    data = cur.fetchall()
    return data

def get_doctors(c_id):
    cur.execute(f"SELECT Name, Start_Time, End_Time FROM doctors JOIN doctor_available ON doctors.DID = doctor_available.DID WHERE CID = {c_id}")
    data = cur.fetchall()
    return data

def get_doctorID(d_name):
    cur.execute(f"SELECT DID FROM doctors WHERE Name = '{d_name}'")
    data = cur.fetchall()
    return data

def book(p_id, c_id, d_id, visit_date):
    cur.execute(f"INSERT INTO booking (PID, CID, DID, Visit_Date, Timestamp) VALUES ({p_id}, {c_id}, {d_id}, '{visit_date}', '{datetime.now()}')")
    mydb.commit()

def show_appointments(p_id):
    cur.execute(f"SELECT * FROM booking WHERE PID = {p_id}")
    data = cur.fetchall()
    return data

def cancel(p_id, c_id, d_id):
    cur.execute(f"UPDATE booking SET Status = 'Cancelled' WHERE PID = {p_id} AND CID = {c_id} AND DID = {d_id}")
    mydb.commit()
