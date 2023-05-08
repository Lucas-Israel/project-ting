import re
import sys


def txt_importer(path_file):
    if not re.search(".txt$", path_file):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
