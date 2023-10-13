import cv2
import pytesseract
import matplotlib.pyplot as plt

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture a frame from the camera

    if not ret:
        print("Failed to capture a frame.")
        break

    # Convert the frame to grayscale for better OCR results
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale image
    text = pytesseract.image_to_string(gray)

    # Display the live video feed and recognized text using matplotlib
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("Document Scanner")
    plt.show()

    print("Scanned Text:")
    print(text)

# Release the camera
cap.release()
