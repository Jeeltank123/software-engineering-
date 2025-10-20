# 37. Count how many vowels and consonants in a word
word = input("Enter word :")
i = 0
vowels =0
consonants=0
while i < len(word):
    ch = word[i]

    if ch>= 'A' and ch<='Z':
        if ch=='A' or ch=='E' or ch =='I' or ch == 'O' or ch == 'U':
            vowels+=1
        else:
            consonants+=1

    elif ch>='a' and ch<='z':
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            vowels+=1
        else:
            consonants+=1
    i+=1
print("Word :",word)
print(f"vowels :{vowels} and consonants :{consonants}")