# Python script demonstrating use of the Animal class created in animal_class.py

#import the module

from animal_class import Animal
def animal_dict(L):
    """

    :param L: A list
    :return: A dict, d, mapping an int to an Animal object. A key in d is all non-negative ints, n, in L.
    A value corresponding to a key is an Animal object with n as its age.
    """
    d = {}
    for n in L:
        if type(n) == int and n >= 0:
            d[n] = Animal(n)
    return d

L = [2,5,'a',-5,0]
animals = animal_dict(L)
print(animals) #Python does not recursively print over the Animal object
for k, v in animals.items():
    print(k, v)


# A function that takes two lists and produces a list of Animal objects
def make_animals(list1,list2):
    """
    The function takes two equal length lists.
    An animal object at index (i) has the age and name corresponding to the same index in L1 and L2 respectively.
    :param list1: A list of ints
    :param list2: A list of strings
    :return: A list of Animal objects
    """
    animal_list = []
    for i in range(len(list1)):
        new_entry = Animal(list1[i])
        new_entry.set_name(list2[i])
        animal_list.append(new_entry)
    return animal_list

L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafocs"]
new_nu =make_animals(L1,L2)
# print(new_nu) #prints  a list of animal objects
for i in new_nu:
    print(i)

