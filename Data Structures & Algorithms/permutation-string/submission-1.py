class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashSet = set()
        alpha = [0]*26

        for c in s1:
            alpha[ord(c)-ord('a')] += 1

        hashSet.add(tuple(alpha))
        
        alpha = [0]*26
        count = 0
        for i in range(len(s2)):
            if count < len(s1):
                count += 1
                alpha[ord(s2[i])-ord('a')] += 1
                continue
            else:
                if tuple(alpha) in hashSet:
                    return True
                else:
                    alpha[ord(s2[i-len(s1)])-ord('a')] -= 1
                    alpha[ord(s2[i])-ord('a')] += 1

        if tuple(alpha) in hashSet:
            return True

        return False