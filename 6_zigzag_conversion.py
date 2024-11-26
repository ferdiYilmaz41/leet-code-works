def convert(s, numRows):
        """ 14/3=4,  7   14/4= 3, 7    14/5=2,9 
        :type s: str
        :type numRows: int 00,10,20,30,21,12,03,13,23,33,24,15,06,16,26,36,
        :rtype: str
        """
        

        if numRows == 1 or numRows >= len(s): 
            return s
        matrix = [['' for _ in range(len(s))] for _ in range(numRows)]
        index=0
        col=0
        row=0
        rowFlag=0
        while index < len(s):
            if(col==0):
                for row in range(numRows):
                    if(index>=len(s)):break
                    
                    matrix[row][col]=s[index]
                    index += 1
            col+=1
            for i in range(numRows-2, -1, -1):
                if(index>=len(s)):break
                
                matrix[i][col]=s[index]
                col+=1
                index+=1
            col-=1
            row=1
            for row in range(1,numRows):
                if(index>=len(s)):break
                    
                matrix[row][col]=s[index]
                index += 1
        
        # for i in range(numRows):
        #     print( '' .join(matrix[i]))
        result = ''
        for i in range(numRows):
             for j in range(len(s)):
                 if matrix[i][j] != '':
                     result += matrix[i][j]
        
        return result


convert("PAYPALISHIRING",4)
            