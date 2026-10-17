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