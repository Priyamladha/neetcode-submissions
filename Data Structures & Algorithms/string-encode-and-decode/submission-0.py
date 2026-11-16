class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(chr(len(s)) + s for s in strs)

    def decode(self, s: str) -> List[str]:
        ans=[]
        i = 0
        while i<len(s):
            length = ord(s[i])
            word = s[i+1:i+1 + length ]
            ans.append(word)
            i+=length+1
        return ans