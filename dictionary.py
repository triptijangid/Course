name = input("Input: ")
char_count = {}
for ch in name:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
repeated_letters = {}

for key in char_count:
    if char_count[key] > 1:
        repeated_letters[key] = char_count[key]
print("Output: ",repeated_letters)