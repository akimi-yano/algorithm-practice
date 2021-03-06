# 804. Unique Morse Code Words
# Easy

# 772

# 749

# Add to List

# Share
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".
# Note:

# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.


# This solution works !:

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictionary = {}
        for i in range(26):
            dictionary[chr(ord('a')+i)] = morse[i]
        
        all_types = set([])
        for word in words:
            ans = ""
            for char in word:
                ans += dictionary[char]
            all_types.add(ans)
        return len(all_types)
        
        
# This solution works - optimization

class Solution:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        all_types = set([])
        for word in words:
            ans = ""
            for char in word:
                ans += Solution.morse[ord(char)-ord('a')]
            all_types.add(ans)
        return len(all_types)
        
        
# This solution works - 1 liner 

class Solution:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len({''.join(Solution.morse[ord(char)-ord('a')] for char in word) for word in words})
        
