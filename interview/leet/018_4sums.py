#!/usr/bin/env python

class Solution:

    def fourSum(self, nums, target):
        # Generate the following DB
        # 1. a dictionary to verify solutions 
        # 2. a level-1 dictionary to hold sum of 2 integers
        # 3. a list of integers to do 2nd addition
        validSolutionDict = dict()
        level1Dict = dict()
        numsLevel2 = list()
        N = len(nums)
        for i in range(N):
            m = nums[i]
            if not m in validSolutionDict:
                validSolutionDict[m] = 1
            else:
                validSolutionDict[m] += 1
            for j in range(i+1, N):
                n = nums[j]
                level1Sum = m + n
                if not level1Sum in level1Dict:
                    level1Dict[level1Sum] = []
                    numsLevel2.append(level1Sum)
                level1Dict[level1Sum].append((i, j))
                # print('i = %d, j = %d, (m, n) = %s, level1Dict: %s, numsLevel2: %s' % (i, j, (nums[m], nums[n]), level1Dict, numsLevel2))
            # print('i = %d, validSolutionDict: %s' % (i, validSolutionDict))

        # print('In 2nd level')
        N = len(numsLevel2)
        self.solutionDict = dict()
        for i in range(N):
            for j in range(i, N):
                m, n = numsLevel2[i], numsLevel2[j]
                if m + n == target:
                    # print(m, n)
                    self.getSolutions(level1Dict[m], level1Dict[n], nums)

        ret = [key for key in self.solutionDict]
        # print(ret)
        return ret

    def getSolutions(self, set1, set2, nums):
        ret = []
        indexList = [(p + q) for p in set1 for q in set2 if len(set(p+q)) == 4]
        for index in indexList:
            sol = tuple(sorted([nums[i] for i in index]))
            if not sol in self.solutionDict:
                self.solutionDict[sol] = 1


sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
nums = [-500,-499,-486,-474,-470,-462,-426,-426,-411,-409,-366,-361,-359,-355,-350,-349,-303,-297,-255,-238,-222,-215,-203,-201,-198,-193,-193,-187,-179,-156,-150,-139,-99,-93,-87,-58,-54,-8,-2,1,5,6,8,9,15,31,37,48,50,95,128,181,201,206,235,244,251,272,285,287,289,305,308,338,357,367,386,391,392,395,395,402,410,449,458,466,478,485,488]
target = -2701
print(nums)
print(sol.fourSum(nums, target))
