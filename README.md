# Description
This project is a simple implementation of a pypdf and PyMuPDF that merges all the PDF files in a given folder and adds a page numbers to the output file.

# Usability
- Modify the Settings.Settings.py file. It contains the following properties:
  - The format of the page number:
    - ###### input_folder: str = 'Input'
  - The folder where the PDF files are located (relative to the project's root folder):
    - ###### input_folder: str = 'Input'
  - The folder where the merged PDF file will be saved (relative to the project's root folder):
    - ###### output_folder: str = 'Output'
- Run the main.py file to merge the PDF files in the input folder and save the merged file in the output folder with the page numbers added.
