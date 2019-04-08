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
breakOnSymbols = False;

for letter in textoTeste:
    #print str(ord(letter)) + ' ' + letter

    if inicio == True and isLetter(letter):
        inicio = False
        breakOnSymbols = True

    if inicio == False and breakOnSymbols == True:
        if isLetter(letter):
            temp.append(letter)
        else:
            print ''.join(temp)
            temp = []
            inicio = True
            breakOnSymbols = False
    else:
        print temp
        temp = []
        inicio = True
        breakOnSymbols = False













#fim
