class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack_ops = []
        for el in operations:
            if el == '+':
                summ = stack_ops[-1] + stack_ops[-2]
                stack_ops.append(summ)
            elif el == 'D':
                doub = 2*stack_ops[-1]
                stack_ops.append(doub)
            elif el == 'C':
                stack_ops.pop()
            else:
                stack_ops.append(int(el))
        return sum(stack_ops)
        