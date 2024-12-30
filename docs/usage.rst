Usage
======

To extract text from a PDF file and any images contained in it, you can use the `PDFTextExtractor` class. Here’s how to use it:

1. Install the required dependencies.
2. Use the class to extract text and images.

Installation
------------
Ensure you have the following dependencies installed:

```bash
pip install PyMuPDF Pillow pytesseract opencv-python

Example usage

Here is an example of how to use the PDFTextExtractor class to extract text from a PDF file:


```python
from pdf_text_extractor import PDFTextExtractor

# Initialize the extractor with the PDF path and image directory
pdf_path = "path/to/your/file.pdf"
image_dir = "path/to/save/images"
extractor = PDFTextExtractor(pdf_path, image_dir)

# Process and extract text
results = extractor.process_and_extract_text()

# Print the results
for result in results:
    print(result)
```