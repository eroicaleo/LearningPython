#!/usr/bin/env python3

import operator

class CityData:
    def __init__(self):
        self.growthRate = 0.0
        self.cityName = 'Star City'
        self.stateName = 'New Star'
        self.data = [0, 0, 0]
        self.isValid = False
    def __str__(self):
        return '"%s, %s": %s, %.3f' % (self.cityName, self.stateName, self.data, self.growthRate)

class StateData:
    def __init__(self, state):
        self.stateName = state
        self.data = [0, 0, 0]
        self.growthRate = 0.0
    def __add__(self, city):
        if self.stateName != city.stateName:
            raise NameError('%s is in %s state, not in %s state' % (city.cityName, city.stateName, self.stateName))
        self.data = [sum(x) for x in zip(self.data, city.data)]
        self.growthRate = (self.data[-1] - self.data[0]) / self.data[0] if self.data[0] > 0 else 0.0
        return self
    def __iadd__(self, city):
        self.__add__(city)
        return self
    def __str__(self):
        return '"%s": %s, %.3f' % (self.stateName, self.data, self.growthRate)

def processLine(line):
    city = CityData()
    lineData = line.rstrip().split(',')
    city.cityName = lineData[0][1:]
    city.stateName = lineData[1][1:-1]
    cityPopulationData = [float(d) for d in lineData[2:]]
    city.data = cityPopulationData
    if cityPopulationData[-1] >= threshold:
        city.growthRate = (cityPopulationData[-1] - cityPopulationData[0]) / cityPopulationData[0]
        city.isValid = True
    else:
        city.isValid = False
    return city

##----------------------------------------------------------------------------------------------------
## Initialize some data
##----------------------------------------------------------------------------------------------------
cityList = list()
stateDict = dict()

threshold = 50000

##----------------------------------------------------------------------------------------------------
## Process the file
##----------------------------------------------------------------------------------------------------
f = open('75f647c2ac77-Metropolitan_Populations_2010-2012_.csv', encoding = "ISO-8859-1")
f.readline()

for line in f:
    city = processLine(line)
    if not city.stateName in stateDict:
        # print('Create a state: %s' % city.stateName)
        stateDict[city.stateName] = StateData(city.stateName)
    stateDict[city.stateName] += city

    if city.isValid:
        cityList.append(city)

f.close()

##----------------------------------------------------------------------------------------------------
## Find the state with top growth rate and top shrinking rate
##----------------------------------------------------------------------------------------------------
cityList = sorted(cityList, key=operator.attrgetter('growthRate'))
print('#'*100)
print('1) Top five cities to target based on highest population growth:')
print('#'*100)
for i in range(5):
    print(cityList[-1-i])
print()

print('#'*100)
print('2) Top five cities to avoid based on the most shrinking population:')
print('#'*100)
for i in range(5):
    print(cityList[i])
print()

##----------------------------------------------------------------------------------------------------
## Process the state
##----------------------------------------------------------------------------------------------------
stateList = sorted(stateDict.values(), key=operator.attrgetter('growthRate'))
print('#'*100)
print('3) Top five states with highest cumulative growth:')
print('#'*100)
for i in range(5):
    print(stateList[-1-i])
