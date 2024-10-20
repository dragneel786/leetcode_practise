class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def eval_it():
            nonlocal idx
            ch = expression[idx]
            if ch in ['&', '|', '!']:
                ret = []
                idx += 1
                while(expression[idx] != ')'):
                    if expression[idx] in ['!', '&', '|']:
                        ret.append(eval_it())

                    elif expression[idx] in ['t', 'f']:
                        ret.append(expression[idx] == 't')

                    idx += 1

                if ch == '&':
                    return all(ret) 

                if ch == '|':
                    return any(ret)

                return not ret[0]

        if len(expression) == 1:
            return expression == 't'

        idx = 0
        return eval_it()