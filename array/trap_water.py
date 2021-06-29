def trap_water(elevations):

    total_water = 0

    def find_left_wall(index, elevation, elevations):
        if index == 0: 
            return elevation
        max_wall = -float('inf')
        for num in elevations[index::-1]:
            max_wall = max(max_wall, num)
        return max_wall

    def find_right_wall(index, elevation, elevations):
        if index == len(elevations) - 1:
            return elevation
        max_wall = -float('inf')
        for num in elevations[index:]:
            max_wall = max(max_wall, num)
        return max_wall

    for i, num in enumerate(elevations):
        left_wall = find_left_wall(i, num, elevations)
        right_wall = find_right_wall(i, num, elevations)
        total_water += min(left_wall, right_wall) - num
    
    
    #print(f'left wall: {find_left_wall(3, 2, arr)}, right wall: {find_right_wall(3,2,arr)}')
    #trap_water([3,2,2,5,2,2,4])
    return total_water
print(trap_water([3,2,1,2,2,3,2]))
        



