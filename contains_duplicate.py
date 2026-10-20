def contains_duplicate(nums):
    gorulen = {}
    for i in range(len(nums)):
        if nums[i] in gorulen:
            return True
        gorulen[nums[i]] = i
    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([]))

def contains_duplicate_set(nums):
    gorulen = set()
    for sayi in nums:
        if sayi in gorulen:
            return True
        gorulen.add(sayi)
    return False

print(contains_duplicate_set([1, 2, 3, 1]))
print(contains_duplicate_set([1, 2, 3, 4]))