from pypdf import PdfReader

def extractPDF(pdf_doc):
    pdf = PdfReader(pdf_doc) #This code will return the index as well as the page details
    raw_text = ''
    
    for index,page in enumerate(pdf.pages):
        raw_text += page.extract_text()
        
    return raw_text


