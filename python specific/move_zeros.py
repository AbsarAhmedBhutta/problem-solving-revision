# 9. Move Zeroes
# Move all zeros to the end while maintaining relative order.
# Do in-place.
# Input:
# [0,1,0,3,12]
# Output:
# [1,3,12,0,0]

def move_zeros(input):
    for i in range(len(input)):
        if input[i] == 0:
            input.remove(input[i])
            input.append(0)
            
    return input

print(move_zeros([0,1,0,3,12]))