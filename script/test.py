import cv2
import numpy as np

def find_document(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour (assuming the document is the largest)
    if contours:
        doc_contour = max(contours, key=cv2.contourArea)
        
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(doc_contour, True)
        doc_polygon = cv2.approxPolyDP(doc_contour, epsilon, True)
        
        # Ensure the polygon has 4 corners (a rectangle)
        if len(doc_polygon) == 4:
            return doc_polygon
    return None

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the default camera, change the index for different cameras.

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()
    
    if not ret:
        print("Error: Could not read a frame from the camera.")
        break
    
    # Find the document in the frame
    doc_polygon = find_document(frame)
    
    if doc_polygon is not None:
        # Draw the outline of the document
        cv2.drawContours(frame, [doc_polygon], -1, (0, 255, 0), 2)
        
        # Perform a perspective transformation to "scan" the document
        width, height = 500, 600
        pts1 = np.float32(doc_polygon)
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        scanned_doc = cv2.warpPerspective(frame, matrix, (width, height))
        
        # Display the scanned document
        cv2.imshow('Scanned Document', scanned_doc)
    
    # Display the camera feed
    cv2.imshow('Camera Feed', frame)
    
    # Exit the loop when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()
