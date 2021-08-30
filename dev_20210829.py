# Minion game - Revised

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

def kevin_score(vowel_set):
    for i, item in enumerate(vowel_set):
        vowel_index = word.index(item)
        kevin_points = []
        for j, letter in enumerate(word[vowel_index:]):
            if j == 0:
                kevin_points.append(letter)
            else:
                new_word = kevin_points[j-1] + letter
                kevin_points.append(new_word)
        return kevin_points

def stuart_score(consonant_set):
    for i, item in enumerate(consonant_set):
        consonant_index = word.index(item)
        stuart_points = []
        for j, letter in enumerate(word[consonant_index:]):
            if j == 0:
                stuart_points.append(letter)
            else:
                new_word = stuart_points[j-1] + letter
                stuart_points.append(new_word)
        return stuart_points

def kevin_count(kevin_final_list):
    print("WORDS" + "\t" + "SCORE")
    for item in kevin_final_list:
        print(item + "\t" + str(word.count(item)))

if __name__ == '__main__':
    kevin_final_list = kevin_score(vowel_set)
    stuart_final_list = stuart_score(consonant_set)
    kevin_count(kevin_final_list)




