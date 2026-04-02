# Python script to demonstrate the map() function

# Set of Fibonacci numbers
numbers = sorted(set([1,1,2,3,5,8,13,21,34,55,89,144]))

# Get and display the triple of each Fib number in the sequence
tripled_num = sorted(set(map(lambda x: x*3, numbers)))

# Display the triples
print(f"Set of Fibonacci numbers:\n{numbers}"
      f"\nThird multiples of Fibonacci numbers:\n{tripled_num}")

# list of names and ages
names = ["Abigail","Bernice","Charlene", "Denise"]
ages = [21,24,22,19]

# using map function to combine the above names and ages for each
combined_data = map(lambda name,age: name + " is " + str(age) + " years old.", names, ages)

# convert the combined map object to a list and display the result
name_age_results = list(combined_data)
for result in name_age_results:
    print(result)

    