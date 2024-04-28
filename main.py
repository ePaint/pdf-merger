from PDFReader import PDFReader
from Settings import SETTINGS
from logger import logger


def main():
    logger.debug(f"Starting process with SETTINGS: {SETTINGS}")
    logger.debug(f"Reading PDFs from {SETTINGS.input_path}")
    pdfs = PDFReader.read_in_folder(SETTINGS.input_path)
    merged_pdf_path = PDFReader.merge_pdfs(pdfs, SETTINGS.output_path)
    logger.debug(f"Adding page numbers to {merged_pdf_path}")
    PDFReader.add_page_numbers(merged_pdf_path, SETTINGS.page_number_format)


if __name__ == '__main__':
    main()
