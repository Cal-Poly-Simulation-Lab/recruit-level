

def variables():
    # define the variable x0 to the value of two as an integer

    # define the variable x1 to the value of two as a flaot

    # cast the variable x0 to a string and store the new value in a variable x0_str

    # define the variable new_str to the value "Hello, World!"

    # define the varialbe str_type to the type of the variable str

    # use slicing to define a new variable h which is only the word "Hello" in str

    # define a formated string, "My name is Gizmo, and I am 42" with the name and age passed
    # as variables using the format() method.

    # return all the variables above
    #return x0, x1, x0_str, new_str, str_typ, h, f
    pass

def lists():
    # Lists are Ordered, Changeable, and Allow Duplicates
    # define a list L with values 1, 2, 3

    # define a list M with values 'apple', 3, 2+4j

    # define a variable m which is the first element of M

    # use slicing to define a new list N which is the first and second elements of L

    # add the value 42 to the list L

    # insert the value 42 into the list M as the second element

    # change the first value of the list M to 'banana'

    # return all the variables above in order created
    #return L, M, m, N
    pass

def tuples():
    # Tuples are Ordered, Unchangeable, and Allow Duplicates
    # define a tuple L with values 1, 2, 3

    # define a tuple M with values 'apple', 3, 2+4j

    # define a variable l which is the second element of M

    # use slicing to define a new tuple N which is the second and third elements of L

    # return all the variables above in order created
    #return L, M, l, N
    pass

def sets():
    # Sets are Unordered, Unchangeable, Unidexed and do not Allow Duplicates
    # define a set L with values 1, 2, 3

    # define a set M with values 'apple', 3, 2+4j

    # add the value 42 to the list L

    # return all the variables above in order created
    #return L, M
    pass

def dictionaries():
    # Dictionaries are Ordered, Changeable, and do not Allow Duplicates
    # Basic definition - a set of key:value pairs
    # define a dictionary L with key/value pairs 'a'/65 and 'b'/66

    # define a dictionary M with key/value pairs 'a'/65 and 3/2+4j, 'colors'/['R', 'G', 'B']

    # define a variable m which is the value associate with the key 'colors' in the dictionary M

    # pop the dictionary entry 'a' from L

    # return all the variables above in order created
    #return L, M, m
    pass

def list_loops(n):
    # define a list L with values 1, 2, 3
    L = [1, 2, 3]
    # define an empty list M

    # use a for loop to get each value in L and multiply it by the input n
    # append each new value computed into M
    for l in L:
        pass
    # return M
    pass

def in_list(fruit):
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    # use an if/else statement to return True it he input fruit is in the list
    # of fruits, and False otherwise

    pass

def list_comprehension(l):
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    # use list comprehension to return a new list with all elements of the list
    # fruits that contain the letter given as the input l

    pass

def if_else_1(a, b):
    # write a simple if-elif-else statement to return
    # the larger of the two values, a and b
    # if a and b are equal, return both in a tuple
    
    pass
    
def  if_else_2(a,b):
    # use the ternary short hand to return the larger of the 
    # two values, a and b.
    # if a and b are equal, return both in a tuple

    pass

def while_1(n):
    # write a while loop to count to n, and return a list
    # with integers from 0 to n
    
    pass

def while_2(n, b):
    # write a while loop to count to n, but skipping b
    # using a continue statement.  Return a list with all numbers
    # counted
    
    pass

def for_1(n):
    # use a for loop to compute the nth fibonacci number
    # fn num = [0 1 2 3 4 5 6 7 ...]
    # fn seq = [0 1 1 2 3 7 8 13 ...]
    f0 = 0
    f1 = 1
    if n == 0:
        return f0
    
    if n in (1, 2):
        # fix this
        pass
    
    for i in range(1, n):
        #fix this
        pass
    
    return f1

def functions_1(L):
    # write a function that doubles the input
    # use this function and liste comprehension to double
    # the elements of the list L

    def doub(l):
        #fix this
        pass
    
    #M = [doub(x) ...]

    pass

def functions_2(n):
    # write a function that uses recursion to find the nth fibonacci number

    def fib_recursion(n):
        if n == 0:
            result = 0
        elif n == 1:
            #fix this
            pass
        else:
            #fix this
            pass

        return result
    
    return fib_recursion(n)

def lambda_function(L, a):
    # Use the filter() method and a lambda expression to filter elements of
    # a list, L, that are greater then the value a.
    
    pass