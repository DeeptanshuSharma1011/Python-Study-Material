from functools import reduce

nums = [2,3,4]

cube = list(map(lambda num: num * num * num, nums))

sum_of_cubes = reduce(lambda a,b : a+b, cube)

print("Cubes: ", cube)
print("Sum of cubes: ", sum_of_cubes)