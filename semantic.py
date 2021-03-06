
import sys
from stack import Stack

from miscl import (
    matFunctions,
    matClassesContainer,
    matClasses
)

class Semantic:

    _tokens = [];_tokensIndex=0;_link=0

    def __init__(self,tokens):
        Semantic._tokens=tokens
        Semantic._tokensIndex = 0
        self.tblFunctions=[]
        self.classesContainer = []
        self.tblClasses=[]
        self.tblInherit=[]



    def PROG(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "class":
            if self.CLASS():
                return True
        if Semantic._tokens[Semantic._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.M_ST():
                return True

    #region Class

    def CLASS(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "class":
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == "ID":
                Semantic._tokensIndex += 1
                if self.CLASS1():
                    return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def CLASS1(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='(':
            Semantic._tokensIndex += 1
            if self.PARENT():
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP==')':
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == ':':
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == '{':
                            Semantic._tokensIndex += 1
                            if self.M_ST():
                                Semantic._tokensIndex += 1
                                if Semantic._tokens[Semantic._tokensIndex].CP == '}':
                                    return True
                                else:
                                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def PARENT(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == 'ID':
            Semantic._tokensIndex += 1
            if self.PARENT():
                return True
        elif Semantic._tokens[Semantic._tokensIndex].CP == ',':
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == 'ID':
                Semantic._tokensIndex += 1
                if self.PARENT():
                    return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            Semantic._tokensIndex -= 1
            return True

    #endregion

    #region FUNC DEF

    def FUNC_DEF(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == 'def':
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == 'ID':
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == '(':
                    Semantic._tokensIndex += 1
                    if self.ARGS():
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == ')':
                            Semantic._tokensIndex += 1
                            if Semantic._tokens[Semantic._tokensIndex].CP == ':':
                                Semantic._tokensIndex += 1
                                if Semantic._tokens[Semantic._tokensIndex].CP == '{':
                                    Semantic._tokensIndex += 1
                                    if self.M_ST():
                                        Semantic._tokensIndex += 1
                                        if self.RET():
                                            Semantic._tokensIndex += 1
                                            if Semantic._tokens[Semantic._tokensIndex].CP == '}':
                                                return True
                                            else:
                                                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                                else:
                                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                            else:
                                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    def ARGS(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['self', 'ID']:
            if self.SELF():
                Semantic._tokensIndex += 1
                if self.DECL_ASGN():
                    return True
        else:
            Semantic._tokensIndex -= 1
            return True

    def SELF(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='self':
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == ',':
                return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            Semantic._tokensIndex -= 1
            return True

    def RET(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='return':
            Semantic._tokensIndex += 1
            if self.E():
                return True
        else:
            Semantic._tokensIndex -= 1
            return True

    #endregion

    #region Statements

    def M_ST(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.S_ST():
                Semantic._tokensIndex += 1
                if self.M_ST():
                    return True

        else:
            Semantic._tokensIndex -= 1
            return True

    def S_ST(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['ID','self', 'while','for','if','def']:
            if Semantic._tokens[Semantic._tokensIndex].CP =='ID':
                Semantic._tokensIndex += 1
                if self.S_ST2():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP == 'self':
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == '.':
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == 'ID':
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == '(':
                            Semantic._tokensIndex += 1
                            if self.DECL_ASGN():
                                Semantic._tokensIndex += 1
                                if Semantic._tokens[Semantic._tokensIndex].CP == ')':
                                    return True
                                else:
                                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            elif Semantic._tokens[Semantic._tokensIndex].CP == 'while':
                if self.WHILE_ST():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP == 'for':
                if self.FOR_ST():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP == 'if':
                if self.IF_ELSE():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP == 'def':
                if self.FUNC_DEF():
                    return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def S_ST2(self):
        # if Semantic._tokens[Semantic._tokensIndex].CP in ['=',',','ASGN_OPT',',','(','elif','else','ID', 'self', 'while', 'for', 'if','}']:
        if Semantic._tokens[Semantic._tokensIndex].CP in ['=',',','ASGN_OPT']:
            if self.LIST():
                return True
        elif Semantic._tokens[Semantic._tokensIndex].CP in ['.','(']:
            if self.FUNC_CALL1():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    #endregions

    #region LOOPS

    def WHILE_ST(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == 'while':
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == '(':
                Semantic._tokensIndex += 1
                if self.E():
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == ')':
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == ':':
                            Semantic._tokensIndex += 1
                            if self.BODY():
                                return True
                        else:
                            sys.exit(
                                self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    def FOR_ST(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == 'for':
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == '(':
                Semantic._tokensIndex += 1
                if self.X():
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == ';':
                        Semantic._tokensIndex += 1
                        if self.Y():
                            Semantic._tokensIndex += 1
                            if Semantic._tokens[Semantic._tokensIndex].CP == ';':
                                Semantic._tokensIndex += 1
                                if self.X():
                                    Semantic._tokensIndex += 1
                                    if Semantic._tokens[Semantic._tokensIndex].CP == ')':
                                        Semantic._tokensIndex += 1
                                        if Semantic._tokens[Semantic._tokensIndex].CP == ":":
                                            Semantic._tokensIndex += 1
                                            if self.BODY():
                                                return True
                                        else:
                                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                                    else:
                                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                            else:
                                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    def X(self):
        if self.DECL_ASGN():
            return True
        else:
            Semantic._tokensIndex -= 1
            return True

    def Y(self):
        if self.E():
            return True
        else:
            Semantic._tokensIndex += 1
            return True

    #endregion

    #region DECL

    def DECL_ASGN(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ["ID","INC_DEC"]:
            if Semantic._tokens[Semantic._tokensIndex].CP=="ID":
                Semantic._tokensIndex+=1
                if Semantic._tokens[Semantic._tokensIndex].CP in ['=',',','ASGN_OPT']:
                    if self.LIST():
                        return True
                elif Semantic._tokens[Semantic._tokensIndex].CP == "INC_DEC":
                    return True
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            elif Semantic._tokens[Semantic._tokensIndex].CP == "INC_DEC":
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == "ID":
                    return True
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def LIST(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['=',',','ASGN_OPT']:
            if self.INIT():
                Semantic._tokensIndex += 1
                if self.LIST2():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP=="ASGN_OPT":
                Semantic._tokensIndex += 1
                if self.E():
                    Semantic._tokensIndex += 1
                    if self.LIST2():
                        return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def INIT(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "=":
            Semantic._tokensIndex += 1
            if self.INIT2():
                return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def LIST2(self):
        # if Semantic._tokens[Semantic._tokensIndex].CP in [',',';']:
        if Semantic._tokens[Semantic._tokensIndex].CP==',':
            Semantic._tokensIndex += 1
            if self.DECL_ASGN():
                return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def INIT2(self):
        if self.E():
            Semantic._tokensIndex += 1
            if self.INIT3():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def INIT3(self):
        if Semantic._tokens[Semantic._tokensIndex].CP =='=':
            if self.INIT():
                return True

        else:
            Semantic._tokensIndex -= 1
            return True

    #endregion

    #region Expression

    def E(self):
        if self.F():
            Semantic._tokensIndex += 1
            if self.E1():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def E1(self):
        if Semantic._tokens[Semantic._tokensIndex].VP == '||':
            Semantic._tokensIndex += 1
            if self.F():
                Semantic._tokensIndex += 1
                if self.E1():
                    return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def F(self):
        if self.G():
            Semantic._tokensIndex += 1
            if self.F1():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def F1(self):
        if Semantic._tokens[Semantic._tokensIndex].VP == '&&':
            Semantic._tokensIndex += 1
            if self.G():
                Semantic._tokensIndex += 1
                if self.F1():
                    return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def G(self):
        if self.H():
            Semantic._tokensIndex += 1
            if self.G1():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def G1(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='RO':
            Semantic._tokensIndex += 1
            if self.H():
                Semantic._tokensIndex += 1
                if self.G1():
                    return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def H(self):
        if self.I():
            Semantic._tokensIndex += 1
            if self.H1():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def H1(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='ADD_SUB':
            Semantic._tokensIndex += 1
            if self.I():
                Semantic._tokensIndex += 1
                if self.H1():
                    return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def I(self):
        if self.J():
            Semantic._tokensIndex += 1
            if self.I1():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def I1(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == 'DIV_MUL':
            Semantic._tokensIndex += 1
            if self.J():
                Semantic._tokensIndex += 1
                if self.I1():
                    return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def J(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST','[']:
            if Semantic._tokens[Semantic._tokensIndex].CP=="ID":
                Semantic._tokensIndex += 1
                if self.J2():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP=="(":
                Semantic._tokensIndex += 1
                if self.E():
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP==")":
                        return True
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            elif Semantic._tokens[Semantic._tokensIndex].VP=="!":
                Semantic._tokensIndex += 1
                if self.J1():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP=="INC_DEC":
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP=="ID":
                    return True
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            elif Semantic._tokens[Semantic._tokensIndex].CP in ['self', 'ID']:
                if self.FUNC_CALL():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP in ['INT_CONST', 'FLT_CONST', 'STR_CONST', 'CHAR_CONST']:
                if self.CONSTANT():
                    return True
            elif Semantic._tokens[Semantic._tokensIndex].CP == "[":
                if self.ARRAY_LIST():
                    return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def J1(self):
        if self.J():
            return True
        else:
            Semantic._tokensIndex -= 1
            return True


    def J2(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='INC_DEC':
            return True
        else:
            Semantic._tokensIndex -= 1
            return True

    #endregion

    #region ARRAY LIST

    def ARRAY_LIST(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "[":
            Semantic._tokensIndex += 1
            if self.VALS():
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == "]":
                    return True
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def VALS(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['ID', 'LO', '(', 'INC_DEC', 'self', 'INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST', '[',',']:
            if Semantic._tokens[Semantic._tokensIndex].CP == ",":
                Semantic._tokensIndex += 1
                if self.E():
                    Semantic._tokensIndex += 1
                    if self.VALS():
                        return True
            elif self.E():
                Semantic._tokensIndex += 1
                if self.VALS():
                    return True

            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            Semantic._tokensIndex -= 1
            return True

    #endregion

    def CONSTANT(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['INT_CONST', 'FLT_CONST','STR_CONST', 'CHAR_CONST']:
            return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    #region FUNC_CALL

    def FUNC_CALL(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['self','ID']:
            if Semantic._tokens[Semantic._tokensIndex].CP == "self":
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == ".":
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == "ID":
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == "(":
                            Semantic._tokensIndex += 1
                            if self.PARAMS():
                                Semantic._tokensIndex += 1
                                if Semantic._tokens[Semantic._tokensIndex].CP == ")":
                                    return True
                                else:
                                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

            elif Semantic._tokens[Semantic._tokensIndex].CP == "ID":
                Semantic._tokensIndex += 1
                if self.FUNC_CALL1():
                    return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def FUNC_CALL1(self):
        if Semantic._tokens[Semantic._tokensIndex].CP==".":
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == "ID":
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == "(":
                    Semantic._tokensIndex += 1
                    if self.PARAMS():
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == ")":
                            return True
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        elif Semantic._tokens[Semantic._tokensIndex].CP == "(":
            Semantic._tokensIndex += 1
            if self.FUNC_CALL2():
                return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def FUNC_CALL2(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == ")":
            Semantic._tokensIndex += 1
            if self.FUNC_CALL3():
                return True
        elif self.PARAMS():
            return True

        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def FUNC_CALL3(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=='.':
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP=='ID':
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == '(':
                    Semantic._tokensIndex += 1
                    if self.PARAMS():
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == ')':
                            return True
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            Semantic._tokensIndex -= 1
            return True


    def PARAMS(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "ID":
            Semantic._tokensIndex += 1
            if self.PARAMS1():
                return True
        elif Semantic._tokens[Semantic._tokensIndex].CP == ",":
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == "ID":
                Semantic._tokensIndex += 1
                if self.PARAMS1():
                    return True

        else:
            Semantic._tokensIndex -= 1
            return True

    def PARAMS1(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "=":
            Semantic._tokensIndex += 1
            if self.E():
                Semantic._tokensIndex += 1
                if self.PARAMS():
                    return True
        elif self.PARAMS():
            return True
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    #endregion

    #region IF-ELSE

    def IF_ELSE(self):
        if Semantic._tokens[Semantic._tokensIndex].CP=="if":
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == "(":
                Semantic._tokensIndex += 1
                if self.E():
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == ")":
                        Semantic._tokensIndex += 1
                        if Semantic._tokens[Semantic._tokensIndex].CP == ":":
                            Semantic._tokensIndex += 1
                            if self.BODY():
                                Semantic._tokensIndex += 1
                                if self.ELIF():
                                    Semantic._tokensIndex += 1
                                    if self.O_ELSE():
                                        return True
                        else:
                            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))


    def ELIF(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "elif":
            Semantic._tokensIndex += 1
            if self.E():
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == ")":
                    Semantic._tokensIndex += 1
                    if Semantic._tokens[Semantic._tokensIndex].CP == ":":
                        Semantic._tokensIndex += 1
                        if self.BODY():
                            return True
                    else:
                        sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            Semantic._tokensIndex -= 1
            return True

    def O_ELSE(self):
        if Semantic._tokens[Semantic._tokensIndex].CP == "else":
            Semantic._tokensIndex += 1
            if Semantic._tokens[Semantic._tokensIndex].CP == ":":
                Semantic._tokensIndex += 1
                if self.BODY():
                    return True
            else:
                sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            Semantic._tokensIndex -= 1
            return True

    #endregion

    def BODY(self):
        if Semantic._tokens[Semantic._tokensIndex].CP in ['ID', 'self', 'while', 'for', 'if', 'def']:
            if self.S_ST():
                return True
        elif Semantic._tokens[Semantic._tokensIndex].CP == "{":
            Semantic._tokensIndex += 1
            if self.M_ST():
                Semantic._tokensIndex += 1
                if Semantic._tokens[Semantic._tokensIndex].CP == "}":
                    return True
                else:
                    sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP, Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))
        else:
            sys.exit(self.errorPrint(Semantic._tokens[Semantic._tokensIndex].CP,Semantic._tokens[Semantic._tokensIndex].VP,Semantic._tokens[Semantic._tokensIndex].LN))

    def errorPrint(self,classPart,valuePart,lineNum):
        return "Error occur where class is "+classPart+" and value is "+valuePart+" line is "+str(lineNum)



    #call this only at function callling time
    def funcLOOKUP(self,N):
        for t in self.tblFunctions:
            if t.name==N:
                return True

        return False


    #call this at function definition time
    #tpl->total parameter list
    def funcINSERT(self,N,TPL):
        for t in self.tblFunctions:
            if t.name == N:
                self.tblFunctions.remove(t)
                break

        self.tblFunctions.append(matFunctions(N,TPL))


    #check if class exist or not
    def classContainerLookup(self,N):
        for t in self.classesContainer:
            if t.name==N:
                return t.link

        return None


    #check if class's members exist or not
    def classLookup(self,name,type):
        for t in self.tblClasses:
            if t.name==name:
                if type!=0 and type==type:
                    return True
                elif type==0:
                    return True

        return False


    def classContainerInsert(self,N,parent):
        self.classesContainer.append(matClassesContainer(N,parent,Semantic._link))
        Semantic._link = +1

    def classInsert(self,name,type):
        self.tblClasses.append(matClasses(name,type))



