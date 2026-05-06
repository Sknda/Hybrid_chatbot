import streamlit as st
import json
import google.generativeai as genai

import os
from dotenv import load_dotenv
from vision_engine import process_image
from chatbot_engine import get_response
from vision_engine import scan_qr_code

# --- 1. CONFIGURATION (MUST BE FIRST) ---
st.set_page_config(page_title="Hybrid NLP Chatbot", layout="wide")

# --- 2. SIDEBAR VISION LAB ---
with st.sidebar:
    st.header("Vision Lab")
    st.write("Upload a QR code image to decode it.")
    qr_file = st.file_uploader("Upload QR Image", type=['jpg', 'png', 'jpeg'])
    
    if qr_file:
        processed_img, qr_data = scan_qr_code(qr_file)
        st.image(processed_img, caption="Scan Result")
        
        if qr_data:
            st.success(f"Found: {qr_data}")
            # Add to chat memory only if it's new information
            qr_msg = f"🔍 **QR Scan Result:** {qr_data}"
            if "last_qr" not in st.session_state or st.session_state.last_qr != qr_data:
                st.session_state.messages.append({"role": "assistant", "content": qr_msg})
                st.session_state.last_qr = qr_data
        else:
            st.warning("No QR code detected.")

# --- 3. MAIN CHAT INTERFACE ---
st.title("🤖 Hybrid Internship Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Type a message..."):
    st.chat_message("user").markdown(prompt)
    
    # Get Hybrid Response (Rules or Gemini)
    response_text, is_rule = get_response(prompt, st.session_state.messages)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        if is_rule:
            st.caption("✅ Rule-Based Match")
        st.markdown(response_text)
    
    st.session_state.messages.append({"role": "assistant", "content": response_text})