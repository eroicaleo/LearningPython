#!/usr/bin/env python3

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line, ret = [], []
        currlen = 0
        for w in words:
            currlen += len(w)
            if currlen > maxWidth:
                # one line has been fullfilled
                numOfSpaces = maxWidth - (currlen - len(w) - len(line))
                if len(line) > 1:
                    lineString = ''
                    a, b = numOfSpaces // (len(line)-1), numOfSpaces % (len(line)-1)
                    print(numOfSpaces, a, b)
                    for i in range(b):
                        lineString += line[i] + ' ' * (a+1)
                    for i in range(b, len(line)-1):
                        lineString += line[i] + ' ' * a
                    lineString += line[-1]
                else:
                    lineString = line[0] + ' '*numOfSpaces
                ret.append(lineString)
                line = [w]
                currlen = len(w)+1
            else:
                line.append(w)
                # patch a space after current word
                currlen += 1
        ret.append(' '.join(line) + ' '*(maxWidth-len(' '.join(line))))
        return ret

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
sol = Solution()
print(sol.fullJustify(words, maxWidth))
