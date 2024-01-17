def majorityElement(nums):
    # Initialize candidate and count
    candidate, count = nums[0], 1

    # Voting process
    for num in nums[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify if the candidate is the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    return candidate

# Example
input_array = [2, 1, 2]
result = majorityElement(input_array)
print(result)  # Output: 2
