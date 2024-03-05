#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        - ignore whitespace
        - - or + ) read in - symbol of final results value(defualt as positive)
        - read until the next non0-digit character or the end of the input
        - convert to integer

        bin(2**32-1) : '0b11111111111111111111111111111111'
        bin(-2**32) : '-0b100000000000000000000000000000000'

        Your runtime beats 47.92 % of python3 submissions (40 ms)
        Your memory usage beats 57.66 % of python3 submissions (16.7 MB)
        """
        e = ''
        for tmp in s:
            if tmp == ' ': 
                if len(e) == 0: continue
                else: break
            elif (tmp in ['-', '+'] and len(e)==0) or tmp.isdigit(): e+=tmp
            else: break

        try:
            int_e = int(e)
            bin_e = bin(int_e)
            print(int_e)
            if e[0] == '-':
                if len(bin_e) >= 35: return -2**31
            else:
                if len(bin_e) >= 34: return 2**31-1
            return int_e

        except:
            return 0

        
# @lc code=end

