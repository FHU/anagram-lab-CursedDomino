def anagram(word1, word2):
    if word1.isspace()  == True:
        return False
    
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')

    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) == len(word2):
        sum1 = 0
        sum2 = 0
        for letter in word1:
            sum1 += word1.count(letter)
        for letter in word2:
            sum2 += word2.count(letter)

        if sum1 == sum2:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    word1 = input()
    word2 = input()
    print(anagram(word1, word2))