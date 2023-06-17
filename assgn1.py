# ans 1
a = "kainat"
a
type(a)
b= ['sarosh', True, 2,3,4,5,34.567]
b
type(b)
c= 45.67
type(c)
d = ('sarosh', True, 2,3,4,5,34.567)
type(d)

#ans 2
var1 = ' '
type(var1)
var2 = '[ DS , ML , Python]'
type(var2)
var3 = [ 'DS' , 'ML' , 'Python' ]
type(var3)
var4 = 1
type(var4)

#ans 3
5/2 #give ans of division
5%2 # gives remainder
5//2 # gives quotient
2**3 # 2 to the power 3

#ans4
my_list = [1, 'two', 3.0, [4, 5], True, 'six', {'seven': 7}, (8, 9), None, {'ten'}]

for element in my_list:
    print(element, type(element))


#ans 5
A = int(input("Enter the number A: "))
B = int(input("Enter the number B: "))

count = 0

while A % B == 0:
    A = A // B
    count += 1

print("Number A is divisible by number B", count, "times.")

# ans 6

# Create a list with 25 int type data
my_list = [2, 5, 12, 9, 10, 15, 8, 18, 21, 30, 14, 33, 36, 40, 25, 27, 31, 48, 51, 55, 63, 72, 80, 81, 90]

# Iterate over the list elements using a for loop
for element in my_list:
    if element % 3 == 0:
        print(element, "is divisible by 3")
    else:
        print(element, "is not divisible by 3")



  #ans 7

my_list = [1, 2, 3]
my_list.append(4)  # Modifies the list by adding a new element.
my_list[0] = 5  # Modifies the value of the first element.
print(my_list)  # Output: [5, 2, 3, 4]


# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing tuple elements
print(my_tuple[0])  # Output: 1

# Attempting to modify a tuple element (which is not possible)
my_tuple[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment

# Concatenating tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)


