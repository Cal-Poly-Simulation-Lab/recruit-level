import Task_2_value_vs_ref

def test_task2():
    L = [1, 2, 3]
    m = 2
    assert Task_2_value_vs_ref.mod_list(L, m) == [2, 4, 6]