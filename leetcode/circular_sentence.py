class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        is_circular_sentence = False
        sentences = sentence.split(' ')
        if len(sentences) == 1:
            return sentences[0][0] == sentences[0][len(sentence) - 1]

        for index in range(len(sentences)):
            word_length = len(sentences[index]) - 1
            if index == len(sentences) -1:
                is_circular_sentence = sentences[index][word_length] == sentences[0][0]
            else:
                if sentences[index][word_length] == sentences[index + 1][0]:
                    is_circular_sentence = True
                else:
                    is_circular_sentence = False
                    break
        return is_circular_sentence

print(Solution().isCircularSentence("Leetcode eisc cool"))