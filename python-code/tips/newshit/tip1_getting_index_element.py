# get the index when iterate
# use enumerate

numbers = [1, 4, 6, 3, 4]

for number in numbers:
    print(number)

# which index ?

for index, number in enumerate(numbers):
    print(index, number)

vowels = list('aeiou')
print(vowels)

for index, vowel in enumerate(vowels):
     print(index, vowel)

