#Approach 1:
class Solution:
    def reverseWords(self, s: str) -> str:
        result, i, n = '', 0, len(s)
        
        while i<n:
            while i<n and s[i]==' ': i+=1
            if i >= n: break
            j = i + 1
            while j<n and s[j]!=' ': j+=1
            sub = s[i:j]
            if len(result)==0: result = sub
            else: result = "".join((sub, ' ', result))
            i = j + 1
        return result

#Approach 2: Pythonic - But not advised in an interview
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))