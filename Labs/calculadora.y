%{
	#include <stdio.h>
	#include <stdlib.h>
	int yylex(void);
	void  yyerror(char *mensaje){
		printf("ERROR: %s\n",mensaje);
		exit(0);
	}
%}

%token NUMERO

%%
programa:
;
programa: linea programa
;
linea: '\n'
;
linea: expresion '\n'	{ printf("VALOR = %d\n",$1); }
;
expresion: NUMERO		{ $$ = $1; }
;
expresion: expresion '+' expresion	{ $$ = $1 + $3; }
%%

