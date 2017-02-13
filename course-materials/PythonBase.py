import sys

#for the lexer
lexemes = []

unvariedLexemes = ["var", "function", "(", "(", "+"];

def SplitSourceByWhitespace(source):
    allSplits = []
    for line in source:
        thisSplit = line.split()
        #for line.split():
        allSplits += thisSplit
    #print(allSplits)
    return allSplits


def SplitByUnvariedLexemes(source):
    i=0
    allSplits = []
    while i< len(source):
        line = source[i]
        unvariedLexemeFound = False;
        for lexeme in unvariedLexemes:

            if(-1 != line.find(lexeme)):
                unvariedLexemeFound = True;
                split = line.split(lexeme)
                allSplits += split
            if not unvariedLexemeFound:
                allSplits += line
        i += 1
    print(allSplits)
    return allSplits


def ReadInput():
    lines = sys.stdin.readlines()
    for line in lines:
        print("echo: "+line)



if __name__ == '__main__':
    print ("starting __main__")
    SplitByUnvariedLexemes(SplitSourceByWhitespace(sys.stdin.readlines()))
