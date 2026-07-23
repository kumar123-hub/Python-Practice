word = input("Enter your word: ")
vowels = 0
consonants = 0
print("Vowels:", end=" ")
for ch in word:
    if ch in "aeiouAEIOU":
        print(ch, end=" ")
        vowels += 1
print()        
print("Consonants:", end=" ")
for ch in word:
    if  ch not in "aeiouAEIOU":
        print(ch, end=" ")
        consonants += 1

print("\nTotal vowels are:", vowels)
print("\nTotal consonants are:", consonants)