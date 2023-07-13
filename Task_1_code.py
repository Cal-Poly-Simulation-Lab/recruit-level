

def variables():
    # define the variable x0 to the value of two as an integer
    x0 = 2
    # define the variable x1 to the value of two as a flaot
    x1 = 2.0
    # cast the variable x0 to a string and store the new value in a variable x0_str
    x0_str = str(x0)
    # define the variable new_str to the value "Hello, World!"
    new_str = "Hello, World!"
    # define the varialbe str_type to the type of the variable str
    str_typ = type(str)
    # use slicing to define a new variable h which is only the word "Hello" in str
    h = new_str[:5]
    # define a formated string, "My name is Gizmo, and I am 42" with the name and age passed
    # as variables using the format() method.
    f = "My name is {}, and I am {}".format('Gizmo', 42)
    # return all the variables above
    return x0, x1, x0_str, new_str, str_typ, h, f
    #pass

def lists():
    # define a list L with values 1, 2, 3
    L = [1,2,3]
    # define a list M with values 'apple', 3, 2+4j
    M = ['apple', 3, 2+4j]
    # define a variable m which is the first element of M
    m = M[0]
    # use slicing to define a new list N which is the first and second elements of L
    N = M[:2]
    # add the value 42 to the list L
    L.append(42)
    # insert the value 42 into the list M as the second element
    M.insert(1, 42)
    # change the first value of the list M to 'banana'
    M[0] = 'banana'
    # return all the variables above
    #pass
    return L, M, m, N

def tuples():
    # define a tuple L with values 1, 2, 3
    # define a tuple M with values 'apple', 3, 2+4j
    # define a variable l which is the second element of M
    # use slicing to define a new tuple N which is the first and second elements of L
    
    # return all the variables above
    pass

def sets():
    pass

def dictionaries():
    pass

def list_loops():
    pass

def list_comprehension():
    pass

def in_list():
    pass
