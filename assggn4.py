#ans 1 
data= [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_data = sorted(data, key=lambda x :x[1])
print(sorted_data)

#ans 2
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x2 = []

# Append the lambda function to the list 'x2'
x2.append(lambda x: x**2)

# Iterate through the 'x2' list and execute each lambda function with elements from 'x1'
for i in x2:
    for val in x1:
        print(i(val))


#ans3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tup=tuple(map(lambda x:str(x), lst))
tup


#ans4
l=[]
for i in range(1,26):
    l.append(i)
l
from functools import reduce
def multiple(x,y):
    return x*y
result= reduce(multiple,l)
result

#ans5
def test(a):
    if a%2==0 and a%3==0 :
        return a 
l= [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
result= list(filter(test, l))
result

#ans6
str1 = ['python', 'php', 'aba', 'radar', 'level']
is_palin = lambda s: s==s[::-1]
result= list(filter(is_palin, str1))
result
