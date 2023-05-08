from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance: Queue):
    new_list = []
    for i in range(len(instance)):
        searched = instance.search(i)
        text_lines = searched["linhas_do_arquivo"]
        file_name = searched["nome_do_arquivo"]
        new_obj = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": text_lines,
        }
        new_list.append(new_obj)
    return new_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    a = Queue()
    process("statics/nome_pedro.txt", a)

    b = exists_word("Pedro", a)
    print(b)
