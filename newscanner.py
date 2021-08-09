import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'CLASS',
    'Example',
    'STATIC',
    'VOID',
    'PUBLIC',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'NOT_EQUAL',
    'CLOSE_CARET',
    'OPEN_CARET',
    'STRING_LITERAL',
    'CHARACTER_LITERAL',
    'FALSE',
    'TRUE',
    'NULL',
    'RETURN',
    'NEW',
    'IF',
    'ELSE',
    'WHILE',
    'STRING',
    'FINAL',
    'ABSTRACT',
    'CONTINUE',
    'FOR',
    'SWITCH',
    'ASSERT',
    'DEFAULT',
    'SEMICOLON',
    'GOTO',
    'PACKAGE',
    'SYNCHRONIZED',
    'BOOLEAN',
    'DO',
    'THIS',
    'BYTE',
    'IMPORT',
    'THROWS',
    'BREAK',
    'IMPLEMENTS',
    'PROTECTED',
    'THROW',
    'CASE',
    'ENUM',
    'INSTANCEOF',
    'TRANSIENT',
    'CATCH',
    'EXTENDS',
    'SHORT',
    'TRY',
    'INTERFACE',
    'FINALLY',
    'LONG',
    'STRICTFP',
    'VOLATILE',
    'CONST',
    'FLOAT',
    'Quote',
    'NATIVE',
    'super',
    'EXPORTS',
    'MODULE',
    'PROVIDES',
    'COMMA',
    'OPEN_CURLY_BRACE',
    'CLOSE_CURLY_BRACE',
    'OPEN_BRACE',
    'CLOSE_BRACE',
)

# use re in python


reserved = {

    'class': 'CLASS',
    'static': 'STATIC',
    'void': 'VOID',
    'public': 'public',
    'false': 'false',
    'true': 'true',
    'null':  'null',
    'return': 'RETURN',
    'new': 'NEW',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'string': 'STRING',
    'final': 'FINAL',
    'abstract':  'ABSTRACT',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'switch':  'SWITCH',
    'assert': 'ASSERT',
    'default': 'DEFAULT',
    'goto': 'GOTO',
    'package': 'PACKAGE',
    'synchronized': 'SYNCHRONIZED',
    'boolean': 'BOOLEAN',
    'do': 'DO',
    'this': 'THIS',
    'byte': 'BYTE',
    'import':  'IMPORT',
    'thros': 'THROWS',
    'break': 'BREAK',
    'implements': 'IMPLEMENTS',
    'protected': 'PROTECTED',
    'throw': 'THROW',
    'case': 'CASE',
    'enume': 'ENUM',
    'instanceof': 'INSTANCEOF',
    'transient':  'TRANSIENT',
    'catch': 'CATCH',
    'extends': 'EXTENDS',
    'short': 'SHORT',
    'try': 'TRY',
    'interface': 'INTERFACE',
    'finally': 'FINALLY',
    'long': 'LONG',
    'strictfp': 'STRICTFP',
    'volatile': 'VOLATILE',
    'const': 'CONST',
    'flaot': 'FLOAT',
    'native': 'NATIVE',
    'super': 'SUPER',
    'exports': 'EXPORTS',
    'module': 'MODULE',
    'provides': 'PROVIDES',
}

tokens = ['NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'CLASS',
          'STATIC',
          'VOID',
          'PUBLIC',
          'OPEN_PAREN',
          'CLOSE_PAREN',
          'NOT_EQUAL',
          'CLOSE_CARET',
          'OPEN_CARET',
          'STRING_LITERAL',
          'CHARACTER_LITERAL',
          'FALSE',
          'TRUE',
          'NULL',
          'RETURN',
          'NEW',
          'IF',
          'ELSE',
          'WHILE',
          'STRING',
          'FINAL',
          'ABSTRACT',
          'CONTINUE',
          'FOR',
          'SWITCH',
          'ASSERT',
          'DEFAULT',
          'SEMICOLON',
          'GOTO',
          'PACKAGE',
          'SYNCHRONIZED',
          'BOOLEAN',
          'DO',
          'THIS',
          'BYTE',
          'IMPORT',
          'THROWS',
          'BREAK',
          'IMPLEMENTS',
          'PROTECTED',
          'THROW',
          'CASE',
          'ENUM',
          'INSTANCEOF',
          'TRANSIENT',
          'CATCH',
          'EXTENDS',
          'SHORT',
          'TRY',
          'INTERFACE',
          'FINALLY',
          'LONG',
          'STRICTFP',
          'VOLATILE',
          'CONST',
          'FLOAT',
          'Quote',
          'NATIVE',
          'super',
          'EXPORTS',
          'MODULE',
          'PROVIDES',
          'COMMA',
          'OPEN_CURLY_BRACE',
          'CLOSE_CURLY_BRACE',
          'OPEN_BRACE',
          'CLOSE_BRACE', ]


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t


