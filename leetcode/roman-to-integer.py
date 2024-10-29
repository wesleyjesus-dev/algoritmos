class Solution(object):
    def romanToInt(self, s:str):
        """
        :type s: str
        :rtype: int
        """
        dictionary = self.createDictionary()
        outNumber = 0
        # LVIII #
        for romainNumber in s:
            outNumber += dictionary.get(romainNumber)
            pass
        print(outNumber)
    

    def createDictionary(self) -> dict[str, int]:
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
            "M": 1000}
        return dict
        
        
