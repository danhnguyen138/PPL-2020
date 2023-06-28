#Nguyen Quang Cong Danh - 1610392

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("vA","abc,<EOF>",101))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("$_rrt","Let,<EOF>",102))

    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("12.3e-30","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","Let,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""""This is a string containing tab \\h asc"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def "  ""","""<EOF>""",107))
    # def test_id_with_double_dollar(self):
    #     """Test Id with double dollar1"""
    #     self.assertTrue(TestLexer.checkLexeme("$$", "$,$,<EOF>", 115))

    # def test_string_with_backslash(self):
    #     """Test string with backslash esc"""
    #     self.assertTrue(TestLexer.checkLexeme("\"I am \\ \"", "I am \\ ,<EOF>", 146))


    # def test_string_with_carriage_return(self):
    #     """Test string with carriage return"""
    #     self.assertTrue(TestLexer.checkLexeme("\"I am \r abc\"", """I am \r""", 150))

    # def test_string_with_error_quote(self):
    #     """Test string with error quote"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "He said me: '"I am a teacher " """,
    #                                           """Error Token \"""", 153))

    # def test_number_with_double_e(self):
    #     """Test number with double e"""
    #     self.assertTrue(TestLexer.checkLexeme("-12.0ee3", "-12.0,ee3,<EOF>", 163))

    # def test_number_with_double_eE(self):
    #     """Test number with double eE"""
    #     self.assertTrue(TestLexer.checkLexeme("12.0eE+3", "12.0,eE,+,3,<EOF>", 164))

    # def test_number_with_error_sign(self):
    #     """Test number with error sign"""
    #     self.assertTrue(TestLexer.checkLexeme("*12.0", "*,12.0,<EOF>", 165))

    # def test_number_with_double_sign(self):
    #     """Test number with double sign"""
    #     self.assertTrue(TestLexer.checkLexeme("12.03e++3", "12.03,Error Token e", 166))

    # def test_number_with_sign_at_the_end(self):
    #     """Test number with sign at the end"""
    #     self.assertTrue(TestLexer.checkLexeme("12.0++", "12.0,+,+,<EOF>", 167))

    # def test_number_with_double_sign_first(self):
    #     """Test number with double at first"""
    #     self.assertTrue(TestLexer.checkLexeme("++12.0", "+,+,12.0,<EOF>", 168))

    # def test_id_with_sign_at_first(self):
    #     """Test id with sign at first"""
    #     self.assertTrue(TestLexer.checkLexeme("++aaa", "+,+,aaa,<EOF>", 169))

    # def test_id_with_sign_at_around(self):
    #     """Test id with sign at around"""
    #     self.assertTrue(TestLexer.checkLexeme("aa+++bb", "aa,+,+,+,bb,<EOF>", 170))


    def test_WS_n(self):
        """Test WS with \n"""
        self.assertTrue(TestLexer.checkLexeme("""\n""", "<EOF>", 101))

    def test_WS_t(self):
        """Test WS with \t"""
        self.assertTrue(TestLexer.checkLexeme("""\t""", "<EOF>", 102))

    def test_WS_f(self):
        """Test WS with \f"""
        self.assertTrue(TestLexer.checkLexeme("""\f""", "<EOF>", 103))

    def test_WS_r(self):
        """Test WS with \r"""
        self.assertTrue(TestLexer.checkLexeme("""\r""", "<EOF>", 104))

    def test_comment_one_line(self):
        """Test Comment ON ONE LINE"""
        self.assertTrue(TestLexer.checkLexeme("""### Check Comment. ##""", "<EOF>", 105))

    def test_comment_multi_line(self):
        """Test Comment ON MULTI LINE"""
        self.assertTrue(TestLexer.checkLexeme("""### Check Comment. \n# Test 1 \n# Test 2 \n##""", "<EOF>", 106))

    def test_comment_multi_line_complex(self):
        """Test Comment ON MULTI LINE WITH ERROR"""
        self.assertTrue(TestLexer.checkLexeme(
            """### Check Comment.\nTest 1 \n# Test 2 \n##""", "<EOF>", 107))

    def test_comment_one_line_error(self):
        """Test one line error : not ## at end"""
        self.assertTrue(TestLexer.checkLexeme("""## Test one line ERROR""", "Unterminated Comment", 108))

    def test_comment_one_line_error2(self):
        """Test one line error : Only # at first line"""
        self.assertTrue(TestLexer.checkLexeme("""# Test one line ERROR ##""", "Error Token #", 109))

    def test_id_sample(self):
        """Test ID sample"""
        self.assertTrue(TestLexer.checkLexeme("variable", "variable,<EOF>", 110))

    def test_id_low_up_letter(self):
        """Test ID with lower letter and upper letter"""
        self.assertTrue(TestLexer.checkLexeme("vAriable", "vAriable,<EOF>", 111))

    def test_id_low_dollar(self):
        """Test Id with dollar and lower letter"""
        self.assertTrue(TestLexer.checkLexeme("$test", "$test,<EOF>", 112))

    def test_id_dollar_up_letter(self):
        """Test Id with dollar and upper letter"""
        self.assertTrue(TestLexer.checkLexeme("$Test", "$Test,<EOF>", 113))

    def test_id_up_letter_first(self):
        """Test Id with upper letter fist"""
        self.assertTrue(TestLexer.checkLexeme("T$est", "Error Token T", 114))

    def test_id_with_double_dollar(self):
        """Test Id with double dollar"""
        self.assertTrue(TestLexer.checkLexeme("$$", "$,$,<EOF>", 115))

    def test_id_with_dollar_up_letter(self):
        """Test Id with dollar and upper letter"""
        self.assertTrue(TestLexer.checkLexeme("$ABC", "$ABC,<EOF>", 116))

    def test_id_with_double_dollar_first_final(self):
        """Test Id with double dollar at first and final"""
        self.assertTrue(TestLexer.checkLexeme("$abc$", "$abc,$,<EOF>", 117))

    def test_id_with_number_at_first(self):
        """Test Id with number at first"""
        self.assertTrue(TestLexer.checkLexeme("1abc", "1,abc,<EOF>", 118))

    def test_id_with_full_low_letter(self):
        """Test Id with full lower letter"""
        self.assertTrue(TestLexer.checkLexeme("abcbcbc", "abcbcbc,<EOF>", 119))

    def test_id_with_full_dollar(self):
        """Test Id with full dollar"""
        self.assertTrue(TestLexer.checkLexeme("$$$$$", "$,$,$,$,$,<EOF>", 120))

    def test_key_break(self):
        """Test keyword break"""
        self.assertTrue(TestLexer.checkLexeme("Break", "Break,<EOF>", 121))

    def test_key_break_error(self):
        """Test keyword Break error"""
        self.assertTrue(TestLexer.checkLexeme("Br_eak", "Error Token B", 122))

    def test_key_while(self):
        """Test keyword While"""
        self.assertTrue(TestLexer.checkLexeme("While.", "While,.,<EOF>", 123))

    def test_key_number(self):
        """Test keyword Number"""
        self.assertTrue(TestLexer.checkLexeme("Number 3", "Number,3,<EOF>", 124))

    def test_key_json(self):
        """Test keyword json"""
        self.assertTrue(TestLexer.checkLexeme("JSON", "JSON,<EOF>", 125))

    def test_key_json_error(self):
        """Test keyword JSON"""
        self.assertTrue(TestLexer.checkLexeme("Json", "Error Token J", 126))

    def test_key_with_add(self):
        """Test keyword with add operator"""
        self.assertTrue(TestLexer.checkLexeme("JSON+", "JSON,+,<EOF>", 127))

    def test_multi_key(self):
        """Test multi keywords"""
        self.assertTrue(TestLexer.checkLexeme("Break JSON Else", "Break,JSON,Else,<EOF>", 128))

    def test_multi_key_with_error(self):
        """Test multi key error"""
        self.assertTrue(TestLexer.checkLexeme("Break Json Else", "Break,Error Token J", 129))

    def test_key_and_id(self):
        """Test keyword with id"""
        self.assertTrue(TestLexer.checkLexeme("var = Break", "var,=,Break,<EOF>", 130))

    def test_number_decimal(self):
        """Test number with decimal simple"""
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 131))

    def test_number_decimal_diff_zero(self):
        """Test number decimal not zero"""
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>", 132))

    def test_number_decimal_with_negative(self):
        """Test number decimal with negative"""
        self.assertTrue(TestLexer.checkLexeme("-123", "-,123,<EOF>", 133))

    def test_number_decimal_with_dot(self):
        """Test number decimal with dot at the end"""
        self.assertTrue(TestLexer.checkLexeme("199.", "199.,<EOF>", 134))

    def test_number_negative_with_dot(self):
        """Test number negative with dot at the end"""
        self.assertTrue(TestLexer.checkLexeme("-123.", "-,123.,<EOF>", 135))

    def test_number_with_decimal_after_dot(self):
        """Test number with decimal after dot"""
        self.assertTrue(TestLexer.checkLexeme("123.2", "123.2,<EOF>", 136))

    def test_number_negative_with_decimal_after_dot(self):
        """Test negative number with decimal after dot"""
        self.assertTrue(TestLexer.checkLexeme("-123.3", "-,123.3,<EOF>", 137))

    def test_number_with_e(self):
        """Test number with e"""
        self.assertTrue(TestLexer.checkLexeme("12.3e3", "12.3e3,<EOF>", 138))

    def test_number_with_E(self):
        """Test number with E"""
        self.assertTrue(TestLexer.checkLexeme("12.3E3", "12.3E3,<EOF>", 139))

    def test_number_with_e_negative(self):
        """Test number with e negative"""
        self.assertTrue(TestLexer.checkLexeme("12.3e-30", "12.3e-30,<EOF>", 140))

    def test_bool_with_true(self):
        """Test bool with true value"""
        self.assertTrue(TestLexer.checkLexeme("aa = True", "aa,=,True,<EOF>", 141))

    def test_bool_with_false(self):
        """Test bool with false value"""
        self.assertTrue(TestLexer.checkLexeme("aa = False", "aa,=,False,<EOF>", 142))

    def test_string_simple(self):
        """Test string simple"""
        self.assertTrue(TestLexer.checkLexeme("\" I am a student \"", " I am a student ,<EOF>", 143))

    def test_string_with_esc(self):
        """Test string with esc"""
        self.assertTrue(TestLexer.checkLexeme("\"I am not \k\"", "Illegal Escape In String: I am not \k", 144))

    def test_string_with_single_quote(self):
        """Test string with single quote esc"""
        self.assertTrue(TestLexer.checkLexeme(""""I am ' " """, "I am ' ,<EOF>", 145))

    def test_string_with_backslash(self):
        """Test string with backslash esc"""
        self.assertTrue(TestLexer.checkLexeme("\"I am \\ \"", "Illegal Escape In String: I am \ ", 146))

    def test_string_zero_char(self):
        """Test String zero char"""
        self.assertTrue(TestLexer.checkLexeme("\"\"", ",<EOF>", 147))

    def test_string_with_backspace(self):
        """Test string with backspace"""
        self.assertTrue(TestLexer.checkLexeme("\"I am \\b\"", "I am \\b,<EOF>", 148))

    def test_string_with_form_feed(self):
        """Test string with form feed"""
        self.assertTrue(TestLexer.checkLexeme("\"I am \\f\"", "I am \\f,<EOF>", 149))

    def test_string_with_carriage_return(self):
        """Test string with carriage return"""
        self.assertTrue(TestLexer.checkLexeme("\"I am \\r\"", """I am \\r,<EOF>""", 150))

    def test_string_with_newline(self):
        """Test string with newline"""
        self.assertTrue(TestLexer.checkLexeme("\"I am \i\"", "Illegal Escape In String: I am \i", 151))

    def test_string_with_quote(self):
        """Test string with quote"""
        self.assertTrue(TestLexer.checkLexeme("""\"He said me: '"I am a teacher'"\"""",
                                              """He said me: '"I am a teacher'",<EOF>""", 152))

    def test_string_with_error_quote(self):
        """Test string with error quote"""
        self.assertTrue(TestLexer.checkLexeme("""\"He said me: '"I am a teacher\"""",
                                              """He said me: '"I am a teacher,<EOF>""", 153))

    def test_unterminated_comment(self):
        """Test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme("""## This is comment """, "Unterminated Comment", 154))

    def test_comment_in_multi_line(self):
        """Test comment in multi line"""
        self.assertTrue(TestLexer.checkLexeme("""## This is comment
        This is line 2 comment
        This is line 3 comment
        ##""", "<EOF>", 155))

    def test_comment_in_multi_line_unterminated(self):
        """Test comment in multi line unterminated"""
        self.assertTrue(TestLexer.checkLexeme("""## This is comment
        This is comment 2
        This is comment 3""", "Unterminated Comment", 156))

    def test_comments_in_one_line(self):
        """Test comments in one line"""
        self.assertTrue(TestLexer.checkLexeme("""## This is comment ##
        ## This is comment 2 ##
        ## This is comment 3 ## """, "<EOF>", 157))

    def test_comments_in_one_line_with_unterminated(self):
        """Test comments in one line with unterminated"""
        self.assertTrue(TestLexer.checkLexeme("""## This is comment
        This is comment 2 ##
        ## This is comment 3""", "Unterminated Comment", 158))

    def test_comment_not_first(self):
        """Test comment with # not at first"""
        self.assertTrue(TestLexer.checkLexeme("""This is comment ##""", "Error Token T", 159))

    def test_comment_lack_at_first(self):
        """Test comment lack a # at first"""
        self.assertTrue(TestLexer.checkLexeme("""# This is comment ##""", "Error Token #", 160))

    def test_comment_lack_at_the_end(self):
        """Test comment lack # at the end"""
        self.assertTrue(TestLexer.checkLexeme("""## This is comment #""", "Unterminated Comment", 161))

    def test_number_with_dot_zero(self):
        """Test number with dot zero"""
        self.assertTrue(TestLexer.checkLexeme("""12.0""", "12.0,<EOF>", 162))

    def test_number_with_double_e(self):
        """Test number with double e"""
        self.assertTrue(TestLexer.checkLexeme("12.0ee3", "12.0,ee3,<EOF>", 163))

    def test_number_with_double_eE(self):
        """Test number with double eE"""
        self.assertTrue(TestLexer.checkLexeme("12.0eE+3", "12.0,eE,+,3,<EOF>", 164))

    def test_number_with_error_sign(self):
        """Test number with error sign"""
        self.assertTrue(TestLexer.checkLexeme("*12.0", "*,12.0,<EOF>", 165))

    def test_number_with_double_sign(self):
        """Test number with double sign"""
        self.assertTrue(TestLexer.checkLexeme("12.03e++3", "12.03,e,+,+,3,<EOF>", 166))

    def test_number_with_sign_at_the_end(self):
        """Test number with sign at the end"""
        self.assertTrue(TestLexer.checkLexeme("12.0++", "12.0,+,+,<EOF>", 167))

    def test_number_with_double_sign_first(self):
        """Test number with double at first"""
        self.assertTrue(TestLexer.checkLexeme("++12.0", "+,+,12.0,<EOF>", 168))

    def test_id_with_sign_at_first(self):
        """Test id with sign at first"""
        self.assertTrue(TestLexer.checkLexeme("++aaa", "+,+,aaa,<EOF>", 169))

    def test_id_with_sign_at_around(self):
        """Test id with sign at around"""
        self.assertTrue(TestLexer.checkLexeme("aa+++bb", "aa,+,+,+,bb,<EOF>", 170))

    def test_error_unclose_string(self):
        """Test error unclose string"""
        self.assertTrue(TestLexer.checkLexeme("""\"Toi la Toi """, """Unclosed String: Toi la Toi """, 171))
    
    def test_id_with_sign_at_around3(self):
        """Test id with sign at around"""
        self.assertTrue(TestLexer.checkLexeme("-12.4e", "-,12.4,e,<EOF>", 172))


