class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        charT, window = {}, {}

        for c in t:
            charT[c] = 1 + charT.get(c, 0)

        have , need = 0, len(charT)
        l = 0
        res = [-1,-1]

        length = float('infinity')
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in charT and charT[s[r]] == window[s[r]]:
                have +=1

            while have == need:
                window[s[l]] -= 1

                if s[l] in charT and  window[s[l]] < charT[s[l]]:
                    have -=1

                tmplen = r-l+1
                if tmplen < length:
                    res=[l,r]
                    length = tmplen
                l += 1

        l, r = res
        return s[l:r+1] if length != float('infinity') else ""
            