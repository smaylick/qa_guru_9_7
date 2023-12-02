import shutil
import zipfile
import pytest
import os

from file_path_os import FILES_DIR, RESOURCES_DIR, ARCHIVE_DIR, FILES_LIST


# создание архива, перемещение файлов в архив, удаление архива после завершения
@pytest.fixture
def create_archive():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)
    with zipfile.ZipFile(ARCHIVE_DIR, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in FILES_LIST:
            add_file = os.path.join(FILES_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(RESOURCES_DIR)
