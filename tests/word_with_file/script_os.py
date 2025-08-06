import os
import shutil

"""
__file__ - обозначает имя текущий файла, в котором находимся
os.path.abspath - определяет полный путь до файла  
"""
CURRENT_FILE = os.path.abspath(__file__)

"""
os.path.dirname - определяем название папки в которой лежит файл
"""
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

"""
os.path.join - склеивает путь до папки с тем, что мы укажем после запятой 
"""
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)


"""
os.path.exists() - существует ли что угодно по пути (файл/папка)

os.path.isfile() - существует ли именно файл

os.path.isdir() - существует ли именно папка

os.mkdir - создает новую папку в текущей директории. mkdir(make directory)
"""
if not os.path.exists("tmp"):
    os.mkdir("tmp")

"""
shutil — модуль для операций с файлами и папками.

rmtree — remove tree = удалить папку со всем содержимым.

os.path.join(CURRENT_DIR, "tmp2") — создаёт путь до папки tmp2, которая находится в директории CURRENT_DIR.

shutil.copy(src, dst)	Копирует файл (без метаинформации)

shutil.copy2(src, dst)	Копирует файл с сохранением даты/прав

shutil.copytree(src, dst)	Копирует папку и всё содержимое

shutil.move(src, dst)	Перемещает файл или папку

shutil.rmtree(path)	Полностью удаляет папку

shutil.make_archive(base, fmt, dir)	Создаёт архив (zip/tar) из папки

shutil.unpack_archive(file, to_dir)	Распаковывает архив

shutil.disk_usage(path)	Получает объём, занято, свободно на диске
"""
# shutil.rmtree(os.path.join(CURRENT_DIR, "tmp2"))
