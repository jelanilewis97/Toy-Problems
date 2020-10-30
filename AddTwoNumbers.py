# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        node = l1
        while node is not None:
            num1 += str(node.val)
            node = node.next
        node = l2
        while node is not None:
            num2 += str(node.val)
            node = node.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        sum = int(num1) + int(num2)
        sum = str(sum)
        list = ListNode(sum[len(sum)-1])
        node = list
        for index in range(1, len(sum)):
            node.next = ListNode(sum[len(sum)-index-1])
            node = node.next
        return list
