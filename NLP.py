import streamlit as st
import PyPDF3 as pdf
from transformers import pipeline

st.cache(show_spinner=False)

#code to render the streamlit browser page
st.header("Prototype NLP Solution for Q&A")
st.text("This demo uses a NLP model for Question Answering.")
choose_file_type = st.selectbox(
    "Choose your file format",
    [" ",
    "PDF"]
)

#function for loading the model from Huggingface
def load_model():
    model_name = "deepset/roberta-base-squad2"
    question_answerer = pipeline(
        'question-answering',
        revision="v1.0",
        model=model_name,
        tokenizer=model_name
        )
    return question_answerer

#function to strip text from the file
def compile_text(num_pages, file):
    total = []
    for i in range(num_pages):
        page_text = file.getPage(i)
        total.append(page_text.extractText())
        separator = " "
        total_output = separator.join(total)
        final = str(total_output)
    return final

#function to strip the whitespace
def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens

#function called upload file that builds a file uploader and returns the uploaded file
def upload_file():
    uploaded_file = st.file_uploader("upload pdfs", type='pdf', accept_multiple_files=False)
    return uploaded_file

#################
# main function #
#################

def main():          
    if choose_file_type=="PDF":
        uploaded_file = upload_file()
        #question = st.text_input(label='Please Insert your question.')
        if uploaded_file is not None:
            
            #read the file into PyPdf3
            read_file = pdf.PdfFileReader(uploaded_file)

            #count the number of pages
            page_count = read_file.getNumPages()

            #compile all of the text from a multipage doc into one object
            compiled = compile_text(page_count, read_file)

            #strip the whitespace
            clean_ws = whitespace_tokenize(compiled)
            
            #join all of the text with whitespace stripped into one object
            joined = " ".join(str(item) for item in clean_ws)

            ### Uncomment to see the fully joined text ###
            #st.write(joined)

            #Load the model
            nlp_pipe = load_model()

            #promt the user for interaction, a question and provide a response
            agree = st.checkbox("Would you like to ask a question")

            if agree == True:
                question = st.text_input(label='Please Insert your question.')
                  
                if question is not None:
                    try:
                        response = nlp_pipe(max_answer_length=100, context=joined, question=question)
                        st.write(f"Response: {response['answer']}.")
                    except ValueError as x:
                        print(" ")

if __name__=="__main__":
    main()