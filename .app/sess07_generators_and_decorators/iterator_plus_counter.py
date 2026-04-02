# Python script to demonstrate a custom
class PlusCounter:
    """
    A simple iterator class that counts from a starting number to an end number,
    incrementing by a specified step.

    Attributes
        current (int): The current value in the iteration.
        end (int): The maximum value the counter should reach.
        step (int): The increment of the counter by one step.
    """
    def __init__(self, start, end, step=1):
        """
        Initialises the PlusCounter object.
        :param start: The starting value for the counter.
        :param end: The maximum value the counter should reach.
        :param step: The number by which the counter should increase per step.
        """
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        """
        Returns a new iterator object.

        :return:PlusCounter object.
        """
        return self
    def __next__(self):
        """
        Returns the next value in the iterator.
        :raises
            StopIteration: If the iterator is exhausted. i.e. current value exceeds max
        :return:
            int: The next value in the iterator.
        """
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += self.step
            return self.current - 1

# Create or instantiate a PlusCounter object
my_counter1 = PlusCounter(1,10)

# Iterate over the entire counter object
for num in my_counter1:
    print(num)
print('\n')

# Create another pluscounter obj to give multiples of 5 from 1 to 75
my_counter2 = PlusCounter(1,75,5)

# iterate over the counter2 obj
for num in my_counter2:
    print(num)





















