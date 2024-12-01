def maxArea( height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        left=0
        right=len(height)-1
        while left<right:
            if height[left]<=height[right]:
                area=(right-left)*height[left]
                left+=1
            else:
                area=(right-left)*height[right]
                right-=1
            if maxArea<area:maxArea=area

        return maxArea



        # Bu benim iğrenç algoritmam// disgusting O(n^2) algorithm.. öğğğğ
        # for index in range(len(height)):
            
        #     for i in range(len(height)):
        #         newIndex=i + index
        #         if newIndex >= len(height): break
        #         if height[index]<=height[newIndex]: 
        #             area=height[index]*(newIndex-index) 
        #         else :
        #             area=height[newIndex]*(index-newIndex)
        #         if area<0:
        #             area=area-area-area
        #         if maxArea<area: maxArea=area

        # return maxArea

height=[1,8,6,2,5,4,8,3,7]
maxArea(height)