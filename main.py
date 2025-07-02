# import smtplib
# import speech_recognition as sr
# from email.message import EmailMessage
# import pyttsx3

# listener = sr.Recognizer()
# tts = pyttsx3.init()

# def talking_tom(text):
#     tts.say(text)
#     tts.runAndWait()

# def mic():
#     with sr.Microphone() as source:
#         print("Talk")
#         tts.say("Speak Now")
#         tts.runAndWait()
#         voice = listener.listen(source, timeout=10)
#         data = listener.recognize_google(voice)
#         print(data)
#         return data.lower()

# def send_mail(receiver, subject, body):
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login("readright2022@gmail.com ","dxghikiuidbtgzws") #readright2022@gmail.com to be replaced by sender's mail
#         email = EmailMessage()
#         email["from"] = "readright2022@gmail.com"
#         email["to"] = receiver
#         email["subject"] = subject
#         email.set_content(body)
#         server.send_message(email)
#         server.quit()
#         print("Email sent successfully")
#         talking_tom("Email sent successfully")
#     except Exception as e:
#         print("An error occurred:", e)
#         talking_tom("An error occurred while sending the email") #allow access for less secure apps for email login

# def main_poc():
#     contact_dict = {"test": "your_email@gmail.com"}  # Replace with your contact dictionary
#     talking_tom("Whom do you want to send this email?")
#     name = mic()
#     receiver = contact_dict.get(name)
#     if receiver is None:
#         print("Recipient not found")
#         talking_tom("Recipient not found")
#         return
#     talking_tom("What's the subject of the email?")
#     subject = mic()
#     talking_tom("Speak the body of the email")
#     body = mic()
#     send_mail(receiver, subject, body)

# if __name__ == "__main__":
#     main_poc()

import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Email Sender", page_icon="📧")

st.title("📧 Send an Email")

# Predefined contact list
contact_dict = {
    "test": "your_email@gmail.com",  # Replace with your test contact
    "sania": "sania@example.com"
}

# Select contact or enter manually
selected_name = st.selectbox("Choose recipient (or type manually):", ["", *contact_dict.keys(), "Custom"])

if selected_name == "Custom":
    receiver = st.text_input("Enter recipient email")
else:
    receiver = contact_dict.get(selected_name, "")

subject = st.text_input("Subject")
body = st.text_area("Body")

# Email credentials (sender)
sender_email = "readright2022@gmail.com"
app_password = "dxghikiuidbtgzws"  # Replace with your Gmail App Password

if st.button("Send Email"):
    if not receiver or not subject or not body:
        st.warning("Please fill in all fields.")
    else:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
            
            email = EmailMessage()
            email["from"] = sender_email
            email["to"] = receiver
            email["subject"] = subject
            email.set_content(body)

            server.send_message(email)
            server.quit()

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
