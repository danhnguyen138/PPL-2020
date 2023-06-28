##NGuyen Quang Cong Danh -1610392

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_constant_202(self):
        """Miss variable"""
        input = """Constant $a = 10 ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Constant $a = 10;
                Function foo(a[5], b) {
                        Constant $b: String = "Story of Yanxi Place";
                        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_wrong_decleare(self):
        """Miss variable"""
        input = """Let ;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_decleare_1(self):
        """Simple program: int main() {} """
        input = """Let a[5]: Number = [1, 2, 3, 4, 5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_wrong_decleare_2(self):
        """Miss variable"""
        input = """Let b[2, 3] = [[1, 2, 3], [4, 5, 6]] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_declare_1(self):

        input = """Let a = {
                name: "Yanxi Place",
                address: "Chinese Forbidden City",
                surface: 10.2,
                people: ["a","b","c"]
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    
    def test_declare_2(self):
    
        input = """Let b[2, 3] = [[1, 2, 3], [4, 5, 6]], b: Number ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_declare_3(self):
       
        input = """Let r = 10, v;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_declare_4(self):
        """Miss variable"""
        input = """Constant $b: String = "Story of Yanxi Place";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_declare_5(self):
        """Simple program: int main() {} """
        input = """Let x,y,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_simple_program_3(self):
        """Simple program: int main() {} """
        input = """Constant $a = 10;
