

def firstPalindrome(self, words):
    def isPanlindrome(word):
        start = 0
        N = len(word)
        end = N - 1

        while (start < end):
            if word[start] == word[end]:
                start += 1
                end -= -1
            else:
                return False

        return True

    for item in words:
        if (isPanlindrome(item) == True):
            print(item)
        print("None")


words = ["notapalindrome", "racecar"]

firstPalindrome(True, words)
