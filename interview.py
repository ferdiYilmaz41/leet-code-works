def closestPalindrome(num):
    def isPalindrome(num):
        return str(num)==str(num)[::-1]
    
    if isPalindrome(num): return num

    left=num-1
    right=num+1
    while not isPalindrome(left):
        left-=1
    while not isPalindrome(right):
        right-=1

    if right-num==num-left: return left
    if right-num<num-left: return right 
    else: return left

#print(closestPalindrome(1000))

def countOfDigits(num):
    if num==0: return 1
    count=0
    if num<0: num+=-2*num 
    while num>0:
        num= num//10
        count+=1
    return count

#print(countOfDigits(-1235))