nums = [2, 7, 11, 15]
target = 9


def run(nums, target):
    # remove every number greater than target from the list
    filtered_nums_list = [num for num in nums if num < target]
    result_list = [] # Results will be inserted into this variable
    
    for number in filtered_nums_list:
        for second_number in nums:
            # sum_of_numbers will be zero if number and second_number are the same, simply to prevent using the same number twice
            sum_of_numbers = number + second_number if number != second_number else 0
            if sum_of_numbers == target:
                # If true, assign numbers to result_list and break the inner loop
                result_list = [number, second_number]
                break
        if result_list:
            # If result_list is not empty, it means result has already been found, so, break the loop
            break

    return result_list


print(run(nums, target))
