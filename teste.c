#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <Windows.h>

#define VERDE "\033[32m"

void carregando(int num_porcent_bottom, int num_porcent_top){
    system("cls");

    printf(VERDE"Iniciando Sistema...\n\n\n"
           "|=================================|======|\n");

    for (int i = 1; i <= (num_porcent_top - num_porcent_bottom)/3; i++)      // cria os espaços
    {
        printf("|");
        
        for (int j = 0; j < i; j++)    //cria a barra de porcentagem
        printf("#");

        for (int j = i; j < 33; j++)      // cria os espaços
            printf(" ");

        if (num_porcent_top >= 0 && num_porcent_top < 10)       // cria o espaço antes do numero de porcentagem e o numero
            printf("|    %d%% |", num_porcent_bottom + ((i) * 3));
        else if (num_porcent_top > 9 && num_porcent_top < 100)
            printf("|  %d%% |", num_porcent_bottom + ((i) * 3));
        else 
            printf("| %d%% |", num_porcent_bottom + (i));

        printf("\n|=================================|======|\n");

        Sleep(500);

        if (i < (num_porcent_top - num_porcent_bottom)/3)
        {
            printf("\e[A\e[K");
            printf("\e[A\e[K");
        }
            
    }
}

int main(){
    //carregando(0, 0);
    carregando(0, 12);
    // carregando(20, 40);
    // carregando(40, 60);
    // carregando(60, 80);
    // carregando(80, 100);
}