def main():
    nums = [2, 3, -9, 100, -10, 15]

    max_val = calc_max(nums)
    min_val = calc_min(nums)
    print_result(max_val, min_val)


def calc_max(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


def calc_min(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


def print_result(max_val, min_val):
    print("The maximum value in the list:", max_val)
    print("The minimum value in the list:", min_val)


main()
