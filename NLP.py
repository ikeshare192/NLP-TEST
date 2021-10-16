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

        question = st.text_input(label='Insert a question.')

    if choose_file_type=="PDF":
        upload_file()

if __name__=="main":
    main()
'''
#function for loading the model from Huggingface
def load_model():
    model_name = "deepset/bert-base-cased-squad2"
    question_answerer = pipeline(
        'question-answering',
        model=model_name,
        tokenizer=model_name
        )
    return question_answerer

#defining the model variable
npl_pipe = load_model()

#read the uploaded pdf file
read_file = pdf.PdfFileReader(uploaded_file)

#count the number of pages in the pdf
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
    response = npl_pipe(max_answer_length=100, context=joined,question=question)
    st.text(f"{response['answer']}.")
'''  