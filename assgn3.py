#ans 1
# def is used to create function
def odd():
    for i in range(1, 26) :
     if i%2==1:
        print(i)

odd()      

#ans 2
"""
When you use *args in the function definition, it allows the function to accept any number of positional arguments, and those arguments are collected into a tuple inside the function.
"""

"""
 When you use **kwargs in the function definition, it allows the function to accept any number of keyword arguments, and those arguments are collected into a dictionary inside the function.
 """

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

def totall(*args):
    res=0
    for num in args:
        res+=num
    return res
print(totall(2,3,4,5,6,7,8,9,10))


#ans 3
# An iterator in Python is a built-in object that helps you access elements from a collection (like a list, tuple, dictionary, etc.) one at a time.

# we use iter() method to initialize the iterator object
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Initialize the iterator
my_iterator = iter(my_list)

# Print the first five elements using the next() method
for i in range(5):
    element = next(my_iterator)
    print(element)


  
#ans 4
# generator function in Python is a special type of function that uses the yield keyword to produce a series of values one at a time, allowing you to iterate over them without needing to store the entire sequence in memory.
# instead of returning a result using the return statement like regular functions, a generator function uses yield to provide values one by one as they are generated. 

def fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b  # Update a and b correctly to generate the next Fibonacci number

# Example: Generate the first 10 Fibonacci numbers and print them within the function
fibonacci_gen = fibonacci_sequence(10)
for num in fibonacci_gen:
    print(num)


#ans 5
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit=1000):
    num = 2
    while num < limit:
        if is_prime(num):
            yield num
        num += 1

# Using the generator function to print the first 20 prime numbers less than 1000
prime_generator = generate_primes()

for _ in range(20):
    print(next(prime_generator))


#ans6
a, b=0, 1
while i < 10 :
    print(a)
    a, b=b, a+b
    i+=1

#ans 7
str1= 'pwskills'
l=[]
for i in range (len(str1)):
    a=str1[i]
    l.append(a)
print(l)



#ans8
def is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num = num // 10

    if original_num == reversed_num:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")




#ans9
l3= [x for x in range(100) if x % 2!= 0]
l3
