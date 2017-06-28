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
        head = None
        nextNode = None
        carry = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            newNode = ListNode(sum % 10)
            if head == None:
                head = newNode
                nextNode = newNode
            else:
                nextNode.next = newNode
                nextNode = nextNode.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            sum = l1.val + carry
            carry = sum // 10
            newNode = ListNode(sum % 10)
            if head == None:
                head = newNode
                nextNode = newNode
            else:
                nextNode.next = newNode
                nextNode = nextNode.next
            l1 = l1.next
        while l2 != None:
            sum = l2.val + carry
            carry = sum // 10
            newNode = ListNode(sum % 10)
            if head == None:
                head = newNode
                nextNode = newNode
            else:
                nextNode.next = newNode
                nextNode = nextNode.next
            l2 = l2.next
        if carry != 0:
            newNode = ListNode(carry)
            nextNode.next = newNode
        return head

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