#include <stdio.h>
#include <string.h>
#include <locale.h>

typedef struct
{
    char nome[20], raca[20], classe[20];
    int INT, CAR, SAB, FOR, CON, DES;
    int hp, idade;
}t_personagem;

int main() {
    setlocale(LC_ALL, "portuguese");
    char char_usuario[20];
    int int_usuario;
    int binario = 0;
    t_personagem escolha;


    printf("\n\n\n_-_-_-_- CRIANDO PERSONAGEM DE RPG -_-_-_-_\n\n");
    printf("qual o nome do seu personagem? ");
    fgets(escolha.nome, 20, stdin);
    printf("o nome escolhido foi: %s\n", escolha.nome);
    //escolhendo o nome do personagem


    printf("selecione sua raca para ver ou escolher:\n");
    printf(" 1. Humano\n 2. Elfo\n 3. Anao\n");
    printf("\ndigite o numero: ");
    scanf("%d", &int_usuario);
    while (int_usuario < 1 || int_usuario > 3)
    {
        printf("numero invalido, digite novamente\n");
        printf(" 1. Humano\n 2. Elfo\n 3. Anão\n");
        printf("\ndigite o numero: ");
        scanf("%d", &int_usuario);
    }
    //primeira seleção da raça com correção de erro

    while (binario == 0){
    switch (int_usuario) {
    case 1:
        strcpy(escolha.raca, "humano");
        printf("\nraca %s -_-_-_-_\n", escolha.raca);
        printf("1. ver status \n2. elfo \n3. anao \n4. para escolher humano \n");
        printf("\ndigite o numero: ");
        scanf("%d", &int_usuario);
        if (int_usuario == 1)
        {
            printf("\n status: \n+2 de carisma\n");
            printf("\n1. escolher humano \n2. elfo \n3. anao \n");
            printf("\ndigite o numero: ");
            scanf("%d", &int_usuario);
            if (int_usuario == 1)
            {   int_usuario = 4;    }
        } 
    break; //Escolha da raca humano

    case 2:
        strcpy(escolha.raca, "Elfo");
        printf("\nraca %s -_-_-_-_\n", escolha.raca);
        printf("1. humano \n2. para ver status \n3. anao \n4. para escolher elfo \n");
        printf("\ndigite o numero: ");
        scanf("%d", &int_usuario);
        if (int_usuario == 2)
        {
            printf("\nstatus: \n+2 de carisma\n");
            printf("\n1. humano \n2. escolher elfo \n3. anao \n");
            printf("\ndigite o numero: \n");
            scanf("%d", &int_usuario);
            if (int_usuario == 2)
            {   int_usuario = 4;    }
        }
    break; //escolha da raça elfo
        
    case 3:
        strcpy(escolha.raca, "Anao");
        printf("\nraca %s -_-_-_-_\n", escolha.raca);
        printf("1. humano 2 \n2. elfo \n3. para ver status \n4. para escolher anao \n");
        printf("\ndigite o numero: ");
        scanf("%d", &int_usuario);
        if (int_usuario == 3)
        {
            printf("\nstatus: \n+2 de carisma\n");
            printf("\n1. humano \n2. elfo \n3. escolher anao \n");
            printf("\ndigite o numero: \n");
            scanf("%d", &int_usuario);
            if (int_usuario == 3)
            {   int_usuario = 4;    }
        }
            
    break; //escolha da raça anao

    case 4:
        binario = 1;
    break; //saída do código
    
    default:
    while (int_usuario < 1 || int_usuario > 3)
    {
    printf("numero invalido, digite novamente\n");
    printf("selecione sua raca para ver ou escolher:\n");
    printf(" 1. Humano\n 2. Elfo\n 3. Anão\n");
    printf("\ndigite o numero: ");
    scanf("%d", &int_usuario);
    } //correção de
     }
      }
    //confirmação de raça
      printf("raca %s escolhida", escolha.raca);

    printf("\nselecione sua classe para ver ou escolher:\n");
    printf(" 1. ladino\n 2. mago\n 3. guerreiro\n 4. bruxo");
    printf("\ndigite o numero: ");
    scanf("%d", &int_usuario);




    printf("\n \n \n         ss\ncafe     ss\n   (o-o)-||\n\n . . . . finalizando projeto . . . . .");
    return 0;
}