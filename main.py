import time                                                                                                                               # Importar la biblioteca time para medir la ejecución

class Stack:
    def __init__(self, maxSize):
        self.__maxSize = maxSize
        self.__stack = [None] * maxSize
        self.__nItems = 0
        self.__ptr = -1
    
    def isEmpty(self):
        return self.__nItems == 0
    
    def isFull(self):
        return self.__nItems == self.__maxSize
    
    def __len__(self):
        return self.__nItems
    
    def push(self, element):
        if self.isFull():
            raise Exception("Stack overflow")
        self.__ptr += 1
        self.__stack[self.__ptr] = element
        self.__nItems += 1
        return f"Element: {element} push"
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        elementPopped = self.__stack[self.__ptr]
        self.__stack[self.__ptr] = None
        self.__ptr -= 1
        self.__nItems -= 1
        return elementPopped
    
    def peek(self):
        return self.__stack[self.__ptr]
    
    def __str__(self):
        stackForm = "{"
        for element in range(self.__nItems):
            stackForm += f"{self.__stack[element]}"
            if element != self.__nItems - 1:  
                stackForm += ", "
        stackForm += "}"
        return stackForm

def identity(x): return x

class Queue(object):
    def __init__(self, size):                                                                                                               # Constructor
        self.__maxSize = size                                                                                                               # Tamaño del arreglo [circular]
        self.__que = [None] * size                                                                                                          # Cola almacenada como una lista
        self.__front = 1                                                                                                                    # La cola vacía tiene frente en 1
        self.__rear = 0                                                                                                                     # Después de rear y
        self.__nItems = 0                                                                                                                   # No hay elementos en la cola

    def insert(self, item):                                                                                                                 # Insertar elemento al final de la cola
        if self.isFull():                                                                                                                   # Si no está llena
            raise Exception("Queue overflow")
        self.__rear += 1                                                                                                                    # Rear se mueve uno a la derecha
        if self.__rear == self.__maxSize:                                                                                                   # Se ajusta al arreglo circular
            self.__rear = 0
        self.__que[self.__rear] = item                                                                                                      # Almacenar elemento en rear
        self.__nItems += 1
        return True

    def remove(self):                                                                                                                       # Remover elemento del frente de la cola
        if self.isEmpty():                                                                                                                  # Y devolverlo, si no está vacía
            raise Exception("Queue underflow")
        front = self.__que[self.__front]                                                                                                    # Obtener el valor en frente
        self.__que[self.__front] = None                                                                                                     # Eliminar referencia del elemento
        self.__front += 1                                                                                                                   # Frente se mueve uno a la derecha
        if self.__front == self.__maxSize:                                                                                                  # Se ajusta al arreglo circular
            self.__front = 0
        self.__nItems -= 1
        return front

    def peek(self):                                                                                                                         # Devolver el elemento más frontal
        return None if self.isEmpty() else self.__que[self.__front]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def __len__(self):
        return self.__nItems

    def __str__(self):                                                                                                                      # Convertir cola a cadena
        ans = "["                                                                                                                           # Comienza con corchete izquierdo
        for i in range(self.__nItems):                                                                                                      # Recorrer los elementos actuales
            if len(ans) > 1:                                                                                                                # Excepto junto al corchete izquierdo,
                ans += ", "                                                                                                                 # Separar elementos con coma
            j = i + self.__front                                                                                                            # Desplazamiento desde el frente
            if j >= self.__maxSize:                                                                                                         # Se ajusta al arreglo circular
                j -= self.__maxSize
            ans += str(self.__que[j])                                                                                                       # Agregar forma de cadena del elemento
        ans += "]"                                                                                                                          # Cierra con corchete derecho
        return ans
                                                                                                                                            # Funciones a utilizar
import re                                                                                                                                   # Importar la biblioteca de expresiones regulares

