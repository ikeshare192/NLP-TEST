import streamlit as st
import PyPDF3 as pdf
from transformers import AutoTokenizer, AutoModelForTableQuestionAnswering, AutoTokenizer, pipeline

st.cache(show_spinner=False)

#code to render the streamlit browser page
st.header("Prototyping NLP Solution")
st.text("This demo uses a model for Question Answering.")
uploaded_file = st.file_uploader(
    "upload pdfs",
    type='pdf',
    accept_multiple_files=False
    )
question = st.text_input(label='Insert a question.')

#model to be loaded from Huggingface
def load_model():
    model_name = "deepset/bert-base-cased-squad2"
    question_answerer = pipeline(
        'question-answering',
        model=model_name,
        tokenizer=model_name
        )
    return question_answerer

#define the model using the load model function
npl_pipe = load_model()

#read the uploaded pdf file
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

#calling the whitespace remover function and joining all text
cleaned = whitespace_tokenize(final)
joined = " ".join(str(item) for item in cleaned)

if (not len(joined)==0) and not (len(question)==0):
    x_dict = npl_pipe(max_answer_length=100, context=joined,question=question)
    st.text(f"Answer: {x_dict['answer']}.")
