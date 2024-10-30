class Solution(object):
    def __init__(self):
        self.dict = self.createDictionary()

    def romanToInt(self, s):
        number = 0
        count = 0
        while count < len(s):
            result = self.checkIfMoreTwoDigit(count,s)
            if result > 0:
                number += result
                count += 2
            else:
              number += self.dict.get(s[count])
              count += 1
              print(count)
        return number
    
    def checkIfMoreTwoDigit(self, index:int, romain:str) -> int:
        result = 0
        loopEnabled = True
        if (index + 1) > len(romain) -1:
            return 0
        while loopEnabled:
            temp = romain[index] + romain[index+1]
            result = self.dict.get(temp)
            if result is None:
                loopEnabled = False
                return 0
            else:
                loopEnabled = False
        return result
    
    def createDictionary(self) -> (str | int):
        dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500, 
            "CM": 900,
            "M": 1000
        }
        return dict