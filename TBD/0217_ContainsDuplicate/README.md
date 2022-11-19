hm = []

for i in nums:
    if i in hm:
        return True
    
    hm.append(i)

return False

同樣用Hashmap
以Set時見的速度會比List快上許多，
主要差別在查詢，
查詢的時間複雜度分別是O(1)及O(n)，
後者會出現TLE。