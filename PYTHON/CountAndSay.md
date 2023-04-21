### [Count And Say](https://leetcode.com/problems/count-and-say/)

## Brief Description:
The Count and Say sequence is a sequence of integers, where each term is created by "saying" the digits of the previous term. To generate a term in the sequence, you start with the first term, which is "1". To generate the second term, you "say" the digits of the first term, which is "one 1", or "11". To generate the third term, you "say" the digits of the second term, which is "two 1s", or "21". And so on.

## Key Insights:
The code implements the Count and Say sequence problem by first defining two helper functions:

freqMapper(seq): This function takes a sequence of integers as input and returns a frequency mapping of the sequence. The frequency mapping is a list of tuples, where each tuple contains the integer value and the frequency of that integer in the sequence. For example, if the input sequence is [1, 1, 2, 3, 3, 3], the frequency mapping would be [(1, 2), (2, 1), (3, 3)].

IntegCreator(freqlist): This function takes a frequency mapping as input and returns an integer sequence. The integer sequence is created by concatenating the frequency and the integer value for each tuple in the frequency mapping. For example, if the input frequency mapping is [(1, 2), (2, 1), (3, 3)], the integer sequence would be "211311".

The main function, countAndSay(n), generates the nth term of the Count and Say sequence by iterating n-1 times. In each iteration, it generates the frequency mapping of the previous term using the freqMapper function, creates the integer sequence from the frequency mapping using the IntegCreator function, and updates the previous term with the new term. After n-1 iterations, the final term is returned

## Code:
```python
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
```
