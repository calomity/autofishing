from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(ocr_version='PP-OCRv2',use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = 'img/last.png'
result = ocr.ocr(img_path, cls=True)
for line in result:
	code = line[1][0]
print(code)