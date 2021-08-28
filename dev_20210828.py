# Minion game

word = 'BANANA'

vowel = ['A', 'E', 'I', 'O', 'U']

num_vowel = 0
vowel_list = []
consonant_list = []

for item in word:
    vowel_found = False
    for idx, vow in enumerate(vowel):
        if item == vow:
            num_vowel += 1
            vowel_list.append(item)
            vowel_found = True
            break
    if not(vowel_found):
        consonant_list.append(item)


print(vowel_list, consonant_list)
print(num_vowel)

vowel_set = sorted(set(vowel_list))
consonant_set = sorted(set(consonant_list))
print(vowel_set, consonant_set)

print(vowel_list.count('A'))