from collections import deque
class CalculatorTask:

    def __init__(self):
        pass
    
    def calculate(self, payload):
        stk = []
        for c in payload:
            if c == ' ':
                continue
            elif c == ')':
                q = deque()
                while stk[-1] != '(':
                    q.appendleft(stk.pop())
                if not stk:
                    raise Exception("Error: Invalid input")
                stk.pop()
                res = self._calculate("".join(q))
                if res < 0 and stk and stk[-1] == '-':
                    res = -res
                    stk[-1] = '+'
                stk.append(str(res))
            else:
                stk.append(c)
        return self._calculate("".join(stk))

    def _calculate(self, payload):
        op = "+"
        stk = []
        val = 0
        for c in payload+"+":
            if c == ' ':
                continue
            if c.isdigit():
                val = val * 10 + int(c)
                continue
            if op == '*':
                stk.append(stk.pop()*val)
            elif op == '/':
                stk.append(int(stk.pop()/val))
            elif op == '-':
                stk.append(-val)
            elif op == "+":
                stk.append(val)
            else:
                raise Exception(f"Error: Invalid operator {op}")
            
            op = c
            val = 0
        return sum(stk)