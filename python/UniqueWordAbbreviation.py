class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = dictionary
        self.abbrs = {}
        for word in dictionary:
            abbr = self.abbreviation(word)
            if abbr in self.abbrs and word != self.abbrs[abbr]:
                self.abbrs[abbr] = ""
            else:
                self.abbrs[abbr] = word

    def abbreviation(self, string):
        return string[:1] + str(len(string) - 2) + string[-1:]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        if abbr in self.abbrs:
            if self.abbrs[abbr] == word:
                return True
            else:
                return False
        return True

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")