def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    secound_min = float('inf')
    
    for i in range(len(numbers)):
        if i != numbers.index(first_min) and numbers[i] < secound_min:
            secound_min = numbers[i]
    return first_min + secound_min