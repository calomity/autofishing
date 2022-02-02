import imageprocessingmodule
import ocrmodule

imageprocessingmodule.firstconvert("img/screen.png")
imageprocessingmodule.secondconvert("img/first.png")
imageprocessingmodule.lastconvert("img/second.png")
code = ocrmodule.tesseract('img/last.png','C:\\Program Files\\Tesseract-OCR\\tesseract.exe')
code.replace('-',"")
print (code)