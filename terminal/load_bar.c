#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>

#define VERDE "\033[32m"
#define LIMPAR_TELA "\033[2J\033[H"

void carregando(int num_porcent_from, int num_porcent_to, char mensagem[31]){

    printf(LIMPAR_TELA VERDE"Iniciando Sistema...\n\n\n"
           "|=================================|======|\n");

        int start = num_porcent_from / 3;

    for (int i = 1; i <= (num_porcent_to - num_porcent_from)/3; i++)    // cria os espaços
    {
        printf("|");

        for (int j = 0; j < i + start; j++)     //cria a barra de porcentagem
            printf("#");
        for (int j = i + start; j < 33; j++)    // cria os espaços
            printf(" ");

        if ((i + start) * 3 < 99)       // exibe a linha de porcentagem de 0 a 100
            printf("|%4d%% |", num_porcent_from + (i * 3));
        else 
            printf("|%4d%% |", num_porcent_from + (i * 3) + 1);

        printf("\n|=================================|======|"
               "\n| %-31s |"
               "\n|=================================|\n", mensagem);

        Sleep(80);


        if (i < (num_porcent_to - num_porcent_from)/3)
            printf("\e[A\e[K\e[A\e[K\e[A\e[K\e[A\e[K");
    }
}

int main(){
    carregando(0, 21, "Compilando sistema principal"); // mensagem deve ter até 31 caracteres
}