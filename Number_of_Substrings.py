def numOfStrings(patterns, word):
    count = 0
    for pattern in patterns:
        if word.count(pattern,0,(len(word))):
            count+=1

    return count
        
print(numOfStrings(["a","abc","bc","d"],"abc"))
print(numOfStrings(["a","b","c"],"aaaaabbbbb"))
print(numOfStrings(["a","a","a"],"ab"))

