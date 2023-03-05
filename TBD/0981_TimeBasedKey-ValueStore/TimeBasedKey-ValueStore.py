from collections import defaultdict

class Solution:
    class TimeMap:

        def __init__(self):
            self.key_time = defaultdict(list)
            self.key_value = defaultdict(list)
        
        def bs_r(self, list, value):
            l = 0
            r = len(list) - 1
            m = 0

            while l <= r:
                m = (l + r) // 2

                if list[m] == value:
                    return m + 1
                elif list[m] < value:
                    l = m + 1
                else:
                    r = m - 1

            if list[m] < value:
                return m + 1
            else:
                return m

        def set(self, key, value, timestamp):
            self.key_time[key].append(timestamp)
            self.key_value[key].append(value)        

        def get(self, key, timestamp):
            if key in self.key_time:
                idx = self.bs_r(self.key_time[key], timestamp)
                # idx = bisect_right(self.key_time[key], timestamp)
            else:
                return ""

            if idx > 0:
                return self.key_value[key][idx - 1]
            else:
                return ""


# input
# [] []

# test case 1
# Output: [null, null, "bar", "bar", null, "bar2", "bar2"]
# input:
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]


# test case 1
# Output: [null, null, null, "", "low", "low", "low", "low"]
# input:
# ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
# [[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 15], ["love", 20], ["love", 25]]

# sol = Solution()

# output = sol.rob(nums)
# print(output)