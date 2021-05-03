import PyPDF2
from gtts import gTTS
pdf=PyPDF2.PdfFileReader('Module_3_Thermodynamics.pdf')
numpages=pdf.getNumPages()
print("Number of pages in PDF:",numpages)
exetext=""
i=1
while i!=numpages:
    exetext=exetext+pdf.getPage(i).extractText()
    i=i+1
with open("result.txt","w",encoding="ANSI") as res:
    res.write(exetext)
    
au=open("result.txt","r")
mt=au.read().replace("\n"," ")
language="en"
out_result=gTTS(text=mt, lang=language, slow=False)
out_result.save("audiobook.mp3")