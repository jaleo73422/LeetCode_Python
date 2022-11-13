基本題要求特殊解考慮Bitwise，
加法分成單純加法不進位跟單純進位兩部分，
兩部份分別計算後再相加，
直到不再進位為止。

使用Python和Java或C不同，
後兩者允許的最長位數為32bits，
超出32bits會被移除成0，
進而終止while，
然而Python允許的位數更長，
迴圈不會被正確的終止，
因此需以mask(0xFFFFFFFF)配合&特性，
將Python限制在跟Java或C一樣的32bits，
超出的32bits會被移除。

解決無限迴圈的問題後，
若結果為負數，
Python會誤判，
需另外處理，
詳見[BEST LeetCode 371 Explanation for Python](https://leetcode.com/problems/sum-of-two-integers/discuss/776952/python-best-leetcode-371-explanation-for-python)。