# Python code to describe, initialize and instantiate a fraction object
# We also implement dunder objects to assist in simple arithmetic operations efficiency

class SimpleFraction(object):
    """
    A number represented as a fraction. Has two properties, a numerator(num) and a denominator(denom)
    """

    def __init__(self, n, d):
        self.num = n
        self.denom = d

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.denom)

    # def times(self, oth):
    #     top = self.num * oth.num
    #     bottom = self.denom * oth.denom
    #     return top/bottom

    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.denom * other.denom
        return SimpleFraction(top, bottom)

    def __float__(self):
        return self.num / self.denom

    def __lt__(self, other):
        if self.num / self.denom < other.num / other.denom:
            return True
        else:
            return False

    def __le__(self, other):
        if self.num / self.denom <= other.num / other.denom:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.num / self.denom > other.num / other.denom:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.num / self.denom >= other.num / other.denom:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.num / self.denom == other.num / other.denom:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num / self.denom != other.num / other.denom:
            return True
        else:
            return False

            # def plus(self, oth):

    #     top = self.num * oth.denom + self.denom * oth.num
    #     bottom = self.denom * oth.denom
    #     return top/bottom

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return SimpleFraction(top, bottom)

    def get_inverse(self):
        return self.denom / self.num

    def invert(self):
        (self.num, self.denom) = (self.denom, self.num)
        # The above is a tuple method that achieves the bottom part but cleaner

        # temp_num = self.num
        # temp_denom = self.denom
        # self.num = temp_denom
        # self.denom = temp_num

    def reduce(self):
        # Function to reduce the numerator and denominator if divisible
        def gcd(n, d):
            while d != 0:
                (d, n) = (n % d, d)
            return n

        if self.denom == 0:
            return None
        elif self.denom == 1:
            return SimpleFraction(self.num, 1)
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num / greatest_common_divisor)
            bottom = int(self.denom / greatest_common_divisor)
            return SimpleFraction(top, bottom)


f1 = SimpleFraction(3, 4)
f2 = SimpleFraction(2, 3)
d = SimpleFraction(9, 12)
x = f1 + d
c = f1 * f2
rip = SimpleFraction(4, 1)
print(f1)
print(f2)

rip_red = rip.reduce()  # when the denominator is one, the function returns an int object which might be awkward to deal with further down the line when trying to have operations with out Fraction object
print(rip_red, type(rip_red))

print(c)
print(c.reduce())

print(x)
print(x.reduce())

print(f1 < f2)
print(d == f1)
print(c != d)
