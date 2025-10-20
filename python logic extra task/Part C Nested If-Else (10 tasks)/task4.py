# 25. Find if a character is alphabet and if so, vowel/consonant.
ch = input("enter character :")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):

    if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
        print("Character is vovel")
    else:
        print('Character is constant')

else :
    print("charecter is not alphabet")
