import sys

#Analisador lexico
reservedWords = ['ABSOLUTE', 'ARRAY','BEGIN', 'CASE', 'CHAR',
                 'CONST', 'DIV', 'DO' ,'DOWTO' ,'ELSE', 'END',
                 'EXTERNAL', 'FILE', 'FOR', 'FORWARD', 'FUNC','FUNCTION','GOTO','IF', 'IMPLEMENTATION',
                 'IN', 'INTEGER', 'INTERFACE', 'INTERRUPT', 'LABEL', 'MAIN', 'NIL', 'NIT' ,'OF', 'PACKED', 'PROC',
                 'PROGRAM', 'REAL', 'RECORD', 'REPEAT', 'SET', 'SHL', 'SHR', 'STRING' ,'THEN', 'TO','TYPE', 'UNIT',
                 'UNTIL', 'USES', 'VAR', 'WHILE', 'WITH', 'XOR']

relationalOperators = ['=', '>=', '<=', '>', '<', '<>']
arithmeticalOperators = ['+', '-', '*', '/', 'mod']
logicalOperators = ['and', 'or', 'not']
specialSymbols = [',', ':', ';', ')', '(']
assignmentSymbol = [':=']

def isLetter(letter):
    return ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122 or letter.lower() == '_'

def isNumber(letter):
    return ord(letter.lower()) >= 48 and ord(letter.lower()) <= 57

def isPoint(letter):
    return letter == '.'

def isCommentStart(letter, nextLetter):
    return letter == '/' and nextLetter == '*'

def isCommentEnd(letter, nextLetter):
    return letter == '*' and nextLetter == '/'

def isParenthesis(letter):
    return letter == '(' or letter == ')'

def isDotComma(letter):
    return letter == ';'

def isComma(letter):
    return letter == ','

def isTwoPoints(letter):
    return letter == ':'

def isApostropheorQuotes(letter):
    return letter == '"' or letter == "'"

def findDouble(letter, nextLetter):
        return (letter == ':' and nextLetter == '=')\
            or (letter == '>' and nextLetter == '=')\
            or (letter == '<' and nextLetter == '=')\
            or (letter == '<' and nextLetter == '>')

def isWordReserved(term):
    if term.upper() in reservedWords:
        return True
    return False

def isIdentifier(term):
    if term.upper() not in reservedWords and isLetter(term[0]) and term.lower() not in logicalOperators and term.lower() not in arithmeticalOperators:
        return True
    return False

def isIntegerNumber(term):
    if isNumber(term[0]):
        if float(term) % 1 == 0:
            return True
    return False

def isRealNumber(term):
    if isNumber(term[0]):
        if float(term) % 1 != 0:
            return True
    return False

def isArithmeticalOperator(term):
    if term in arithmeticalOperators:
        return True
    return False

def isRelationalOperator(term):
    if term in relationalOperators:
        return True
    return False

def isLogicalOperator(term):
    if term in logicalOperators:
        return True
    return False

def isSpecialSymbol(term):
    if term in specialSymbols:
        return True
    return False

def isAssignment(term):
    if term in assignmentSymbol:
        return True
    return False

def isEnd(term):
    return term == '.'

def isOtherSymbol(term):
    return isDotComma(term) or isComma(term) or isTwoPoints(term) or isArithmeticalOperator(term)\
                or isRelationalOperator(term) or isEnd(term) or isParenthesis(term) or isEnd(term)

def classifyTerm(term):
    if isSpecialSymbol(palavra):
        print palavra + ' SIMBOLOESPECIAL'
    elif isLogicalOperator(palavra):
        print palavra + ' OPERADORLOGICO'
    elif isRelationalOperator(palavra):
        print palavra + ' OPERADORRELACIONAL'
    elif isArithmeticalOperator(palavra):
        print palavra + ' OPERADORARITMETICO'
    elif isAssignment(palavra):
        print palavra + ' ATRIBUICAO'
    elif isWordReserved(palavra):
        print palavra + ' PALAVRARESERVADA'
    elif isIdentifier(palavra):
        print palavra + ' IDENTIFICADOR'
    elif isRealNumber(palavra):
        print palavra + ' NUMEROREAL'
    elif isIntegerNumber(palavra):
        print palavra + ' NUMEROINTEIRO'
    elif isLogicalOperator(palavra):
        print palavra + ' OPERADORLOGICO'
    elif isArithmeticalOperator(palavra):
        print palavra + ' OPERADORARITMETICO'
    elif isEnd(palavra):
        print palavra + ' FIM'


