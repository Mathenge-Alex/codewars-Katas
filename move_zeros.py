# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    cleaned_list = [x for x in lst if x != 0]
    total_zeros = lst.count(0)
    cleaned_list.extend([0] * total_zeros)
        
    return cleaned_list



print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))