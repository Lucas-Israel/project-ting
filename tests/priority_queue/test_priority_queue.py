import pytest
from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process


def test_basic_priority_queueing():
    answer_list = [3, 19]
    path_list = [
        "statics/novo_paradigma_globalizado-min.txt",
        "statics/arquivo_teste.txt",
    ]
    prio_q = PriorityQueue()
    for index, path in enumerate(path_list):
        process(path, prio_q)
        if index == 0:
            assert len(prio_q.regular_priority) == 1
        if index == 1:
            assert len(prio_q.high_priority) == 1

    for index in range(2):
        assert prio_q.search(index)["qtd_linhas"] == answer_list[index]

    prio_q.dequeue()

    assert len(prio_q) == 1

    with pytest.raises(IndexError):
        prio_q.search(50)
