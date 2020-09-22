class myRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = myRange(1, 10)
# for num in nums:
#     print(num)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


# create a generator
def my_Range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


count = my_Range(1, 10)
print(next(count))
print(next(count))
print(next(count))

