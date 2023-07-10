# Modify the code below to

def mod_list(L):
    #new_L = L
    new_L = []
    #for l in new_L:
    for l in L:
        new_L.append(2*l)

    return new_L

L = [1, 2, 3]
print("the list is: ", L)

new_L = mod_list(L)
print('the list after calling the function is: ', L)
print('the new list is: ', new_L)