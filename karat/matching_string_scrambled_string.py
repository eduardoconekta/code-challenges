'''
You are running a classroom and suspect that some of your students are passing around the answers to multiple choice questions disguised as random strings.

Given a list of words and a string, find which word in the list is scrambled up inside the string, if any. There will be at most one matching word. The letters don't need to be contiguous.

Example:
words = ['cat', 'dog', 'bird', 'car', 'baby']
string1 = 'tcabnihjs' -> cat
string2 = 'tbcanihjs' -> cat
string3 = 'baykkjl' -> None
string4 = 'bbabylkkj' -> baby

'''




def isAlreadyInTuple(arr, letter):
    for i in range(len(arr)):
        if arr[i][0] == letter:
            return i
    return -1

def findOcurrencesInList(words, scrambled_string):
    separated_letters = []
    word_counter = 0
    for letter in words:
        exists = isAlreadyInTuple(separated_letters, letter)
        if exists != -1:
            temp_list = list(separated_letters[exists])
            temp_list[1] +=1 
            separated_letters[exists] = tuple(temp_list)
        else:
            separated_letters.append((letter, 1))
    for i in range(len(separated_letters)):
        word_counter = 0
        for j in scrambled_string:
            if separated_letters[i][0] == j:
                word_counter += 1 
        if word_counter < separated_letters[i][1]: 
            return None
        
    return words

words = ["cat", "dog", "bird", "car", "baby"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"

for word in words:
    print findOcurrencesInList(word, string4)
