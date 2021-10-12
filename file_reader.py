import PyPDF3 as pdf
import streamlit as st



uploaded_file = st.file_uploader("upload pdfs", tupe=pdf,
                                    accept_multiple_files=True,)
'''
pdf_file_obj = open('paper.pdf', 'rb')
read_file = pdf.PdfFileReader(pdf_file_obj)
page1 = read_file.getPage(0)
text = page1.extractText()
print(text)
'''