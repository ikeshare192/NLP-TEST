import streamlit as st
import PyPDF3 as pdf
from transformers import (
    AutoTokenizer,
    AutoModelForTableQuestionAnswering,
    AutoTokenizer,
    Pipeline)

st.cache(show_spinner=False)

model_name = "deepset/roberta-base-squad2"

#model to be loaded from Huggingface
def load_model():
    question_answerer = pipeline(
        'question-answering',
        model=model_name,
        tokenizer=model_name
        )
    return question_answerer

npl_pipe = load_model()

st.header("Prototyping NLP Solution")
st.text("This demo uses a model for Question Answering.")

uploaded_file = st.file_uploader(
    "upload pdfs",
    type='pdf',
    accept_multiple_files=False
    )

read_file = pdf.PdfFileReader(uploaded_file)
page1 = read_file.getPage(0)
text = page1.extractText()

question = st.text_input(label='Insert a question.')
#uncomment below to enable viewing of the context
context = st.text_area(label="Context")

def remove_whitespace(text):
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens

#cleaned = remove_whitespace(text)
#joined = " ".join(str(item) for item in cleaned)


if (not len(joined)==0) and not (len(question)==0):
    x_dict = npl_pipe(max_answer_length=50, context=text,question=question)
    st.text(f"Answer: {x_dict['answer']}.")
