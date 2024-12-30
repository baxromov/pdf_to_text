API Reference
=============

PDFTextExtractor
---------------

The `PDFTextExtractor` class is responsible for extracting text and images from a given PDF file.

.. autoclass:: pdf_text_extractor.PDFTextExtractor
   :members:
   :undoc-members:
   :show-inheritance:

Methods
--------

__init__(pdf_path, image_dir)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Initialize the PDFTextExtractor class with the path to the PDF file and the directory where images will be saved.

__extract_images_from_pdf()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extract images from the PDF and save them as PNG files in the specified directory.

__preprocess_image(image_path)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Preprocess the image to improve OCR accuracy by applying grayscale, contrast enhancement, and denoising.

__extract_text_from_image(image_path)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extract text from the image using Tesseract OCR after preprocessing.

process_and_extract_text()
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extract and process text from both the PDF file and images contained in it. Returns a list of dictionaries containing the extracted text.