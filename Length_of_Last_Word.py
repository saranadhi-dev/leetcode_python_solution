def lengthOfLastWord(s):
        s = s.strip()
        return(len(s.split(' ')[-1]))

print(lengthOfLastWord('   fly me   to   the moon  '))
