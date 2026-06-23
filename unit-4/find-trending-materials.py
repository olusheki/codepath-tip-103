def find_trending_materials(brands):
    # we want to return a list of the materials that show up at least twice
    # understand : we're taking in a list of dictionaries, which have a name and materials key
    # match: we can use for loops, and store results in a dict
    # plan: we iterate through the initial list and then the materials
    # get the frequency of each of the materials, only return the keys > 1 or >= 2
    count_1 = {}
    for brand in brands:
        for m in brand['materials']:
            if m in count_1:
                count_1[m] += 1
            else:
                count_1[m] = 1
    # ^ O(n * m) where n is brands, m is average number of materials
    
    res = []    
    for key, val in count_1.items():
        if val > 1:
            res.append(key)
    return res
    # O(n) time, O(n) space

'''
In the fast-changing world of fashion, certain materials and practices become 
trending based on how frequently they are adopted by brands. You want
to identify which materials and practices are trending. A material or
practice is considered "trending" if it appears in the dataset more than once.

Write the find_trending_materials() function, which takes a list of brands 
(each with a list of materials or practices) and returns a list of materials
or practices that are trending (i.e., those that appear more than once across all brands).

Evaluate the time and space complexity of your solution. Define your variables
and provide a rationale for why you believe your solution has the stated time 
and space complexity.
'''

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))


'''
Example Output:
['organic cotton', 'recycled polyester', 'bamboo']
['hemp', 'linen']
['recycled polyester']
'''