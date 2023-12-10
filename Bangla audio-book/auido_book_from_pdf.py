import pyttsx3
from PyPDF2 import PdfReader

book = open('stephen_hawking_a_brief_history_of_time.pdf', 'rb')
pdf_reader = PdfReader(book)
pages = len(pdf_reader.pages)
print(pages)

friend = pyttsx3.init()

for i in range(2, pages):
    page_number = 2
    page = pdf_reader.pages[i]
    text = page.extract_text()

    friend.say(text)
    friend.runAndWait()

