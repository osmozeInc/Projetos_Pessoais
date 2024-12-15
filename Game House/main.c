#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>

#define VERDE "\033[32m"

void carregando(int num_porcent){
    char bar_porcent[33];

    if (num_porcent == 0)
        strcpy(bar_porcent, "                                 |   ");
    else if (num_porcent == 20)
        strcpy(bar_porcent, "#######                          |  ");
    else if (num_porcent == 40)
        strcpy(bar_porcent, "#############                    |  ");
    else if (num_porcent == 60)
        strcpy(bar_porcent, "####################             |  ");
    else if (num_porcent == 80)
        strcpy(bar_porcent, "###########################      |  ");
    else if (num_porcent == 100)
        strcpy(bar_porcent, "#################################| ");

    system("cls");
    printf(VERDE"Iniciando Sistema...\n"
           "|=================================|======|\n"
           "|%s%d%% |\n"
           "|=================================|======|", bar_porcent, num_porcent);
}

int main(){
    system("chcp 65001");

    carregando(0);
    // compila todos os arquivos com as dependencias e executa o programa
    system("gcc configuracoes/configuracoes.c ranking/ranking.c game_house.c -o game_house.exe");
    carregando(20);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c Jogos/jogo_da_velha.c -o Jogos/jogo_da_velha.exe");
    carregando(40);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c Jogos/jogo_de_dados.c -o Jogos/jogo_de_dados.exe");
    carregando(60);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c configuracoes/configurar_cores.c -o configuracoes/configurar_cores.exe");
    carregando(80);
    system("gcc configuracoes/configuracoes.c ranking/ranking.c ranking/placar_ranking.c -o ranking/placar_ranking.exe");
    carregando(100);

    system("game_house.exe");
}