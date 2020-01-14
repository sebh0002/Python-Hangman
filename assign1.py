alist = []
correct = 0
count = 0
error = 0
blist = []
words = ['cow', 'horse', 'deer', 'elephant', 'lion', 'tiger', 'baboon', 'donkey', 'fox',
'giraffe']
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p", "q", "r", "s", "t", "u" ,"v", "w," "x", "y", "z"]
print("Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")
x = int(input("Please enter an integer number (>=0 and <10) to choose the word in the list:"))
alist.extend(words[x])
print("The length of the word is", len(alist))
while error <=5 and correct != len(alist):
    letter = input("Enter a letter:")        
    while count < len(alist):
        count = count + 1
        blist.append("_")
    if letter in alist:
        position = alist.index(letter)
        blist.pop(position)
        blist.insert(position, letter)
        print(blist)
        correct = correct + 1
        print("The letter is in the word. Letters matched so far:", correct)
    else:
        error = error + 1
        if error >= 1:
            print("The letter is not in the word. Letters matched so far:", correct)
            if error == 1:
                print("------------")
            if error == 2:
                print("------------")
                print("|          |")
            elif error == 3:
                print("------------")
                print("|          |")
                print("|           O")
            elif error == 4:
                print("------------")
                print("|          |")
                print("|           O")
                print("|         /  |")
            elif error == 5:
                print("------------")
                print("|          |")
                print("|           O")
                print("|         /  |")
                print("|           | ")
            elif error == 6:
                print("------------")
                print("|          |")
                print("|           O")
                print("|         /  |")
                print("|           | ")
                print("|          / |")
                print("|              ")
                print("Too many errors, you lost.")
                print("The word was", "".join(alist))
                print("Goodbye.")    

if correct == len(blist):
    print("You have found the mystery word. You win!")
    print("Goodbye.")