# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = nextNode = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            newNode = ListNode(carry % 10)
            carry //= 10
            nextNode.next = newNode
            nextNode = nextNode.next
        return head.next

# temp2 = ListNode(0)
# temp3 = ListNode(4)
# temp4 = ListNode(3)
temp2 = ListNode(0)
temp5 = ListNode(1)
temp6 = ListNode(8)
temp7 = ListNode(9)
# temp2.next = temp3
# temp3.next = temp4
temp5.next = temp6
# temp6.next = temp7
s = Solution()
result = s.addTwoNumbers(temp5,temp2)
while result != None:
    print(result.val)
    result = result.next