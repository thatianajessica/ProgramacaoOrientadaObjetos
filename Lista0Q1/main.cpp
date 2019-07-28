#include <iostream>
#include <math.h>

using namespace std;

struct numeroComplexo
{
    float parteReal;
    float parteIm;
};

void imprimeNumero(struct numeroComplexo numComplexo)
{
    if (numComplexo.parteIm >= 0){
        cout << numComplexo.parteReal << " +" << numComplexo.parteIm <<"i" << endl;
    }else{
        cout << numComplexo.parteReal << " " << numComplexo.parteIm <<"i" << endl;
    }

}

struct numeroComplexo somaNumeros(struct numeroComplexo num1, struct numeroComplexo num2){
    struct numeroComplexo numero;
    float parteReal = num1.parteReal + num2.parteReal;
    float parteIm = num1.parteIm + num2.parteIm;
    numero.parteIm = parteIm;
    numero.parteReal = parteReal;
    return numero;
}

float calcularModulo(struct numeroComplexo num){
    float quadrados = (num.parteReal*num.parteReal) + (num.parteIm*num.parteIm);
    float modulo = sqrt(quadrados);
    return modulo;
}

int main()
{
    struct numeroComplexo teste, num1, num2,resultadoSoma, num3;
    float modulo;

    //imprimir um numero
    teste.parteReal = 2;
    teste.parteIm = 2;
    imprimeNumero(teste);

    //somar dois numeros
    num1.parteReal = 1;
    num1.parteIm = 2;
    num2.parteReal = 3;
    num2.parteIm = -2;

    resultadoSoma = somaNumeros(num1,num2);
    imprimeNumero(resultadoSoma);

    //modulo de um numero
    num3.parteReal = 0;
    num3.parteIm = 2;

    modulo = calcularModulo(num3);
    cout <<"O modulo do numero complexo eh " << modulo << endl;

    return 0;
}
