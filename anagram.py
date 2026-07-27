def check_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if sorted(string1) == sorted(string2):
        return "The strings are Anagrams"
    else:
        return "The strings are Not Anagrams"


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print(check_anagram(string1, string2))