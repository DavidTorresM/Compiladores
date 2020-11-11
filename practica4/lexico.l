D           [0-9]
L           [a-zA-Z_]
H           [a-fA-F0-9]
E           [Ee][+-]?{D}+
FS          (f|F|l|L)
IS          (u|U|l|L)*

%{
#include <stdio.h>

void count();
%}

%%
"/*"            { printf("<span class='text-primary'>/*</span>"); }

"auto"          { printf("<span class='text-primary'>auto</span>"); }
"break"         { printf("<span class='text-primary'>break</span>"); }
"case"          { printf("<span class='text-primary'>case</span>"); }
"char"          { printf("<span class='text-primary'>char</span>"); }
"const"         { printf("<span class='text-primary'>const</span>"); }
"continue"      { printf("<span class='text-primary'>continue</span>"); }
"default"       { printf("<span class='text-primary'>default</span>"); }
"do"            { printf("<span class='text-primary'>do</span>"); }
"double"        { printf("<span class='text-primary'>double</span>"); }
"else"          { printf("<span class='text-primary'>else</span>"); }
"enum"          { printf("<span class='text-primary'>enum</span>"); }
"extern"        { printf("<span class='text-primary'>extern</span>"); }
"float"         { printf("<span class='text-primary'>float</span>"); }
"for"           { printf("<span class='text-primary'>for</span>"); }
"goto"          { printf("<span class='text-primary'>goto</span>"); }
"if"            { printf("<span class='text-primary'>if</span>"); }
"int"           { printf("<span class='text-primary'>int</span>"); }
"long"          { printf("<span class='text-primary'>long</span>"); }
"register"      { printf("<span class='text-primary'>register</span>"); }
"return"        { printf("<span class='text-primary'>return</span>"); }
"short"         { printf("<span class='text-primary'>short</span>"); }
"signed"        { printf("<span class='text-primary'>signed</span>"); }
"sizeof"        { printf("<span class='text-primary'>sizeof</span>"); }
"static"        { printf("<span class='text-primary'>static</span>"); }
"struct"        { printf("<span class='text-primary'>struct</span>"); }
"switch"        { printf("<span class='text-primary'>switch</span>"); }
"typedef"       { printf("<span class='text-primary'>typedef</span>"); }
"union"         { printf("<span class='text-primary'>union</span>"); }
"unsigned"      { printf("<span class='text-primary'>unsigned</span>"); }
"void"          { printf("<span class='text-primary'>void</span>"); }
"volatile"      { printf("<span class='text-primary'>volatile</span>"); }
"while"         { printf("<span class='text-primary'>while</span>"); }

{L}({L}|{D})*       { printf("<span>%s</span>",yytext ); }

0[xX]{H}+{IS}?      { printf("<span>%s</span>",yytext ); }
0{D}+{IS}?      { printf("<span>%s</span>",yytext ); }
{D}+{IS}?       { printf("<span>%s</span>",yytext ); }
L?'(\\.|[^\\'])+'   { printf("<span>%s</span>",yytext );}

{D}+{E}{FS}?        { printf("<span>%s</span>",yytext ); }
{D}*"."{D}+({E})?{FS}?  { printf("<span>%s</span>",yytext ); }
{D}+"."{D}*({E})?{FS}?  { printf("<span>%s</span>",yytext ); }


"..."           { printf("<span>...</span>"); }
">>="           { printf("<span>>>=</span>"); }
"<<="           { printf("<span><<=</span>"); }
"+="            { printf("<span>+=</span>"); }
"-="            { printf("<span>-=</span>"); }
"*="            { printf("<span>*=</span>"); }
"/="            { printf("<span>/=</span>"); }
"%="            { printf("<span>&#37;=</span>"); }
"&="            { printf("<span>&=</span>"); }
"^="            { printf("<span>^=</span>"); }
"|="            { printf("<span>|=</span>"); }
">>"            { printf("<span>>></span>"); }
"<<"            { printf("<span><<</span>"); }
"++"            { printf("<span>++</span>"); }
"--"            { printf("<span>--</span>"); }
"->"            { printf("<span>-></span>"); }
"&&"            { printf("<span>&&</span>"); }
"||"            { printf("<span>||</span>"); }
"<="            { printf("<span><=</span>"); }
">="            { printf("<span>>=</span>"); }
"=="            { printf("<span>==</span>"); }
"!="            { printf("<span>!=</span>"); }
";"             { printf("<span>;</span>"); }
("{"|"<%")      { printf("<span class='text-secondary'>{</span>"); }
("}"|"%>")      { printf("<span class='text-secondary'>}</span>"); }
","         { printf("<span class='text-secondary'>,</span>"); }
":"         { printf("<span class='text-secondary'>:</span>"); }
"="         { printf("<span class='text-secondary'>=</span>"); }
"("         { printf("<span class='text-secondary'>(</span>"); }
")"         { printf("<span class='text-secondary'>)</span>"); }
("["|"<:")      { printf("<span class='text-secondary'>[</span>"); }
("]"|":>")      { printf("<span class='text-secondary'>]</span>"); }
"."         { printf("<span class='text-secondary'>.</span>"); }
"&"         { printf("<span class='text-secondary'>&</span>"); }
"!"         { printf("<span class='text-secondary'>!</span>"); }
"~"         { printf("<span class='text-secondary'>~</span>"); }
"-"         { printf("<span class='text-secondary'>-</span>"); }
"+"         { printf("<span class='text-secondary'>+</span>"); }
"*"         { printf("<span class='text-secondary'>*</span>"); }
"/"         { printf("<span class='text-secondary'>/</span>"); }
"%"         { printf("<span class='text-secondary'>&#37;</span>"); }
"<"         { printf("<span class='text-secondary'><</span>"); }
">"         { printf("<span class='text-secondary'>></span>"); }
"^"         { printf("<span class='text-secondary'>^</span>"); }
"|"         { printf("<span class='text-secondary'>|</span>"); }
"?"         { printf("<span class='text-secondary'>?</span>"); }

\n     { printf("<br></br>"); }
[ \t\v\f]     { printf("&nbsp;&nbsp;&nbsp;&nbsp;"); }
"\""     { printf("<span style='color:#fef82d;'>\"</span>"); }
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


    printInit();

    ++argv, --argc;  /* skip over program name */
    if ( argc > 0 )
            yyin = fopen( argv[0], "r" );
    else
            yyin = stdin;

    yylex();

    printFin();
}

