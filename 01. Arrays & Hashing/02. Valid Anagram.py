# 242. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False # Since the two words are not the same
        word_s = [letter for letter in s]
        word_t = [letter for letter in t]
        # ['w'] ['o'] ['r'] ['d']
        # a visual of the solution and how i solved it
        # ['o'] ['w'] ['d'] ['r']
        for letter in word_s: # here we are looping through the first word letters
            if letter in word_t:
                word_t.remove(letter) # This will remove the founded letter and will keep going 
            else:
                return False # if the letter was not found then we will return false 
        return True # if the for loop went all the to here and did not return any falsy 