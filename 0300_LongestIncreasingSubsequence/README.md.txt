解法1: Dynamic programming
解法1-1: ... X [i X X]
解法1-2: [X X i] X ...

LIS[i]為以i開頭或結尾的LTS。

解法2: Greedy Algorithm

nums = [10, 9, 2, 5, 1, 4, 101, 18, 6]

[X, X,  X, X,   X, ..., X]
[X, 10, X, X,   X, ..., X]
[X, 9,  X, X,   X, ..., X]
[X, 2,  X, X,   X, ..., X]
[X, 2,  5, X,   X, ..., X]
[X, 1,  5, X,   X, ..., X]
[X, 1,  4, X,   X, ..., X]
[X, 1,  4, 101, X, ..., X]
[X, 1,  4, 18,  X, ..., X]
[X, 1,  4, 6,   X, ..., X]

取每段遞減區間中的最小值作為數列。