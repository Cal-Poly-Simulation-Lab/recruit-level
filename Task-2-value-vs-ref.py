# The code below has a few problems
# Modify the code so that you can double the value of each item in the list
# One important modification will be to ensure that the code does not modify the
# reference to the list L.

def mod_list(L, m):
    """
    Returns a new list which is modified by m, i.e., new_L = m * L

    Parameter L:  The list to modify

    Parameter m:  The modificaiton factor used to modify the list L
    """
    #new_L = L
    new_L = []
    #for l in new_L:
    for l in L:
        new_L.append(m * l)

    return new_L

L = [1, 2, 3]
print("the list is: ", L)

new_L = mod_list(L)
print('the list after calling the function is: ', L)
print('the new list is: ', new_L)
