import Task_1_code as t1

class TestTask_1_2:
    def test_variables(self):
        result = t1.variables()

        assert type(result[0]) == int
        assert result[0] == 2

        assert type(result[1]) == float
        assert result[1] == 2.0

        assert type(result[2]) == str
        assert result[2] == '2'

        assert type(result[3]) == str
        assert result[3] == 'Hello, World!'

        assert result[4] == type(str)

        assert result[5] == "Hello"

        assert result[6] == "My name is Gizmo, and I am 42"

class TestTask_1_3:
    def test_lists(self):
        result = t1.lists()

        assert type(result[0]) == type([int])
        assert result[0][:3] == [1,2,3]
        
        assert type(result[1]) == type([])
        assert result[1][1:4] == [42, 3, 2+4j]

        assert result[2] == 'apple'

        assert result[3] == ['apple', 3]
        assert result[0] == [1,2,3,42]

    def test_tuples(self):
        result = t1.tuples()
        
        assert type(result[0]) == type(())
        assert result[0] == (1, 2, 3)

        assert type(result[1]) == type(())
        assert result[1] == ('apple', 3, 2+4j)
        
        assert result[2] == 3
        
        assert result[3] == (2, 3)

    def test_sets(self):
        result = t1.sets()

        assert type(result[0]) == type({1})
        assert result[0] == {1,2,3, 42}

        assert type(result[1]) == type({1})
        assert result[1] == {'apple', 3, 2+4j}

    def test_dectionaries(self):
        result = t1.dictionaries()

        assert type(result[0]) == type({})
        assert result[0] == {'b': 66}

        assert type(result[1]) == type({})
        assert result[1] == {'a': 65, 3: 2+4j, 'colors': ['R', 'G', 'B']}

        assert type(result[2]) == type([])
        assert result[2] == ['R', 'G', 'B']

    def test_loops(self):
        result1 = t1.list_loops(2)

        result2 = t1.in_list('kiwi')

        result3 = t1.list_comprehension('a')

        assert result1 == [2, 4, 6]
        assert result2 == True
        assert result3 == ["apple", "banana", "mango"]
        pass

class TestTask_1_4:
    def test_if_else_1(self):
        # case 1
        a, b = 3, 5
        result = t1.if_else_1(a, b)
        assert result == b

        # case 2
        a, b = 5, 3
        result = t1.if_else_1(a, b)
        assert result == a

        # case 3
        a, b = 5, 5
        result = t1.if_else_1(a, b)
        assert result == (a, b)

    def test_if_else_2(self):
        # case 1
        a, b = 3, 5
        result = t1.if_else_2(a, b)
        assert result == b

        # case 2
        a, b = 5, 3
        result = t1.if_else_2(a, b)
        assert result == a

        # case 3
        a, b = 5, 5
        result = t1.if_else_2(a, b)
        assert result == (a, b)

    def test_while(self):
        result = t1.while_1(4)
        assert result == [0, 1, 2, 3, 4]

        result = t1.while_2(4, 3)
        assert result == [0, 1, 2, 4]

    def test_for(self):
        # case 0: n = 0
        assert t1.for_1(0) == 0

        # case 1: n = 1
        assert t1.for_1(1) == 1

        # case 2: n = 2
        assert t1.for_1(2) == 1

        # case 3: n = 7
        assert t1.for_1(7) == 13
 
    def test_funtions(self):
        result = t1.functions_1([2, 2.5, 6])
        assert result == [4, 5, 12]

        result2 = t1.functions_2(0)
        assert result2 == 0
        assert t1.functions_2(0) == 0
        assert t1.functions_2(1) == 1
        assert t1.functions_2(2) == 1
        assert t1.functions_2(7) == 13

    def test_lambda(self):
        result = t1.lambda_function([1, 2 ,3], 2)

        assert result == [3]