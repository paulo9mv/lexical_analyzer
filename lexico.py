import sys

texto = sys.argv[1]

f = open(texto, "r")
contents = f.read()

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

textoTeste = 'program and or not = >= <= > < <> + - * mod , : ; . ) ( := 900 2.3 2.2 with nit of packed teste;\nvar x,y: and integer;\nconst banana := 2;\nbanana = 1 + * - / 2;\nconst pi := 3.1416;\n/* inicio do programa  12312 31232131 */\nbegin\nread(x);\n\
if (x >= y) then\ny := x ;\nelse\ny := -x;\nwriteln(x);\nwrite(y);\nend.'

def isLetter(letter):
    return ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122

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
        print term + ' PALAVRARESERVADA'

def isIdentifier(term):
    if term.upper() not in reservedWords and isLetter(term[0]) and term.lower() not in logicalOperators and term.lower() not in arithmeticalOperators:
        print term + ' IDENTIFICADOR'

def isIntegerNumber(term):
    if isNumber(term[0]):
        if float(term) % 1 == 0:
            print term + ' NUMEROINTEIRO'

def isRealNumber(term):
    if isNumber(term[0]):
        if float(term) % 1 != 0:
            print term + ' NUMEROREAL'

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



temp = []
inicio = True
breakOnSymbols = False
breakOnLetters = False
comment = False
string = False

i = 0

while i < len(contents):
    letter = contents[i]


    if i + 1 != len(contents):
        nextLetter = contents[i+1]

    if isCommentStart(letter, nextLetter):
        comment = True
    elif isCommentEnd(letter, nextLetter):
        i = i + 1
        comment = False
    elif inicio == True and isApostropheorQuotes(letter):
        temp.append(letter)
        string = True
        inicio = False
    elif inicio == False and string == True:
        temp.append(letter)
        if isApostropheorQuotes(letter) and nextLetter == ')':
            palavra = ''.join(temp)
            print palavra + ' STRING'
            temp = []
            string = False
            inicio = True

    elif comment == False and string == False:
        if inicio == True and isParenthesis(letter):
            temp.append(letter)
            #print ''.join(temp)
            palavra = ''.join(temp)
            if isSpecialSymbol(palavra):
                print palavra + ' SIMBOLOESPECIAL'
            temp = []

        elif inicio == True and findDouble(letter, nextLetter):
            temp.append(letter)
            temp.append(nextLetter)
            #print ''.join(temp)
            palavra = ''.join(temp)
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
            temp = []
        elif inicio == True and (isLetter(letter) or isNumber(letter)):

            inicio = False
            breakOnSymbols = True
        elif inicio == True and isDotComma(letter):
            temp.append(letter)

            palavra = ''.join(temp)
            if isSpecialSymbol(palavra):
                print palavra + ' SIMBOLOESPECIAL'
            elif isLogicalOperator(palavra):
                print palavra + ' OPERADORLOGICO'
            elif isRelationalOperator(palavra):
                print palavra + ' OPERADORRELACIONAL'
            elif isArithmeticalOperator(palavra):
                print palavra + ' OPERADORARITMETICO'


            temp = []



        elif inicio == True and isComma(letter):
            temp.append(letter)


            palavra = ''.join(temp)
            if isSpecialSymbol(palavra):
                print palavra + ' SIMBOLOESPECIAL'
            elif isLogicalOperator(palavra):
                print palavra + ' OPERADORLOGICO'
            elif isRelationalOperator(palavra):
                print palavra + ' OPERADORRELACIONAL'
            elif isArithmeticalOperator(palavra):
                print palavra + ' OPERADORARITMETICO'

            temp = []
        elif inicio == True and isTwoPoints(letter):
            temp.append(letter)


            palavra = ''.join(temp)
            if isSpecialSymbol(palavra):
                print palavra + ' SIMBOLOESPECIAL'
            elif isLogicalOperator(palavra):
                print palavra + ' OPERADORLOGICO'
            elif isRelationalOperator(palavra):
                print palavra + ' OPERADORRELACIONAL'
            elif isArithmeticalOperator(palavra):
                print palavra + ' OPERADORARITMETICO'

            temp = []
        elif inicio == True and isArithmeticalOperator(letter):
            temp.append(letter)


            palavra = ''.join(temp)
            if isSpecialSymbol(palavra):
                print palavra + ' SIMBOLOESPECIAL'
            elif isLogicalOperator(palavra):
                print palavra + ' OPERADORLOGICO'
            elif isRelationalOperator(palavra):
                print palavra + ' OPERADORRELACIONAL'
            elif isArithmeticalOperator(palavra):
                print palavra + ' OPERADORARITMETICO'

            temp = []
        elif inicio == True and isEnd(letter):
            temp.append(letter)


            palavra = ''.join(temp)
            if isSpecialSymbol(palavra):
                print palavra + ' SIMBOLOESPECIAL'
            elif isLogicalOperator(palavra):
                print palavra + ' OPERADORLOGICO'
            elif isRelationalOperator(palavra):
                print palavra + ' OPERADORRELACIONAL'
            elif isArithmeticalOperator(palavra):
                print palavra + ' OPERADORARITMETICO'
            elif isEnd(palavra):
                print palavra + ' FINAL'

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
                    isWordReserved(palavra)
                    isIdentifier(palavra)
                    isRealNumber(palavra)
                    isIntegerNumber(palavra)
                    if isLogicalOperator(palavra):
                        print palavra + ' OPERADORLOGICO'
                    if isArithmeticalOperator(palavra):
                        print palavra + ' OPERADORARITMETICO'
                    temp = []
                    inicio = True
                    breakOnSymbols = False
                    i = i - 1
            else:
                palavra = ''.join(temp)
                isWordReserved(palavra)
                isIdentifier(palavra)
                isRealNumber(palavra)
                isIntegerNumber(palavra)
                if isLogicalOperator(palavra):
                    print palavra + ' OPERADORLOGICO'
                if isArithmeticalOperator(palavra):
                    print palavra + ' OPERADORARITMETICO'
                temp = []
                inicio = True
                breakOnSymbols = False
                i = i - 1

        else:
            if len(temp) > 0:
                print temp
            temp = []
            inicio = True
            breakOnSymbols = False
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













#fim
