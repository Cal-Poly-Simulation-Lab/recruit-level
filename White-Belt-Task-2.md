## Task 2 - A Word on How Variables are Stored
In the bigger world of *computer science* we need to worry about how data is stored in memory on a computer.  There is a lot going on here (and the folks in the CSC department may take issue with the expination here) but we can break it down to variables stored as **values** or **references**[^1].

We need to take a moment to see how data in a variable changes.  For example, if we write the following code, notice what happens:
```
>>> # Example 1
>>> a = 5
>>> b = a
>>> print(a)
>>> print(b)
>>> a = 8
>>> print(a)
>>> print(b)
```
If you type this code into the Python shell, you will see that `a=5`, `b=5`, then `a=8` and `b=5`. As expected, b is assigned the value of a, and then when a changes value (to 8) b does not change values.  Now try this:
```
>>> # Example 2
>>> a = [1, 2, 3]
>>> b = a
>>> print(a)
>>> print(b)
>>> a[0] = 42
>>> print(a)
>>> print(b)
```
What the heck?  Notice that when we changed the value of the 1<sup>st</sup> element of `a` to 42, the variable b also changed?  Why is this?  Well, in the first example, the variable a and b are **value types** meaning they variable stores the value directly in memory.  In the second example, `a` and `b` are **reference types**.  The picture below sums up the situation.  In this case, the **pointer** is the value assigned to the variable `b` which is a`` refernce to the values in the list.  The link is referencing the langauge C#, but is applicable to Python as well [Value vs. Reference Type](https://open4tech.com/reference-vs-value-types-in-c/).

![image](https://github.com/Cal-Poly-Simulation-Lab/recruit-level/assets/12238951/b3517e8b-f2c4-4e7f-82ef-1c115b55d733)

Basically, for complicated reasons that have to do with speed and memory management, variables are stored as values on the the **stack** or as a reference to a value on the **heap**.  We'll skip the details here, but think of the variable `a = 5` as a variable storing the value *5* on the stack.  The variable `a = [1, 2, 3]` is stored as a pointer on the stack, and *references* the memory that stores the values 1, 2, 3, in the list.  When a is assigned to the list, the the *value* of a on the stack is the location or *address* of the memory on your computer that stores the values of the list.

So what is going on in example 2?
* The variable a is assigned `a = [1, 2, 3] ` which creates a pionter on the stack which references some other address in memory.
* The variable b is assigned to the *pointer* stored in the stack for a,  `b = a`.
* The first value of the list stored in the variable `a` (i.e., the first value in the list *referenced* by the value on the stack) is modified.
* But since the variable `b` points to the same address in memory as the variable `a`, when `b` is printed, the values of the list appear to have changed.

In reality, the varialbe `b` never changed, only the value of the list referenced by the variable `b` changed.

This may seem like unnecessary complications, but there really are a lot of good reasons to work with variables this way.  But, it does mean you need to be careful with you *copy* a variable with the assignment operator (the equals sign).  We will take advantage of refernces later on in a variety of ways as you progress through the PolySim belt program.

Side note, to get around this issue, we can use slicing.  For example:
```
>>> # Example 3
>>> a = [1, 2, 3]
>>> b = a[:]
>>> print(a)
>>> print(b)
>>> a[0] = 42
>>> print(a)
>>> print(b)
```

In this example, the values in the list assigned to the variable `b` do not change.  This is because the slicing operator **:** creates a reference to a new address in memory to story the values in the list.

- [ ] to complete Task 2 towards your White Belt, 

[^1]:Side note: You may have heard the term **pointer**.  Pointers are similar to referneces at a high level.  Many languages (but not all) use references or pointers.  C and C++ use pointers heavily.
