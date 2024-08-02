# License Plate Recognition with OpenCV and Tesseract OCR

## Overview
This project aims to recognize license plates from vehicle images using OpenCV for image processing and Tesseract OCR for text recognition. The system detects license plates, extracts them from images, and recognizes the characters on the plates, providing an automated solution for license plate recognition.

## Features
- Detects license plates from vehicle images.
- Extracts the region of interest (ROI) containing the license plate.
- Recognizes characters on the license plate using Tesseract OCR.
- Provides accurate and efficient license plate recognition.

## Technologies Used
- **OpenCV:** For image processing and license plate detection.
- **Tesseract OCR:** For recognizing text from the extracted license plate region.
- **Python:** The programming language used to implement the project.

Ensure Tesseract OCR is installed on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

## Usage
1. Run the script:
    ```bash
    python license_plate_recognition.py
    ```
2. Enter the path to the input image when prompted.
3. The recognized license plates will be printed in the console and the annotated images will be saved in the `output` directory.

