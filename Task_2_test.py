import Task_2_code as t2

def test_val_vs_ref():
    L = [1, 2, 3]
    m = 2
    expected = [2, 4, 6]
    result = t2.mod_list(L, m)
    assert result == expected