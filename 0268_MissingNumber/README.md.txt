解法1:
nums[i]: X X X X X ? => 0 1 2 3 4 5
i:       0 1 2 3 4 5(= len(nums))
ans = sum(nums) - sum(i)

解法2:
1) n ^ 0 = n
2) n ^ n = 0
3) n1 ^ n2 ^ n3 = n3 ^ n1 ^ n2