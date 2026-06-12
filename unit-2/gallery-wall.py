'''You are tasked with organizing a collection of art prints represented by a list of strings collection. 
You need to display these prints on a single wall in a 2D array format that meets the following criteria:

The 2D array should contain only the elements of the array collection.
Each row in the 2D array should contain distinct strings.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them. Note that the 2D array can have a different number of elements on each row.

Example Usage:

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))
Example Output:

[
  ["O'Keefe", "Kahlo", "Picasso", "Warhol"],
  ["O'Keefe", "Kahlo"],
  ["O'Keefe"]
]
Example 1 Explanation:
All elements of collections were used, and each row of the 2D array contains 
distinct strings, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

[["Kusama", "Monet", "Ofili", "Banksy"]]
Example 2 Explanation: 
All elements of the array are distinct, so we can keep all of them in the first 
row of the 2D array.
'''
from collections import Counter

def organize_exhibition(collection):
    # The frequency of the name that appears the most will be the min rows
    freq = Counter(collection)
    rows = max(freq.values())
    ans = [[] for _ in range(rows)]

    for key, val in freq.items():
        for i in range(val):
            ans[i].append(key)

    return ans

if __name__ == "__main__":
    collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]
    collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

    print(organize_exhibition(collection1))
    print(organize_exhibition(collection2))