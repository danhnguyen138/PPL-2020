#Nguyen Quang Cong Danh - 1610392

from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class NumberType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass

class JSONType(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[Expr]
    eletype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type

@dataclass
class MType:
    intype: List[Symbol]
    restype: Type





class StaticChecker(BaseVisitor):
    def __init__(self, ctx):
        self.ctx = ctx
        self.global_envi = [[Symbol("print", MType([Symbol("arg",StringType())], VoidType())),
        Symbol("printLn", MType([Symbol("arg", StringType())], VoidType())),
        Symbol("read", MType([], StringType()))]]
            # Symbol("read", MType([], StringType())),
            # Symbol("print", MType([StringType()], VoidType())),
            # Symbol("printSLn", MType([StringType()], VoidType()))]]
    def lookup(self,name,lst,func):
        for item in lst:
            for x in item:
                if name == func(x):
                    return x
        return None
    #Ham tim kiem trong 1 list
    def lookupinlist(self,name,lst,func):
        for x in lst:
            if name==func(x):
                return x
        return None
    #Ham tim kiem trong object
    def setType(self,name,lst,typ,func):
        flash=False
        for item in lst:
            for x in item:
                if name==func(x):
                    flash=True
                    if isinstance(x.mtype, MType):
                        
                        x.mtype.restype=typ
                        break
                    elif isinstance(x.mtype, ArrayType):
                        x.mtype.eletype=typ
                        break
                    else:
                        x.mtype=typ
                        break
            if flash:
                break
        return None
    #Ham lay ten ham
    def getNameMtype(self,lst):
        for item in lst:
            for x in item:
                if isinstance(x.mtype,MType):
                    return x.name
        return ""
    #hame cap nhat lai type ham
    def setTypeGlobal(self,name,lst,typ,func):
        for item in lst:
            if name==func(item):
                if isinstance(item.mtype, MType):
                    item.mtype.restype=typ
        return None
    def check(self):
        return self.visit(self.ctx, self.global_envi)

    def visitProgram(self, ctx, o):
        entry_point=False
        for decl in ctx.decl:
            if isinstance(decl, FuncDecl):
                if decl.name.name=='main':
                    entry_point=True
                    break
        
        if entry_point==False:
            raise NoEntryPoint()
        prog_envi=o
        for decl in ctx.decl:
            if isinstance(decl, VarDecl):
                self.visit(decl,prog_envi)
            elif isinstance(decl, ConstDecl):
                self.visit(decl,prog_envi)
            elif isinstance(decl, FuncDecl):
                self.visit(decl,prog_envi)
        # print(prog_envi)
    def visitVarDecl(self,ctx,o):
        is_redecl= self.lookupinlist(ctx.variable.name, o[0], lambda x: x.name)
        if is_redecl:
            raise Redeclared(Variable(), ctx.variable.name)
        else:
            #xu ly voi array
            if ctx.varDimen:
                
                #Khong co type
                if isinstance(ctx.typ, NoneType):
                    #suy dien tu varInit
                    if ctx.varInit:
                        typ= self.visit(ctx.varInit,o)
                        o[0]+= [Symbol(ctx.variable.name, ArrayType(ctx.varDimen, typ[1]))]
                    else:
                        o[0]+= [Symbol(ctx.variable.name, ArrayType(ctx.varDimen, Unknown()))]

                else:
                    o[0]+= [Symbol(ctx.variable.name, ArrayType(ctx.varDimen, ctx.typ))]
            else:
                if isinstance(ctx.typ, NoneType):
                    if ctx.varInit:
                        #can kiem tra kieu typ co phai unknown hay khong
                        typ= self.visit(ctx.varInit,o)
                        o[0]+=[Symbol(ctx.variable.name, typ[1])]
                    else:
                        o[0]+=[Symbol(ctx.variable.name, Unknown())]
    def visitConstDecl(self,ctx,o):
        is_redecl= self.lookupinlist(ctx.constant.name, o[0], lambda x: x.name)
        if is_redecl:
            raise Redeclared(Constant(), ctx.constant.name)
        else:
          
            if ctx.constDimen:
                
                if isinstance(ctx.typ, NoneType):
                    typ= self.visit(ctx.constInit,o)
                    o[0]+=[Symbol(ctx.constant.name, ArrayType(ctx.constDimen,typ[1]))]
                else:
                    o[0]+=[Symbol(ctx.constant.name, ArrayType(ctx.constDimen,ctx.typ))]
            else:
                if isinstance(ctx.typ, NoneType):
                    typ=self.visit(ctx.constInit,o)
                    #can kiem tra kieu typ co phai unknown hay khong
                    o[0]+= [Symbol(ctx.constant.name, typ[1])]
                else:
                    o[0]+= [Symbol(ctx.constant.name, ctx.typ)]
    def visitFuncDecl(self,ctx,o):
        is_refunc= self.lookup(ctx.name.name, o, lambda x: x.name)
        if is_refunc:
            raise Redeclared(Function(), ctx.name.name)
        else:
           
         
            paramlist=[]
            #Tao 1 Symbol co the chinh sua sau
            if ctx.param:
                for decl in ctx.param:
                    is_reparam=self.lookupinlist(decl.variable.name, paramlist, lambda x:x.name)
                    if is_reparam:
                        raise Redeclared(Parameter(), decl.variable.name)
                    else:
                        if decl.varDimen:
                            paramlist+=[Symbol(decl.variable.name, ArrayType(decl.varDimen, Unknown()))]
                        else:
                            paramlist+=[Symbol(decl.variable.name, Unknown())]
            o[0]+=[Symbol(ctx.name.name, MType(paramlist, Unknown()))]
            

            env=[[Symbol(ctx.name.name, MType(paramlist, Unknown()))]]+o
       
            for decl in ctx.param:
                self.visit(decl,env)
            for body in ctx.body:
                self.visit(body,env)


            o[0]=env[-1]
    def checkSameType(self,typ1,typ2):
        if isinstance(typ1, NumberType) and isinstance(typ2, NumberType):
            return True
        elif isinstance(typ1, StringType) and isinstance(typ2, StringType):
            return True
        elif isinstance(typ1, BoolType) and isinstance(typ2, BoolType):
            return True
        elif isinstance(typ1, VoidType) and isinstance(typ2, VoidType):
            return True
        elif isinstance(typ1, ArrayType) and isinstance(typ2, ArrayType):
            return True
        elif isinstance(typ1, JSONType) and isinstance(typ2, JSONType):
            return True
        else:
            return False
    def visitAssign(self,ctx,o):
        rhs=self.visit(ctx.rhs,o)
        lhs=self.visit(ctx.lhs,o)
    
        if isinstance(rhs[1], Unknown) and isinstance(lhs[1], Unknown):
            raise TypeCannotBeInferred(ctx)
        elif not isinstance(lhs[1], Unknown) and isinstance(rhs[1], Unknown):
            if isinstance(ctx.rhs, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                self.setTypeGlobal(rhs[0],o[-1],lhs[1],lambda x: x.name)
            #Cap nhat lai typ cua Id
            elif isinstance(ctx.rhs, Id):
                #Lay ten cua function 
                func_name=self.getNameMtype(o)
                if func_name:
                    #Lay symbol trong Function
                    symbol_func= self.lookupinlist(func_name, o[-1], lambda x:x.name)
                    if symbol_func:
                        listparam=symbol_func.mtype.intype
                        check_param=self.lookupinlist(ctx.rhs.name, listparam, lambda x:x.name)
                        if check_param:
                            
                            check_param.mtype=lhs[1]
            self.setType(rhs[0], o,lhs[1], lambda x: x.name)
            if isinstance(ctx.rhs, ArrayAccess):
                func_name=self.getNameMtype(o)
                
                symbol_func= self.lookupinlist(func_name, o[-1], lambda x:x.name)
                if symbol_func:
                    listparam=symbol_func.mtype.intype
                
                    check_param=self.lookupinlist(rhs[0], listparam, lambda x:x.name)
                    if check_param:
                    
                        if isinstance(check_param.mtype, ArrayType):
                            check_param.mtype.eletype= lhs[1]
                        
                self.setType(rhs[0], o, lhs[1], lambda x: x.name)
            elif isinstance(ctx.rhs, JSONAccess):
                pass
        elif isinstance(lhs[1], Unknown) and not isinstance(rhs[1], Unknown):
            #xem thu co Set lai bien toan cuc hay khong
            
            
            if isinstance(ctx.lhs, ArrayAccess):
                func_name=self.getNameMtype(o)
                
                symbol_func= self.lookupinlist(func_name, o[-1], lambda x:x.name)
                if symbol_func:
                    listparam=symbol_func.mtype.intype
                
                    check_param=self.lookupinlist(lhs[0], listparam, lambda x:x.name)
                    if check_param:
                    
                        if isinstance(check_param.mtype, ArrayType):
                            check_param.mtype.eletype= rhs[1]
                        
                self.setType(lhs[0], o, rhs[1], lambda x: x.name)
            elif isinstance(ctx.lhs, Id):
                func_name=self.getNameMtype(o)
                symbol_func= self.lookupinlist(func_name, o[-1], lambda x:x.name)
                if symbol_func:
                    listparam=symbol_func.mtype.intype
                    check_param=self.lookupinlist(lhs[0], listparam, lambda x:x.name)
                    if check_param:
                       check_param.mtype=rhs[1]
                self.setType(lhs[0],o,rhs[1],lambda x: x.name)
            elif isinstance(ctx.lhs, JSONAccess):
                pass
        elif not self.checkSameType(lhs[1], rhs[1]) and not isinstance(lhs[1], JSONType) and not isinstance(rhs[1], JSONType):
            raise TypeMismatchInStatement(ctx)
        elif isinstance(lhs[1], VoidType):
            raise TypeMismatchInStatement(ctx)
    
    def visitIf(self,ctx,o):
        for ifthen in ctx.ifthenStmt:
           
            checkBol= self.visit(ifthen[0],o)
            if isinstance(checkBol[1], BoolType):
                env=[[]]+o
               
                for decl in ifthen[1]:
                    self.visit(decl,env)
                
            else:
                raise TypeMismatchInStatement(ctx)
        if ctx.elseStmt:
            env=[[]]+o
            for decl in ctx.elseStmt:
                self.visit(decl,env)

    def checkParam(self,expr,o,typ):
        func_name=self.getNameMtype(o)
        selfexpr=self.visit(expr,o)
        #Lay symbol trong global list
        symbol_func=self.lookupinlist(func_name,o[-1],lambda x:x.name)
        if symbol_func:
            listparam=symbol_func.mtype.intype
            if isinstance(expr, Id):
                check_param=self.lookupinlist(selfexpr[0], listparam, lambda x:x.name)
                if check_param:
                    check_param.mtype=typ
                    return True
                else:
                    return False
            if isinstance(expr, ArrayAccess):
                check_param=self.lookupinlist(selfexpr[0], listparam, lambda x:x.name)
                if check_param:
                    check_param.mtype.eletype=typ
                    return True
                else:
                    return False
        
        return False
    def visitBinaryOp(self,ctx,o):
        op=str(ctx.op)
        left= self.visit(ctx.left,o)
        right=self.visit(ctx.right,o)
        #Con Kieu JSon
        if op in ['+','-','*','/','%']:

            if isinstance(left[1], Unknown):
                if isinstance(ctx.left, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(left[0],o[-1],NumberType(),lambda x: x.name)
                    left=[op,NumberType()]
                else:
                    self.checkParam(ctx.left,o,NumberType())
                    self.setType(left[0], o, NumberType(), lambda x: x.name)
                    left=[op,NumberType()]
            if isinstance(right[1], Unknown):
                if isinstance(ctx.right, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(right[0],o[-1],NumberType(),lambda x: x.name)
                    right=[op,NumberType()]
                else:
                    self.checkParam(ctx.right, o, NumberType())
                    self.setType(right[0], o, NumberType(), lambda x:x.name)
                    right=[op,NumberType()]
            if isinstance(left[1], NumberType) and isinstance(right[1], NumberType):
                return [op,NumberType()]
            elif isinstance(left[1], JSONType) and isinstance(right[1], NumberType):
                return [op,NumberType()]
            elif isinstance(left[1], NumberType) and isinstance(right[1], JSONType):
                return [op,NumberType()]
            else:

                raise TypeMismatchInExpression(ctx)
        if op in ['+.','==.']:
           
            if isinstance(left[1], Unknown):
                if isinstance(ctx.left, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(left[0],o[-1],StringType(),lambda x: x.name)
                    left=[op,StringType()]
                else:
                    self.checkParam(ctx.left,o,StringType())
                    self.setType(left[0], o, StringType(), lambda x: x.name)
                    left=[op,StringType()]



                
            if isinstance(right[1], Unknown):
                if isinstance(ctx.right, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(right[0],o[-1],StringType(),lambda x: x.name)
                    right=[op,StringType()]
                else:
                    self.checkParam(ctx.right, o, StringType())
                    self.setType(right[0], o, StringType(), lambda x:x.name)
                    right=[op,StringType()]


            if isinstance(left[1], StringType) and isinstance(right[1], StringType):
                return [op,StringType()]
            elif isinstance(left[1], JSONType) and isinstance(right[1], StringType):
                return [op,StringType()]
            elif isinstance(left[1], StringType) and isinstance(right[1], JSONType):
                return [op,StringType()]
            else:
                raise TypeMismatchInExpression(ctx)

            
        if op in ['==','!=','<','>','<=','>=']:
            
            if isinstance(left[1], Unknown):
                if isinstance(ctx.left, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(left[0],o[-1],NumberType(),lambda x: x.name)
                    left=[op,NumberType()]
                else:
                    self.checkParam(ctx.left,o,NumberType())
                    self.setType(left[0], o, NumberType(), lambda x: x.name)
                    left=[op,NumberType()]
            if isinstance(right[1], Unknown):
                if isinstance(ctx.right, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(right[0],o[-1],NumberType(),lambda x: x.name)
                    right=[op,NumberType()]
                else:
                    self.checkParam(ctx.right, o, NumberType())
                    self.setType(right[0], o, NumberType(), lambda x:x.name)
                    right=[op,NumberType()]
           
            if isinstance(left[1], NumberType) and isinstance(right[1], NumberType):
                return [op,BoolType()]
            elif isinstance(left[1], JSONType) and isinstance(right[1], NumberType):
                return [op,BoolType()]
            elif isinstance(left[1], NumberType) and isinstance(right[1], JSONType):
                return [op,BoolType()]
            else:

                raise TypeMismatchInExpression(ctx)  
        if op in ['&&','||']:
            if isinstance(left[1], Unknown):
                if isinstance(ctx.left, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(left[0],o[-1],BoolType(),lambda x: x.name)
                    left=[op,BoolType()]
                else:
                    self.checkParam(ctx.left,o,BoolType())
                    self.setType(left[0], o, BoolType(), lambda x: x.name)
                    left=[op,BoolType()]



                
            if isinstance(right[1], Unknown):
                if isinstance(ctx.right, CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(right[0],o[-1],BoolType(),lambda x: x.name)
                    right=[op,BoolType()]
                else:
                    self.checkParam(ctx.right, o, BoolType())
                    self.setType(right[0], o, BoolType(), lambda x:x.name)
                    right=[op,BoolType()]
            if isinstance(left[1], BoolType) and isinstance(right[1], BoolType):
                return [op,BoolType()]
            elif isinstance(left[1], JSONType) and isinstance(right[1], BoolType):
                return [op,BoolType()]
            elif isinstance(left[1], BoolType) and isinstance(right[1], JSONType):
                return [op,BoolType()]
            else:

                raise TypeMismatchInExpression(ctx)  
    def visitUnaryOp(self,ctx,o):
        op= str(ctx.op)
        expr= self.visit(ctx.body,o)
        if op in ['!']:
                 
            if isinstance(expr[1], Unknown):
                if isinstance(ctx.expr[1], CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(expr[0],o[-1],BoolType(),lambda x: x.name)
                    expr=[op,BoolType()]
                else:
                    self.checkParam(ctx.expr, o, BoolType())
                    self.setType(expr[0], o, BoolType(), lambda x:x.name)
                    expr=[op,BoolType()]
            
            if isinstance(expr[1], BoolType) or isinstance(expr[1], JSONType) :
                return [op,BoolType()]
            else:
                raise TypeMismatchInExpression(ctx)
        if op in ['-']:
            if isinstance(expr[1], Unknown):
                if isinstance(ctx.expr[1], CallExpr):
                #Cap nhat lai typ cua ham dang goi
                    self.setTypeGlobal(expr[0],o[-1],NumberType(),lambda x: x.name)
                    expr=[op,NumberType()]
                else:
                    self.checkParam(ctx.expr, o, NumberType())
                    self.setType(expr[0], o, NumberType(), lambda x:x.name)
                    expr=[op,NumberType()]
            
            if isinstance(expr[1], NumberType) or isinstance(expr[1], JSONType) :
                return [op,NumberType()]
            else:
                raise TypeMismatchInExpression(ctx)   
    def visitArrayAccess(self,ctx,o):
        nameArray=self.visit(ctx.arr,o)
        nameArray=nameArray[0]
        is_unrec=self.lookup(nameArray, o, lambda x: x.name)
        if is_unrec:
            return [nameArray,is_unrec.mtype.eletype]
        else:
            if nameArray[0]=='$':
                raise Undeclared(Constant(), nameArray)
            else:
                raise Undeclared(Variable(), nameArray)
    def visitJSONAccess(self,ctx,o):
        nameJson=self.visit(ctx.json,o)
        nameJson=nameJson[0]
        is_unrec=self.lookup(nameJson, o, lambda x: x.name)
        if is_unrec:
            return [nameJson,JSONType()]
        else:
            if nameJson[0]=='$':
                raise Undeclared(Constant(), nameJson)
            else:
                raise Undeclared(Variable(), nameJson)
    def visitCallExpr(self,ctx,o):
        
      
        is_unrec=self.lookupinlist(ctx.method.name, o[-1], lambda x:x.name)
        if is_unrec:
            paramlist=is_unrec.mtype.intype
            for paramdecl in paramlist:
                    #Kiem tra cac bien da suy dien het chua
                if isinstance(paramdecl.mtype, Unknown):
                    raise TypeCannotBeInferred(ctx)
            param=ctx.param
        
                #Kiem tra so luong cac bien cung nhu kieu co giong nhau ko
            if len(param)==len(paramlist):
                flash=True
                for i in range(0,len(param)):
                    expr=self.visit(param[i],o)
                   
                    if not self.checkSameType(paramlist[i].mtype, expr[1]):
                        flash=False
                        break
                if flash==False:
                 
                    raise TypeMismatchInExpression(ctx)
            else:
                raise TypeMismatchInExpression(ctx)
            return [ctx.method.name,is_unrec.mtype.restype]
        else:
            raise Undeclared(Function(), ctx.method.name)
    def visitCallStmt(self,ctx,o):
        nameStmt=ctx.method.name

        is_unrec=self.lookupinlist(nameStmt, o[-1], lambda x:x.name)
        #Kiem tra co khai bao hay chua
        if is_unrec:
            #Kiem tra co phai kieu VoidType hay ko
            if  isinstance(is_unrec.mtype.restype, Unknown):
                is_unrec.mtype.restype=VoidType()
            elif not isinstance(is_unrec.mtype.restype, VoidType):
                raise TypeMismatchInStatement(ctx)
            else:
                paramlist=is_unrec.mtype.intype
                for paramdecl in paramlist:
                    #Kiem tra cac bien da suy dien het chua
                    if isinstance(paramdecl.mtype, Unknown):
                        raise TypeCannotBeInferred(ctx)
                param=ctx.param
                #Kiem tra so luong cac bien cung nhu kieu co giong nhau ko
                if len(param)==len(paramlist):
                    flash=True
                    for i in range(0,len(param)):
                        expr=self.visit(param[i],o)
                        if not self.checkSameType(paramlist[i].mtype, expr[1]):
                            flash=False
                            break
                    if flash==False:
                        raise TypeMismatchInStatement(ctx)
                else:
                    raise TypeMismatchInStatement(ctx)


               

                #Kiem tra doi so tham so

        else:
            raise Undeclared(Function(), ctx.method.name)
    #Nen lam cach nao 
    def visitId(self,ctx,o):
     
        is_unrec=self.lookup(ctx.name, o, lambda x:x.name)
        if is_unrec:
            return [ctx.name,is_unrec.mtype]
        else:
            if ctx.name[0]=='$':
                raise Undeclared(Constant(), ctx.name)
            else:
                raise Undeclared(Variable(), ctx.name)
    def visitForIn(self,ctx,o):
        expr=self.visit(ctx.expr,o)
        if expr[0]=='array':
          
            env=[[Symbol(ctx.idx1.name, expr[1])]]+o
            for body in ctx.body:
                self.visit(body,env)
        elif isinstance(ctx.expr, Id):
            searchid=self.lookup(ctx.expr.name, o, lambda x:x.name)
       
            if isinstance(searchid.mtype,ArrayType):
                env=[[Symbol(ctx.idx1.name, searchid.mtype.eletype)]]+o
                for body in ctx.body:
                    self.visit(body,env)
            else:
                raise TypeMismatchInStatement(ctx)
        else:
            raise TypeMismatchInStatement(ctx)
    def visitForOf(self,ctx,o):
        expr=self.visit(ctx.expr,o)
        if isinstance(expr[1], JSONType):
            env=[[Symbol(ctx.idx1.name,JSONType())]]+o
            for body in ctx.body:
                self.visit(body,env)
        elif isinstance(ctx.expr, Id):
            searchid=self.lookup(ctx.expr.name, o, lambda x:x.name)
            if isinstance(searchid, JSONType):
                env=[[Symbol(ctx.idx1.name,JSONType())]]+o
                for body in ctx.body:
                    self.visit(body,env)
            else:
                raise TypeMismatchInStatement(ctx)
        else:
            raise TypeMismatchInStatement(ctx)
    def visitWhile(self,ctx,o):
        exp=self.visit(ctx.exp,o)
        if isinstance(exp[1], BoolType):
            env=[[]]+o
            for sl in ctx.sl:
                self.visit(sl,env)
        else:
            raise TypeMismatchInStatement(ctx)
   
    def visitReturn(self,ctx,o):
        if ctx.expr:
            expr=self.visit(ctx.expr,o)
            #Lay ten cua Ham
            name_func=self.getNameMtype(o)
            #Lay Symbol cua ham
            sym_bol=self.lookupinlist(name_func, o[-1], lambda x:x.name)
            if sym_bol:
                type_func=sym_bol.mtype.restype
                if isinstance(type_func, Unknown):
                    sym_bol.mtype.restype=expr[1]
                else:
                    if self.checkSameType(type_func, expr[1]):
                        pass
                    else:
                        raise TypeMismatchInStatement(ctx)
        else:

           
            #Lay ten cua Ham
            name_func=self.getNameMtype(o)
            #Lay Symbol cua ham
            sym_bol=self.lookupinlist(name_func, o[-1], lambda x:x.name)
            if sym_bol:
                type_func=sym_bol.mtype.restype
                if isinstance(type_func, Unknown):
                    sym_bol.mtype.restype=VoidType()
                else:
                    if self.checkSameType(type_func, VoidType()):
                        pass
                    else:
                        raise TypeMismatchInStatement(ctx)
    def visitNumberLiteral(self,ctx,o):
        return ['Number',NumberType()]
    def visitStringLiteral(self,ctx,o):
        return ['String',StringType()]
    def visitBooleanLiteral(self,ctx,o):
        return ['Boolean',BoolType()]
    def visitJSONLiteral(self,ctx,o):
        return ['Json',JSONType()]
    def visitArrayLiteral(self,ctx,o):
        firstArray=ctx.value[0]
        if isinstance(firstArray, ArrayLiteral):
            return self.visit(firstArray,o)
        else:
            return ['array',self.visit(firstArray,o)[1]]
    def visitBreak(self,ctx,o):
        pass
    def visitContinue(self,ctx,o):
        pass
    def visitIntLiteral(self,ctx,o):
        pass

            
            



            

        

                


                

        

        
