#Nguyen Quang Cong Danh - 1610392

import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """	
Function main() {
    b= a{"name"}{"id"} ;
}"""
        expect = "Program([FuncDecl(Id(main)[],[Assign(Id(b),JSONAccess(Id(a),[StringLiteral(name),StringLiteral(id)]))])])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))




    def test_simple_program_3512(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = "Program([VarDecl(Id(x),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_constant_202(self):
        """Miss variable"""
        input = """Constant $a = 10 ;"""
        expect = "Program([ConstDecl(Id($a),NoneType,NumberLiteral(10.0))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                        Constant $b: String = "Story of Yanxi Place";
                        }"""
        expect = "Program([ConstDecl(Id($a),NoneType,NumberLiteral(10.0)),FuncDecl(Id(foo)[VarDecl(Id(a),[NumberLiteral(5.0)],NoneType),VarDecl(Id(b),NoneType)],[ConstDecl(Id($b),StringType,StringLiteral(Story of Yanxi Place))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_wrong_decleare(self):
        """Miss variable"""
        input = """Let a,b:String;"""
        expect = "Program([VarDecl(Id(a),NoneType),VarDecl(Id(b),StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_wrong_decleare_1(self):
        """Simple program: int main() {} """
        input = """Let a[5]: Number = [1, 2, 3, 4, 5];"""
        expect = "Program([VarDecl(Id(a),[NumberLiteral(5.0)],NumberType,ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0),NumberLiteral(5.0)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_wrong_decleare_2(self):
        """Miss variable"""
        input = """Let b[2, 3] = [[1, 2, 3], [4, 5, 6]] ;"""
        expect = "Program([VarDecl(Id(b),[NumberLiteral(2.0),NumberLiteral(3.0)],NoneType,ArrayLiteral(ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)),ArrayLiteral(NumberLiteral(4.0),NumberLiteral(5.0),NumberLiteral(6.0))))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_declare_1(self):

        input = """Let a = {
                name: True,
                address: [3,4,5],
                surface: 10,
                people: ["a","b","c"]
                };"""
        expect = "Program([VarDecl(Id(a),NoneType,[(Id(name='name'), BooleanLiteral(value=False)), (Id(name='address'), ArrayLiteral(value=[NumberLiteral(value=3.0), NumberLiteral(value=4.0), NumberLiteral(value=5.0)])), (Id(name='surface'), NumberLiteral(value=10.0)), (Id(name='people'), ArrayLiteral(value=[StringLiteral(value='a'), StringLiteral(value='b'), StringLiteral(value='c')]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_declare_2(self):
    
        input = """Let b[2, 3] = [[1, 2, 3], [4, 5, 6]], b: Number ;"""
        expect = "Program([VarDecl(Id(b),[NumberLiteral(2.0),NumberLiteral(3.0)],NoneType,ArrayLiteral(ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)),ArrayLiteral(NumberLiteral(4.0),NumberLiteral(5.0),NumberLiteral(6.0)))),VarDecl(Id(b),NumberType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_declare_3(self):
       
        input = """Let r = 10, v;"""
        expect = "Program([VarDecl(Id(r),NoneType,NumberLiteral(10.0)),VarDecl(Id(v),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    
    def test_declare_4(self):
        """Miss variable"""
        input = """Constant $b: String = "Story of Yanxi Place";"""
        expect = "Program([ConstDecl(Id($b),StringType,StringLiteral(Story of Yanxi Place))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_declare_5(self):
        """Simple program: int main() {} """
        input = """Let x,y,d;"""
        expect = "Program([VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(d),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    
    def test_function_1(self):
        """Miss variable"""
        input = """Constant $a = 10;
Function foo(a[5], b) {
Constant $b: String = "Story of Yanxi Place";
Let i = 0;
While (i < 5) {
a[i] = (b + 1) * $a;
Let u: Number = i + 1;

If (a[u] == 10) {
Return $b;
}
i = i + 1;
}
Return $b + ": Done";
}"""
        expect = "Program([ConstDecl(Id($a),NoneType,NumberLiteral(10.0)),FuncDecl(Id(foo)[VarDecl(Id(a),[NumberLiteral(5.0)],NoneType),VarDecl(Id(b),NoneType)],[ConstDecl(Id($b),StringType,StringLiteral(Story of Yanxi Place)),VarDecl(Id(i),NoneType,NumberLiteral(0.0)),While(BinaryOp(<,Id(i),NumberLiteral(5.0)),[Assign(ArrayAccess(Id(a),[Id(i)]),BinaryOp(*,BinaryOp(+,Id(b),NumberLiteral(1.0)),Id($a))),VarDecl(Id(u),NumberType,BinaryOp(+,Id(i),NumberLiteral(1.0))),If(BinaryOp(==,ArrayAccess(Id(a),[Id(u)]),NumberLiteral(10.0)),[Return(Id($b))]),Assign(Id(i),BinaryOp(+,Id(i),NumberLiteral(1.0)))]),Return(BinaryOp(+,Id($b),StringLiteral(: Done)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_simple_program_3(self):
        """Simple program: int main() {} """
        input = """Constant $a = 10;
Function foo(a[5], b) {

a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);

Return $b + ": Done";
}"""
        expect = "Program([ConstDecl(Id($a),NoneType,NumberLiteral(10.0)),FuncDecl(Id(foo)[VarDecl(Id(a),[NumberLiteral(5.0)],NoneType),VarDecl(Id(b),NoneType)],[Assign(ArrayAccess(Id(a),[NumberLiteral(2.0)]),BinaryOp(+,CallExpr(Id(foo),[NumberLiteral(2.0)]),CallExpr(Id(foo),[CallExpr(Id(bar),[NumberLiteral(2.0),NumberLiteral(3.0)])]))),Return(BinaryOp(+,Id($b),StringLiteral(: Done)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_delcare_7(self):
        """Miss variable"""
        input = """Constant $a = 10;
