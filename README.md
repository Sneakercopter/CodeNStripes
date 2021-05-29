# CodeNStripes
Solution to the 2021 Adidas Code N Stripes Challenge

## The Task
CodeNStripes was an Adidas hosted reverse engineering coding challenge. The challenge consisted of various test inputs and example outputs and the task was to create a function `adidas_microchallenge_1` which takes an input and applies some hidden logic based on the input paramaters to achieve the desired results.


This hidden logic had to be deduced only from example inputs and outputs and no further hints were provided. As it turned out, each further character which was added to the input string added some additional unique logic. 


## The Solution
My solution to the challenge is written in Python3 and is availabile in `submission.py`. Time was a factor in this challenge so enjoy my repeated code and poor practices! From all provided examples, the largest provided input was 6 characters in length so there were 6 unique permutations on each inputs provided. The logic was also applied right to left so the indexing outlined below assumes a 6 character input.


**Given a 6 character input**
- Index 5: Recognise the fact that we accept characters as well as numbers, all characters must be converted to their numerical ASCII representation.
- Index 4: Take the number in this index and square it.
- Index 3: Take the number in this index and convert it to binary.
- Index 2: Take the number in this index and divide it by two. Then, make sure to round down the result.
- Index 1: Take the number in this index and convert it to Base-8 (Octal).
- Index 0: Take the number in this index and get the right most single digit of the number and use that as an index. Given the alphabetic order, use that index to get the character that would sit at that number.


After working out all of these conversions, a final string is constructed of all the index results appended together in the same order they were indexed in. This result is then base64 encoded and returned. There were no test cases which had more than 6 characters so there was no evidence to say there was cyclic behaviour of this pattern beyond 6 characters (Although that would have been a cool twist!). 


## Example
Given input `adidas`, the correct result is `aDE0NDUyMTEwMDEwMDk0MDkxMTU=`. Base64 decoded, the output is `h1445211001009409115` - you can work out how I got to this answer via the steps above :-).


## Final Thoughts
This challenge was great and I think Adidas should continue to do them! There is a prize for the top 10 fastest submissions - I solved mine in almost exactly 1 hour and 30 minutes but i'm sure there are quicker people out there! If you did this challenge as well, please open source - I'm curious to see how you tackled it!