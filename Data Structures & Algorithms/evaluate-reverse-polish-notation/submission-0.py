class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations={
            "+":lambda x,y:y+x,
            "-":lambda x,y:y-x,
            "*":lambda x,y:y*x,
            "/":lambda x,y:int(y/x)
        }
        stack=[]
        for token in tokens:
            if token in operations:
                stack.append(operations[token](stack.pop(),stack.pop()))
            else:
                stack.append(int(token))
        return stack[-1]
            
            
