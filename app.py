import streamlit as st
from app_methods import *

# Page configuration
st.set_page_config(
    page_title="Text Analysis Tool",
    page_icon="📊",
    initial_sidebar_state="expanded"
)


def main():
    """
    Main function to run the Streamlit NLP application.
    """

    st.title("NLP Application With Streamlit")

    # Sidebar menu
    menu = [
        "Text Analysis Dashboard",
        "File-Based NLP Analysis"
    ]

    choice = st.sidebar.selectbox("Menu", menu)

    # ---------------------------------------------------------
    # TEXT ANALYSIS DASHBOARD
    # ---------------------------------------------------------
    if choice == "Text Analysis Dashboard":

        st.subheader("Analyze Text")

        # Text input
        raw_text = st.text_area(
            "Enter Text Here...",
            height=250
        )

        # Number of common tokens
        num_most_common = st.sidebar.number_input(
            "Most Common Tokens",
            min_value=1,
            max_value=10,
            value=5
        )

        # Analyze button
        if st.button("Analyze"):

            if raw_text.strip():
                analyze_text(
                    raw_text,
                    num_most_common
                )
            else:
                st.warning("Please enter some text to analyze.")


    # ---------------------------------------------------------
    # FILE-BASED NLP ANALYSIS
    # ---------------------------------------------------------
    elif choice == "File-Based NLP Analysis":

        st.subheader("Upload and Analyze Text Files")

        # File uploader
        text_file = st.file_uploader(
            "Upload Files",
            type=["pdf", "docx", "txt"]
        )

        # Number of common tokens
        num_most_common = st.sidebar.number_input(
            "Most Common Tokens",
            min_value=1,
            max_value=10,
            value=5
        )

        # Analyze uploaded file
        if text_file is not None:

            raw_text = handle_uploaded_file(text_file)

            if raw_text:
                analyze_text(
                    raw_text,
                    num_most_common
                )


# -------------------------------------------------------------
# PROGRAM ENTRY POINT
# -------------------------------------------------------------
if __name__ == "__main__":
    main()