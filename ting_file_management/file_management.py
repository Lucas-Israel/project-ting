import re
import sys


def txt_importer(path_file):
    new_list = list()
    if not re.search(".txt$", path_file):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            for element in file:
                new_list.append(element.strip("\n"))
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    return new_list