# t_CLASS = "\\b(class)\\b "
# t_PUBLIC = "\\b(public)\\b"
# t_VOID = "\\b(void)\\b"
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_OPEN_PAREN = "(\\().*"
t_CLOSE_PAREN = "(\\)).*"
t_SEMICOLON = "(;).*"
t_NOT_EQUAL = "(\\!=).*"
t_CLOSE_CARET = "(>).*"
t_OPEN_CARET = "(<).*"
t_Quote = "(').*"
t_STRING_LITERAL = '\"(\\.|[^\\"])*\"'
t_CHARACTER_LITERAL = r"\'(\\.|[^\\'])*\'"
t_FALSE = "\\b(false)\\b."
t_TRUE = "\\b(true)\\b."
t_NULL = "\\b(null)\\b."
t_RETURN = "\\b(return)\\b."
t_NEW = "\\b(new)\\b."
t_IF = "\\b(if)\\b."
t_ELSE = "\\b(else)\\b."
t_WHILE = "\\b(while)\\b."
t_STATIC = "\\b(static)\\b."
t_STRING = "\\b(String)\\b."
t_FINAL = "\\b(final)\\b."
t_ABSTRACT = "\\b(abstract)\\b."
t_CONTINUE = "\\b(continue)\\b."
t_FOR = "\\b(for)\\b."
t_SWITCH = "\\b(switch)\\b."
t_ASSERT = "\\b(assert)\\b."
t_DEFAULT = "\\b(default)\\b."
t_GOTO = "\\b(goto)\\b."
t_PACKAGE = "\\b(package)\\b."
t_SYNCHRONIZED = "\\b(synchronized)\\b."
t_BOOLEAN = "\\b(boolean)\\b."
t_DO = "\\b(do)\\b."
t_THIS = "\\b(this)\\b."
t_BYTE = "\\b(byte)\\b."
t_IMPORT = "\\b(import)\\b."
t_THROWS = "\\b(throws)\\b."
t_BREAK = "\\b(break)\\b."
t_IMPLEMENTS = "\\b(implements)\\b."
t_PROTECTED = "\\b(protected)\\b."
t_THROW = "\\b(throw)\\b."
t_CASE = "\\b(case)\\b."
t_ENUM = "\\b(enum)\\b."
t_INSTANCEOF = "\\b(instanceof)\\b."
t_TRANSIENT = "\\b(transient)\\b."
t_CATCH = "\\b(catch)\\b."
t_EXTENDS = "\\b(extends)\\b."
t_SHORT = "\\b(short)\\b."
t_TRY = "\\b(try)\\b."
t_INTERFACE = "\\b(INTERFACE)\\b."
t_FINALLY = "\\b(FINALLY)\\b."
t_LONG = "\\b(LONG)\\b."
t_STRICTFP = "\\b(strictfp)\\b."
t_VOLATILE = "\\b(volatile)\\b."
t_CONST = "\\b(const)\\b."
t_FLOAT = "\\b(float)\\b."
t_NATIVE = "\\b(native)\\b."
t_super = "\\b(super)\\b."
t_EXPORTS = "\\b(exports)\\b."
t_MODULE = "\\b(module)\\b."
t_PROVIDES = "\\b(provides)\\b."
t_COMMA = "(,).*"
t_OPEN_CURLY_BRACE = "(\\{).*"
t_CLOSE_CURLY_BRACE = "(\\}).*"
t_OPEN_BRACE = "(\\[).*"
t_CLOSE_BRACE = "(\\]).*"
# A regular expression rule with some action code


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
# digit = r'([0-9])'
# nondigit = r'([_A-Za-z])'
t_ignore = r"/'''.*"

# Error handling rule


def t_error(t):
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
data = '''
public class Example {
    public static void main(String[] args) {
      3 + 4 * 10+ -20 *2  ;
    }
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
