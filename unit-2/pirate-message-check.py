'''
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew.
She will know she can trust the message if it contains all of the letters in the alphabet.
Given a string message containing only lowercase English letters and whitespace,
write a function can_trust_message() that returns True if the message contains every 
letter of the English alphabet at least once, and False otherwise.

Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
Example Output:

True
False
'''

def can_trust_message(message):
    '''
    O(n) complexity, O(1) space
    Intuition was the fact that only checking for 26 characters is doable.
    Luckily, everything is already lowercased.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char in message:
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    message1 = "sphinx of black quartz judge my vow"
    message2 = "trust me"

    print(can_trust_message(message1))
    print(can_trust_message(message2))