Function foo(a[5], b) {

a[2] = Call(foo, [2]) + Call(foo, [Call(bar, [2, 3])]);

Return $b + ": Done";
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_simple_program_05(self):
        """ Simple program """
        input = """Let number;
                    Let check;
                    Let arr[4],num,brr[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))  

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))                

    def test_more_complex_program_24(self):
        """More complex program"""
        input = """
        Function print(boolean arr[]){}
        Function test_prog(){
            Let arr[10]:Boolean;
            Call(print,[arr]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))        
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))                

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_more_complex_program_31(self):
        """More complex program"""
        input = """
        Function main(){
            Call(foo,[2])[3+x] = a[b[2]] + 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))        

    def test_more_complex_program_32(self):
        """More complex program"""
        input = """
        Function c(){
            3[3+x] = True[b[2]] +3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))        

    def test_more_complex_program_33(self):
        """More complex program"""
        input = """
        Function c(){
            Let arr[3];
            crr[3+x-y*342]=10;
            Call(dr,[2,4])[3+x-y*342]=23;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))                

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))        

    def test_more_complex_program_38(self):
        """More complex program"""
        input = """Function main(){ If (a){} 
        Elif (b){}
        Elif (c)
        { For i In a { Call(foo,[2,4]);}} 
        Else {} 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_more_complex_program_39(self):
        """More complex program"""
        input = """Function main( ){ If (a){ If (b){ If (c){ Let a;} Else {}} Else{}}}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_more_complex_program_40(self):
        """More complex program"""
        input = """Function main() {
            d=(a+b)+(c+d);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_more_complex_program_41(self):
        """More complex program"""
        input = """Function main () {
            Call(putItrln,[2]);
            Call(put,[2])[4]=5;
            (Call(put,[3]))[5]=10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_more_complex_program_42(self):
        """More complex program"""
        input = """Function main( ){ 
            While (x>=9){
                i=0;
                i=count/12;
                Call(arr,[3,arr[4]]);
            }
         }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_more_complex_program_43(self):
        """More complex program"""
        input = """Function main( ){
        Let i,count;
        i=count/12;
        Call(goo, [3,arr[4]]);
        a=a && 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_more_complex_program_45(self):
        """More complex program"""
        input = """Function main( ){ 
            Call(foo,[3])[3+x] = a[b[2]] +3;
           Call(goo,[2])[x+3] = a[b[2+z]] + t;
   
            a=100;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_more_complex_program_46(self):
        """More complex program"""
        input = """Function main() { If(i>1) {} Else {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

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
                Else{}
            }
            Return a;  
        }"""
        expect = "Error on line 9 col 16: Else"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_more_complex_program_53(self):
        """More complex program with error"""
        input = """Function main() {"""
        expect = "Error on line 1 col 17: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_more_complex_program_54(self):
        """More complex program with error"""
        input = """Let number;
                    Let check[5]:String;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_more_complex_program_55(self):
        """More complex program with error"""
        input = """Let number;
                    Let check[]:String=["a+b,c","der","read\\b"];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_more_complex_program_56(self):
        """More complex program with error"""
        input = """Let number;
                   Let check[x+y+3];
        """
        expect = "Error on line 2 col 29: x"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_more_complex_program_57(self):
        """More complex program with error"""
        input = """Let number;
                    Let check[3];
                    t=5;
        """
        expect = "Error on line 3 col 20: t"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_more_complex_program_58(self):
        """More complex program with error"""
        input = """Function main(){
            
            While (a!=b){
                 a=c;
                d=b;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_more_complex_program_59(self):
        """More complex program"""
        input = """
        Function main() {
            If (a == b){
                If (c == d){
                    Call(foo,[]);}
                Else{
                    Call(foo,[]);}}
            Else{
                Call(foo,[]);}
            Else {
                //comment
            }
        }
        """
        expect = "Error on line 10 col 12: Else"
        self.assertTrue(TestParser.checkParser(input,expect,259))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))        

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_more_complex_program_64(self):
        """More complex program with error"""
        input = """Function main(){
                While(a==b){
                    ab=c;
                }
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_more_complex_program_66(self):
        """More complex program with error"""
        input = """Let x,y;
        Let tong, hieu, tich, thuong;
        Function main(){
            tong = x + y;
            hieu= x - y;
            Let arr[];
            tich = x * y;
            Let average;
            average = tong/2;
            Return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_more_complex_program_70(self):
        """More complex program with error"""
        input = """Function main( ){ Call(foo,[2,4]);}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_more_complex_program_72(self):
        """More complex program with error"""
        input = """{}
        """
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_more_complex_program_73(self):
        """More complex program with error"""
        input = """Let a;
                    Let a=2;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_more_complex_program_74(self):
        """More complex program with error"""
        input = """Let int;
        Let num;
        Function count( a, b){};
        """
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_more_complex_program_75(self):
        """More complex program with error"""
        input = """
        Function main( ){ If (a){ If (b){ If (c){ a=b;} Else {}} Else{} }}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_more_complex_program_76(self):
        """More complex program with error"""
        input = """
        Function main( ){ If If (b){} If (c){} Else {} else {}}
        """
        expect = "Error on line 2 col 29: If"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_more_complex_program_77(self):
        """More complex program with error"""
        input = """
        Function main() {check = 1 + 2 - 3 * 4  == 5 != 6;}
        """
        expect = "Error on line 2 col 53: !="
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_more_complex_program_78(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For For i In a{
                if (a==c)
                    if (d=f)
                        if(lv=2) continue;
                        else c = a[cc+9];
                    else disc/4;
                else break;
            }
            return a;  
        }
        """
        expect = "Error on line 2 col 16: For"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_more_complex_program_79(self):
        """More complex program with error"""
        input = """Function main(){
            a = b + c + d;
            Call(arr,[]);
            a = a / Call(sub,[a,b]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_more_complex_program_80(self):
        """More complex program with error"""
        input = """Let a;
        Function main(){}
        Let z;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_more_complex_program_81(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In [2,4]{
                If (a==c){
                    If (d==f){
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {disc=4;}
                }
                Else {Break;}
            }
            Return a;  
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_more_complex_program_82(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In [2,4,5]{
                If (a==c){
                    If (d==f){
                        a=b["name"];
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {disc=4;}
                }
                Else {Break;}
            }
            Return a;  
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_more_complex_program_83(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In [2,4,5]{
                If (a==c){
                    If (d==f){
                        a=b["name"];
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {disc=4;}
                }
                Else {Break;}
            } Else{}
            Return a;  
        }
        """
        expect = "Error on line 11 col 14: Else"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_more_complex_program_84(self):
        """More complex program with error"""
        input = """Function foo(  c[], i){
            For i In [2,4,5]{
                If (a==c){
                    If (d==f){
                        a=b["name"];
                        If(lv==2) {Continue;}
                        Else {c = a[cc+9];}}
                    Else {disc=4;}
                }
                Else {Break;}
            } 
            Return a;  
        }
        Function main( ){
            While(x>=9){
            i=0;
            i=count/12;
            Call(goo,[3,arr[10]]);
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_more_complex_program_85(self):
        """More complex program with error"""
        input = """Function main(){
        Let arr[x+2];
        Return 0;
        }
        """
        expect = "Error on line 2 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_more_complex_program_86(self):
        """More complex program with error"""
        input = """Function main( argc,  srrgv[]){
        Let boolean;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_more_complex_program_87(self):
        """More complex program with error"""
        input = """Let a;
        Function plusFuncInt( x,  y) {
            Let sum;
            For i In a{
                If(x==5){
                    Break;}
            }
            Returns x;
        }       
        """
        expect = "Error on line 8 col 20: x"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_more_complex_program_88(self):
        """More complex program with error"""
        input = """Let a;
        Function break( x,  y) {
            Let sum;
           For i Of{ a: "a,bc"}{
                If(x==5){
                    Break;}
            }
            Return x;
        }       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_more_complex_program_89(self):
        """More complex program with error"""
        input = """Function main( arg[])
        {
            While (a!=b){

            }
            
           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_more_complex_program_90(self):
        """More complex program with error"""
        input = """
        Function main(){
            Let i;
            i=0;
            For i In a{
                Call(print,[]);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_more_complex_program_91(self):
        """More complex program with error"""
        input = """Function main(  argc ,  argv[] )
        {
            Let c ;
            Let i ;
           For i In [1,2,3,4,5,6]{
                Let d ;
                d = i + 3 ;
                If(d>5)
                    {Call(putInt,[3]);}
            }
            Call(print,[d]);
            Return i ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_more_complex_program_92(self):
        """More complex program with error"""
        input = """Function main(  argc ,  argv[] )
        {
            Let c[2+3+4] ;
            Let i ;
            For i In n {
                Let d ;
                d = i + 3 ;
                putInt(d) ;
            }
            print(d);
            Return i;
        }
        """
        expect = "Error on line 3 col 19: +"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_more_complex_program_93(self):
        """More complex program with error"""
        input = """Function main(  argc ,  argv[] )
        {
            Let c ;
            Let i ;
            For i In n{
                Let d=3 ;
                i=d- 3 ;
                Call(putInt,[d] ) ;
            }
            Call(print,[d]);
            Return i ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_more_complex_program_94(self):
        """More complex program with error"""
        input = """Function main(  argc ,  argv[] )
        {
            Let c ;
            Let i ;
            For i In n{
                Let d=3 ;
                i=d- 3 ;
                Call(putInt,[d] ) ;
            }
            Call(print,[d]);
            Return i ;
            5;
        }
        """
        expect = "Error on line 12 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_more_complex_program_95(self):
        """More complex program with error"""
        input = """Function main(  argc ,  argv[] )
        {
            Let c ;
            Let i ;
            For i In n{
                Let d=3 ;
                i=d- 3 ;
                Call(putInt,[d] ) ;
            }
            c+d;
            Call(print,[d]);
            Return i ;
        }
        """
        expect = "Error on line 10 col 13: +"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_more_complex_program_96(self):
        """More complex program with error"""
        input = """Function main(){
            foo["name"] = a[b[2]] + 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_more_complex_program_97(self):
        """More complex program with error"""
        input = """
        Let i;
        If(i>=3){
            a+b=c;
        }
        """
        expect = "Error on line 3 col 8: If"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_more_complex_program_98(self):
        """More complex program with error"""
        input = """Function main( arg[])
        {
            For i In n{}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_more_complex_program_99(self):
        """More complex program with error"""
        input = """Function main( arg[])
        {
            For i In {}
        }
        """
        expect = "Error on line 3 col 21: {"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_more_complex_program_100(self):
        """More complex program with error"""
        input = """Function main(){
            Let a+b;
            a = int + 1;
        };
        """
        expect = "Error on line 2 col 17: +"
        self.assertTrue(TestParser.checkParser(input,expect,300))

