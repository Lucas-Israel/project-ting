from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    b = Queue()
    a = process("statics/arquivo_teste.txt", b)
    print(a)
