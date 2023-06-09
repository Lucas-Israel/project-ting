from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    for num in range(len(instance)):
        if instance.search(num)["nome_do_arquivo"] == path_file:
            return

    file = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(new_dict)
    print(new_dict)


def remove(instance: Queue):
    de_q = instance.dequeue()
    if de_q == -1:
        return print("Não há elementos")
    print(f"Arquivo {de_q['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
