'''
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
    
    bouncy and flouncy both increment the value of the variable tigger by 1.
    trouncy and pouncy both decrement the value of the variable tigger by 1.

Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

Example 1:
    operations = ["trouncy", "flouncy", "flouncy"]
    final_value_after_operations(operations)
	
	Output: 2

Example 2:
    operations = ["bouncy", "bouncy", "flouncy"]
    final_value_after_operations(operations)
	
	Output: 4
'''

def final_value_after_operations(operations):
	tigger = 1
	for op in operations:
		if op == 'bouncy' or op == 'flouncy':
			tigger += 1
		else:
			tigger -= 1
	return tigger

if __name__ == "__main__":
	operations = ["trouncy", "flouncy", "flouncy"]
	print(final_value_after_operations(operations))
	