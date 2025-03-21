class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        items=list(zip(names,heights))
        for i in range(n):
            for j in range(n-i-1):
                if items[j][1]<items[j+1][1]:
                    items[j],items[j+1]=items[j+1],items[j]
        sorted_names=[name for name,hight in items]
        return sorted_names


