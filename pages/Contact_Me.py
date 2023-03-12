import streamlit as st


class ContactMe:
    def __init__(self):
        st.header("Contact Me")
        self._email_form()

    @staticmethod
    def _email_form():
        with st.form(key="email_form"):
            user_email = st.text_input("Your emial address")
            message = st.text_area("Your message")
            button = st.form_submit_button()


if __name__ == "__main__":
    contact = ContactMe()
