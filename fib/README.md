Recall the definition of the Fibonacci numbers:

*f<sub>1</sub>* := 1

*f<sub>2</sub>* := 2

*f<sub>n</sub>* := *f<sub>n−1</sub>* + *f<sub>n−2</sub>* (*n* ≥ 3)

Given two numbers *a* and *b*, calculate how many Fibonacci numbers are in the range [*a*, *b*].

## Input

The input contains several test cases. Each test case consists of two non-negative integer numbers *a* and *b*. Input is terminated by *a* = *b* = 0. Otherwise, *a* ≤ *b* ≤ 10<sup>100</sup>. The numbers *a* and *b* are given with no superfluous leading zeros.

## Output

For each test case output on a single line the number of Fibonacci numbers *f<sub>i</sub>* with *a* ≤ *f<sub>i</sub>* ≤ *b*.

## Sample Input

```
10 100
1234567890 9876543210
0 0
```

## Sample Output

```
5
4
```

***
