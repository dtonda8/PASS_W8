# PASS_W8
No in-builts allowed :)

### Q1: Valid Anagram (adapted from [here](https://leetcode.com/problems/valid-anagram/description/))
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:  
**Input**: `s` = "anagram", `t` = "nagaram"  
**Output**: true  

Example 2:  
**Input**: `s` = "rat", `t` = "car"  
**Output**: false

Constraints:  
1 <= `s.length`, `t.length` <= $5 \times 10^4$  
`s` and `t` consist of lowercase English letters.

---

### Q2: Power of Three 
Given an integer `n`, return true if it is a power of three (without using the `log` function). Otherwise, return false.

An integer `n` is a power of three, if there exists an integer x such that `n` == $3^x$.

Example 1:
**Input**: n = 27  
**Output**: true  
Explanation: 27 = $3^3$


Example 2:  
**Input**: n = 0  
**Output**: false  
Explanation: There is no x where $3^x$ = 0.

Example 3:  
**Input**: n = -1  
**Output**: false  
Explanation: There is no x where $3^x$ = -1.

Extra: if you done the iterative approach, try the recursive approach (or vice versa)

---
### Testing you algorithm
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
```

- If you encounter errors with the above, make sure that at least python runs on terminal
```sh
python3
```

- You may be directed to Microsoft Store (Windows), if so install python from there
- For if issues persist on Mac,  see this: https://docs.python-guide.org/starting/install3/osx/
