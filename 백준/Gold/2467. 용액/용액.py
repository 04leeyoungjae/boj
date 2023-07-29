def find_closest_to_zero(liquids):
    liquids.sort()
    
    left = 0 
    right = len(liquids) - 1
    closest_sum = float('inf')
    closest_pair = ()
    
    while left < right:
        current_sum = liquids[left] + liquids[right]
        
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            closest_pair = (liquids[left], liquids[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1
    
    return closest_pair

N = int(input())
liquids = list(map(int, input().split()))

result = find_closest_to_zero(liquids)
print(result[0], result[1])