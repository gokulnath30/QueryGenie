import streamlit as st

# Set up the title of the app
st.title("ChatGPT-like Chatbot")

# Initialize session state for messages if not already present
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to simulate a chatbot response
def get_chatbot_response(user_input):
    # This is where you would integrate your chatbot logic.
    # For now, we'll return a simple placeholder response.
    return f"Chatbot response to: {user_input}"

# Display messages


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

    for message in st.session_state.messages:
        st.write(f"**{message['role']}:** {message['text']}")
