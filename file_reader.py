import PyPDF3 as pdf
import streamlit as st

"""
This code will upload a multi-page
pdf file, read it, and format it
for tokenization.
"""

#upload a pdf file in streamlit browser
uploaded_file = st.file_uploader(
    "upload pdfs",
    type='pdf',
    accept_multiple_files=False
    )

#pdf filereader class that reads the upladed file
read_file = pdf.PdfFileReader(uploaded_file)

#count the number of pages
count = read_file.getNumPages()

#read the text from every page and append it to one list
total = []
for i in range(count):
    page_text = read_file.getPage(i)
    total.append(page_text.extractText())
    separator = " "
    total_output = separator.join(total)
    final = str(total_output)

#clean the whitespace
def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens

'''
calling the whitespace remover function and joining
#it all together
'''
cleaned = whitespace_tokenize(final)
joined = " ".join(str(item) for item in cleaned)


st.write(joined)
'''