def isValid(expression):
                                                                                                                                            # eliminarEspaciosDeLaExpresion
    expression = expression.replace(" ", "")
    
                                                                                                                                            # verificarSiLaExpresionEstaVacia
    if not expression:
        return False
    
                                                                                                                                            # verificarSiLosParentesisEstanBalanceados (cantidad de '(' y ')')
    if expression.count('(') != expression.count(')'):
        return False
    
                                                                                                                                            # expresionRegularParaVerificarSiLaSintaxisEsValida (números, operadores, paréntesis)
    pattern = r"^[0-9()+\-*/.]+$"
    if not re.match(pattern, expression):
        return False
    
                                                                                                                                            # verificarQueLosOperadoresEstanEnLugaresCorrectos (sin operadores consecutivos, etc.)
                                                                                                                                            # estaExpresionRegularEvitaOperadoresConsecutivosOAlInicioOFinal
    errorPattern = r"(^[+\-*/])|([+\-*/]{2,})|([+\-*/]$)"
    if re.search(errorPattern, expression):
        return False
    
                                                                                                                                            # siLlegaAquiLaExpresionPareceValida
    return True

def precedence(operator, operators=["|", "&", "+-", "*/%", "^", "()"]):
                                                                                                                                            # iterarPorLosOperadoresParaDevolverElValorDePrecedenciaDelOperador
    for p, ops in enumerate(operators):
        if operator in ops:
            return p + 1                                                                                                                    # devolverLaPrecedenciaDelOperadorDesdeUno

def isDelimiter(char, operators=["|", "&", "+-", "*/%", "^", "()"]):
                                                                                                                                            # devolverTrueSiElCaracterEsUnDelimitadorBasadoEnSuPrecedencia
    return precedence(char) == len(operators)

def nextToken(s):                                                                                                                           # analizarElSiguienteTokenDeLaCadenaDeEntrada
    token = ""                                                                                                                              # elTokenPuedeSerUnOperadorOUnoOperando
    s = s.strip()                                                                                                                           # eliminarEspaciosALosLadosDeLaCadena
    if len(s) > 0:                                                                                                                          # siNoSeHaLlegadoAlFinalDeLaCadena
        if precedence(s[0]):                                                                                                                # verificarSiElPrimerCaracterEsUnOperador
            token = s[0]                                                                                                                    # elTokenEsUnOperadorDeUnCaracter
            s = s[1:]                                                                                                                       # eliminarElOperadorDeLaCadena
        else:                                                                                                                               # siEsUnOperandoTomarCaracteresHastaElSiguienteOperadorOEspacio
            while len(s) > 0 and not (
                precedence(s[0]) or s[0].isspace()
            ):
                token += s[0]
                s = s[1:]
    return token, s                                                                                                                         # devolverElTokenYLaCadenaRestante

def postfixTranslate(formula):                                                                                                              # traducirUnaFormulaInfijaAPostfija
    if not isValid(formula): raise Exception("The expression is not valid.")                                                                # verificarSiLaFormulaEsValida
    postfix = Queue(100)                                                                                                                    # almacenarTemporalmenteLaExpresionPostfijaEnUnaCola
    stack = Stack(100)                                                                                                                      # usarUnaPilaParaOperadoresDuranteElAnalisis
    result = []                                                                                                                             # almacenarLosPasosParaVisualizacion
    
    token, formula = nextToken(formula)                                                                                                     # obtenerElPrimerTokenDeLaFormula
    while token:                                                                                                                            # mientrasHayaTokensPorProcesar
        tokenPrecedence = precedence(token)                                                                                                 # obtenerLaPrecedenciaDelToken
        isDelimiterToken = isDelimiter(token)                                                                                               # verificarSiElTokenEsUnDelimitador
        
        if isDelimiterToken:                                                                                                                # siElTokenEsUnDelimitador (como parentesis)
            if token == '(':                                                                                                                # siEsUnParentesisDeApertura
                stack.push(token)                                                                                                           # apilarElParentesisDeApertura
            else:                                                                                                                           # siEsUnParentesisDeCierre
                while not stack.isEmpty():                                                                                                  # desapilarElementosDeLaPila
                    top = stack.pop()
                    if top == '(':                                                                                                          # hastaEncontrarUnParentesisDeApertura
                        break
                    else:                                                                                                                   # ponerElRestoEnLaColaDeSalida (notacion postfija)
                        postfix.insert(top)
        
        elif tokenPrecedence:                                                                                                               # siElTokenEsUnOperador
            while not stack.isEmpty():                                                                                                      # verificarElOperadorEnLaCimaDeLaPila
                top = stack.pop()
                if top == '(' or precedence(top) < tokenPrecedence:                                                                         # siEsUnParentesisOUnOperadorDeMenorPrecedencia
                    stack.push(top)                                                                                                         # volverAApilarlo
                    break                                                                                                                   # detenerElCiclo
                else:                                                                                                                       # siElOperadorEnLaCimaTieneMayorPrecedencia, moverloALaCola
                    postfix.insert(top)
            stack.push(token)                                                                                                               # apilarElOperadorActual
        
        else:                                                                                                                               # siElTokenEsUnOperando (numero)
            postfix.insert(token)                                                                                                           # agregarloDirectamenteALaCola
        
                                                                                                                                            # mostrarElEstadoDespuesDeCadaIteracion
        result.append(f"Token: {token}, Precedence: {tokenPrecedence if tokenPrecedence else 'N/A'}, Type: {'Operator' if tokenPrecedence else 'Operand'}")
        result.append(f"Stack: {stack}")
        result.append(f"Queue: {postfix}\n")
        
        token, formula = nextToken(formula)                                                                                                 # obtenerElSiguienteToken
    
    while not stack.isEmpty():                                                                                                              # alFinalDeLaEntradaVaciarLaPila
        postfix.insert(stack.pop())                                                                                                         # ponerLosOperadoresRestantesEnLaCola
    
    ans = ""
    while not postfix.isEmpty():                                                                                                            # convertirLaColaEnCadena
        if len(ans) > 0:
            ans += " "                                                                                                                      # separarTokensConEspacios
        ans += postfix.remove()
    
    result.append(f"The postfix representation of {formula} is {ans}")
    return result

