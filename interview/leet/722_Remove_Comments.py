#!/usr/bin/env python3

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        length, i, ret = len(source), 0, []
        while i < length:
            index1 = source[i].find('//')
            index2 = source[i].find('/*')
            if index2 > index1 >= 0 or index1 >= 0 > index2:
                ret += [source[i][:index1]]
            elif index1 > index2 >= 0 or index2 >= 0 > index1:
                tmp = source[i][:index2]
                index3, i = source[i].find('*/', index2+2), i+1
                while index3 < 0 and i < length:
                    index3, i = source[i].find('*/'), i+1
                source[i-1], i = tmp + source[i-1][index3+2:], i-2
            else:
                ret += [source[i]]
            i += 1
        return list(filter(len, ret))

source = ["a/*/b//*c","blank","d/*/e*//f"]
source = ["a/*comment", "line", "more_comment*/b"]
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source = ["/*/dadb/*/aec*////*//*ee*//*//b*////*badbda//*bbacdbbd*//ceb//*cdd//**//de*////*"]
sol = Solution()
print(sol.removeComments(source))
