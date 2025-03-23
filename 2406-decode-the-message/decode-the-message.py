class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyDict={}
        lett='a'
        ans=""
        for letter in key:
            if letter==" ":
                continue
            elif letter not in keyDict :
                keyDict[letter]=lett
                lett=chr(ord(lett)+1)
        for letter in message:
            if letter==" ":
                ans += " "
            else:
                ans += keyDict.get(letter, '')
        return ans