import streamlit as st

def main():
    st.sidebar.title("QueryGenie")
    # Initialize session state for view
    if 'view' not in st.session_state:
        st.session_state.view = 'Home'
    if 'user' not in st.session_state:
        st.session_state.user = None
    st.markdown(
        """
        <style>
        /* Target the sidebar */
        .css-1d391kg {
            width: auto; /* Adjust this value to reduce the sidebar width */
        }
        /* Target the sidebar content */
        .css-1d391kg .css-1lcbmhc {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Add custom CSS to position the login/profile buttons at the bottom of the sidebar

    # Sidebar buttons
    if st.sidebar.button('Home'):
        st.session_state.view = 'Home'
    if st.sidebar.button('Upload File'):
        st.session_state.view = 'Upload File'

    # Display content based on the selected view
    if st.session_state.view == 'Home':
        st.title("Welcome to QueryGenie")
        st.write("This is the home page.")

    elif st.session_state.view == 'Upload File':
        st.title("Upload a File")
        uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)


        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.success(f"File {uploaded_file.name} uploaded successfully!")

if __name__ == "__main__":
    main()