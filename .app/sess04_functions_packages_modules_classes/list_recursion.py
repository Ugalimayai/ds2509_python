# Python script to demonstrate how we can use recursion to break down nested lists

# Python script to find out if an element e is inside a list
def in_list_of_lists(L,e):
    """ L is a list of lists whose elements are lists containing ints
        returns true if e is an element within the lists of L and False otherwise.
        The base case is a list of one object, we then get a bool to find if e == element
        else: we initialise the first object and keep going over the list from index 1 to the end
        """
    if len(L) == 1:
        return e in L[0]
    else:
        first = L[0]
        if e in first:
            return True
        else:
            return in_list_of_lists(L[1:],e)

test_list1 = [[1,2,3],[4,5,6]]
print(in_list_of_lists(test_list1,9))



#function to perform simple top level reversal on a list. This ignores any nested lists and treats them as one element
def my_rev(L):
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]]

test_list2 = [[1,2,3],[4,5,6], 'abc']
print(my_rev(test_list2))

#function that recursively tracks every nested list and reverses it

def deep_rev(L):
    if len(L) == 1:
	    #if there is only one element, it still makes sense to confirm whether its a list
        if type(L[0]) != list:
            return L
        else:
            return [deep_rev(L[0])]
    else:
	    #with many elements, first eliminate the case when it is not a list by performing reversal and concatenate with the first element
        if type(L[0]) != list:
            return deep_rev(L[1:]) + [L[0]]
        else:
            return deep_rev(L[1:]) + [deep_rev(L[0])]
test_list3 = [[1,2,3],[4,5,6], 'abc', 'def']
print(deep_rev(test_list3))