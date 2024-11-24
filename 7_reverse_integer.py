""" This is my first try but has bad runtime and space, so the better one is under this code.
class Solution(object):
    def reverse(self, x):
        ""
        :type x: int
        :rtype: int
        ""
        if x<-2**31 or x>2**31-1:
            return 0
        if -10<x<10:
            return x
        if x<0:
            y = int(str(-x)[::-1])  # reverse it without "-"
            y = -y
        else:
            y = str(x)[::-1]
            y=int(y)
            
        if y<-2**31 or y>2**31-1:
            return 0

        return y
"""
""" This is kinda better

class Solution(object):
    def reverse(self, x):
        ""
        :type x: int
        :rtype: int
        ""
        if x<-10**31 or x>10**31-1: return 0
        sign = -1 if x < 0 else 1 
        x = abs(x)
        y=0

        while x:
            y= y*10 + x%10
            x= x // 10
        y *= sign
        return 0 if y < -2**31 or y > 2**31 - 1 else y

"""
