# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagram(string_a, string_b):
     # [assignment] Add your code here
    """returns True if the strings are anagrams of each other

    str, list -> boolean"""
    new_a = string_a.lower()
    new_b = string_b.lower()
    i = 0
    if len(string_a) != len(string_b):
        return False
    else:
        while i <= len(new_a)-1:
            if new_a[i] in new_b:
                list(new_b).remove(new_a[i])
            i = i+1
            break
        if len(list(new_b)) == 0:
            return True
        else:
            return False
