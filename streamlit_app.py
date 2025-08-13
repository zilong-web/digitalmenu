import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="My First Streamlit App",
    layout="wide"
)

# Add sidebar
with st.sidebar:
    st.title("Sidebar")
    st.write("This is your navigation area")
    
    # Example sidebar controls
    user_name = st.text_input("What's your name?")
    button_clicked = st.button("Say hello")

# Main content area
st.title("Hello World in Streamlit!")
st.write("This is the main content area.")

# Interactive element
if button_clicked:
    if user_name:
        st.success(f"Hello, {user_name}! 👋")
    else:
        st.warning("Please enter your name first!")
