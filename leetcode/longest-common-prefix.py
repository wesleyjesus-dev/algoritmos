# ["abab","aba",""]
class Solution(object):
    def longestCommonPrefix(self, strs:list):
        prefixes = {}
        last_word = ""

        if len(strs) == 1: # se o array tiver apenas uma palavra
            return word
        
        last_prefix = ""

        for word in strs:
            last_match = ""
            for index_character in range(len(word) -1): # avalia letra por letra
                # ultima palavra for diferente de vazio?
                if last_word != "":
                    # se a ultima palavra for diferente de vazio e o indice 0 de ambas combinem
                    print("word: {index_a} last_word {index_b}".format(index_a = word[index_character],index_b = last_word[index_character]))
                    if word[index_character] == last_word[index_character]:
                        last_match += word[index_character]
                    else:
                        if last_match != "":
                            last_match = ""
                        else:
                            break
                # se nao, guarda a ultima palavra
                else:
                    last_word = word
        return ""

print(Solution().longestCommonPrefix(["abab","aba",""]))
