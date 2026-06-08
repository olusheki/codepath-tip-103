'''
Write a function linear_search() to help Winnie the Pooh locate his lost items.
The function accepts a list items and a target value as parameters.
The function should return the first index of target in items, and -1 if target is not in items.
Do not use any built-in functions.

Example 1:
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    linear_search(items, target)
	
    Output: 3

Example 2:
    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    linear_search(items, target)
    
	Output: -1
'''

def linear_search(items, target):
	count = 0
	for item in items:
		if item == target:
			return count
		else:
			count += 1
	return -1

if __name__ == "__main__":
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))