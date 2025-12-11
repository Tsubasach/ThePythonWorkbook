letter=input("Input Letter:")
while True:
    #vowel=["a","i","e","u","o","E","I","U","O","A"]
    vowel=["a","i","e","u","o",65,73,69,85,79]
    #vowelcode=[65,73,69,85,79]
    if letter.isalpha() and len(letter) == 1:


        if letter in vowel or ord(letter) in vowel:
            
            print("ITS vowel")
            break
        if letter=="y" or letter=="Y":
            print("'Y' sometimes is vowel sometimes is consonant")
            break
        else:
            print("Its consonant")
            break


    else:
        letter=input("Please input One letter")