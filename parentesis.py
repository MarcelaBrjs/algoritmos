#  ACTIVIDAD: Parentesis - 11/08/2021

#  INSTRUCCIONES: Recibes una string conteniendo solo () y []. Crea un
#  algoritmo para validar que la sintaxis de los corchetes es correcta:
#  Ejemplos validos:
#  - '()'
#  - '()()()()()()()()()'
#  - '([])[]()'
#  Ejemplos no validos:
#  - ')'
#  - '()['
#  - '(([))]'
#  - '(((((((((((((((((((((((((((((((((('

def validandoParentesis(string):

    stack = []

    if string != '':
        for i in string:
            if i == '[' or i == '(':
                stack.append(i)
            elif i == ']' or i == ')' and len(stack) > 0:
                if stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '(' and i == ')':
                    stack.pop()
                else:
                    return 'La sintaxis de la cadena es incorrecta.'
            else:
                return 'La sintaxis de la cadena es incorrecta.'
        if len(stack) == 0:
            return 'La sintaxis de la cadena es correcta.'
        else:
            return 'La sintaxis de la cadena es incorrecta.'
    else:
        return 'La cadena está vacia.'


# Pruebas
print('#1. Resultado esperado: Cadena vacía')
print(validandoParentesis(''))

print('#2. Resultado esperado: Sintaxis correcta')
print(validandoParentesis('()'))
print(validandoParentesis('()()()()()()()()()'))
print(validandoParentesis('([])[]()'))

print('#2. Resultado esperado: Sintaxis incorrecta')
print(validandoParentesis(')'))
print(validandoParentesis('()['))
print(validandoParentesis('(([))]'))
print(validandoParentesis('(((((((((((((((((((((((((((((((((('))
