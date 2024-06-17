

def character_count(string):
    character_stastic = {}
    string = string.lower()
    for character in string:
        if character in character_stastic:
            character_stastic[character] += 1
        else:
            character_stastic[character] = 1
    return character_stastic


string = input()
result = character_count(string)
print(result)
