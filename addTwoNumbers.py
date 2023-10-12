
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def addOneDigit(val1, val2, carry):
            if val1 is None and val2 is None and carry == 0:
                return None
            elif val1 is None and val2 is None and carry != 0:
                sum = carry
            elif val1 is None:
                sum = val2.val + carry
            elif val2 is None:
                sum = val1.val + carry
            else:
                sum = val1.val + val2.val + carry

            if sum > 9:
                result = ListNode(sum - 10)
                carry = 1
            else:
                result = ListNode(sum)
                carry = 0

            l1_next = val1.next if val1 else None
            l2_next = val2.next if val2 else None

            result.next = addOneDigit(l1_next, l2_next, carry)

            return result

        return addOneDigit(l1, l2, 0)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def addOneDigit(l1, l2, carry):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            if not l1 and not l2 and carry == 0:
                return None
            
            sum = val1 + val2 + carry
            digit = sum % 10
            carry = sum // 10
            

            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None

            result = ListNode(digit, addOneDigit(l1_next, l2_next, carry))
            return result

        return addOneDigit(l1, l2, 0)

