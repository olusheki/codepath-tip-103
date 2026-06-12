'''
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped.
The treasure chest has a secret code written in pirate language, and Captain Feathersword believes 
the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency 
of every letter present in the code is equal. To disable the trap, Captain Feathersword must
remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to 
remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function can_make_balanced() 
that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, 
and False otherwise.

Example Usage:

code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 
Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
'''
import heapq

def can_make_balanced(code):
    '''
    idea: get the frequency of each of the characters. Then, see if there's more than one character that differs by one. If so, not balanced.
    '''
    freq = {}
    #This block is O(n)
    
    for char in code:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] = freq[char] + 1
    
    #Got the frequency, but... I don't know how to do the logic for the second part.
    #Wait, if we use a heap then we can extract the max value (the char with the highest freqeuncy), then we take the freq
    #table when that value is removed then return boolean if those are equal.

    strikes = 0
    baseline = freq[code[0]]
    for char, num in freq.items():
        if num != baseline:
            strikes += 1
    if strikes > 1:
        return False
    else: 
        return True

if __name__ == "__main__":
    code1 = "arghh"
    code2 = "haha"

    print(can_make_balanced(code1)) 
    print(can_make_balanced(code2)) 