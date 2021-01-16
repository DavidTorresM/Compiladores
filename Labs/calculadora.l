%{
	#include "calculadora.tab.h"
%}


%%
[0-9]+			{ 
				yylval = atoi(yytext);
				return NUMERO;
				}
[\n]			{
				return '\n';
				}
[+]				return '+';
%%
