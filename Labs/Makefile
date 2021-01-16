a.out: main.o lex.yy.o calculadora.tab.o
	gcc main.o lex.yy.o calculadora.tab.o -ll
main.o: main.c calculadora.tab.c
	gcc -c main.c
lex.yy.o: lex.yy.c
	gcc -c lex.yy.c
calculadora.tab.o: calculadora.tab.c
	gcc -c calculadora.tab.c
lex.yy.c: calculadora.l calculadora.tab.c
	flex calculadora.l
calculadora.tab.c: calculadora.y
	bison -d calculadora.y
clean:
	rm -f a.out main.o calculadora.tab.* lex.yy.*
run: a.out
	./a.out
