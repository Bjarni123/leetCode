class Solution(object):
    def makeEqual(self, words):
        letters = {}
        for word in words:
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        wordsCount = len(words)
        for letterCount in letters.values():
            if letterCount % wordsCount != 0:
                return False
        return True
    
print(Solution.makeEqual(0, ["ab","a"]))
        