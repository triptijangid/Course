N = int(input("Enter value of N: "))
text = input("Enter the string: ")

vowel_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for character in text.lower():   # convert to lowercase to handle uppercase letters
    if character in vowels:
        vowel_count += 1

if vowel_count >= N / 2:
    print("Feel good!")
else:
    print("Feel bad!")