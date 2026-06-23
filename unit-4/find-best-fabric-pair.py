def find_best_fabric_pair(fabrics, budget):
    # understand : we're given a list of tuples, where the first index is the material, and the second is the cost
    # fabrics is the list, while budget is an integer representing how much the pair should be under
    # we need to return the combination of fabrics that is as high as possible in value without exceeding budget
    
    # match : we could probably use a brute O(n^2) finding every possible pair
    # we could use the sort function then two pointers to find an optimal solution
    
    # plan: we start by sorting the fabrics array by the second value
    # then we use a while loop where the condition is that l < r
    # we plan on returning when the combined budget exceeds it, then return it where the value is just less.
    l , r = 0, len(fabrics) - 1
    f = sorted(fabrics, key=lambda x: x[1]) #O(nlogn)
    while l < r:
        combine = f[l][1] + f[r][1]
        if combine == budget:
            return (f[l][0], f[r][0])
        elif combine > budget:
            r -= 1
        elif combine < budget:
            l += 1
            
            # we can try for a bigger value, but there might be a solution where it is lower
        #break
    #return 0

'''
You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget.
Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics
whose combined cost is the highest possible without exceeding the budget.

Write the find_best_fabric_pair() function, which takes a list of fabrics 
(each with a name and cost) and a budget. The function should return the names
of the two fabrics whose combined cost is the closest to the budget without exceeding it.

Evaluate the time and space complexity of your solution. Define your variables 
and provide a rationale for why you believe your solution has the stated time 
and space complexity.
'''

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

'''
Example Output:
('Hemp', 'Organic Cotton')
('Tencel', 'Recycled Wool')
('Bamboo', 'Linen')
'''