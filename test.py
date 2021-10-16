import streamlit as st
import PyPDF3 as pdf
from transformers import AutoTokenizer, AutoModelForTableQuestionAnswering, AutoTokenizer, pipeline

st.cache(show_spinner=False)

#code to render the streamlit browser page
st.header("Prototype NLP Solution for Q&A")
st.text("This demo uses a NLP model for Question Answering.")
choose_file_type = st.selectbox(
    "Choose your file format",
    [" ",
    "PDF"]
)

def main():

    #function called upload file that builds a file uploader and returns the uploaded file
    def upload_file():
        uploaded_file = st.file_uploader("upload pdfs", type='pdf', accept_multiple_files=False)
        return uploaded_file

    if choose_file_type=="PDF":
        upload_file()
        
question = st.text_input(label='Insert a question.')
if __name__=="main":
    main()