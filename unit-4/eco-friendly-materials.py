def count_material_usage(brands):
    
    #understand -> input is brands (list of dictionaries)
    #plan -> create dictionary, iterate through and increment value, return result
    
    # we could also use defaultdict(list)
    result = {}
    
    for brand in brands:
        for m in brand["materials"]:
            #if it exists, increment value by 1
            if m in result:
                result[m] += 1
            #if not in dictionary, add value 
            else:
                result[m] = 1
    
    return result

'''
Certain materials are recognized as eco-friendly due to their low environmental impact.
You need to track which materials are used by various brands and count how many times 
each material appears across all brands. This will help identify the most commonly 
used eco-friendly materials.

Write the count_material_usage() function, which takes a list of brands 
(each with a list of materials) and returns the material names and the 
number of times each material appears across all brands.

Evaluate the time and space complexity of your solution.
Define your variables and provide a rationale for why you believe your
solution has the stated time and space complexity.
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

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))

'''
Exmaple Output:
{'organic cotton': 2, 'recycled polyester': 2, 'bamboo': 2}
{'hemp': 2, 'linen': 2, 'organic cotton': 1, 'recycled wool': 1}
{'organic cotton': 1, 'recycled polyester': 2, 'hemp': 1, 'bamboo': 1}
'''