nums = [1, 2, 3]
# print(next(nums))  # returns an error coz nums isn't an iterator

# for num in nums:
#     print(num)

# print(dir(nums)) # has __iter__ method meaning its an iterable
# iterator is an object with a state so that it can remember its position during iteration

i_nums = iter(nums)  # makes it an iterator
# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))


while True:
    try:
        items = next(i_nums)
        print(items)
    except StopIteration:
        break
