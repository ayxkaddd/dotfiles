#!/usr/bin/python3

import cv2
import sys
from pyzbar import pyzbar

# Load the QR code image
image_path = sys.argv[-1]
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use pyzbar to detect and decode QR codes
qr_codes = pyzbar.decode(gray)

# Loop over the detected QR codes
for qr_code in qr_codes:
    # Extract the data from the QR code
    data = qr_code.data.decode('utf-8')
    print(data)
