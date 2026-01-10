class Solution:
  def largestGoodInteger(self, num: str) -> str:
    return max(num[i - 2:i + 1]
               if num[i] == num[i - 1] == num[i - 2]
               else '' for i in range(2, len(num)))
        # ----------
        # max_good = ""

        # for i in range(len(num) - 2):
        #     # Take substring of length 3
        #     sub = num[i:i+3]

        #     # Check if all characters are the same
        #     if sub[0] == sub[1] == sub[2]:
        #         # Update maximum good integer
        #         if sub > max_good:
        #             max_good = sub

        # return max_good


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Multiple same digits, should return largest
    assert solution.largestGoodInteger("6777133339") == "777"
    
    # Test case 2: No three same digits, should return empty string
    assert solution.largestGoodInteger("2891047258") == ""
    
    # Test case 3: Three same digits at the start
    assert solution.largestGoodInteger("111222333") == "333"
    
    # Test case 4: Multiple groups, largest is first
    assert solution.largestGoodInteger("999111222") == "999"
    
    print("All test cases passed!")

# Question = https://leetcode.com/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2026-01-10