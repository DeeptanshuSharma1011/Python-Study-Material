from functools import reduce

nums = [4,2,9,7,5,1,6,8]


evens = list(filter(lambda num: num%2==0, nums))

double = list(map(lambda num: num*2, evens))

sum = reduce(lambda a,b : a+b, double)

print("Evens: ", evens)
print("Doubled: ", double)
print("Sum: ", sum)