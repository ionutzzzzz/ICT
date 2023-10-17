import cv2
import pytesseract
import matplotlib.pyplot as plt

# Initialize components
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture a frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("Document Scanner")
    plt.show()

    print("Scanned Text:")
    print(text)

cap.release()
