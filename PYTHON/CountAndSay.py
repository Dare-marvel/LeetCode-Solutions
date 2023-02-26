# Link to the problem : https://leetcode.com/problems/count-and-say/

class Solution:
    def freqMapper(self, seq):
        # initialize an empty list to store the frequency mapping
        l = []
        # initialize a counter to keep track of the frequency of the current character
        c = 1
        # loop through the sequence
        for i in range(len(seq)):
            # if the current character is the same as the next character, increment the counter
            if i < len(seq)-1 and seq[i] == seq[i+1]:
                c += 1
            else:
                # otherwise, add the current character and its frequency to the frequency mapping
                l.append([int(seq[i]), c])
                # reset the counter for the next character
                c = 1
        # return the frequency mapping
        return l

    def IntegCreator(self, freqlist):
        # initialize an empty string to store the integer sequence
        newStr = str()
        # loop through the frequency mapping
        for i in range(len(freqlist)):
            # concatenate the frequency and the character to the integer sequence
            newStr += str(freqlist[i][1]) + str(freqlist[i][0])
        # return the integer sequence
        return newStr

    def countAndSay(self, n: int) -> str:
        # initialize the previous sequence as "1"
        prevStr = '1'
        # loop n-1 times to generate the nth sequence
        for i in range(n-1):
            # generate the frequency mapping for the previous sequence
            # create the integer sequence from the frequency mapping
            newStr = self.IntegCreator(self.freqMapper(prevStr))
            # update the previous sequence with the new sequence
            prevStr = newStr
        # return the final sequence
        return prevStr