def postfixEvaluate(formula):                                                                                                               # traducirInfijaAPostfijaYEvaluarElResultado
    postfixSteps = postfixTranslate(formula)                                                                                                # obtenerLosPasosDeLaConversion
    postfixExpression = postfixSteps[-1].split()                                                                                            # laExpresionPostfijaFinal (ultimoElementoDeLaLista)
    
                                                                                                                                            # filtrarSoloNumerosYOperadoresValidos
    validTokens = [token for token in postfixExpression if token.isdigit() or token in "|&+-*/%^"]
    
    operandStack = Stack(100)                                                                                                               # pilaParaAlmacenarOperandos
    for token in validTokens:
        tokenPrecedence = precedence(token)                                                                                                 # verificarSiElTokenEsUnOperador
        
        if tokenPrecedence:                                                                                                                 # siElTokenEsUnOperador
            right = operandStack.pop()                                                                                                      # obtenerElOperandoDerecho
            left = operandStack.pop()                                                                                                       # obtenerElOperandoIzquierdo
            
                                                                                                                                            # realizarLaOperacionCorrespondiente
            if token == '|':                                                                                                                # operacion OR
                operandStack.push(left | right)
            elif token == '&':                                                                                                              # operacion AND
                operandStack.push(left & right)
            elif token == '+':                                                                                                              # suma
                operandStack.push(left + right)
            elif token == '-':                                                                                                              # resta
                operandStack.push(left - right)
            elif token == '*':                                                                                                              # multiplicacion
                operandStack.push(left * right)
            elif token == '/':                                                                                                              # division
                operandStack.push(left / right)
            elif token == '%':                                                                                                              # modulo
                operandStack.push(left % right)
            elif token == '^':                                                                                                              # potencia
                operandStack.push(left ^ right)
        else:                                                                                                                               # siElTokenEsUnOperando (numero)
            operandStack.push(int(token))                                                                                                   # convertirElTokenAEnteroYApilarlo
        
                                                                                                                                            # mostrarElEstadoLuegoDeProcesarCadaToken
        print(f"After processing {token}, the stack holds: {operandStack}")
    
    print(f"Final result = {operandStack.pop()}")                                                                                           # alFinalDeLaEntradaMostrarElResultado

if __name__ == "__main__":
    infixExpression = input("Enter the arithmetic expression: ")                                                                            # solicitarAlUsuarioUnaExpresion
    startTime = time.time()                                                                                                                 # guardarHoraDeInicio
    postfixSteps = postfixTranslate(infixExpression)                                                                                        # convertirLaExpresionInfijaAPostfija
    print("\n".join(postfixSteps))                                                                                                          # mostrarElProcesoPasoAPasoSoloUnaVez
    postfixEvaluate(infixExpression)                                                                                                        # evaluarLaExpresionPostfija
    endTime = time.time()                                                                                                                   # guardarHoraFinal
    totalTime = endTime - startTime                                                                                                         # calcularTiempoTotalDeEjecucion
    print(f"Execution time: {totalTime}")                                                                                                   # mostrarTiempoTotalDeEjecucion
