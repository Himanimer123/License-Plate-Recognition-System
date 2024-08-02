import cv2
import pytesseract

# Ensure Tesseract OCR is installed and its path is set correctly
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to process each frame
def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Use OpenCV's edge detection to detect the license plate
    edged = cv2.Canny(gray, 30, 200)
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to find the best candidate for a license plate
    for c in contours:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        
        if len(approx) == 4:  # If the contour has 4 vertices, it could be a rectangle
            x, y, w, h = cv2.boundingRect(c)
            license_plate = gray[y:y + h, x:x + w]

            # Use Tesseract to recognize the text on the license plate
            text = pytesseract.image_to_string(license_plate, config='--psm 8')
            print(f'License Plate Text: {text.strip()}')

            # Draw the rectangle and the detected text on the image
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            frame = cv2.putText(frame, text.strip(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

            break

    return frame

# Main function to capture video from camera and process frames
def main():
    # Open a connection to the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print('Error: Could not open camera.')
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print('Error: Could not read frame.')
            break

        # Process the frame
        processed_frame = process_frame(frame)

        # Display the resulting frame
        cv2.imshow('License Plate Recognition', processed_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
