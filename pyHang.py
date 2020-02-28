wordList = []
correct = 0
count = 0
error = 0
answerList = []
letterList = []
words = ['cow', 'horse', 'deer', 'elephant', 'lion', 'tiger', 'baboon', 'donkey', 'fox',
'giraffe']
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p", "q", "r", "s", "t", "u" ,"v", "w," "x", "y", "z"]
print("Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")
x = int(input("Please enter an integer number (>=0 and <10) to choose the word in the list:"))
#selected animal added to wordList
wordList.extend(words[x])
print("The length of the word is", len(wordList))
while error <=5 and correct != len(wordList):
    letter = input("Enter a letter:")
    
    #check if letter already guessed
    if letter in letterList:
        while letter in letterList:
            print("Letter already entered, choose a new letter. Current Guesses are ", letterList)
            letter = input()
    letterList.append(letter)  

    #initiialize the answerList to underscores (to the length of the chosen word)
    while count < len(wordList):
        count = count + 1
        answerList.append("_")

    #checks if animal name contains letter, if so removes _ and replaces with the letter in users' answerList
    if letter in wordList:
        while letter in wordList:
            position = wordList.index(letter)
            answerList.pop(position)
            answerList.insert(position, letter)
            wordList.pop(position)
            wordList.insert(position, "_")            
            print(answerList)
            correct = correct + 1
            
        print("The letter is in the word. Letters matched so far:", correct)
    else:
        error = error + 1
        if error >= 1:
            print("The letter is not in the word. Letters matched so far:", correct)
            if error == 1:
                print("------------")
            elif error == 2:
                print("------------")
                print("|           |")
            elif error == 3:
                print("------------")
                print("|           |")
                print("|           O")
            elif error == 4:
                print("------------")
                print("|           |")
                print("|           O")
                print("|          / |")
            elif error == 5:
                print("------------")
                print("|           |")
                print("|           O")
                print("|          / |")
                print("|           | ")
            elif error == 6:
                print("------------")
                print("|           |")
                print("|           O")
                print("|          / |")
                print("|           | ")
                print("|          / |")
                print("|              ")
                print("Too many errors, you lost.")
                print("The word was", words[x] , ".")
                print("Goodbye.")    

if correct == len(answerList):
    print("You have found the mystery word. You win!")
    print("Goodbye.")