Function foo(a[5], b) {
Let r = 10, v;
v = 23;
If (a){ Let r=20;}
Elif (b){}
Return $b + ": Done";
}"""
        expect = "Program([ConstDecl(Id($a),NoneType,NumberLiteral(10.0)),FuncDecl(Id(foo)[VarDecl(Id(a),[NumberLiteral(5.0)],NoneType),VarDecl(Id(b),NoneType)],[VarDecl(Id(r),NoneType,NumberLiteral(10.0)),VarDecl(Id(v),NoneType),Assign(Id(v),NumberLiteral(23.0)),If(Id(a),[VarDecl(Id(r),NoneType,NumberLiteral(20.0))])ElseIf(Id(b),[]),Return(BinaryOp(+,Id($b),StringLiteral(: Done)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_simple_program_if(self):
        """Simple program: int main() {} """
        input = """Constant $a = 10;
Function foo(a[5], b) {
Let r = 10, v;
v = 23;

If (a){ Let r=20;}
Elif (b){}
Return $b + ": Done";
}"""
        expect = "Program([ConstDecl(Id($a),NoneType,NumberLiteral(10.0)),FuncDecl(Id(foo)[VarDecl(Id(a),[NumberLiteral(5.0)],NoneType),VarDecl(Id(b),NoneType)],[VarDecl(Id(r),NoneType,NumberLiteral(10.0)),VarDecl(Id(v),NoneType),Assign(Id(v),NumberLiteral(23.0)),If(Id(a),[VarDecl(Id(r),NoneType,NumberLiteral(20.0))])ElseIf(Id(b),[]),Return(BinaryOp(+,Id($b),StringLiteral(: Done)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_simple_program_05(self):
        """ Simple program """
        input = """Let number;
                    Let check;
                    Let arr[4],num,brr[5];"""
        expect = "Program([VarDecl(Id(number),NoneType),VarDecl(Id(check),NoneType),VarDecl(Id(arr),[NumberLiteral(4.0)],NoneType),VarDecl(Id(num),NoneType),VarDecl(Id(brr),[NumberLiteral(5.0)],NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_simple_program_15(self):
        """ Simple program """
        input = """Let date;
        Function pRINT(a){
            date=9;
            Let i;
        For i In a {
                Call(printLn,[i]);
            }
                date=date+1;
            Return 1;
        }
        """
        expect = "Program([VarDecl(Id(date),NoneType),FuncDecl(Id(pRINT)[VarDecl(Id(a),NoneType)],[Assign(Id(date),NumberLiteral(9.0)),VarDecl(Id(i),NoneType),ForIn(Id(i),Id(a),[CallStmt(Id(printLn),[Id(i)])]),Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0))),Return(NumberLiteral(1.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))        

    def test_more_complex_program_11(self):
        """More complex program"""
        input = """Let date;
        Function pRINT(a){
            date=9;
            Let i;
            For i In a {
                date=date+1;
            }
                date=date+1;
            Return 1;
        
        }
        """
        expect = "Program([VarDecl(Id(date),NoneType),FuncDecl(Id(pRINT)[VarDecl(Id(a),NoneType)],[Assign(Id(date),NumberLiteral(9.0)),VarDecl(Id(i),NoneType),ForIn(Id(i),Id(a),[Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0)))]),Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0))),Return(NumberLiteral(1.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318))        

    def test_more_complex_program_12(self):
        """More complex program"""
        input = """Let date;
        Function pRINT(a){
            date=9;
            Let i;
            For i In a {
                date=date+1;
            }
                date=date+1;
            Let a = {
                
                };
            For key In a {
                Call(printLn, ["Value of " + key + ": " + a[key]]);
            }
                Return 1;
        
        }
        """
        expect = "Program([VarDecl(Id(date),NoneType),FuncDecl(Id(pRINT)[VarDecl(Id(a),NoneType)],[Assign(Id(date),NumberLiteral(9.0)),VarDecl(Id(i),NoneType),ForIn(Id(i),Id(a),[Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0)))]),Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0))),VarDecl(Id(a),NoneType,[()]),ForIn(Id(key),Id(a),[CallStmt(Id(printLn),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLiteral(Value of ),Id(key)),StringLiteral(: )),ArrayAccess(Id(a),[Id(key)]))])]),Return(NumberLiteral(1.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))  

    def test_more_complex_program_13(self):
        """More complex program"""
        input = """Let date;
        Function pRINT(a){
            date=9;
            Let i;
            For i In a {
                date=date+1;
            }
                date=date+1;
            Let a = {
name: "Yanxi Place",
address: "Chinese Forbidden City"
};
For key In a {
Call(printLn, ["Value of " + key + ": " + a[key]]);
}
        Break;
            Return 1;
        
        }
        """
        expect = "Program([VarDecl(Id(date),NoneType),FuncDecl(Id(pRINT)[VarDecl(Id(a),NoneType)],[Assign(Id(date),NumberLiteral(9.0)),VarDecl(Id(i),NoneType),ForIn(Id(i),Id(a),[Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0)))]),Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0))),VarDecl(Id(a),NoneType,[(Id(name='name'), StringLiteral(value='Yanxi Place')), (Id(name='address'), StringLiteral(value='Chinese Forbidden City'))]),ForIn(Id(key),Id(a),[CallStmt(Id(printLn),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLiteral(Value of ),Id(key)),StringLiteral(: )),ArrayAccess(Id(a),[Id(key)]))])]),Break(),Return(NumberLiteral(1.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_more_complex_program_14(self):
        input = """Let date;
        Function pRINT(a){
            date=9;
            Let i;
            For i In a {
                date=date+1;
            }
                date=date+1;
            Let a = {
name: "Yanxi Place",
address: "Chinese Forbidden City"
};
For key In a {
Call(printLn, ["Value of " + key + ": " + a[key]]);
}
        Continue;
            Return 1;
        
        }
        """
        expect = "Program([VarDecl(Id(date),NoneType),FuncDecl(Id(pRINT)[VarDecl(Id(a),NoneType)],[Assign(Id(date),NumberLiteral(9.0)),VarDecl(Id(i),NoneType),ForIn(Id(i),Id(a),[Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0)))]),Assign(Id(date),BinaryOp(+,Id(date),NumberLiteral(1.0))),VarDecl(Id(a),NoneType,[(Id(name='name'), StringLiteral(value='Yanxi Place')), (Id(name='address'), StringLiteral(value='Chinese Forbidden City'))]),ForIn(Id(key),Id(a),[CallStmt(Id(printLn),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLiteral(Value of ),Id(key)),StringLiteral(: )),ArrayAccess(Id(a),[Id(key)]))])]),Continue(),Return(NumberLiteral(1.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_more_complex_program_22(self):
        """More complex program"""
        input = """Function array(num){   
            For i In [1,2,3]{
                arr[i]=num;
            }
        }
        Function compute( x, y, tong[]){
            Call(tong,[10]);
            For i In [3] {
                tong=tong+arr[i];
            }
            Return tong;
        }
        """
        expect = "Program([FuncDecl(Id(array)[VarDecl(Id(num),NoneType)],[ForIn(Id(i),ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)),[Assign(ArrayAccess(Id(arr),[Id(i)]),Id(num))])]),FuncDecl(Id(compute)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(tong),NoneType)],[CallStmt(Id(tong),[NumberLiteral(10.0)]),ForIn(Id(i),ArrayLiteral(NumberLiteral(3.0)),[Assign(Id(tong),BinaryOp(+,Id(tong),ArrayAccess(Id(arr),[Id(i)])))]),Return(Id(tong))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,322))        

    def test_more_complex_program_23(self):
        """More complex program"""
        input = """
        Let arr[10];
        Function print(arr[]){}
        Function compute(x,y,tong[]){
            For i In [10,20]{
                arr[i]=True;
                Call(print,[]);
            }
        }
        """
        expect = "Program([VarDecl(Id(arr),[NumberLiteral(10.0)],NoneType),FuncDecl(Id(print)[VarDecl(Id(arr),NoneType)],[]),FuncDecl(Id(compute)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(tong),NoneType)],[ForIn(Id(i),ArrayLiteral(NumberLiteral(10.0),NumberLiteral(20.0)),[Assign(ArrayAccess(Id(arr),[Id(i)]),BooleanLiteral(false)),CallStmt(Id(print),[])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,323))                

    def test_more_complex_program_24(self):
        """More complex program"""
        input = """
        Function print(boolean, arr[]){}
        Function test_prog(){
            Let arr[10]:Boolean;
            Call(print,[arr]);
        }
        """
        expect = "Program([FuncDecl(Id(print)[VarDecl(Id(boolean),NoneType),VarDecl(Id(arr),NoneType)],[]),FuncDecl(Id(test_prog)[],[VarDecl(Id(arr),[NumberLiteral(10.0)],BooleanType),CallStmt(Id(print),[Id(arr)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_more_complex_program_25(self):
        """More complex program"""
        input = """
        Let a;
        Function printsss(a){
            Call(print,[a]);
        }
        Function test_program(){
            a = "dfghjkfg";
            Call(print,[a]);
        }
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(printsss)[VarDecl(Id(a),NoneType)],[CallStmt(Id(print),[Id(a)])]),FuncDecl(Id(test_program)[],[Assign(Id(a),StringLiteral(dfghjkfg)),CallStmt(Id(print),[Id(a)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,325))     
    def test_more_complex_program_26(self):
        """More complex program"""
        input = """
        Let a, b, c;
        Constant $x=3, $y=5, $z="abc";
        Let g, h, y;
        Function nty(){}
        Let x, y, z;
        Let a,w,q; 
        ##
        =======================================
        Comment here
        =======================================
        ##
        """
        expect = "Program([VarDecl(Id(a),NoneType),VarDecl(Id(b),NoneType),VarDecl(Id(c),NoneType),ConstDecl(Id($x),NoneType,NumberLiteral(3.0)),ConstDecl(Id($y),NoneType,NumberLiteral(5.0)),ConstDecl(Id($z),NoneType,StringLiteral(abc)),VarDecl(Id(g),NoneType),VarDecl(Id(h),NoneType),VarDecl(Id(y),NoneType),FuncDecl(Id(nty)[],[]),VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(z),NoneType),VarDecl(Id(a),NoneType),VarDecl(Id(w),NoneType),VarDecl(Id(q),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))        
    def test_more_complex_program_27(self):
        """More complex program"""
        input = """
        Let a;
        Function plusFuncInt(x,y) {
            Return x + y;
        }
        Function plusFuncDouble( x,  y) {
            Return x + y;
        }       
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(plusFuncInt)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[Return(BinaryOp(+,Id(x),Id(y)))]),FuncDecl(Id(plusFuncDouble)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[Return(BinaryOp(+,Id(x),Id(y)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,327))        

    def test_more_complex_program_28(self):
        """More complex program"""
        input = """
        Let a;
        Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Return sum-45673;
        }
        Function plusFuncDouble( x,  y) {
            If(x>=y){
                Return x;}
            Else{
                Return y;
                }
        }       
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(plusFuncInt)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[VarDecl(Id(sum),NoneType),Assign(Id(sum),BinaryOp(+,BinaryOp(*,Id(x),NumberLiteral(567.0)),BinaryOp(/,Id(y),NumberLiteral(1234.0)))),Return(BinaryOp(-,Id(sum),NumberLiteral(45673.0)))]),FuncDecl(Id(plusFuncDouble)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[If(BinaryOp(>=,Id(x),Id(y)),[Return(Id(x))])Else([Return(Id(y))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,328))        

    def test_more_complex_program_29(self):
        """More complex program"""
        input = """
        Let a;
        Function plusFuncInt( x,  y) {
            Let sum;
            For x In [1,2,3]{
                If(x==5){
                    Break;
                }
            }
            Return x;
        }       
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(plusFuncInt)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[VarDecl(Id(sum),NoneType),ForIn(Id(x),ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)),[If(BinaryOp(==,Id(x),NumberLiteral(5.0)),[Break()])]),Return(Id(x))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,329))                

    def test_more_complex_program_30(self):
        """More complex program"""
        input = """
        Let a;
        Function plusFuncDouble( x,  y) {
           For x In [3,2,1]{
            If (y<x){
                Continue;}
            Else{
                Return y;
                }
            }
        }       
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(plusFuncDouble)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[ForIn(Id(x),ArrayLiteral(NumberLiteral(3.0),NumberLiteral(2.0),NumberLiteral(1.0)),[If(BinaryOp(<,Id(y),Id(x)),[Continue()])Else([Return(Id(y))])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_more_complex_program_31(self):
        """More complex program"""
        input = """
        Function main(){
            Call(foo,[2])[3+x] = a[b[2]] + 3;
        }
        """
        expect = "Program([FuncDecl(Id(main)[],[Assign(ArrayAccess(CallExpr(Id(foo),[NumberLiteral(2.0)]),[BinaryOp(+,NumberLiteral(3.0),Id(x))]),BinaryOp(+,ArrayAccess(Id(a),[ArrayAccess(Id(b),[NumberLiteral(2.0)])]),NumberLiteral(3.0)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,331))        

    def test_more_complex_program_32(self):
        """More complex program"""
        input = """
        Function c(){
            3[3+x] = True[b[2]] +3;
        }
        """
        expect = "Program([FuncDecl(Id(c)[],[Assign(ArrayAccess(NumberLiteral(3.0),[BinaryOp(+,NumberLiteral(3.0),Id(x))]),BinaryOp(+,ArrayAccess(BooleanLiteral(false),[ArrayAccess(Id(b),[NumberLiteral(2.0)])]),NumberLiteral(3.0)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,332))        

    def test_more_complex_program_33(self):
        """More complex program"""
        input = """
        Function c(){
            Let arr[3];
            crr[3+x-y*342]=10;
            Call(dr,[2,4])[3+x-y*342]=23;
        }
        """
        expect = "Program([FuncDecl(Id(c)[],[VarDecl(Id(arr),[NumberLiteral(3.0)],NoneType),Assign(ArrayAccess(Id(crr),[BinaryOp(-,BinaryOp(+,NumberLiteral(3.0),Id(x)),BinaryOp(*,Id(y),NumberLiteral(342.0)))]),NumberLiteral(10.0)),Assign(ArrayAccess(CallExpr(Id(dr),[NumberLiteral(2.0),NumberLiteral(4.0)]),[BinaryOp(-,BinaryOp(+,NumberLiteral(3.0),Id(x)),BinaryOp(*,Id(y),NumberLiteral(342.0)))]),NumberLiteral(23.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,333))        

    def test_more_complex_program_34(self):
        """More complex program"""
        input = """
        Function foo (  a ,  b [] )
        {
            Let c ;
            Let i ;
            i = a + 3 ;
            If( i >0) {
                Let d ;
                d = i + 3 ;
                Call(putInt,[d] ) ;
            }
            Return i ;
        }
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),NoneType),VarDecl(Id(b),NoneType)],[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType),Assign(Id(i),BinaryOp(+,Id(a),NumberLiteral(3.0))),If(BinaryOp(>,Id(i),NumberLiteral(0.0)),[VarDecl(Id(d),NoneType),Assign(Id(d),BinaryOp(+,Id(i),NumberLiteral(3.0))),CallStmt(Id(putInt),[Id(d)])]),Return(Id(i))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,334))        

    def test_more_complex_program_35(self):
        """More complex program"""
        input = """
        Function main(  argc ,  argv[] )
        {
            Let c ;
            Let i ;
            For i Of a{
                Let d ;
                d = i + 3 ;
                Call(putID,[d] ) ;
            }
      
            Return i ;
        }
        """
        expect = "Program([FuncDecl(Id(main)[VarDecl(Id(argc),NoneType),VarDecl(Id(argv),NoneType)],[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType),ForOf(Id(i),Id(a),[VarDecl(Id(d),NoneType),Assign(Id(d),BinaryOp(+,Id(i),NumberLiteral(3.0))),CallStmt(Id(putID),[Id(d)])]),Return(Id(i))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,335))    
    def test_more_complex_program_36(self):
        """More complex program"""
        input = """
        Function main(  argc ,  str )
        {
            Let c ;
            Let i ;
            i=10;
            If( c==True){
                Let d ;
                str = "Hello World";
                 Call(put, [d]);
            }
            Call(print,[str]);
            Return i ;
        }
        """
        expect = "Program([FuncDecl(Id(main)[VarDecl(Id(argc),NoneType),VarDecl(Id(str),NoneType)],[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType),Assign(Id(i),NumberLiteral(10.0)),If(BinaryOp(==,Id(c),BooleanLiteral(false)),[VarDecl(Id(d),NoneType),Assign(Id(str),StringLiteral(Hello World)),CallStmt(Id(put),[Id(d)])]),CallStmt(Id(print),[Id(str)]),Return(Id(i))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_more_complex_program_37(self):
        """More complex program"""
        input = """
        Function count( money[]){
            Let sum,i;
            sum=0;
            i=0;
            While (i<3){
                sum=sum+money[i+1];
            }
            
        }
        Function main(  argc[] ,  str )
        {
            Let c ;
            Call(argsc,[]);
            Call(asss,[t]);
            Return i ;
        }
        """
        expect = "Program([FuncDecl(Id(count)[VarDecl(Id(money),NoneType)],[VarDecl(Id(sum),NoneType),VarDecl(Id(i),NoneType),Assign(Id(sum),NumberLiteral(0.0)),Assign(Id(i),NumberLiteral(0.0)),While(BinaryOp(<,Id(i),NumberLiteral(3.0)),[Assign(Id(sum),BinaryOp(+,Id(sum),ArrayAccess(Id(money),[BinaryOp(+,Id(i),NumberLiteral(1.0))])))])]),FuncDecl(Id(main)[VarDecl(Id(argc),NoneType),VarDecl(Id(str),NoneType)],[VarDecl(Id(c),NoneType),CallStmt(Id(argsc),[]),CallStmt(Id(asss),[Id(t)]),Return(Id(i))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,337))        

    def test_more_complex_program_38(self):
        """More complex program"""
        input = """Function main(){ If (a){} 
        Elif (b){}
        Elif (c)
        { For i In a { Call(foo,[2,4]);}} 
        Else {} 
        }"""
        expect = "Program([FuncDecl(Id(main)[],[If(Id(a),[])ElseIf(Id(b),[])ElseIf(Id(c),[ForIn(Id(i),Id(a),[CallStmt(Id(foo),[NumberLiteral(2.0),NumberLiteral(4.0)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_more_complex_program_39(self):
        """More complex program"""
        input = """Function main( ){ If (a){ If (b){ If (c){ Let a;} Else {}} Else{}}}"""
        expect = "Program([FuncDecl(Id(main)[],[If(Id(a),[If(Id(b),[If(Id(c),[VarDecl(Id(a),NoneType)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_more_complex_program_40(self):
        """More complex program"""
        input = """Function main() {
            d=(a+b)+(c+d);
        }"""
        expect = "Program([FuncDecl(Id(main)[],[Assign(Id(d),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),BinaryOp(+,Id(c),Id(d))))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_more_complex_program_41(self):
        """More complex program"""
        input = """Function main () {
            Call(putItrln,[2]);
            Call(put,[2])[4]=5;
            (Call(put,[3]))[5]=10;
        }"""
        expect = "Program([FuncDecl(Id(main)[],[CallStmt(Id(putItrln),[NumberLiteral(2.0)]),Assign(ArrayAccess(CallExpr(Id(put),[NumberLiteral(2.0)]),[NumberLiteral(4.0)]),NumberLiteral(5.0)),Assign(ArrayAccess(CallExpr(Id(put),[NumberLiteral(3.0)]),[NumberLiteral(5.0)]),NumberLiteral(10.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_more_complex_program_42(self):
        """More complex program"""
        input = """Function main( ){ 
            While (x>=9){
                i=0;
                i=count/12;
                Call(arr,[3,arr[4]]);
            }
         }"""
        expect = "Program([FuncDecl(Id(main)[],[While(BinaryOp(>=,Id(x),NumberLiteral(9.0)),[Assign(Id(i),NumberLiteral(0.0)),Assign(Id(i),BinaryOp(/,Id(count),NumberLiteral(12.0))),CallStmt(Id(arr),[NumberLiteral(3.0),ArrayAccess(Id(arr),[NumberLiteral(4.0)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_more_complex_program_43(self):
        """More complex program"""
        input = """Function main( ){
        Let i,count;
        i=count/12;
        Call(goo, [3,arr[4]]);
        a=a && 1;
        }"""
        expect = "Program([FuncDecl(Id(main)[],[VarDecl(Id(i),NoneType),VarDecl(Id(count),NoneType),Assign(Id(i),BinaryOp(/,Id(count),NumberLiteral(12.0))),CallStmt(Id(goo),[NumberLiteral(3.0),ArrayAccess(Id(arr),[NumberLiteral(4.0)])]),Assign(Id(a),BinaryOp(&&,Id(a),NumberLiteral(1.0)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_more_complex_program_44(self):
        """More complex program"""
        input = """Function main( ){ 
        While(gh==true){
            i=0;
            fghj=67/hj;
     
        While(x<=10){
        i=count/12;}
        While(x>=9){
            Call(goo,[3,arr[10]]);
       }
            }
        }"""
        expect = "Program([FuncDecl(Id(main)[],[While(BinaryOp(==,Id(gh),Id(true)),[Assign(Id(i),NumberLiteral(0.0)),Assign(Id(fghj),BinaryOp(/,NumberLiteral(67.0),Id(hj))),While(BinaryOp(<=,Id(x),NumberLiteral(10.0)),[Assign(Id(i),BinaryOp(/,Id(count),NumberLiteral(12.0)))]),While(BinaryOp(>=,Id(x),NumberLiteral(9.0)),[CallStmt(Id(goo),[NumberLiteral(3.0),ArrayAccess(Id(arr),[NumberLiteral(10.0)])])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_more_complex_program_45(self):
        """More complex program"""
        input = """Function main( ){ 
            Call(foo,[3])[3+x] = a[b[2]] +3;
           Call(goo,[2])[x+3] = a[b[2+z]] + t;
   
            a=100;
        }"""
        expect = "Program([FuncDecl(Id(main)[],[Assign(ArrayAccess(CallExpr(Id(foo),[NumberLiteral(3.0)]),[BinaryOp(+,NumberLiteral(3.0),Id(x))]),BinaryOp(+,ArrayAccess(Id(a),[ArrayAccess(Id(b),[NumberLiteral(2.0)])]),NumberLiteral(3.0))),Assign(ArrayAccess(CallExpr(Id(goo),[NumberLiteral(2.0)]),[BinaryOp(+,Id(x),NumberLiteral(3.0))]),BinaryOp(+,ArrayAccess(Id(a),[ArrayAccess(Id(b),[BinaryOp(+,NumberLiteral(2.0),Id(z))])]),Id(t))),Assign(Id(a),NumberLiteral(100.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_more_complex_program_46(self):
        """More complex program"""
        input = """Function main() { If(i>1) {} Else {}
        }"""
        expect = "Program([FuncDecl(Id(main)[],[If(BinaryOp(>,Id(i),NumberLiteral(1.0)),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_more_complex_program_47(self):
        """More complex program"""
        input = """Function swap( a,  b){ 
            Let tmp;
            tmp = a;
            a = b;
            b = tmp;
            Call(printf,[a, b]);
            Return True;
        }
        Function main(){
            Let a,b;
            Let result;
            result = Call(swap,[a,b]);
            Call(print,[result]);
        }"""
        expect = "Program([FuncDecl(Id(swap)[VarDecl(Id(a),NoneType),VarDecl(Id(b),NoneType)],[VarDecl(Id(tmp),NoneType),Assign(Id(tmp),Id(a)),Assign(Id(a),Id(b)),Assign(Id(b),Id(tmp)),CallStmt(Id(printf),[Id(a),Id(b)]),Return(BooleanLiteral(false))]),FuncDecl(Id(main)[],[VarDecl(Id(a),NoneType),VarDecl(Id(b),NoneType),VarDecl(Id(result),NoneType),Assign(Id(result),CallExpr(Id(swap),[Id(a),Id(b)])),CallStmt(Id(print),[Id(result)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_more_complex_program_48(self):
        """More complex program"""
        input = """Function c(){
            s = a +b + c * d;
            d = a && b;
            e = !a;
            Return str;
        }
        Function main(){
            Let a[1];
            If (True){ Return a;}
            Else{ Return b;}
        }"""
        expect = "Program([FuncDecl(Id(c)[],[Assign(Id(s),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d)))),Assign(Id(d),BinaryOp(&&,Id(a),Id(b))),Assign(Id(e),UnaryOp(!,Id(a))),Return(Id(str))]),FuncDecl(Id(main)[],[VarDecl(Id(a),[NumberLiteral(1.0)],NoneType),If(BooleanLiteral(false),[Return(Id(a))])Else([Return(Id(b))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_more_complex_program_49(self):
        """More complex program"""
        input = """Function foo(  c[]){
            If (a==c){
                If (d==f){
                    If(lv==2) {c=d;}
                    Else {c = a[cc+9];}}
                Else {a=disc/4;}}
            Else {scj=7/3;}
            Return 0;
        }"""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(c),NoneType)],[If(BinaryOp(==,Id(a),Id(c)),[If(BinaryOp(==,Id(d),Id(f)),[If(BinaryOp(==,Id(lv),NumberLiteral(2.0)),[Assign(Id(c),Id(d))])Else([Assign(Id(c),ArrayAccess(Id(a),[BinaryOp(+,Id(cc),NumberLiteral(9.0))]))])])Else([Assign(Id(a),BinaryOp(/,Id(disc),NumberLiteral(4.0)))])])Else([Assign(Id(scj),BinaryOp(/,NumberLiteral(7.0),NumberLiteral(3.0)))]),Return(NumberLiteral(0.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_more_complex_program_50(self):
        """More complex program"""
        input = """Function foo(  c[], i){
            For i In [3,5]{
                If (a==c){
                    If (d==f){
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {a=disc/4;}}
                Else {Break;}
            }
            Return a;  
        }"""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType)],[ForIn(Id(i),ArrayLiteral(NumberLiteral(3.0),NumberLiteral(5.0)),[If(BinaryOp(==,Id(a),Id(c)),[If(BinaryOp(==,Id(d),Id(f)),[If(BinaryOp(==,Id(lv),NumberLiteral(2.0)),[Continue()])Else([Assign(Id(c),ArrayAccess(Id(a),[BinaryOp(+,Id(cc),NumberLiteral(9.0))]))])])Else([Assign(Id(a),BinaryOp(/,Id(disc),NumberLiteral(4.0)))])])Else([Break()])]),Return(Id(a))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_more_complex_program_51(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In [3,5]{
                If (a==c){
                    If (d==f){
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {a=disc/4;}}
                Else {Break; a=a+3; b=a-v;}
            }
            Return a;  
        }"""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType)],[ForIn(Id(i),ArrayLiteral(NumberLiteral(3.0),NumberLiteral(5.0)),[If(BinaryOp(==,Id(a),Id(c)),[If(BinaryOp(==,Id(d),Id(f)),[If(BinaryOp(==,Id(lv),NumberLiteral(2.0)),[Continue()])Else([Assign(Id(c),ArrayAccess(Id(a),[BinaryOp(+,Id(cc),NumberLiteral(9.0))]))])])Else([Assign(Id(a),BinaryOp(/,Id(disc),NumberLiteral(4.0)))])])Else([Break(),Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(3.0))),Assign(Id(b),BinaryOp(-,Id(a),Id(v)))])]),Return(Id(a))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_more_complex_program_52(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In [3,5]{
                If (a==c){
                    If (d==f){
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {a=disc/4;}}
                Else {Break; a=a+3; b=a-v;}
            }
            Return a;  
        }"""
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType)],[ForIn(Id(i),ArrayLiteral(NumberLiteral(3.0),NumberLiteral(5.0)),[If(BinaryOp(==,Id(a),Id(c)),[If(BinaryOp(==,Id(d),Id(f)),[If(BinaryOp(==,Id(lv),NumberLiteral(2.0)),[Continue()])Else([Assign(Id(c),ArrayAccess(Id(a),[BinaryOp(+,Id(cc),NumberLiteral(9.0))]))])])Else([Assign(Id(a),BinaryOp(/,Id(disc),NumberLiteral(4.0)))])])Else([Break(),Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(3.0))),Assign(Id(b),BinaryOp(-,Id(a),Id(v)))])]),Return(Id(a))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_more_complex_program_53(self):
        """More complex program with error"""
        input = """Function main() {}"""
        expect = "Program([FuncDecl(Id(main)[],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_more_complex_program_54(self):
        """More complex program with error"""
        input = """Let number;
                    Let check[5]:String;
        """
        expect = "Program([VarDecl(Id(number),NoneType),VarDecl(Id(check),[NumberLiteral(5.0)],StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_more_complex_program_55(self):
        """More complex program with error"""
        input = """Let number;
                    Let check[3]:String=["a+b,c","der","read\\b"];
        """
        expect = "Program([VarDecl(Id(number),NoneType),VarDecl(Id(check),[NumberLiteral(3.0)],StringType,ArrayLiteral(StringLiteral(a+b,c),StringLiteral(der),StringLiteral(read\b)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_more_complex_program_56(self):
        """More complex program with error"""
        input = """Let number;
                   Let check[x+y+3];
        """
        expect = "Program([VarDecl(Id(number),NoneType),VarDecl(Id(check),[BinaryOp(+,BinaryOp(+,Id(x),Id(y)),NumberLiteral(3.0))],NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_more_complex_program_57(self):
        """More complex program with error"""
        input = """Let number;
                    Let check[3];
                    t=5;
        """
        expect = "Program([VarDecl(Id(number),NoneType),VarDecl(Id(check),[NumberLiteral(3.0)],NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_more_complex_program_58(self):
        """More complex program with error"""
        input = """Function main(){
            
            While (a!=b){
                 a=c;
                d=b;
            }
        }"""
        expect = "Program([FuncDecl(Id(main)[],[While(BinaryOp(!=,Id(a),Id(b)),[Assign(Id(a),Id(c)),Assign(Id(d),Id(b))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_more_complex_program_59(self):
        """More complex program"""
        input = """
        Function main() {
            If (a == b){
                If (c == d){
                    Call(foo,[]);}
                Else{
                    Call(foo,[]);}
            Else{
                Call(foo,[]);}
            
        }
        """
        expect = "Program([FuncDecl(Id(main)[],[If(BinaryOp(==,Id(a),Id(b)),[If(BinaryOp(==,Id(c),Id(d)),[CallStmt(Id(foo),[])])Else([CallStmt(Id(foo),[])])])Else([CallStmt(Id(foo),[])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_more_complex_program_60(self):
        """More complex program"""
        input = """Function main(){
        Let i, num;
        Let data;
       
        ## Allocates the memory for 'num' elements.##
        If(data == True)
        {
       
      Call(exit,[]);
        }
    
        ## Stores the number entered by the user.##
        For i In [1,2,3,4,5]
        {
            a=a+1;
        }
        ## Loop to store largest number at address data##
        For i In [3,5,7]
        {
            ## Change < to > if you want to find the smallest number##
            If(data < (data + i)){
            data = (data + i);}
        }
       
        Return 0;
        }
        """
        expect = "Program([FuncDecl(Id(main)[],[VarDecl(Id(i),NoneType),VarDecl(Id(num),NoneType),VarDecl(Id(data),NoneType),If(BinaryOp(==,Id(data),BooleanLiteral(false)),[CallStmt(Id(exit),[])]),ForIn(Id(i),ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0),NumberLiteral(5.0)),[Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(1.0)))]),ForIn(Id(i),ArrayLiteral(NumberLiteral(3.0),NumberLiteral(5.0),NumberLiteral(7.0)),[If(BinaryOp(<,Id(data),BinaryOp(+,Id(data),Id(i))),[Assign(Id(data),BinaryOp(+,Id(data),Id(i)))])]),Return(NumberLiteral(0.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_more_complex_program_61(self):
        """More complex program with error"""
        input = """
        Function mainarg()
        {
            For a In r{
                a=a+4;
            }
        }
        """
        expect = "Program([FuncDecl(Id(mainarg)[],[ForIn(Id(a),Id(r),[Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(4.0)))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,361))        

    def test_more_complex_program_62(self):
        """More complex program with error"""
        input = """Function main()
        {
            Let i;
            i = 0;
            While(i==1)
            {
                a=a+3;
            }
            b=c;
        }
        """
        expect = "Program([FuncDecl(Id(main)[],[VarDecl(Id(i),NoneType),Assign(Id(i),NumberLiteral(0.0)),While(BinaryOp(==,Id(i),NumberLiteral(1.0)),[Assign(Id(a),BinaryOp(+,Id(a),NumberLiteral(3.0)))]),Assign(Id(b),Id(c))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_more_complex_program_63(self):
        """More complex program with error"""
        input = """Function main() {
            Let year;
           
            If ( year%400 == 0){
                Call(print,[year]);}
            Elif ( year%100 == 0){
                 Call(print,[year]);}
            If ( year%4 == 0 ){
                 Call(print,[year]);}
            Else{
                Call(print,[year]);} 
            Return 0;
            }
        """
        expect = "Program([FuncDecl(Id(main)[],[VarDecl(Id(year),NoneType),If(BinaryOp(==,BinaryOp(%,Id(year),NumberLiteral(400.0)),NumberLiteral(0.0)),[CallStmt(Id(print),[Id(year)])])ElseIf(BinaryOp(==,BinaryOp(%,Id(year),NumberLiteral(100.0)),NumberLiteral(0.0)),[CallStmt(Id(print),[Id(year)])]),If(BinaryOp(==,BinaryOp(%,Id(year),NumberLiteral(4.0)),NumberLiteral(0.0)),[CallStmt(Id(print),[Id(year)])])Else([CallStmt(Id(print),[Id(year)])]),Return(NumberLiteral(0.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_more_complex_program_64(self):
        """More complex program with error"""
        input = """Function main(){
                While(a==b){
                    ab=c;
                }
           }
        """
        expect = "Program([FuncDecl(Id(main)[],[While(BinaryOp(==,Id(a),Id(b)),[Assign(Id(ab),Id(c))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_more_complex_program_65(self):
        """More complex program with error"""
        input = """Function main()
        {
	       Call(cllrrs,[]);
	    Let no_star, no_row, i, j;
            For i Of {
name: "Yanxi Place",
address: "Chinese Forbidden City"
}
	    {
		   a=a+v;
           }
		
			Call(print,[]);
		
	Call(print,[""]);
	    
	
        }
        """
        expect = "Program([FuncDecl(Id(main)[],[CallStmt(Id(cllrrs),[]),VarDecl(Id(no_star),NoneType),VarDecl(Id(no_row),NoneType),VarDecl(Id(i),NoneType),VarDecl(Id(j),NoneType),ForOf(Id(i),[(Id(name='name'), StringLiteral(value='Yanxi Place')), (Id(name='address'), StringLiteral(value='Chinese Forbidden City'))],[Assign(Id(a),BinaryOp(+,Id(a),Id(v)))]),CallStmt(Id(print),[]),CallStmt(Id(print),[StringLiteral()])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_more_complex_program_66(self):
        """More complex program with error"""
        input = """Let x,y;
        Let tong, hieu, tich, thuong;
        Function main(){
            tong = x + y;
            hieu= x - y;
            Let arr[5];
            tich = x * y;
            Let average;
            average = tong/2;
            Return 0;
        }
        """
        expect = "Program([VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(tong),NoneType),VarDecl(Id(hieu),NoneType),VarDecl(Id(tich),NoneType),VarDecl(Id(thuong),NoneType),FuncDecl(Id(main)[],[Assign(Id(tong),BinaryOp(+,Id(x),Id(y))),Assign(Id(hieu),BinaryOp(-,Id(x),Id(y))),VarDecl(Id(arr),[NumberLiteral(5.0)],NoneType),Assign(Id(tich),BinaryOp(*,Id(x),Id(y))),VarDecl(Id(average),NoneType),Assign(Id(average),BinaryOp(/,Id(tong),NumberLiteral(2.0))),Return(NumberLiteral(0.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_more_complex_program_67(self):
        """More complex program with error"""
        input = """Function operator( num){   
            Let x;
            x = 12;
            Let y;
            y = 5;
            Let tong, hieu, tich, thuong;
            tong = x + y;
            hieu= x - y;
            tich = x * y;
        }
  
        Function compute( x, y, tong[]){
            Call(operate,[10]);
            Return tong;
        }
        """
        expect = "Program([FuncDecl(Id(operator)[VarDecl(Id(num),NoneType)],[VarDecl(Id(x),NoneType),Assign(Id(x),NumberLiteral(12.0)),VarDecl(Id(y),NoneType),Assign(Id(y),NumberLiteral(5.0)),VarDecl(Id(tong),NoneType),VarDecl(Id(hieu),NoneType),VarDecl(Id(tich),NoneType),VarDecl(Id(thuong),NoneType),Assign(Id(tong),BinaryOp(+,Id(x),Id(y))),Assign(Id(hieu),BinaryOp(-,Id(x),Id(y))),Assign(Id(tich),BinaryOp(*,Id(x),Id(y)))]),FuncDecl(Id(compute)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(tong),NoneType)],[CallStmt(Id(operate),[NumberLiteral(10.0)]),Return(Id(tong))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_more_complex_program_68(self):
        """More complex program with error"""
        input = """Let arr[10];
        Function print( arr[]){}
        Function compute( x, y, tong[]){
            For i In a{
                arr[i]=True;
                Call(print,[arr]);
            }
        }
        """
        expect = "Program([VarDecl(Id(arr),[NumberLiteral(10.0)],NoneType),FuncDecl(Id(print)[VarDecl(Id(arr),NoneType)],[]),FuncDecl(Id(compute)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType),VarDecl(Id(tong),NoneType)],[ForIn(Id(i),Id(a),[Assign(ArrayAccess(Id(arr),[Id(i)]),BooleanLiteral(false)),CallStmt(Id(print),[Id(arr)])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_more_complex_program_69(self):
        """More complex program with error"""
        input = """Let a;
        Function plusFuncInt( x,  y) {
            Constant $sum="abc";
            sum = x*567 + y/1234;
            Return sum-45673;
        }
        Function plusFuncDouble( x,  y) {
            If(x>=y){
                Return x;}
            Else{
                Return y;}
        }       
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(plusFuncInt)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[ConstDecl(Id($sum),NoneType,StringLiteral(abc)),Assign(Id(sum),BinaryOp(+,BinaryOp(*,Id(x),NumberLiteral(567.0)),BinaryOp(/,Id(y),NumberLiteral(1234.0)))),Return(BinaryOp(-,Id(sum),NumberLiteral(45673.0)))]),FuncDecl(Id(plusFuncDouble)[VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)],[If(BinaryOp(>=,Id(x),Id(y)),[Return(Id(x))])Else([Return(Id(y))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_more_complex_program_70(self):
        """More complex program with error"""
        input = """Function main( ){ Call(foo,[2,4]);}
        """
        expect = "Program([FuncDecl(Id(main)[],[CallStmt(Id(foo),[NumberLiteral(2.0),NumberLiteral(4.0)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_more_complex_program_71(self):
        """More complex program with error"""
        input = """Function main( ){
            While(x>=9){
            i=0;
            i=count/12;
            Call(goo,[3,arr[10]]);
        }
        }
        
        """
        expect = "Program([FuncDecl(Id(main)[],[While(BinaryOp(>=,Id(x),NumberLiteral(9.0)),[Assign(Id(i),NumberLiteral(0.0)),Assign(Id(i),BinaryOp(/,Id(count),NumberLiteral(12.0))),CallStmt(Id(goo),[NumberLiteral(3.0),ArrayAccess(Id(arr),[NumberLiteral(10.0)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_more_complex_program_72(self):
        """More complex program with error"""
        input = """{}
        """
        expect = "Program([])"
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_more_complex_program_73(self):
        """More complex program with error"""
        input = """Let a;
                    Let a=2;
        """
        expect = "Program([VarDecl(Id(a),NoneType),VarDecl(Id(a),NoneType,NumberLiteral(2.0))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_more_complex_program_74(self):
        """More complex program with error"""
        input = """Let int;
        Let num;
        Function count( a, b){}
        """
        expect = "Program([VarDecl(Id(int),NoneType),VarDecl(Id(num),NoneType),FuncDecl(Id(count)[VarDecl(Id(a),NoneType),VarDecl(Id(b),NoneType)],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_more_complex_program_75(self):
        """More complex program with error"""
        input = """
        Function main( ){ If (a){ If (b){ If (c){ a=b;} Else {}} Else{} }}
        """
        expect = "Program([FuncDecl(Id(main)[],[If(Id(a),[If(Id(b),[If(Id(c),[Assign(Id(a),Id(b))])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_more_complex_program_76(self):
        """More complex program with error"""
        input = """
        Function main( ){ If (b){} If (c){} Else {} }
        """
        expect = "Program([FuncDecl(Id(main)[],[If(Id(b),[]),If(Id(c),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_more_complex_program_77(self):
        """More complex program with error"""
        input = """
        Function main() {check = 1 + 2 - 3 * 4  == 5 ;}
        """
        expect = "Program([FuncDecl(Id(main)[],[Assign(Id(check),BinaryOp(==,BinaryOp(-,BinaryOp(+,NumberLiteral(1.0),NumberLiteral(2.0)),BinaryOp(*,NumberLiteral(3.0),NumberLiteral(4.0))),NumberLiteral(5.0)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_more_complex_program_78(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In a{
                If (a==c){
                    If (d==f){
                        If(lv==2) {Continue;}
                        Else{ c = a[cc+9];}
                        }
                    Else {a=disc/4;}
                    }
                Else {Break;}
            }
            Return a;  
        }
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(c),NoneType),VarDecl(Id(i),NoneType)],[ForIn(Id(i),Id(a),[If(BinaryOp(==,Id(a),Id(c)),[If(BinaryOp(==,Id(d),Id(f)),[If(BinaryOp(==,Id(lv),NumberLiteral(2.0)),[Continue()])Else([Assign(Id(c),ArrayAccess(Id(a),[BinaryOp(+,Id(cc),NumberLiteral(9.0))]))])])Else([Assign(Id(a),BinaryOp(/,Id(disc),NumberLiteral(4.0)))])])Else([Break()])]),Return(Id(a))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_more_complex_program_79(self):
        """More complex program with error"""
        input = """Function main(){
            a = b + c + d;
            Call(arr,[]);
            a = a / Call(sub,[a,b]);
        }
        """
        expect = "Program([FuncDecl(Id(main)[],[Assign(Id(a),BinaryOp(+,BinaryOp(+,Id(b),Id(c)),Id(d))),CallStmt(Id(arr),[]),Assign(Id(a),BinaryOp(/,Id(a),CallExpr(Id(sub),[Id(a),Id(b)])))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_more_complex_program_80(self):
        """More complex program with error"""
        input = """Let a;
        Function main(){}
        Let z;
        """
        expect = "Program([VarDecl(Id(a),NoneType),FuncDecl(Id(main)[],[]),VarDecl(Id(z),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    