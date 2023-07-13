import Task_2_value_vs_ref

def test_task2():
    L = [1, 2, 3]
    m = 2
    expected = [2, 4, 6]
    result = Task_2_value_vs_ref.mod_list(L, m)
    assert result == expected