import streamlit as st
from smtplib import SMTPException
from send_email import send_email


class ContactMe:
    def __init__(self):
        st.set_page_config(page_title="Contact Me")
        st.header("Contact Me")
        self._email_form()

    @staticmethod
    def _email_form():
        with st.form(key="email_form"):
            not_work_message = """
            Sending email will not work because app is not secure. 
            Contact me on LinkedIn: https://www.linkedin.com/in/%C5%82ukasz-kuk-6726a2164
            """
            st.info(not_work_message)
            user_email = st.text_input("Your email address")
            raw_message = st.text_area("Your message")
            message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
            button = st.form_submit_button("Submit")
            if button:
                try:
                    # send_email(message)
                    # st.info("You email was send successfully!")
                    st.info(not_work_message)
                except SMTPException:
                    st.info("Something went wrong, try again later!")


if __name__ == "__main__":
    contact = ContactMe()
