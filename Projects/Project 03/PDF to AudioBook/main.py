import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('book.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    newVoiceRate = 145
    speaker.setProperty('rate',newVoiceRate)
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()