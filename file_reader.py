import PyPDF3 as pdf
import streamlit as st



uploaded_file = st.file_uploader(
    "upload pdfs",
    type='pdf',
    accept_multiple_files=False
    )

read_file = pdf.PdfFileReader(uploaded_file)
page1 = read_file.getPage(0)
text = page1.extractText()
#st.write(text)
