import streamlit as st

def display_health_record():
    st.title("Patient Health Record")
    st.subheader("Patient Information")
    st.write("Name: John Doe")
    st.write("Age: 35")
    st.write("Gender: Male")
    st.write("Height: 175 cm")
    st.write("Weight: 70 kg")
    st.write("BMI Index: 22.86 (Normal)")

    st.subheader("Medical History")
    st.write("1. Blood Pressure: 120/80 mmHg")
    st.write("2. Cholesterol Level: 180 mg/dL")
    st.write("3. Heart Rate: 75 bpm")
    st.write("4. Blood Sugar Level: 90 mg/dL")
    st.write("5. Surgeries: Appendectomy (2010)")
    st.write("6. Vaccines: Tetanus (2020)")
    st.write("7. Allergies: None")

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
