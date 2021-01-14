D           [0-9]
DO          [0-7]
L           [a-zA-Z_]
H           [a-fA-F0-9]
E           [Ee][+-]?{D}+
FS          (f|F|l|L)
IS          (u|U|l|L)*
SIG         (+|-)

%{
#include <stdio.h>

void count();
%}

%%
"/*"            { printf("<Comentario>"); }

"auto"          { printf("<Palabra_reservada>"); }
"break"         { printf("<Palabra_reservada>"); }
"case"          { printf("<Palabra_reservada>"); }
"const"         { printf("<Palabra_reservada>"); }
"continue"      { printf("<Palabra_reservada>"); }
"default"       { printf("<Palabra_reservada>"); }
"do"            { printf("<Palabra_reservada>"); }
"double"        { printf("<Palabra_reservada>"); }
"else"          { printf("<Palabra_reservada>"); }
"enum"          { printf("<Palabra_reservada>"); }
"extern"        { printf("<Palabra_reservada>"); }
"float"         { printf("<Palabra_reservada>"); }
"for"           { printf("<Palabra_reservada>"); }
"goto"          { printf("<Palabra_reservada>"); }
"if"            { printf("<Palabra_reservada>"); }
"register"      { printf("<Palabra_reservada>"); }
"return"        { printf("<Palabra_reservada>"); }
"signed"        { printf("<Palabra_reservada>"); }
"sizeof"        { printf("<Palabra_reservada>"); }
"static"        { printf("<Palabra_reservada>"); }
"char"          { printf("<Palabra_reservada>"); }
"int"           { printf("<Palabra_reservada>"); }
"long"          { printf("<Palabra_reservada>"); }
"short"         { printf("<Palabra_reservada>"); }
"struct"        { printf("<Palabra_reservada>"); }
"switch"        { printf("<Palabra_reservada>"); }
"typedef"       { printf("<Palabra_reservada>"); }
"union"         { printf("<Palabra_reservada>"); }
"unsigned"      { printf("<Palabra_reservada>"); }
"void"          { printf("<Palabra_reservada>"); }
"volatile"      { printf("<Palabra_reservada>"); }
"while"         { printf("<Palabra_reservada>"); }

{L}({L}|{D})*       { printf("<Identificador>"); }
0[xX]{H}+{IS}?      { printf("<Constante-Entera>"); }
0{DO}+{IS}?      	{ printf("<Constante-Entera-OCTAL>"); }
{D}+{IS}?       	{ printf("<Constante-Entera-DECIMAL>"); }
L?\"(\\.|[^\\"])*\"   { printf("<Constante-Cadena>");}

{D}+{E}{FS}?        { printf("<Constante-Flotante>"); }
{D}*"."{D}+({E})?{FS}?  { printf("<Constante-Flotante>"); }
{D}+"."{D}*({E})?{FS}?  { printf("<Constante-Flotante>"); }

"..."           { printf("<Elipsis>"); }
">>="           { printf("<operador-asignacion>"); }
"<<="           { printf("<operador-asignacion>"); }
"+="            { printf("<operador-asignacion>"); }
"-="            { printf("<operador-asignacion>"); }
"*="            { printf("<operador-asignacion>"); }
"/="            { printf("<operador-asignacion>"); }
"%="            { printf("<operador-asignacion>"); }
"&="            { printf("<operador-asignacion>"); }
"^="            { printf("<operador-asignacion>"); }
"|="            { printf("<operador-asignacion>"); }

">>"            { printf("<Operador-BITS>"); }
"<<"            { printf("<Operador-BITS>"); }

"++"            { printf("<Operador-INCREMENTO>"); }
"--"            { printf("<Operador-DECREMENTO>"); }


"->"            { printf("<Operador-ESTRUCTURA>"); }

"&&"            { printf("<Operador-LOGICO>"); }
"||"            { printf("<Operador-LOGICO>"); }

"<="            { printf("<Operador-RELACION>"); }
">="            { printf("<Operador-RELACION>"); }

"=="            { printf("<Operador-IGUALDAD>"); }
"!="            { printf("<Operador-IGUALDAD>"); }



";"             { printf("<Punto-Coma>"); }
("{"|"<%")      { printf("<span class='text-secondary'>{</span>"); }
("}"|"%>")      { printf("<span class='text-secondary'>}</span>"); }

","         { printf("<span class='text-secondary'>,</span>"); }
":"         { printf("<Operador-TERNARIO>"); }
"="         { printf("<Operador-ASIGNACION>"); }
"("         { printf("<Operador-CAST>"); }
")"         { printf("<Operador-CAST>"); }
("["|"<:")  { printf("<Operador [>"); }
("]"|":>")  { printf("<Operador ]>"); }
"."         { printf("<Operador-ESTRUCTURA>"); }
"&"         { printf("<Operador-BITS>"); }
"!"         { printf("<Operador-LOGICO>"); }
"~"         { printf("<Operador-BITS>"); }
"-"         { printf("<Operador-ARITMETICOS>"); }
"+"         { printf("<Operador-ARITMETICOS>"); }
"*"         { printf("<Operador-ARITMETICOS>"); }
"/"         { printf("<Operador-ARITMETICOS>"); }
"%"         { printf("<Operador-ARITMETICOS>"); }

"<"         { printf("<Operador-RELACION>"); }
">"         { printf("<Operador-RELACION>"); }

"^"         { printf("<Operador-BITS>"); }
"|"         { printf("<Operador-BITS>"); }

"?"         { printf("<Operador-TERMARIO>"); }

\n     		{ printf("\n"); }
[ \t\v\f]   { printf(" "); }
"\""     	{ printf("<Constante-Char>"); }
.           { /* ignore bad characters */ }

%%

void printFin(){
printf("<script src='https://code.jquery.com/jquery-3.5.1.slim.min.js' integrity='sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj' crossorigin='anonymous'></script>");
printf("<script src='https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx' crossorigin='anonymous'></script>");
printf("</body>");
printf("</html>");

}
void printInit(){
printf("<!DOCTYPE html>");
printf("<html>");
printf("<head>");
printf("    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css' integrity='sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2' crossorigin='anonymous'>");
printf("    <title>Parser de C</title>");
printf("</head>");
printf("<body style='background-color:#FF0000;'>");
}


int main( int argc, char **argv )
{
	int x = 3 > 4 ? 1:2;

    //printInit();

    ++argv, --argc;  /* skip over program name */
    if ( argc > 0 )
            yyin = fopen( argv[0], "r" );
    else
            yyin = stdin;

    yylex();

    //printFin();
}

