lex.yy.c: lexico.l
	flex lexico.l
a.out: lex.yy.c
	gcc -C lex.yy.c -lfl
clean:
	rm -f a.out lex.yy.c
run: a.out
	./a.out