temp = []
inicio = True
breakOnSymbols = False
comment = False
string = False

i = 0

texto = sys.argv[1]

f = open(texto, "r")
contents = f.read()

while i < len(contents):
    letter = contents[i]


    #pega o proximo caracter
    if i + 1 != len(contents):
        nextLetter = contents[i+1]

    #confere comentarios
    if isCommentStart(letter, nextLetter):
        comment = True
    elif isCommentEnd(letter, nextLetter):
        i = i + 1
        comment = False

    #Checamos as strings aqui, inicio da string
    elif inicio == True and isApostropheorQuotes(letter):
        temp.append(letter)
        string = True
        inicio = False
    #Meio da string
    elif inicio == False and string == True:
        temp.append(letter)
        #Fim da string
        if isApostropheorQuotes(letter):
            palavra = ''.join(temp)
            print palavra + ' STRING'
            temp = []
            string = False
            inicio = True

    elif comment == False and string == False:
        #Check if is double term, like >= <=
        if inicio == True and findDouble(letter, nextLetter):
            temp.append(letter)
            temp.append(nextLetter)

            palavra = ''.join(temp)
            classifyTerm(palavra)
            temp = []
            i = i + 1

        #Checamos se sao letras ou numeros, como var1 4.1323 4
        elif inicio == True and (isLetter(letter) or isNumber(letter)):
            inicio = False
            breakOnSymbols = True

        #Analisa simbolos como ) ( ;
        elif inicio == True and isOtherSymbol(letter):
            temp.append(letter)

            palavra = ''.join(temp)
            classifyTerm(palavra)

            temp = []

        ##Analisa palavras com numeros --> var, var1, else
        if inicio == False and breakOnSymbols == True:

            if isLetter(letter) or isNumber(letter) or isPoint(letter):
                if len(temp) == 0:
                    temp.append(letter)
                elif len(temp) > 0 and isNumber(temp[0]) and isPoint(letter):
                    temp.append(letter)
                elif len(temp) > 0 and isLetter(temp[0]) and not isPoint(letter):

                    temp.append(letter)
                elif len(temp) > 0 and isNumber(letter) or isLetter(letter):

                    temp.append(letter)
                else:
                    palavra = ''.join(temp)
                    classifyTerm(palavra)
                    temp = []
                    inicio = True
                    breakOnSymbols = False
                    i = i - 1

            else:
                palavra = ''.join(temp)
                classifyTerm(palavra)

                temp = []
                inicio = True
                breakOnSymbols = False
                i = i - 1

        # else:
        #     if len(temp) > 0:
        #         print temp
        #     temp = []
        #     inicio = True
        #     breakOnSymbols = False

    i = i + 1

#
# for letter in textoTeste:
#     #print str(ord(letter)) + ' ' + letter
#     if isOpenParenthesis(letter):
#         print ''.join(temp)
#         temp = []
#         inicio = True
#         breakOnSymbols = False
#
#     if inicio == True and (isLetter(letter) or isNumber(letter)):
#         inicio = False
#         breakOnSymbols = True
#     elif inicio == True and isOpenParenthesis(letter):
#         temp.append(letter)
#         print ''.join(temp)
#         temp = []
#
#     ##Analisa palavras com numeros --> var, var1, else
#     if inicio == False and breakOnSymbols == True:
#         if isLetter(letter) or isNumber(letter) or isPoint(letter):
#             temp.append(letter)
#         else:
#             print ''.join(temp)
#             temp = []
#             inicio = True
#             breakOnSymbols = False
#
#     else:
#         print temp
#         temp = []
#         inicio = True
#         breakOnSymbols = False



# elif inicio == True and isRelationalOperator(letter):
#     temp.append(letter)
#
#
#     palavra = ''.join(temp)
#     if isSpecialSymbol(palavra):
#         print palavra + ' SIMBOLOESPECIAL'
#     elif isLogicalOperator(palavra):
#         print palavra + ' OPERADORLOGICO'
#     elif isRelationalOperator(palavra):
#         print palavra + ' OPERADORRELACIONAL'
#     elif isArithmeticalOperator(palavra):
#         print palavra + ' OPERADORARITMETICO'
#
#     temp = []













#fim
