import Task_1_code as t1

class TestTaks1:

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

    def test_lists(self):
        result = t1.lists()

        assert type(result[0]) == type([int])
        assert result[0][:3] == [1,2,3]
        
        assert type(result[1]) == type([])
        assert result[1][1:4] == ['apple', 3, 2+4j]

        assert result[2] == 'apple'

        assert result[3] == ['apple', 3]
        assert result[0] == [1,2,3,42]
        assert result[1] == ['banana', 42, 3, 2+4j]

