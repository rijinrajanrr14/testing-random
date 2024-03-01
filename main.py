import streamlit as st
from extractor import FacebookExtractor

# Instantiate the FacebookExtractor class
facebook_extractor = FacebookExtractor()

# Streamlit UI
st.title("Facebook Post Comments Extraction")

page_id_input = st.text_input("Enter Page ID:")
post_id_input = st.text_input("Enter Post ID:")
access_token_input = st.text_input("Enter Access Token:")

if st.button("Start"):
    if not (page_id_input and post_id_input and access_token_input):
        st.warning("Please enter Page ID, Post ID, and Access Token.")
    else:
        st.info("Scraping in progress... Please wait.")
        try:
            df = facebook_extractor.extract_post_and_comments(page_id_input, post_id_input, access_token_input)
            st.success("Scraping completed successfully.")
            st.write(df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
jkjj