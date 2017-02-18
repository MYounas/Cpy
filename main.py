
from lexical import Lexical

import re


def main():

    temp="";lineNum=1

    f = open('test.txt', 'rb+')

    breakers=[ '(' , ')' , '[' , ']' , '{' , '}' , '=' , ',' , ' ' , '\n' , '\r'
            , '<' , '>' , '-' , '+' , '*' , '/' , '%' , ':' , ';' , '.' ]

    invalidPrint=[ '=' , ' ' , '\n' , '\r' , '<' , '>' , '-' , '+' , '*' , '/' , '%']

    lex=Lexical()

    while True:
        ch = f.read(1)

        ch=str(ch,'utf-8')

        # print("current position", f.tell())

        if not ch: break

        #working for separation of float and ID
        if ch == '.':
            f.seek(-2, 1)
            OneLeft = str(f.read(1),'utf-8')
            f.seek(1, 1)
            OneRight = str(f.read(1),'utf-8')
            if (re.match("[0-9]", OneLeft) or OneLeft in ['+','-'] ) and re.match("[0-9]", OneRight):
                f.seek(-1, 1)
                temp += ch
                continue
            else:
                f.seek(-2, 1)
                ch = f.read(1)
                ch = str(ch, 'utf-8')

        elif ch == '+' or ch == '-':
            OneRight = str(f.read(1),'utf-8')
            f.seek(-1, 1)
            if re.match("[0-9]", OneRight) or OneRight=='.':
                temp += ch
                continue


        if ch in breakers:

            if lex.chk_FLT_CONST(temp, lineNum):
                printToken("FLT_CONST", temp, lineNum)
                temp = ""

            if lex.chk_keywords(temp, lineNum):
                printToken("Keyword", temp, lineNum)
                temp = ""

            elif lex.chk_ID(temp,lineNum):
                printToken("ID",temp,lineNum)
                temp = ""

            elif lex.chk_INT_CONST(temp,lineNum):
                printToken("INT_CONST",temp,lineNum)
                temp = ""

            elif lex.chk_STR_CONST(temp,lineNum):
                printToken("STR_CONST",temp,lineNum)
                temp = ""

            elif lex.chk_CHAR_CONST(temp,lineNum):
                printToken("CHAR_CONST",temp,lineNum)
                temp = ""

            # elif lex.chk_falto():
            #     temp = ""

            if ch not in invalidPrint:
                printToken(str(ch), '-', lineNum)
                print(ch+" at "+str(lineNum))
            if ch=='\n':
                lineNum+=1

            else:
                print("Error at "+str(lineNum) + " where value is "+temp)
                temp=""


        else:
            temp+=str(ch)


        #check for inc_DEc and add_sub and asgn
        if ch in ['+','-','*','/','%']:
            OneRight = str(f.read(1),'utf-8')
            if  ch==OneRight:
                temp=ch+ch
                printToken("INC_DEC",temp,lineNum)
                temp=""
                # continue
            elif OneRight == '=':
                temp=ch+OneRight
                printToken("ASGN_OPT",temp,lineNum)
                temp=""
            elif ch in ['+','-']:
                f.seek(-1,1)
                printToken("ADD_SUB", str(ch), lineNum)
            elif ch == '*':
                f.seek(-1,1)
                printToken("MUL", str(ch), lineNum)
            elif ch in ['/','%']:
                f.seek(-1,1)
                printToken("DIV_REM", str(ch), lineNum)

        # check for RO
        if ch in ['<', '>', '=', '!']:
            OneRight = str(f.read(1), 'utf-8')
            if OneRight == '=':
                temp = ch + OneRight
                printToken("RO", temp, lineNum)
                temp = ""
            else:
                f.seek(-1,1)
                printToken("RO", str(ch), lineNum)


    f.close()


fileData=""

def printToken(CPart,VPart,line):
    global fileData
    string="( "+CPart+" , "+VPart+" , "+str(line)+" )"
    print(string)
    fileData+=string+"\n"


if __name__=="__main__":main()

fout=open("output.txt",'w')
fout.write(fileData)
fout.close()


