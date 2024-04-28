import os
import time
from pypdf import PdfReader, PdfMerger
from fitz import open as fitz_open
from logger import logger


class PDFReader:
    @staticmethod
    def read_in_folder(folder_path: str) -> list[PdfReader]:
        """
            Read in all PDFs in a folder and return a list of PdfReader objects
            :param folder_path: str - path to the folder
            :return: list[PdfReader] - list of PdfReader objects
        """

        logger.info(f"Reading in folder: {folder_path}")
        if not os.path.exists(folder_path):
            logger.error(f"Folder not found: {folder_path}")
            raise FileNotFoundError(f"Folder not found: {folder_path}")

        for file in os.listdir(folder_path):
            logger.info(f"Reading in file: {file}")
            if file.endswith(".pdf"):
                file_path = os.path.join(folder_path, file)
                yield PdfReader(file_path)

    @staticmethod
    def merge_pdfs(pdfs: list[PdfReader], folder_path: str) -> str:
        """
            Merge PDFs into one PDF, save it to the output folder and return the PdfReader object
            :param pdfs: list[PdfReader] - list of PdfReader objects
            :param folder_path: str - path to the output folder
            :return: PdfReader - merged PDF path
        """

        timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
        output_file = f"merged_{timestamp}.pdf"
        output_path = os.path.join(folder_path, output_file)
        merger = PdfMerger()

        for pdf in pdfs:
            merger.append(pdf)

        merger.write(output_path)
        merger.close()
        logger.info(f"PDFs merged successfully to {output_path}")

        return output_path

    @staticmethod
    def add_page_numbers(pdf_path: str, page_number_format: str) -> None:
        """
            Add page numbers to a PDF using fitz
            :param pdf_path: str - path to the PDF
            :param page_number_format: str - format of the page number
            :return: None
        """

        pdf = fitz_open(pdf_path)
        page_number_format = page_number_format.replace("[TOTAL_PAGES]", str(len(pdf)))

        for page_number, page in enumerate(pdf.pages()):
            _, _, _, height = page.rect
            text = page_number_format.replace("[PAGE_NUMBER]", str(page_number + 1))
            page.insert_text(
                point=(20, height - 20),
                text=text,
                fontsize=10,
            )

        pdf.save(pdf_path, incremental=True, encryption=False)
