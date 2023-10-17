# import cv2
# import pytesseract
# from PIL import Image
# from collections import Counter

# # Load the image
# image_path = './data/test.png'
# frame = cv2.imread(image_path)

# if frame is None:
#     print(f"Failed to load the image from {image_path}")
# else:
#     # Pre-process the image
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
#     # Perform OCR with pytesseract and Tesseract
#     text_pytesseract = pytesseract.image_to_string(Image.fromarray(gray), config='--oem 3 --psm 6', lang='eng')
#     text_tesseract = pytesseract.image_to_string(Image.fromarray(gray), lang='eng')
    
#     # Create a list of the OCR results
#     ocr_results = [text_pytesseract, text_tesseract]
    
#     # Calculate confidence scores for each result
#     confidences = [pytesseract.image_to_osd(Image.fromarray(gray), output_type=pytesseract.Output.STRING)]
    
#     # Find the result with the highest confidence score
#     most_common_result = Counter(ocr_results).most_common(1)
#     most_common_text = most_common_result[0][0]
    
#     print("OCR Results:")
#     for result, confidence in zip(ocr_results, confidences):
#         print(f"Text: {result}\nConfidence: {confidence}\n")
    
#     print("Most Common Result:")
#     print(most_common_text)


import os
import pytesseract
from PIL import Image


image = Image.open("../data/test.png")


text = pytesseract.image_to_string(image)


print(text)

