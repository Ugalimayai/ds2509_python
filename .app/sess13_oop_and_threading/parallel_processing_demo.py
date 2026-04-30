# Python script to demonstrate running multiple processes concurrently

#import the required modules
import multiprocessing as mp

# function to calculate the square of a number
def square(n):
    return n*n

#run the application
if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]

    # create a pool of processes
    with mp.Pool() as pool:
        # map the 'square' function to the list of numbers across multiple processes
        squared_results = pool.map(square, numbers)

        # display the squared results
        print(squared_results)