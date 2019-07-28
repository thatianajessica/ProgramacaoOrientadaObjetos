#include <iostream>
#include <math.h>

using namespace std;

struct quadrado{
    float lado;
};

struct circulo{
    float raio;
};

float areaQuadrado(struct quadrado quadrado){
    float area = quadrado.lado*quadrado.lado;
    return area;
}

float areaCirculo(struct circulo circulo){
    float area = M_PI * (circulo.raio*circulo.raio);
    return area;
}

float areaSomaQuadrados(struct quadrado* quadrados, int tam_vetor){
    float area_total = 0;
    for (int i = 0 ; i < tam_vetor ; i++) {
        area_total = area_total + areaQuadrado(quadrados[i]);
    }
    return area_total;
}

float areaSomaCirculos(struct circulo* circulos, int tam_vetor){
    float area_total = 0;
    for (int i = 0; i < tam_vetor; i++) {
        area_total = area_total + areaCirculo(circulos[i]);
    }
    return  area_total;
}

float areaSomaCirculosQuadrados(struct circulo* circulos, int tam_vetorcirculo, struct quadrado* quadrados, int tam_vetorquadrados){
    float area_totalquadrados = 0, area_totalcirculos = 0;
    float area_total;
    area_totalcirculos = areaSomaCirculos(circulos, tam_vetorcirculo);
    area_totalquadrados = areaSomaQuadrados(quadrados, tam_vetorquadrados);
    area_total = area_totalcirculos + area_totalquadrados;
    return area_total;

}


int main()
{
    //area quadrado
    struct quadrado testeQuadrado;
    float area1 = 0;


    testeQuadrado.lado = 2;
    area1 = areaQuadrado(testeQuadrado);

    cout << "Area do quadrado = " <<area1 << endl;

    //area circulo
    struct circulo testeCirculo;
    float area2 = 0;

    testeCirculo.raio = 10;
    area2 = areaCirculo(testeCirculo);

    cout << "Area do circulo = " <<area2 << endl;

    //vetor de quadrados - soma das areas
    struct quadrado vetorQuadrado[2];
    float area_total;


    int tam_vetor = sizeof (vetorQuadrado) / sizeof(vetorQuadrado[0]);

    for (int i = 0; i< tam_vetor; i++) {
        vetorQuadrado[i].lado = (2*i) + 1;
    }
    area_total = areaSomaQuadrados(vetorQuadrado, tam_vetor);

    cout << "Area da soma dos quadrados = " <<area_total << endl;

    //vetor de circulos
    struct circulo vetorCirculo[2];
    float area_total2;

    int tam_vetor2 = sizeof (vetorCirculo) / sizeof(vetorCirculo[0]);

    for (int j = 0 ; j < tam_vetor2 ; j++) {
        vetorCirculo[j].raio = (2*j) + 1;
    }
    area_total2 = areaSomaCirculos(vetorCirculo, tam_vetor2);
    cout << "Area da soma dos circulos = " <<area_total2 << endl;

    //somar vetores de circulos com vetores de quadrados
    float area_total3 = areaSomaCirculosQuadrados(vetorCirculo, tam_vetor2, vetorQuadrado, tam_vetor);
    cout << "Area da soma dos circulos e quadrados = " <<area_total3 << endl;
    return 0;
}
