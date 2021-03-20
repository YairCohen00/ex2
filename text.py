def revword(word:str):
    word = word.lower()[::-1]
    return word

def countword():
    counter = 1
    word = new_file[0]
    for x in new_file[1:]:
        temp = revword(x)
        print(temp)
        if temp == word:
            counter += 1
    return counter

file = open("text.txt")
new_file = file.read().split()
print(countword())