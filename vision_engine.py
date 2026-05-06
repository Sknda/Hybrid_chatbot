import cv2
import numpy as np 

def process_image(uploaded_file):
    # Convert Streamlit upload to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Example 1: Grayscale (Basic processing)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Example 2: Face Detection (Standard Internship POC)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles on the original image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Convert back to RGB for Streamlit display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb, len(faces)



def scan_qr_code(uploaded_file):
    # Convert Streamlit upload to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # Initialize QR Detector
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    
    # Draw Green Box if QR is found
    if bbox is not None:
        for i in range(len(bbox)):
            pt1 = tuple(bbox[i][0].astype(int))
            pt2 = tuple(bbox[(i+1) % len(bbox)][0].astype(int))
            cv2.line(img, pt1, pt2, (0, 255, 0), 3)

    # Convert to RGB for Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb, data if data else None