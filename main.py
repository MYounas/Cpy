
from lexical import Lexical
from Token import Token


import re


class Main():

    _tokens=[];_tokensIndex=0

    _temp = "";_lineNum = 1;_codeFile="code.txt";_outputFile="output.txt";_fileData=""

    _breakers = ['(', ')', '[', ']', '{', '}', '=', ',', ' ', '\n', '\r'
        , '<', '>', '-', '+', '*', '/', '%', ':', ';', '.', '!', '&', '|', '#' , '"' , '\'' , '\t']

    _invalidPrint = ['=', ' ', '\n', '\r', '<', '>', '-', '+', '*', '/', '%', '!', '&', '|', '#' , '"' , '\'' , '\t']


    def __init__(self):
        Main._fileData=""
        Main._lineNum=1
        Main._tokens=[]
        Main._tokensIndex=0

    def DECL_ASGN(self):
        if Main._tokens[Main._tokensIndex].CP=="ID":
            Main._tokensIndex+=1
            if self.LIST():
                return True

        return False

    def LIST(self):
        if self.INIT():
            Main._tokensIndex += 1
            if self.LIST2():
                return True

        return False


    def INIT(self):
        # if Main._tokens[Main._tokensIndex].CP in ['=',',','$']:
        if Main._tokens[Main._tokensIndex].CP == "=":
            Main._tokensIndex += 1
            if self.INIT2():
                return True
            # else:
            #     Main._tokensIndex -= 1
            #     return True

        else:
            Main._tokensIndex -= 1
            return True


    def LIST2(self):
        # if Main._tokens[Main._tokensIndex].CP  in [',','$']:
        if Main._tokens[Main._tokensIndex].CP==',':
            Main._tokensIndex += 1
            if self.DECL_ASGN():
                return True
            # else:
            #     Main._tokensIndex -= 1
            #     return True

        else:
            Main._tokensIndex -= 1
            return True



    def INIT2(self):
        if self.E():
            Main._tokensIndex += 1
            if self.INIT3():
                return True

        return False

    def INIT3(self):
        if Main._tokens[Main._tokensIndex].CP =='=':
            if self.INIT():
                return True

        else:
            Main._tokensIndex -= 1
            return True


    def E(self):
        if self.F():
            Main._tokensIndex += 1
            if self.E1():
                return True

        return False

    def E1(self):
        # if Main._tokens[Main._tokensIndex].CP in ['LO',')']:
        if Main._tokens[Main._tokensIndex].VP == '||':
            Main._tokensIndex += 1
            if self.F():
                Main._tokensIndex += 1
                if self.E1():
                    return True

        else:
            Main._tokensIndex -= 1
            return True

        # return False

    def F(self):
        if self.G():
            Main._tokensIndex += 1
            if self.F1():
                return True

        return False


    def F1(self):
        # if Main._tokens[Main._tokensIndex].CP in ['LO', ')']:
        if Main._tokens[Main._tokensIndex].VP == '&&':
            Main._tokensIndex += 1
            if self.G():
                Main._tokensIndex += 1
                if self.F1():
                    return True

        else:
            Main._tokensIndex -= 1
            return True


    def G(self):
        if self.H():
            Main._tokensIndex += 1
            if self.G1():
                return True

        return False

    def G1(self):
        # if Main._tokens[Main._tokensIndex].CP in ['RO','LO', ')']:
        if Main._tokens[Main._tokensIndex].CP=='RO':
            Main._tokensIndex += 1
            if self.H():
                Main._tokensIndex += 1
                if self.G1():
                    return True

        else:
            Main._tokensIndex -= 1
            return True


    def H(self):
        if self.I():
            Main._tokensIndex += 1
            if self.H1():
                return True

        return False


    def H1(self):
        # if Main._tokens[Main._tokensIndex].CP in ['ADD_SUB','RO', 'LO', ')']:
        if Main._tokens[Main._tokensIndex].CP=='ADD_SUB':
            Main._tokensIndex += 1
            if self.I():
                Main._tokensIndex += 1
                if self.H1():
                    return True

        else:
            Main._tokensIndex -= 1
            return True


    def I(self):
        if self.J():
            Main._tokensIndex += 1
            if self.I1():
                return True

        return False

    def I1(self):
        # if Main._tokens[Main._tokensIndex].CP in ['DIV_MUL','ADD_SUB', 'RO', 'LO', ')']:
        if Main._tokens[Main._tokensIndex].CP == 'DIV_MUL':
            Main._tokensIndex += 1
            if self.J():
                Main._tokensIndex += 1
                if self.I1():
                    return True

        else:
            Main._tokensIndex -= 1
            return True


    def J(self):
        if Main._tokens[Main._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST']:
            if Main._tokens[Main._tokensIndex].CP=="ID":
                Main._tokensIndex += 1
                if self.J2():
                    return True
            elif Main._tokens[Main._tokensIndex].CP=="(":
                Main._tokensIndex += 1
                if self.E():
                    Main._tokensIndex += 1
                    if Main._tokens[Main._tokensIndex].CP==")":
                        return True
            elif Main._tokens[Main._tokensIndex].VP=="!":
                Main._tokensIndex += 1
                if self.J1():
                    return True
            elif self.FUNC_CALL():
                return True
            elif Main._tokens[Main._tokensIndex].CP=="INC_DEC":
                Main._tokensIndex += 1
                if Main._tokens[Main._tokensIndex].CP=="ID":
                    return True
            elif self.CONSTANT():
                return True

        return False


    def J1(self):
        if self.J():
            return True

        else:
            Main._tokensIndex -= 1
            return True


    def J2(self):
        # if Main._tokens[Main._tokensIndex].CP in ['INC_DEC', 'DIV_MUL', 'ADD_SUB', 'RO', 'LO', ')']:
        if Main._tokens[Main._tokensIndex].CP=='INC_DEC':
            return True
        else:
            Main._tokensIndex -= 1
            return True


    def CONSTANT(self):
        if Main._tokens[Main._tokensIndex].CP in ['INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST']:
            return True

        return False

    def FUNC_CALL(self):
        # if Main._tokens[Main._tokensIndex].CP in ['self','ID']:
        if Main._tokens[Main._tokensIndex].CP == "self":
            Main._tokensIndex += 1
            if Main._tokens[Main._tokensIndex].CP == ".":
                Main._tokensIndex += 1
                if Main._tokens[Main._tokensIndex].CP == "ID":
                    Main._tokensIndex += 1
                    if Main._tokens[Main._tokensIndex].CP == "(":
                        Main._tokensIndex += 1
                        if self.PARAMS():
                            Main._tokensIndex += 1
                            if Main._tokens[Main._tokensIndex].CP == ")":
                                return True

        elif Main._tokens[Main._tokensIndex].CP == "ID":
            Main._tokensIndex += 1
            if self.FUNC_CALL1():
                return True

        return False


    def FUNC_CALL1(self):
        # if Main._tokens[Main._tokensIndex].CP in ['.', '(']:
        if Main._tokens[Main._tokensIndex].CP==".":
            Main._tokensIndex += 1
            if Main._tokens[Main._tokensIndex].CP == "ID":
                Main._tokensIndex += 1
                if Main._tokens[Main._tokensIndex].CP == "(":
                    Main._tokensIndex += 1
                    if self.PARAMS():
                        Main._tokensIndex += 1
                        if Main._tokens[Main._tokensIndex].CP == ")":
                            return True

        elif Main._tokens[Main._tokensIndex].CP == "(":
            Main._tokensIndex += 1
            if self.FUNC_CALL2():
                return True

        return False


    def FUNC_CALL2(self):
        # if Main._tokens[Main._tokensIndex].CP in [')', 'ID']:
        if Main._tokens[Main._tokensIndex].CP == ")":
            Main._tokensIndex += 1
            if self.FUNC_CALL3():
                return True
        elif self.DECL_ASGN():
            return True

        return False


    def FUNC_CALL3(self):
        # if Main._tokens[Main._tokensIndex].CP in ['.', '$']:
        if Main._tokens[Main._tokensIndex].CP=='.':
            Main._tokensIndex += 1
            if Main._tokens[Main._tokensIndex].CP=='ID':
                Main._tokensIndex += 1
                if Main._tokens[Main._tokensIndex].CP == '(':
                    Main._tokensIndex += 1
                    if self.PARAMS():
                        Main._tokensIndex += 1
                        if Main._tokens[Main._tokensIndex].CP == ')':
                            return True

        else:
            Main._tokensIndex -= 1
            return True


    def PARAMS(self):
        # if Main._tokens[Main._tokensIndex].CP=="ID":
        if self.DECL_ASGN():
            return True
        else:
            Main._tokensIndex -= 1
            return True


    def IF_ELSE(self):
        if Main._tokens[Main._tokensIndex].CP=="if":
            Main._tokensIndex += 1
            if Main._tokens[Main._tokensIndex].CP == "(":
                Main._tokensIndex += 1
                if self.E():
                    Main._tokensIndex += 1
                    if Main._tokens[Main._tokensIndex].CP == ")":
                        if Main._tokens[Main._tokensIndex].CP == ":":
                            Main._tokensIndex += 1
                            if self.BODY2():
                                Main._tokensIndex += 1
                                if self.ELIF():
                                    Main._tokensIndex += 1
                                    if self.O_ELSE():
                                        return True

        return False


    def ELIF(self):
        if Main._tokens[Main._tokensIndex].CP == "elif":
            Main._tokensIndex += 1
            if self.E():
                Main._tokensIndex += 1
                if Main._tokens[Main._tokensIndex].CP == ")":
                    Main._tokensIndex += 1
                    if Main._tokens[Main._tokensIndex].CP == ":":
                        Main._tokensIndex += 1
                        if self.BODY2():
                            return True

        return True


    def O_ELSE(self):
        if Main._tokens[Main._tokensIndex].CP == "else":
            Main._tokensIndex += 1
            if Main._tokens[Main._tokensIndex].CP == ":":
                Main._tokensIndex += 1
                if self.BODY2():
                    return True

        return True


    def BODY2(self):
        if self.S_ST2():
            return True
        elif Main._tokens[Main._tokensIndex].CP == "{":
            Main._tokensIndex += 1
            if self.M_ST2():
                Main._tokensIndex += 1
                if Main._tokens[Main._tokensIndex].CP == "}":
                    return True

        return False


    def M_ST2(self):
        if self.S_ST2():
            Main._tokensIndex += 1
            if self.M_ST2():
                return True

        return True



    def mainMethod(self,f):
        lex = Lexical()

        self.flagStr=0;self.flagChar=0;self.flagFloat=0

        while True:
            ch = str(f.read(1), 'utf-8')

            if not ch: break

            # working for separation of float and ID

            if ch == '.':
                if self.flagFloat:
                    if lex.chk_FLT_CONST(Main._temp, Main._lineNum):
                        self.printToken("FLT_CONST", Main._temp, Main._lineNum)
                        Main._tokens.append(Token("FLT_CONST", Main._temp, Main._lineNum))
                        f.seek(-1,1)
                        Main._temp = ""
                        self.flagFloat=0
                        continue
                elif Main._temp=="":
                    OneRight = str(f.read(1), 'utf-8')
                    if re.match("[0-9]",OneRight):
                        self.flagFloat=1
                        Main._temp+=ch+OneRight
                        continue
                    else:
                        f.seek(-1,1)
                elif Main._temp!="":
                    f.seek(-2, 1)
                    OneLeft = str(f.read(1), 'utf-8')
                    f.seek(1, 1)
                    OneRight = str(f.read(1), 'utf-8')
                    if (re.match("[0-9]", OneLeft) or OneLeft in ['+', '-']) and re.match("[0-9]", OneRight):
                        self.flagFloat=1
                        Main._temp += ch+OneRight
                        continue
                    else:
                        f.seek(-1,1)

            elif ch == '+' or ch == '-':
                f.seek(-2, 1)
                OneLeft = str(f.read(1), 'utf-8')
                f.seek(1, 1)
                OneRight = str(f.read(1), 'utf-8')
                TwoRight = str(f.read(1), 'utf-8')
                f.seek(-2, 1)
                if (not re.match("[0-9A-Za-z]", OneLeft)) and (re.match("[0-9]", OneRight) or re.match("[0-9]", TwoRight)):
                    Main._temp += ch
                    continue

            if ch in Main._breakers:

                if ch =='"' and self.flagStr==1:
                    Main._temp+=ch


                if lex.chk_FLT_CONST(Main._temp, Main._lineNum):
                    self.printToken("FLT_CONST", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("FLT_CONST", Main._temp, Main._lineNum))
                    self.flagFloat=0
                    Main._temp = ""

                if lex.chk_keywords(Main._temp, Main._lineNum):
                    self.printToken(Main._temp,"-", Main._lineNum)
                    Main._tokens.append(Token(Main._temp,"-", Main._lineNum))
                    Main._temp = ""

                elif lex.chk_ID(Main._temp, Main._lineNum):
                    self.printToken("ID", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("ID", Main._temp, Main._lineNum))
                    Main._temp = ""

                elif lex.chk_INT_CONST(Main._temp, Main._lineNum):
                    self.printToken("INT_CONST", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("INT_CONST", Main._temp, Main._lineNum))
                    Main._temp = ""

                elif lex.chk_STR_CONST(Main._temp, Main._lineNum):
                    self.flagStr=0
                    ch=''
                    self.printToken("STR_CONST", Main._temp[1:-1], Main._lineNum)
                    Main._tokens.append(Token("STR_CONST", Main._temp[1:-1], Main._lineNum))
                    Main._temp = ""

                elif Main._temp != "":
                    Main._temp = "Error at " + str(Main._lineNum) + " where value is " + Main._temp
                    Main._fileData += Main._temp + "\n"
                    Main._temp = ""

                if ch not in Main._invalidPrint and ch!='':
                    self.printToken(str(ch), '-', Main._lineNum)
                    Main._tokens.append(Token(str(ch), '-', Main._lineNum))
                if ch == '\n':
                    Main._lineNum += 1


            else:
                Main._temp += str(ch)

            if ch == '"':
                Main._temp+=ch
                while True:
                    ch = str(f.read(1), 'utf-8')
                    if ch =='\\':
                        OneRight = str(f.read(1), 'utf-8')
                        if OneRight=='"' or OneRight=='\\':
                            Main._temp += OneRight
                        else:
                            f.seek(-1, 1)
                            Main._temp += ch
                    elif ch not in ['"','\n']:
                        Main._temp+=ch
                    elif ch == '"':
                        f.seek(-1,1)
                        self.flagStr = 1
                        break
                    elif ch == '\n':
                        f.seek(-1, 1)
                        break

            if ch == '\'':
                Main._temp+=ch
                char1 = str(f.read(1), 'utf-8')
                char2 = str(f.read(1), 'utf-8')

                if char1=='\\':
                    char3 = str(f.read(1), 'utf-8')
                    if char2=='\'':
                        Main._temp += char2 + char3
                    elif char3!='\n':
                        Main._temp += char1 + char2 + char3
                    else:
                        Main._temp += char1
                    if char3=='\n':
                        Main._lineNum+=1
                elif char2!='\n':
                    Main._temp += char1 + char2
                elif char2 == '\n':
                    Main._lineNum += 1


                if lex.chk_CHAR_CONST(Main._temp, Main._lineNum):
                    self.printToken("CHAR_CONST", Main._temp[1:-1], Main._lineNum)
                    Main._tokens.append(Token("CHAR_CONST", Main._temp[1:-1], Main._lineNum))
                    Main._temp = ""
                else:
                    Main._temp = "Error at " + str(Main._lineNum) + " where value is " + Main._temp
                    Main._fileData += Main._temp + "\n"
                    Main._temp = ""


            if ch =='#':
                OneRight = str(f.read(1), 'utf-8')
                if OneRight == '*':
                    while True:
                        first = str(f.read(1), 'utf-8')
                        if not first:
                            break
                        if first == '*':
                            second = str(f.read(1), 'utf-8')
                            if second == '#':
                                break
                        elif first == '\n':
                            Main._lineNum+=1
                else:
                    f.readline()
                    Main._lineNum+=1

                continue



            # check for inc_DEc and add_sub and asgn
            if ch in ['+', '-', '*', '/', '%']:
                OneRight = str(f.read(1), 'utf-8')
                if ch == OneRight:
                    Main._temp = ch + ch
                    self.printToken("INC_DEC", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("INC_DEC", Main._temp, Main._lineNum))
                    Main._temp = ""
                elif OneRight == '=':
                    Main._temp = ch + OneRight
                    self.printToken("ASGN_OPT", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("ASGN_OPT", Main._temp, Main._lineNum))
                    Main._temp = ""
                elif ch in ['+', '-']:
                    f.seek(-1, 1)
                    self.printToken("ADD_SUB", str(ch), Main._lineNum)
                    Main._tokens.append(Token("ADD_SUB", str(ch), Main._lineNum))
                elif ch in ['*','/', '%']:
                    f.seek(-1, 1)
                    self.printToken("DIV_MUL", str(ch), Main._lineNum)
                    Main._tokens.append(Token("DIV_MUL", str(ch), Main._lineNum))
                # elif ch == '*':
                #     f.seek(-1, 1)
                #     self.printToken("MUL", str(ch), Main._lineNum)
                #     Main._tokens.append(Token("MUL", str(ch), Main._lineNum))
                # elif ch in ['/', '%']:
                #     f.seek(-1, 1)
                #     self.printToken("DIV_REM", str(ch), Main._lineNum)
                #     Main._tokens.append(Token("DIV_REM", str(ch), Main._lineNum))
                else:
                    f.seek(-1, 1)

            # check for RO
            if ch in ['<', '>', '=', '!']:
                OneRight = str(f.read(1), 'utf-8')
                if OneRight == '=':
                    Main._temp = ch + OneRight
                    self.printToken("RO", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("RO", Main._temp, Main._lineNum))
                    Main._temp = ""
                elif ch == '=':
                    f.seek(-1, 1)
                    self.printToken('=', '-', Main._lineNum)
                    Main._tokens.append(Token('=', '-', Main._lineNum))
                elif ch != '!':
                    f.seek(-1, 1)
                    self.printToken("RO", str(ch), Main._lineNum)
                    Main._tokens.append(Token("RO", str(ch), Main._lineNum))
                elif ch == '!':
                    f.seek(-1, 1)
                    self.printToken("LO", str(ch), Main._lineNum)
                    Main._tokens.append(Token("LO", str(ch), Main._lineNum))
                    # self.printToken("LO", str(ch), Main._lineNum)

            # check for LO
            if ch in ['&', '|']:
                OneRight = str(f.read(1), 'utf-8')
                if ch == OneRight:
                    Main._temp = ch + OneRight
                    self.printToken("LO", Main._temp, Main._lineNum)
                    Main._tokens.append(Token("LO", Main._temp, Main._lineNum))
                    Main._temp = ""
                elif ch != OneRight:
                    temp = "Error at " + str(Main._lineNum) + " where value is " + str(ch)
                    Main._fileData += temp + "\n"
                    f.seek(-1, 1)
                    Main._temp = ""

        self.printToken("$", "-", Main._lineNum)
        Main._tokens.append(Token("$", "-", Main._lineNum))

    def printToken(self,CPart, VPart, line):
        string = "( " + CPart + " , " + VPart + " , " + str(line) + " )"
        print(string)
        Main._fileData += string + "\n"

