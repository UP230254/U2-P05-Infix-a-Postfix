import Pila

class Infix2Postfix:
    def __init__(self):
        self.prioridad = {'(': 0,'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sqrt': 3,'sin': 4, 'cos': 4, 'tan': 4, 'log': 4, 'ln': 4,'asin': 4, 'acos': 4, 'atan': 4, 'alog': 4, 'aln': 4}

    def infix2postfix(self, expresion):
        pila, postfix = Pila.Pila(), []
        pila.push('(')
        expresion += ')'
        i = 0

        while i < len(expresion):
            if expresion[i].isspace():
                i += 1
                continue
            if expresion[i] == '(':
                pila.push('(')
            elif expresion[i] == ')':
                while pila.get_top() != '(':
                    postfix.append(pila.pop())
                pila.pop()
            elif expresion[i].isdigit() or (expresion[i] == '-' and (i == 0 or expresion[i-1] in '()+-*/^')):
                num = '-' if expresion[i] == '-' else ''
                i += num == '-'
                while i < len(expresion) and (expresion[i].isdigit() or expresion[i] == '.'):
                    num += expresion[i]
                    i += 1
                postfix.append(num)
                continue
            else:
                op = next((expresion[i:i+k] for k in (4, 3, 2, 1) if expresion[i:i+k] in self.prioridad), expresion[i])
                i += len(op) - 1
                while self.prioridad.get(pila.get_top(), -1) >= self.prioridad[op]:
                    postfix.append(pila.pop())
                pila.push(op)
            i += 1
        return ' '.join(postfix)
