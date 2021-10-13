import PyPDF3 as pdf
import streamlit as st



uploaded_file = st.file_uploader(
    "upload pdfs",
    type='pdf',
    accept_multiple_files=False
    )

read_file = pdf.PdfFileReader(uploaded_file)
page1 = read_file.getPage(0)
raw = page1.extractText()

def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens

cleaned = whitespace_tokenize(raw)
joined = " ".join(str(item) for item in cleaned)

st.write(joined)
