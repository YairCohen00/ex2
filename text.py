file = open("C:\yair\course\ex2/text.txt")
new_file = file.read().split()
def revword(word:str):
    word = word.lower()[::-1]
    return word

def countword():
    counter = 1
    word = new_file[0]
    print(word)
    for x in new_file[1:]:
        temp = revword(x)
        if temp == word:
            print(temp)
            counter += 1
    return counter

print(countword())