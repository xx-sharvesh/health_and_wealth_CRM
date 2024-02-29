import streamlit as st

def display_health_record():
    st.title("Patient Health Record")
    st.subheader("Patient Information")
    name = st.text_input("Name", "John Doe")
    age = st.number_input("Age", min_value=0, max_value=150, step=1, value=35)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0 if "Male" == "John Doe" else 1)
    height = st.text_input("Height", "175 cm")
    weight = st.text_input("Weight", "70 kg")
    bmi_index = st.text_input("BMI Index", "22.86 (Normal)")

    st.subheader("Medical History")
    blood_pressure = st.text_input("1. Blood Pressure", "120/80 mmHg")
    cholesterol_level = st.text_input("2. Cholesterol Level", "180 mg/dL")
    heart_rate = st.text_input("3. Heart Rate", "75 bpm")
    blood_sugar_level = st.text_input("4. Blood Sugar Level", "90 mg/dL")
    surgeries = st.text_input("5. Surgeries", "Appendectomy (2010)")
    vaccines = st.text_input("6. Vaccines", "Tetanus (2020)")
    allergies = st.text_input("7. Allergies", "None")

    if st.button("Save"):
        # Here you can save the updated health record data to your data source
        st.success("Health Record Updated!")

def signup():
    st.title("Signup")
    name = st.text_input("Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    if st.button("Sign Up"):
        # Here you can save the signup data to your data source
        st.success("Signup Successful!")

def set_appointments():
    st.title("Set Appointments")
    st.subheader("Fill out the form below to set an appointment:")
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    appointment_reason = st.text_area("Reason for Appointment")
    if st.button("Apply"):
        # Process the appointment and display it
        st.subheader("Your Appointments:")
        st.write("1. You have an appointment on {} at {} for {}".format(appointment_date.strftime('%B %d, %Y'), appointment_time.strftime('%I:%M %p'), appointment_reason))

def main():
    st.title("Patient Health Portal")

    page = st.sidebar.radio("Navigation", ["Login", "Signup", "Health Record", "Set Appointments"])

    if page == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Dummy authentication (no actual authentication)
            if username == "dummyuser" and password == "dummypassword":
                display_health_record()
            else:
                st.error("Invalid Username or Password")

    elif page == "Signup":
        signup()

    elif page == "Health Record":
        display_health_record()

    elif page == "Set Appointments":
        set_appointments()

if __name__ == "__main__":
    main()
