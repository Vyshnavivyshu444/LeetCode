class Solution:
    def reverseString(self, s: List[str]) -> None:
        # we can also do this by reverse()
      # s.reverse()
        i=0
        j=len(s)-1
        while i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp 
            i+=1
            j-=1
