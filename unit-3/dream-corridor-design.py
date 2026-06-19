'''
You are an architect designing a corridor for a futuristic dream space.
The corridor is represented by a list of integer values where each value represents the width 
of a segment of the corridor. Your goal is to find two segments such that the corridor formed 
between them (including the two segments) has the maximum possible area. 
The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.

def max_corridor_area(segments):
    pass
Example Usage:

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 
Example Output:

49
1
'''

def max_corridor_area(segments):
    l,r = 0, len(segments) - 1
    maxVal = (min(segments[l], segments[r]) * ((r - l)))
    count = 0
    while l < r:
        maxVal = max(maxVal,((r-l) * min(segments[l], segments[r])))
        #larea = (min(segments[l+1], segments[r]) * ((r - l)))
        #rarea = (min(segments[l], segments[r-1]) * ((r - l)))
        # print("Count:", count, "l:", l, " r:", r, "max:", maxVal)
        # print("larea:", larea, "r:", rarea)
        # if larea >= rarea:
        #     l += 1
        #     maxVal = max(maxVal, larea)
        # else:
        #     r -= 1
        #     maxVal = max(maxVal, rarea)
        if l > r:
            r -= 1
        else:
            l += 1
    return maxVal



if __name__ == "__main__":
    print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
    print(max_corridor_area([1, 1]))  
