#Nguyen Quang Cong Danh - 1610392

from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *


class ASTGeneration(CSELVisitor):
    #program: declare+ EOF ;
    def visitProgram(self, ctx: CSELParser.ProgramContext):
        program=[]
        for x in ctx.declare():
            program= program+self.visit(x)
        return Program(program)
    #declare: vardecls|constants|funcdecls;
    def visitDeclare(self, ctx: CSELParser.DeclareContext):
        if ctx.vardecls():
            return self.visit(ctx.vardecls())
        elif ctx.constants():
            return self.visit(ctx.constants())
        else:
            return self.visit(ctx.funcdecls())
    #vardecls: LET vardecl (CM vardecl)* SM;
    def visitVardecls(self, ctx: CSELParser.VardeclsContext):
        return [self.visit(x) for x in ctx.vardecl()]
    #vardecl:IDV (COLON types)? (ASSIGN literals)?|arraydecl (COLON types)? (ASSIGN arraylit)?;       
    def visitVardecl(self,ctx:CSELParser.VardeclContext):
        if ctx.IDV():
            #idv cua var
            idv= Id(ctx.IDV().getText())
            if ctx.COLON():
                types= self.visit(ctx.types())
                if ctx.ASSIGN():
                    expr= self.visit(ctx.expr())
                    return VarDecl(idv,None,types,expr)
                else:
                    return VarDecl(idv,None,types,None)

            else:
                types= NoneType()
                if ctx.ASSIGN():
                    expr= self.visit(ctx.expr())
                    return VarDecl(idv,None,types,expr)
                else:
                    return VarDecl(idv,None,types,None)
        else:
            #arraydecl
            #can chinh sua arraydecl
            #chua hoan thanh
            arraydecl= self.visit(ctx.arraydecl())
            if ctx.COLON():
                types= self.visit(ctx.types())
                if ctx.ASSIGN():
                    expr= self.visit(ctx.expr())
                    return VarDecl(arraydecl[0],arraydecl[1],types,expr)
                else:
                    return VarDecl(arraydecl[0],arraydecl[1],types,None)

            else:
                types= NoneType()
                if ctx.ASSIGN():
                    expr= self.visit(ctx.expr())
                    return VarDecl(arraydecl[0],arraydecl[1],types,expr)
                else:
                    return VarDecl(arraydecl[0],arraydecl[1],types,None)
    #arraydecl: IDV LSB (expr3 (CM expr3)*)? RSB;

    def visitArraydecl(self,ctx:CSELParser.ArraydeclContext):
        idv=Id(ctx.IDV().getText())
        arrayblock=[]
        if ctx.expr3():
            arrayblock=[self.visit(expr) for expr in ctx.expr3()]
        
        return [idv,arrayblock]
    #constants: CONSTANT consdecl(CM consdecl)* SM ;
    def visitConstants(self,ctx:CSELParser.ConstantsContext):
        return [self.visit(x) for x in ctx.consdecl()]

    #consdecl: IDC (COLON types)? (ASSIGN literals)|arrayconsdecl (COLON types)? (ASSIGN arraylit);
    def visitConsdecl(self,ctx:CSELParser.ConsdeclContext):
        if ctx.IDC():
            #idv cua var
            idc= Id(ctx.IDC().getText())
            if ctx.COLON():
                types= self.visit(ctx.types())
               
                expr= self.visit(ctx.expr())
                return ConstDecl(idc,None,types,expr)
                
                    

            else:
                types= NoneType()
               
                expr= self.visit(ctx.expr())
                return ConstDecl(idc,None,types,expr)
                
        else:
            arraydecl= self.visit(ctx.arraydecl())
            if ctx.COLON():
                types= self.visit(ctx.types())
                
                expr= self.visit(ctx.expr())
                return ConstDecl(arraydecl[0],arraydecl[1],types,expr)
               
                    

            else:
                types= NoneType()
                if ctx.ASSIGN():
                    expr= self.visit(ctx.expr())
                    return ConstDecl(arraydecl[0],arraydecl[1],types,expr)
                else:
                    return ConstDecl(arraydecl[0],arraydecl[1],types,None)
    #types: NUMBER|STRING|JSON|BOOLEAN;
    def visitTypes(self,ctx:CSELParser.TypesContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.STRING():
            return StringType()
        elif ctx.JSON():
            return JSONType()
        else:
            return BooleanType()
    #funcdecls: FUNCTION IDV LP paralist? RP LCB body* RCB ;
    def visitFuncdecls(self,ctx:CSELParser.FuncdeclsContext):
        id_function= Id(ctx.IDV().getText())
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
           
        if (ctx.paralist()):
            #param la 1 list
            param=self.visit(ctx.paralist())
            #body la 1 list
           
            return [FuncDecl(id_function,param,body)]
        else:
            #body tra ve 1 list
            
            return [FuncDecl(id_function,[],body)]
    #paralist: parameter (CM parameter)*;
    def visitParalist(self,ctx:CSELParser.ParalistContext):
        return [self.visit(x) for x in ctx.parameter()]
    
    #parameter: IDV | index_oper|IDC;
    def visitParameter(self,ctx:CSELParser.ParameterContext):
        if (ctx.IDV()):
            return VarDecl(Id(ctx.IDV().getText()),None,NoneType(),None)
        else:
            return self.visit(ctx.index_oper())
    #index_oper: IDV LSB RSB|IDV LSB (expr3 (CM expr3)*) RSB;
    def visitIndex_oper(self,ctx:CSELParser.Index_operContext):
        idv=Id(ctx.IDV().getText())
        arrayblock=[]
        if ctx.expr3():
            arrayblock=[self.visit(expr) for expr in ctx.expr3()]
        return VarDecl(idv,arrayblock,NoneType(),None)
        
    #body: statement|vardecls|constants;
    def visitBody(self,ctx:CSELParser.BodyContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        elif ctx.vardecls():
            return self.visit(ctx.vardecls())
        else:
            return self.visit(ctx.constants())
    #statement: assign_stmt|if_stmt|for_stmt|while_stmt|break_stmt|continue_stmt|call_stmt|return_stmt;
    def visitStatement(self,ctx:CSELParser.StatementContext):
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
    #assign_stmt:lhs ASSIGN expr SM;
    def visitAssign_stmt(self,ctx:CSELParser.Assign_stmtContext):
        return [Assign(self.visit(ctx.lhs()),self.visit(ctx.expr()))]
    def visitLhs(self,ctx:CSELParser.LhsContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return Id(ctx.IDV().getText())

    #if_stmt: ifs elifs* elses?;
    def visitIf_stmt(self,ctx:CSELParser.If_stmtContext):
        elses=[]
        if (ctx.elses()):
            elses=self.visit(ctx.elses())
        if ctx.elifs():
            return [If([self.visit(ctx.ifs())]+[self.visit(x) for x in ctx.elifs()], elses)]
        else:
            return [If ([self.visit(ctx.ifs())],elses)]

    #ifs: IF LP expr1 RP LCB body* RCB;
    def visitIfs(self,ctx:CSELParser.IfsContext):
        expr= self.visit(ctx.expr1())
     
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
        return (expr,body)
    #elifs:ELIF LP expr1 RP LCB body* RCB;
    def visitElifs(self,ctx:CSELParser.ElifsContext):
        expr= self.visit(ctx.expr1())
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
        return (expr,body)
    #elses: ELSE LCB body* RCB;
    def visitElses(self,ctx:CSELParser.ElsesContext):
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
        return body
    
    #for_stmt: infor| offor;
    def visitFor_stmt(self,ctx:CSELParser.For_stmtContext):
        if ctx.infor():
            return self.visit(ctx.infor())
        else:
            return self.visit(ctx.offor())
    #infor: FOR IDV IN expr LCB body* RCB;
    def visitInfor(self,ctx:CSELParser.InforContext):
        idv= Id(ctx.IDV().getText())
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
       
        return [ForIn(idv,self.visit(ctx.expr()),body)]
    #offor: FOR IDV OF expr LCB body* RCB;
    def visitOffor(self,ctx:CSELParser.OfforContext):
        idv = Id(ctx.IDV().getText())
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
        return [ForOf(idv,self.visit(ctx.expr()),body)]
    #while_stmt: WHILE LP expr1 RP LCB body* RCB;
    def visitWhile_stmt(self,ctx:CSELParser.While_stmtContext):
        expr=self.visit(ctx.expr1())
        body=[]
        if ctx.body():
            for x in ctx.body():
                body=body+self.visit(x)
        return [While(expr,body)]
    #break_stmt: BREAK SM;
    #continue_stmt: CONTINUE SM;
    #call_stmt: CALL LP IDV CM LSB list_call? RSB RP SM;
    #list_call: expr (CM expr)*;
    #return_stmt: RETURN expr SM;
    def visitBreak_stmt(self,ctx:CSELParser.Break_stmtContext):
        return [Break()]
    def visitContinue_stmt(self,ctx:CSELParser.Continue_stmtContext):
        return [Continue()]
    def visitCall_stmt(self,ctx:CSELParser.Call_stmtContext):
        func_name=Id(ctx.IDV().getText())
        list_param=[]
        if ctx.list_call():
            list_param=self.visit(ctx.list_call())
        return [CallStmt(func_name,list_param)]
    def visitReturn_stmt(self,ctx:CSELParser.Return_stmtContext):
        expr=self.visit(ctx.expr())
        return [Return(expr)]


    #index_oper: IDV LSB RSB|IDV LSB index_operators RSB;
    #arraylit: simple_array|multi_array;
    #simple_array: LSB literals3 ( CM literals3)* RSB;
    #multi_array: LSB simple_array(CM simple_array)* RSB| LSB multi_array(CM multi_array) RSB; 
    #constants: CONSTANT consdecl(CM consdecl)* SM ;
    #expr1: expr2 (EQUAL|NOT_EQUAL|LT|GT|LE|GE) expr2|expr2;
    def visitExpr(self,ctx:CSELParser.ExprContext):
        if ctx.ADDDOT():
            return BinaryOp(ctx.ADDDOT().getText(),self.visit(ctx.expr1(0)),self.visit(ctx.expr1(1)))
        elif ctx.EQUALDOT():
            return BinaryOp(ctx.EQUALDOT().getText(),self.visit(ctx.expr1(0)),self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1(0))
    def visitExpr1(self,ctx:CSELParser.Expr1Context):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        elif ctx.LT():
            return BinaryOp(ctx.LT().getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        elif ctx.GT():
            return BinaryOp(ctx.GT().getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        elif ctx.LE():
            return BinaryOp(ctx.LE().getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        elif ctx.GE():
            return BinaryOp(ctx.GE().getText(),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        else:
            return self.visit(ctx.expr2(0))
    #expr2: expr2 (ANDAND|OR) expr3|expr3;
    def visitExpr2(self,ctx:CSELParser.Expr2Context):
        if ctx.ANDAND():
            return BinaryOp(ctx.ANDAND().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3())) 
        else:
            return self.visit(ctx.expr3())
    #expr3: expr3 (ADD|SUB) expr4|expr4;
    def visitExpr3(self,ctx:CSELParser.Expr3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())
    #expr4: expr4( MUL|DIV|MOD) expr5|expr5;
    def visitExpr4(self,ctx:CSELParser.Expr4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())
    #expr5: NOT expr5|expr6;
    def visitExpr5(self,ctx:CSELParser.Expr5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())
    #expr6: SUB expr6| expr7;
    def visitExpr6(self,ctx:CSELParser.Expr6Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(),self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())

    #expr7: expr7 key_operators |expr7 LSB index_operators RSB | expr8;
    def visitExpr7(self,ctx:CSELParser.Expr7Context):
        if (ctx.key_operators()):
            json_name=self.visit(ctx.expr7())
            idx=self.visit(ctx.key_operators())
            return JSONAccess(json_name,idx)
        elif (ctx.index_operators()):
            arr=self.visit(ctx.expr7())
            idx=self.visit(ctx.index_operators())
            return ArrayAccess(arr,idx)
        else:
            return self.visit(ctx.expr8())
    #key_operators: LCB expr RCB | LCB expr RCB key_operators;
    def visitKey_operators(self,ctx:CSELParser.Key_operatorsContext):
        child_number=ctx.getChildCount()
        key_operators=list()
        if child_number==3:
            return [self.visit(ctx.expr())]
        else:
            return self.visit(ctx.key_operators())+[self.visit(ctx.expr())]

    #index_operators: expr3 | expr3 CM index_operators;
    def visitIndex_operators(self,ctx:CSELParser.Index_operatorsContext):
        child_number=ctx.getChildCount()
        if child_number==3:
            return [self.visit(ctx.expr3())]+self.visit(ctx.index_operators())
        else:
            return [self.visit(ctx.expr3())]
    #expr8: IDV|NUMBERLIT|BOOLEANLIT|STRINGLIT|LP expr RP|call_expr|IDC;
    def visitExpr8(self,ctx:CSELParser.Expr8Context):
        if (ctx.IDV()):
            return Id(ctx.IDV().getText())
        elif (ctx.NUMBERLIT()):
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif (ctx.BOOLEANLIT()):
            return BooleanLiteral(True if ctx.BOOLEANLIT().getText=="True" else False)
        elif (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        elif (ctx.call_expr()):
            return self.visit(ctx.call_expr())
        elif (ctx.expr()):
            return self.visit(ctx.expr())
        elif ctx.IDC():
            return Id(ctx.IDC().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        else:
            return self.visit(ctx.jsonlit())

    #call_expr: CALL LP IDV CM LSB list_call? RSB RP;
    def visitCall_expr(self,ctx:CSELParser.Call_exprContext):
        func_name=Id(ctx.IDV().getText())
        list_param=[]
        if ctx.list_call():
            list_param=self.visit(ctx.list_call())
        return CallExpr(func_name,list_param)
    #list_call: expr (CM expr)*;
    def visitList_call(self,ctx:CSELParser.List_callContext):
        if (ctx.CM()):
            return [self.visit(expr) for expr in ctx.expr()]
        else:
            return [self.visit(ctx.expr(0))]
    def visitArraylit(self, ctx: CSELParser.ArraylitContext):
        if ctx.simple_array():
            return self.visit(ctx.simple_array())
        else:
            return self.visit(ctx.multi_array())

    # simple_array : LP literals3 (CM literals3)* RP ;
    # literals3: NUMBERLIT | BOOLEANLIT | STRINGLIT| jsonlit;
    def visitSimple_array(self, ctx: CSELParser.Simple_arrayContext):
        css = list()
        for x in ctx.literals3():

            if x.NUMBERLIT():
                css.append(NumberLiteral(float(x.NUMBERLIT().getText())))
            elif x.jsonlit():
                css.append(self.visit(x.jsonlit()))
            elif x.BOOLEANLIT():
                css.append(BooleanLiteral(True if x.BOOLEANLIT().getText() == "True" else False))
            else:
                css.append(StringLiteral(x.STRINGLIT().getText()))
        return ArrayLiteral(css)


    # multi_array : LP simple_array (CM simple_array)* RP | LP multi_array (CM multi_array)* RP ;
    def visitMulti_array(self, ctx: CSELParser.Multi_arrayContext):

        if ctx.simple_array():

            return ArrayLiteral([self.visit(x) for x in ctx.simple_array()])

        else:

            return ArrayLiteral([self.visit(x) for x in ctx.multi_array()])
    #jsonlit: LCB jsonlist? RCB;
    #jsonlist: jsonmember (CM jsonmember)*;
    #jsonmember: IDV COLON expr;
    #literals2: NUMBERLIT|BOOLEANLIT|STRINGLIT|arraylit|jsonlit;
    def visitJsonlit(self,ctx:CSELParser.JsonlitContext):
        if ctx.jsonlist():
            return self.visit(ctx.jsonlist())
        return [()]
    def visitJsonlist(self,ctx:CSELParser.JsonlistContext):
        return [self.visit(x) for x in ctx.jsonmember()]
    def visitJsonmember(self,ctx:CSELParser.JsonmemberContext):
        return (Id(ctx.IDV().getText()),self.visit(ctx.expr()))
    # def visitLiteral2(self,ctx:CSELParser.Literals2Context):
    #     if ctx.NUMBERLIT():
    #         return NumberLiteral(float(ctx.NUMBERLIT().getText()))
    #     elif ctx.BOOLEANLIT():
    #         return BooleanLiteral(True if ctx.BOOLEANLIT().getText=="True" else False)
    #     elif ctx.STRINGLIT():
    #         return StringLiteral(ctx.STRINGLIT().getText())
    #     elif ctx.arraylit():
    #         return self.visit(ctx.arraylit())
       
        


    
        
