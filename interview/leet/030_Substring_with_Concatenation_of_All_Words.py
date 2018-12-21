#!/usr/bin/env python
class Solution:
    def findSubstring(self, s, words):
        ret = []
        if len(s) == 0 or len(words) == 0:
            return ret
        self.wordsDict, self.uniqueWordsList, self.scoreList = self.getUniqueWordsAndScoreList(words)
        self.stringToIndex(s)
        self.total_score = len(words)
        self.wordLen = len(words[0])
        print(self.index)
        for offset in range(self.wordLen):
            subIndex = self.index[offset::self.wordLen]
            ret += self.checkSubIndex(subIndex, offset)
        return ret

    def getUniqueWordsAndScoreList(self, words):
        wordsDict = dict()
        uniqueWordsList = []
        scoreList = []
        for word in words:
            if not word in wordsDict: 
                uniqueWordsList.append(word)
                wordsDict[word] = len(uniqueWordsList) - 1
                scoreList.append(1)
            else:
                scoreList[wordsDict[word]] += 1
        return wordsDict, uniqueWordsList, scoreList

    def stringToIndex(self, s):
        word_len = len(self.uniqueWordsList[0])
        self.index = [-1] * (len(s) - word_len + 1)
        for i in range(len(self.index)):
            if s[i:i+word_len] in self.wordsDict:
                self.index[i] = self.wordsDict[s[i:i+word_len]]
            else:
                self.index[i] = -1

    def checkSubIndex(self, subIndex, offset):
        print(subIndex)
        currScoreList = [0] * len(self.scoreList)
        score = 0
        head = 0
        ret = []

        for i in range(len(subIndex)):
            ix = subIndex[i]  
            print('head = %d, i = %d, ix = %d' % (head, i, ix))
            if ix == -1:
                print('i = %d, I am in loc 1' % i)
                currScoreList = [0] * len(self.scoreList)
                score = 0
                head = i + 1
                print('score: %d' % score)
            elif currScoreList[ix] == self.scoreList[ix]:
                print('i = %d, I am in loc 2' % i)
                for j in range(head, i):
                    jx = subIndex[j]
                    if jx == ix:
                        head = j + 1
                        break
                    else:
                        score -= 1
                        currScoreList[jx] -= 1
                print('score: %d' % score)
            elif currScoreList[ix] < self.scoreList[ix]:
                print('i = %d, I am in loc 3' % i)
                currScoreList[ix] += 1
                if score + 1 == self.total_score:
                    ret.append(head*self.wordLen+offset)
                    currScoreList[subIndex[head]] -= 1
                    head += 1
                else:
                    score += 1
                print('score: %d, currScoreList: %s' % (score, currScoreList))

        print(ret)
        return ret

    def checkCurrentIndex(self, index, i, numOfWords, wordLen):
        # print('hi: %d' % i)
        if index[i] == -1:
            return False
        score = [0] * numOfWords
        total_score = 0
        for j in range(i, min(i+numOfWords*wordLen, len(index)), wordLen):
            # print('j : %d, index[j]: %d' % (j, index[j]))
            if index[j] == -1:
                return False
            elif score[index[j]] == 1:
                return False
            else:
                score[index[j]] = 1
                total_score += 1
        if total_score == numOfWords:
            return True
        return False


sol = Solution()
# s = "barfoothefoobarman"
# words = ["foo","bar"]
# print(sol.getUniqueWordsAndScoreList(words))
# sol.findSubstring(s, words)

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# print(sol.getUniqueWordsAndScoreList(words))
# sol.findSubstring(s, words)

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# print(sol.getUniqueWordsAndScoreList(words))
# sol.findSubstring(s, words)

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(sol.getUniqueWordsAndScoreList(words))
sol.findSubstring(s, words)
