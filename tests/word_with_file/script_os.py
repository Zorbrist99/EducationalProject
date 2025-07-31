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
TMP_DIR = os.path.join(CURRENT_DIR, "[SuperSliv.biz] Задание.txt")
print(TMP_DIR)

##TODO:дописать команды по проверки наличия файла.
# if not os.path.exists("tmp2"):
#     os.mkdir("tmp2")
#
# shutil.rmtree(os.path.join(CURRENT_DIR, "tmp2"))
