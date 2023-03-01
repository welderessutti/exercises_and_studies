package com.mycompany.sistemadecadastro;

import java.util.Scanner;

public class SistemaDeCadastro {

    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        boolean continuaOuNao = true;
        
        while (continuaOuNao) {
            System.out.println(""
                + "--MENU--\n"
                + "0 - Sair\n"
                + "1 - Cadastrar\n"
                + "2 - Visualizar\n"
                + "3 - Apagar\n"
                + "4 - Limpar");
            
            System.out.print("Digite a opção: ");
            int opcao = entrada.nextInt();
        
            switch (opcao) {
                case 0:
                    continuaOuNao = false;
                    break;
                case 1:
                    break;
                case 2:
                    break;
                case 3:
                    break;
                case 4:
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        }
        System.out.println("Saindo...");
    }
}
