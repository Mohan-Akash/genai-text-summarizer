import streamlit as st
from summarize import summarize_text
import PyPDF2

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Generative AI Text Summarizer")

# Choose between Text or PDF input
input_type = st.radio("Choose input type:", ("Text", "PDF"))

input_text = ""

# Text input section
if input_type == "Text":
    input_text = st.text_area("Enter the text to summarize:", height=300)

# PDF upload section
elif input_type == "PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
            input_text = pdf_text
            st.text_area("Extracted Text from PDF:", value=pdf_text, height=300)
        except Exception as e:
            st.error("❌ Error reading PDF: " + str(e))

# Summary length options
length_option = st.radio("Select summary length:", ("light", "small", "medium", "large"))

# Summarize Button
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("🔄 Generating summary..."):
            summary = summarize_text(input_text, length=length_option)
            st.subheader("📄 Summary Output:")
            st.write(summary)
    else:
        st.warning("⚠️ Please provide some input text or upload a valid PDF.")

