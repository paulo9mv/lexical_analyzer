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
specialSymbols = [',', ':', ';', '.']
assignmentSymbol = [':=']


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

def findAssingment(letter, nextLetter):
    return letter == ':' and nextLetter == '='

def isWordReserved(term):
    print 'oi'

def isIdentifier(term):
    print 'oi'

def isIntegerNumber(term):
    print 'oi'

def isRealNumber(term):
    print 'oi'

def isArithmeticalOperator(term):
    print 'oi'

def isRelationalOperator(term):
    print 'oi'

def isLogicalOperator(term):
    print 'oi'

def isSpecialSymbol(term):
    print 'oi'

def isAssignment(term):
    print 'oi'

def isEnd(term):
    print 'oi'



print len(reservedWords)

textoTeste = 'program teste;\nvar x,y: integer;\nconst pi := 3.1416;\n/* inicio do programa */\nbegin\nread(x);\n\
if (x > y) then\ny := x ;\nelse\ny := -x;\nwriteln(x);\nwrite(y);\nend.'

temp = []
inicio = True
breakOnSymbols = False
breakOnLetters = False
comment = False

i = 0

while i < len(textoTeste):
    letter = textoTeste[i]
    #print letter
    if i + 1 != len(textoTeste):
        nextLetter = textoTeste[i+1]

    if isCommentStart(letter, nextLetter):
        comment = True
    elif isCommentEnd(letter, nextLetter):
        comment = False
    elif comment == False:
        if inicio == True and isParenthesis(letter):
            temp.append(letter)
            print ''.join(temp)
            temp = []
        elif inicio == True and findAssingment(letter, nextLetter):
            temp.append(letter)
            temp.append(nextLetter)
            print ''.join(temp)
            temp = []
        elif inicio == True and (isLetter(letter) or isNumber(letter)):
            inicio = False
            breakOnSymbols = True
        elif inicio == True and isDotComma(letter):
            temp.append(letter)
            print ''.join(temp)
            temp = []
        elif inicio == True and isComma(letter):
            temp.append(letter)
            print ''.join(temp)
            temp = []


        ##Analisa palavras com numeros --> var, var1, else
        if inicio == False and breakOnSymbols == True:
            if isLetter(letter) or isNumber(letter) or isPoint(letter):
                temp.append(letter)
            else:
                print ''.join(temp)
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
