class Solution(object):
    def evalRPN(self, tokens):
        n = len(tokens)
        S = [0] * n
        top=0

        for i in range(n):
            t = tokens[i]

            if t == "+" or t == "-" or t == "*" or t == "/":

                top= top- 1
                b = S[top]

                top = top- 1
                a = S[top]

                if t=="+":
                    r= a+b

                if t =="-":
                    r = a-b

                if t== "*":
                    r=a* b

                if t =="/":
                    r =int(float(a) / float(b))

                S[top]= r
                top = top + 1

            else:

                x = int(t)

                S[top] = x
                top = top + 1

        return S[top - 1]