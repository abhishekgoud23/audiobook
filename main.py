import pyttsx3   #importing py text to speech 
import PyPDF2    #PDF library
book = open('M1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book) #reads pdf format
pages = pdfReader.numPages             #number of pages

speaker = pyttsx3.init()               #initiating
for num in range(100, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)                  #speaks the text
    speaker.runAndWait()