import streamlit as st
from transformers.pipelines import pipeline
import PyPDF3 as pdf


st.cache(show_spinner=False)

def load_model():
    question_answerer = pipeline('question-answering')
    return question_answerer

npl_pipe = load_model()

st.header("Prototyping NLP Solution")
st.text("This demo uses a model for Question Answering.")
add_text_sidebar = st.sidebar.title("Menu")
add_text_sidebar = st.sidebar.text("Just some random text.")
question = st.text_input(label='Insert a question.')
text = st.text_area(label="Context")

if (not len(text)==0) and not (len(question)==0):
    x_dict = npl_pipe(max_answer_length=50, context=text,question=question)
    st.text(f"Answer: {x_dict['answer']}.")
'''
pdf_file_obj = open('paper.pdf', 'rb')
read_file = pdf.PdfFileReader(pdf_file_obj)
page1 = read_file.getPage(0)
text = page1.extractText()
print(text)
'''