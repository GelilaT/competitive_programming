class Solution(object):
    def sortSentence(self, s):
        dic = {}
        for i in s.split():
            dic[i[-1]] = i[:-1]

        final = []
        for num, word in sorted(dic.items()):
            final.append(word)
        return " ".join(final)
