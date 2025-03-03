#Here we gonna do reading text content from PDFs and crafting new PDFs from existing documents.
import PyPDF2
pdfFileobj = open('/home/asaduzzaman-rayhan/Downloads/book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(22) #----> here we extracting the 22 number page's text
print(pageObj.extractText()) #----> by this we can extract the text from pdf
pdfFileobj.close()

#Decrypting PDFs
print(pdfReader.isEncrypted)
print(pdfReader.getPage(0))
print(pdfReader.decrypt('rosebud'))#---> here we are decrypting the pdf with password rosebud
pageObj = pdfReader.getPage(0)
print(pageObj)

#copying pages
pdf1File = open('meetingminutes.pdf', 'rb' )
pdf2File = open('meetingminutes2.pdf', 'rb' )
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfwriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfwriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfwriter.addPage(pageObj)



pdfOutputFile = open('combinedminutes.pdf', 'wb')
print(pdfwriter.write(pdfOutputFile))
print(pdfOutputFile.close())
print(pdf1File.close())
print(pdf2File.close())

#Rotating pages
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

#Overlaying Pages
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

#Encrypting PDFs
pdfReader = PyPDF2.PdfFileReader(open('/home/asaduzzaman-rayhan/Downloads/book.pdf', 'rb'))
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
           pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

#Word Documents
import docx
doc = docx.Document('demo.docx')
len(doc.paragraphs)
#Run Attributes
'''
bold--->TThe text appears in bold.

italic--->TThe text appears in italic.

underline--->TThe text is underlined.

strike--->TThe text appears with strikethrough.

double_strike--->TThe text appears with double strikethrough.

all_caps--->TThe text appears in capital letters.

small_caps--->TThe text appears in capital letters, with lowercase letters two points smaller.

shadow--->TThe text appears with a shadow.

outline--->TThe text appears outlined rather than solid.

rtl--->TThe text is written right-to-left.

imprint--->The text appears pressed into the page.

emboss-->The text appears raised off the page in relief.'''

