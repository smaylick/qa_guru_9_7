import os
import requests
from file_path_os import FILES_DIR


def test_download_pdf_file():  # загрузка PDF-файла
    content = requests.get(
        url='https://zagorie.ru/upload/iblock/4ea/4eae10bf98dde4f7356ebef161d365d5.pdf'
    ).content
    with open(os.path.join(FILES_DIR, "file_pdf.pdf"), 'wb') as file:
        file.write(content)


def test_download_xlsx_file():  # загрузка XLSX-файла
    content = requests.get(
        url='https://itsm365.com/documents_rus/web/Content/Resources/doc/import_ou_xlsx.xlsx/import_ou_xlsx.xlsx'
    ).content
    with open(os.path.join(FILES_DIR, "file_xlsx.xlsx"), 'wb') as file:
        file.write(content)


def test_download_csv_file():  # загрузка CSV-файла
    content = requests.get(
        url='https://itsm365.com/documents_rus/web/Content/Resources/doc/import_ou_csv.csv'
    ).content
    with open(os.path.join(FILES_DIR, "file_csv.csv"), 'wb') as file:
        file.write(content)
