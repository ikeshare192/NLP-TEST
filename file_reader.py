import PyPDF3 as pdf

#file = open('Machine Learning White Paper - Isaac Shareef.pdf', 'rb')

pdf_file_obj = open('paper.pdf', 'rb')
read_file = pdf.PdfFileReader(pdf_file_obj)
page1 = read_file.getPage(0)
text = page1.extractText()
print(text)