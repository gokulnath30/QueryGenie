import streamlit as st

def main():
    # Custom CSS to style the sidebar and chat box
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            width: 10px !important; /* Set the width to your desired value */
        }
        .st-emotion-cache-1gv3huu {
            width: 3px;
        }
        .st-emotion-cache-6qob1r eczjsme11:hover .css-1lcbmhc {
            opacity: 1;
        }
        .css-1lcbmhc {
            opacity: 0;
            transition: opacity 0.3s;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("QueryGenie")
    # Initialize session state for view
    if 'view' not in st.session_state:
        st.session_state.view = 'Home'
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    def get_chatbot_response(user_input):
        # This is where you would integrate your chatbot logic.
        # For now, we'll return a simple placeholder response.
        return f"Chatbot response to: {user_input}"

    # Sidebar buttons
    if st.sidebar.button('🏠 Home'):
        st.session_state.view = 'Home'
    if st.sidebar.button('📁 Upload File'):
        st.session_state.view = 'Upload File'

    # Display content based on the selected view
    if st.session_state.view == 'Home':
        st.title("Home")
        # Display previous messages
        for message in st.session_state.messages:
            st.write(f"**{message['role']}:** {message['text']}")

        # Chat input box
        user_input = st.chat_input("Type your message here...")

        # Handle user input
        if user_input:
            # Append user message to session state
            st.session_state.messages.append({"role": "You", "text": user_input})
            
            # Get chatbot response
            bot_response = get_chatbot_response(user_input)
            
            # Append bot response to session state
            st.session_state.messages.append({"role": "Chatbot", "text": bot_response})


    elif st.session_state.view == 'Upload File':
        st.title("Upload a File")
        uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.success(f"File {uploaded_file.name} uploaded successfully!")

if __name__ == "__main__":
    main()
