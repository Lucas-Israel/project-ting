from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    new_list = []
    for index in range(len(instance)):
        searched = instance.search(index)
        text_lines = searched["linhas_do_arquivo"]
        file_name = searched["nome_do_arquivo"]
        occur = []
        for index2, text_line_word in enumerate(text_lines):
            if word.lower() in text_line_word.lower():
                occur.append({"linha": index2 + 1})
        if len(occur) < 1:
            return new_list
        new_dict = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": occur,
        }
        new_list.append(new_dict)
    return new_list


def search_by_word(word, instance):
    new_list = []
    for index in range(len(instance)):
        searched = instance.search(index)
        text_lines = searched["linhas_do_arquivo"]
        file_name = searched["nome_do_arquivo"]
        occur = []
        for index2, text_line_word in enumerate(text_lines):
            if word.lower() in text_line_word.lower():
                occur.append({"linha": index2 + 1, "conteudo": text_line_word})
        if len(occur) < 1:
            return new_list
        new_dict = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": occur,
        }
        new_list.append(new_dict)
    return new_list
