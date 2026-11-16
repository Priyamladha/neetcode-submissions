class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        charT, window = {}, {}
        length = float('inf')
        result = [-1,-1]
        l = 0

        for c in t:
            charT[c] = 1 + charT.get(c, 0)
        
        have, need = 0, len(charT)
        for r in range(len(s)):
            currentChar = s[r]
            window[currentChar] = 1 + window.get(currentChar, 0)

            if currentChar in charT and window[currentChar] == charT[currentChar]:
                have +=1

            while have == need:
                window[s[l]] -= 1
                if s[l] in charT and window[s[l]] < charT[s[l]]:
                    have -=1

                tmpLen = r-l+1
                if tmpLen < length:
                    length = tmpLen
                    result = [l,r]
                l+=1

        l, r = result            
        return s[l:r+1] if length != float('inf') else "" 
        