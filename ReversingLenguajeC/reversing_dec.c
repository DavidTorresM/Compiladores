#include <stdio.h>

int funcion(){
    
    float a = 34E-23;
    
    while(a--){
        printf("hola");
    }
}

int main(void){

    short x = 10;
    int y = 15;
    long z = 15;

    z = funcion();

    return 0;
}

