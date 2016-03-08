class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        m = [0] * 256
        bulls, cows = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if m[int(secret[i])] < 0:
                    cows += 1
                m[int(secret[i])] += 1
                if m[int(guess[i])] > 0:
                    cows += 1
                m[int(guess[i])] -= 1
        return str(bulls) + "A" + str(cows) + "B"