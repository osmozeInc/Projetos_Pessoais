#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <Windows.h>

#define VERDE "\033[32m"

void carregando(int num_porcent_bottom, int num_porcent_top){
    int start = 0;

    system("cls");
    printf(VERDE"Iniciando Sistema...\n\n\n"
           "|=================================|======|\n");

    if (num_porcent_bottom > 3)
        start = num_porcent_bottom / 3;

    for (int i = 1; i <= (num_porcent_top - num_porcent_bottom)/3; i++)      // cria os espaços
    {
        printf("|");
        for (int j = 0; j < i + start; j++)    //cria a barra de porcentagem
        printf("#");
        for (int j = i + start; j < 33; j++)      // cria os espaços
            printf(" ");

        if (((i + start) * 3) < 10)       // cria o espaço antes do numero de porcentagem e o numero
            printf("|%4d%% |", num_porcent_bottom + (i * 3));
        else if ((i + start) * 3 >= 10 && (i + start) * 3 < 99)
            printf("|%4d%% |", num_porcent_bottom + (i * 3));
        else 
            printf("|%4d%% |", num_porcent_bottom + (i * 3) + 1);

        printf("\n|=================================|======|\n");
        Sleep(200);


        if (i < (num_porcent_top - num_porcent_bottom)/3)
        {
            printf("\e[A\e[K");
            printf("\e[A\e[K");
        }
            
    }
}

int main(){
    //carregando(0, 0);
    carregando(12, 100);
    // carregando(20, 40);
    // carregando(40, 60);
    // carregando(60, 80);
    // carregando(80, 100);
}