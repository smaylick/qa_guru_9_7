import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, 'files')
RESOURCES_DIR = os.path.join(CURRENT_DIR, 'resources')
ARCHIVE_DIR = os.path.join(RESOURCES_DIR, 'archive.zip')
FILES_LIST = os.listdir(FILES_DIR)
