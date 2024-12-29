import pytesseract
import cv2

# Path to the image
image_path = '1.png'

# Read the image
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply adaptive thresholding
binary_image = cv2.adaptiveThreshold(
    blurred_image,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# Optional: Resize image for better OCR (Tesseract performs better on larger text)
scaled_image = cv2.resize(binary_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Optional: Sharpen the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
sharpened_image = cv2.morphologyEx(scaled_image, cv2.MORPH_CLOSE, kernel)

# Configure Tesseract OCR
custom_config = r'--oem 3 --psm 6'

# Perform OCR
text = pytesseract.image_to_string(sharpened_image, config=custom_config)

# Output the extracted text
print(text)