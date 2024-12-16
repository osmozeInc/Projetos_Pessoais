#include <stdio.h>
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
    system("chcp 65001");

    // compila todos os arquivos com as dependencias e executa o programa
    system("gcc configuracoes/configuracoes.c ranking/ranking.c game_house.c -o game_house.exe");
    carregando(0, 20);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c Jogos/jogo_da_velha.c -o Jogos/jogo_da_velha.exe");
    carregando(20, 40);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c Jogos/jogo_de_dados.c -o Jogos/jogo_de_dados.exe");
    carregando(40, 60);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c configuracoes/configurar_cores.c -o configuracoes/configurar_cores.exe");
    carregando(60, 80);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c ranking/placar_ranking.c -o ranking/placar_ranking.exe");
    carregando(81, 100); // é ideal que o carregamento que não comece de 0 seja em mutiplos de 3


    system("game_house.exe");
}