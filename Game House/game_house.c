#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include "configuracoes\configuracoes.h"


void GameHouse()
{
    const char* resetar = reset();
    system("cls || clear");
    printf("%s", resetar);
    printf("  _____                          _    _                                 \n");
    printf(" / ____|                        | |  | |                                \n");
    printf("| |  __  __ _ _ __ ___   ___    | |__| | ___  _   _  ___  ___           \n");
    printf("| | |_ |/ _` | '_ ` _ \\ / _ \\   |  __  |/ _ \\| | | |/ __|/ _ \\      \n");
    printf("| |__| | (_| | | | | | |  __/   | |  | | (_) | |_| |\\__ \\  __/        \n");
    printf(" \\_____/\\__,_|_| |_| |_|\\___|   |_|  |_|\\___/ \\___/ |___/\\___|    \n");
    printf("                                                                      \n\n");
}

int Menu() 
{
    const char* fundo = CorDeDestaqueMenu();
    const char* texto = CorDoTextoMenu();
    const char* resetar = reset();
    int opcao = 1;

    printf("\n\n\n\n\n\n");
    while (1)
    {
        printf("\n");
        ApagarLinha(6);

        if (opcao == 1)
        {
            printf("%s1. Jogo da Velha (enter)%s\n", fundo, resetar);
            printf("%s2. Jogo de dados\n", texto);
            printf("3. Configurações\n");
            printf("4. Placar de jogadores\n");
            printf("5. Sair\n");
            printf("Escolha uma opção: ");
        }
        
        if (opcao == 2)
        {
            printf("%s1. Jogo da Velha%s\n", texto, resetar);
            printf("%s2. Jogo de dados (enter)%s\n", fundo, resetar);
            printf("%s3. Configurações\n", texto);
            printf("4. Placar de jogadores\n");
            printf("5. Sair\n");
            printf("Escolha uma opção: ");
        }

        if (opcao == 3)
        {
            printf("%s1. Jogo da Velha\n", texto);
            printf("2. Jogo de dados%s\n", resetar);
            printf("%s3. Configurações (enter)%s\n", fundo, resetar);
            printf("%s4. Placar de jogadores\n", texto);
            printf("5. Sair\n");
            printf("Escolha uma opção: ");
        }

        if (opcao == 4)
        {
            printf("%s1. Jogo da Velha\n", texto);
            printf("2. Jogo de dados\n");
            printf("3. Configurações%s\n",resetar);
            printf("%s4. Placar de jogadores (enter)%s\n", fundo, resetar);
            printf("%s5. Sair\n", texto);
            printf("Escolha uma opção: ");
        }

        if (opcao == 5)
        {
            printf("%s1. Jogo da Velha\n", texto);
            printf("2. Jogo de dados\n");
            printf("3. Configurações\n");
            printf("4. Placar de jogadores%s\n", resetar);
            printf("%s5. Sair (enter)%s\n", fundo, resetar);
            printf("%sEscolha uma opção: ", texto);
        }

        int tecla = LerTecla(opcao, 5);
        if (tecla != 13) opcao = tecla;
        else break;
    }
    return opcao;
}

int main() 
{
    while (1)
    {
        system("cls || clear");
        GameHouse(); // nome do sistema
        int opcao = Menu();
        printf("%d\n", opcao);

        if (opcao == 1) system(".\\Jogos\\jogo_da_velha.exe");

        else if (opcao == 2) system(".\\Jogos\\jogo_de_dados.exe");

        else if (opcao == 3) system(".\\configuracoes\\configurar_cores.exe");

        else if (opcao == 4) system(".\\ranking\\placar_ranking.exe");

        else if (opcao == 5) // sair
        {
            char mensagem[23] = "\nObrigado por jogar!\n\n";
            for (int i = 0; i < 22; i++) 
            {
                printf("%c", mensagem[i]);
                Sleep(100);
            }
            return 0;
        }
    }
}
