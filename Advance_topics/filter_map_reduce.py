

nums = [4,2,9,7,5,1,6,8]

# evens = []

# for i in nums:
#     if i%2==0:
#         evens.append(i)

# def is_evens(num):
#     return num%2==0

# is_evens = lambda num: num%2==0

# evens = list(filter(is_evens, nums))

evens = list(filter(lambda num: num%2==0, nums))

print(evens)