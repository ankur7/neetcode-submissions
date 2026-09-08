class Solution:
    def __init__(self):
        self.delimiter = "(^&$#^)"
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ''
        for strr in strs:
            encoded += self.delimiter + strr

        return encoded       
        

    def decode(self, s: str) -> List[str]:
        print('ss', s)
        if not s:
            return []

        decoded = s.split(self.delimiter)[1:(len(s)) - 1]
        print(decoded)
        result = []
        for strr in decoded:            
            result.append(strr)
        # if not result:
        #     return [""]
        return result
        