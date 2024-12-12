# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead=ListNode(0)
        dummy=dummyhead
        rem=0
        sum=0
        while l1 or l2 or rem:
            sum=rem
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
            rem=sum//10
            num=sum%10
            dummy.next=ListNode(num)
            dummy=dummy.next

        return dummyhead.next

                

        

            

            


        
        