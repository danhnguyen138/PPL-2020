#Nguyen Quang Cong Danh - 1610392
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        """Simple program: main"""
        input = """Function hello() {
            Let a;
        }
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """
            Let c=3;
            Function main() {
            Let a=c;
        }
        
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redecl(self):
        """More complex program"""
        input = """
        Let a,a;
        
        Function main() {
            
        }

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = """
        Let a;
        
        Function main(a,b) {
            Let b;
        }

        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = """
            Let a;
        
            Function main(a,b,a[10]) {
                Let b;
        }

        """
        expect ="Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a) {
                Let b=$a;
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_assign(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a) {
                Let b=$a;
                Let c=True;
                c=b;
        }

        """
        expect = "Type Mismatch In Statement: Assign(Id(c),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_assign1(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a) {
                Let b;
                Let c=True;
                c=b;
                a=c;
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_assign2(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a,b[10]) {
                b[1]=2;
                Let c=10;
                c=a;
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    def test_assign3(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a,b) {
                b{"name"}=2;
                Let c=10;
                c=a;
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_assign4(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a,b[10]) {
                Let d={
                    name:3
                }
                Let e;
                Let c=10;
                c=a+b[1]+d{"name"}+e;
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_assign5(self):
        """Complex program"""
        input = """
            Constant $a=4;
        
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+d{"name"}+e;
        }

        """
        expect = "Undeclared Variable: d"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_CallExpr(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a;
            Let b;
            Function add(c,d){
                Return c+d;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_CallExpr1(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a;
            Let b;
            Function add(c,d){
             
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
        }

        """
        expect = "Type Cannot Be Inferred: CallExpr(Id(add),[NumberLiteral(3.0),NumberLiteral(4.0)])"
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_CallExpr2(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a;
            Let b;
            Function add(c,d){
                c=10;
                d=c;
                Return;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Call(add,[2,3]);
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_CallExpr3(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a;
            Let b;
            Function add(c,d){
                c=10;
                d=c;
              
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                Call(add,[2]);
        }

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(add),[NumberLiteral(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test_CallExpr4(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a;
            Let b;
            Function add(c,d){
                c=10;
                d=c;
              
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_CallExpr5(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
              
            }
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test_CallExpr6(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
              
            }
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test_CallExpr7(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
              
            }
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Let d="String";
            d=Call(add,[3,4]);
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                
          
        }

        """
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),ArrayAccess(Id(b),[NumberLiteral(1.0)])),Id(e)),CallExpr(Id(add),[NumberLiteral(3.0),NumberLiteral(4.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test_redecl_func(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
              
            }
            Function add(a,b){

            }
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Let d="String";
            d=Call(add,[3,4]);
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                
          
        }

        """
        expect = "Redeclared Function: add"
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test_check_func_type(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
                d=Call(add,[c,d]);
                Return ;
              
            }
          
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Let d="String";
            d=Call(add,[3,4]);
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                
          
        }

        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test_check_func_type1(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
                c=$c;
                d=Call(add,[c,d]);
                Return ;
              
            }
          
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Let d="String";
            d=Call(add,[3,4]);
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                
          
        }

        """
        expect = "Undeclared Constant: $c"
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_check_if(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
                d=Call(add,[c,d]);
              
            }
          
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Let d="String";
            d=Call(add,[3,4])+$k;
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                For x In [[1,2,3],[2,3,4]]{
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Undeclared Constant: $k"
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_check_if_2(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function add(c,d){
                c=a;
                d=c;
                d=Call(add,[c,d]);
              
            }
          
            Function plusFuncInt( x,  y) {
            Let sum;
            sum = x*567 + y/1234;
            Let d="String";
            d=Call(add,[3,4]);
            Return sum-45673;
        }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e+Call(add,[3,4]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                For x In d {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: Assign(Id(d),CallExpr(Id(add),[NumberLiteral(3.0),NumberLiteral(4.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_check_For_Off(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of json {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_check_For_Off2(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of {
                    name:"string1",
                    age:3
                } {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test_check_For_Off3(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of d {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: ForOf(Id(x),Id(d),[If(BinaryOp(==,Id(x),NumberLiteral(5.0)),[Break()])])"
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_check_For_Off4(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of e {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: ForOf(Id(x),Id(e),[If(BinaryOp(==,Id(x),NumberLiteral(5.0)),[Break()])])"
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_check_For_In(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x In e {
                    If(a==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: ForIn(Id(x),Id(e),[If(BinaryOp(==,Id(a),NumberLiteral(5.0)),[Break()])])"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_check_For_In2(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x In [3,6] {
                    If(a==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_check_If(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                }
                
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_check_If2(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                } Elif (c==5){
                    addSum= json{"age"};
                }Else{
                    addSum= c;
                }
                
          
        }

        """
        expect = "Undeclared Variable: addSum"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_check_If3(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           Function add(a,b){
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                   If (a==3){
                       addSum=a+3+d[5];
                   }
                } Elif (c==5){
                  
                }Else{
       
                }
                Let add=Call(add,[4,5]);
                
          
        }
            

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_check_Function(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a="Hello world";
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=Call(divide,[5,10]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of d {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: ForOf(Id(x),Id(d),[If(BinaryOp(==,Id(x),NumberLiteral(5.0)),[Break()])])"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_check_Function2(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function add(a,b){
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+Call(divide,[3,4]);
                Call(add,[3,6]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of e {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(add),[NumberLiteral(3.0),NumberLiteral(6.0)])"
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_check_Function3(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function add(a,b){
                Let a;
                Let b;
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x In e {
                    If(a==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_check_Function4(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b,b[20]){
                Return a/b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x In [3,6] {
                    If(a==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_check_Function5(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
             Function divide(a,b){
                Return a/b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Call(divide,[4,5]);
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(divide),[NumberLiteral(4.0),NumberLiteral(5.0)])"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_check_Function6(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function add(a,b){
               
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+Call(add,[5,6])+Call(divide,[5,10]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                } Elif (c==5){
                    addSum= json{"age"};
                }Else{
                    addSum= c;
                }
                
          
        }

        """
        expect = "Undeclared Variable: addSum"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_check_If3(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           Function add(a,b){
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                   If (a==3){
                       addSum=a+3+d[5];
                   }
                } Elif (c==5){
                  
                }Else{
       
                }
                Let addSum=Call(add,[4,5]);
                addSum="Hello world";
                
          
        }
            

        """
        expect = "Type Mismatch In Statement: Assign(Id(addSum),StringLiteral(Hello world))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_more_complex_program_42(self):
        """More complex program"""
        input = """
        Function arr(a,b[10]){
            a=10;
            Let c[3]:Number=[3,4,6];
            c[1]=b[3];
            Return;
        }
        Function main( ){ 
            Let x=3;
            While (x>=9){
                Let i,count;
                i=0;
                i=count/12;
                Let d[3]:Number=[1,2,3]
                Call(arr,[3,d]);
            }
         }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_more_complex_program_43(self):
        """More complex program"""
        input = """Function main( ){
        Let i,count;
        i=count/12;
        Call(goo, [3,arr[4]]);
        a=a && 1;
        }"""
        expect = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_more_complex_program_44(self):
        """More complex program"""
        input = """
        Function arr(a,b[10]){
            a=10;
            Let c[3]:Number=[3,4,6];
            c[1]=b[3];
            Return;
        }
        Function main( ){ 
            Let x=3;
            While (x>=9){
                Let i,count;
                i=0;
                i=count/12;
                Let d[3]:Number=[1,2,3]
                Call(arr,[3,d[2]]);
            }
         }"""
        expect = "Type Mismatch In Statement: CallStmt(Id(arr),[NumberLiteral(3.0),ArrayAccess(Id(d),[NumberLiteral(2.0)])])"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_check_If4(self):
        """Complex program"""
        input = """
            Constant $a=4,$k=13;
            Let a=10;
            Let b;
           
            Function main(a,b[10]) {
                
                Let e=$k;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                   Let divide=json{"name"};
                   divide=addSum;
                }
                
          
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_check_If5(self):
        """Complex program"""
        input = """
            Constant $a=4, $k=12;
            Let a=10;
            Let b=a;
           
            Function main(a,b[10]) {
                
                Let e=$k;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                   For a In [1,2,3]{
                       For c Of json {

                       }
                   }
                } Elif (c==5){
                    addSum= json{"age"};
                }Else{
                    addSum= c;
                }
                
          
        }

        """
        expect = "Undeclared Variable: addSum"
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_check_If6(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
           Function add(a,b){
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                   If (a==3){
                       addSum=a+3+d[5];
                   }
                } Elif (c==5){
                    Let addSum=d[3]+4; 
                   If (a==3){
                       addSum=a+3+d[5];
                   }
                }Else{
                    Let add1=Call(add,[4,5]);
                }
                Let add=Call(add,[4,5]);
                
          
        }
            

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_check_Function7(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a="Hello world";
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=Call(divide,[5,10]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of d {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: ForOf(Id(x),Id(d),[If(BinaryOp(==,Id(x),NumberLiteral(5.0)),[Break()])])"
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_check_Function8(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function add(a,b){
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+Call(divide,[3,4]);
                Call(add,[3,6]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x Of e {
                    If(x==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(add),[NumberLiteral(3.0),NumberLiteral(6.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_check_Function9(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function add(a,b){
                Let a;
                Let b;
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x In e {
                    If(a==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_check_Function10(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b,b[20]){
                Return a/b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                For x In [3,6] {
                    If(a==5){
                    Break;
                }
                }
                
          
        }

        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_check_Function11(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
             Function divide(a,b){
                Return a/b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+e;
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Call(divide,[4,5]);
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                }
                
          
        }

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(divide),[NumberLiteral(4.0),NumberLiteral(5.0)])"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_check_Function12(self):
        """Complex program"""
        input = """
            Constant $a=4;
            Let a=10;
            Let b;
            Function divide(a,b){
                Return a/b;
            }
            Function add(a,b){
               
                Return a+b;
            }
            Function main(a,b[10]) {
                
                Let e;
                Let c=10;
                c=a+b[1]+Call(add,[5,6])+Call(divide,[5,10]);
                Let d[3,3]=[[1,2,3],[2,3,4]];
                Let json={
                    name:"string1",
                    age:3
                };
                Let isTrue= True;
                If (isTrue) {
                   Let addSum=d[3]+4; 
                } Elif (c==5){
                    addSum= json{"age"};
                }Else{
                    addSum= c;
                }
                
          
        }

        """
        expect = "Undeclared Variable: addSum"
        self.assertTrue(TestChecker.test(input, expect, 452))

   