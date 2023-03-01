/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package com.mycompany.switchcase;

import java.util.Scanner;

/**
 *
 * @author welder
 */
public class SwitchCase {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String tipo;
        int opcao;

        System.out.print("Digite um número: ");
        opcao = entrada.nextInt();

        switch (opcao) {
            case 1:
                tipo = "UM";
                break;
            case 2:
                tipo = "DOIS";
                break;
            case 3:
                tipo = "TRÊS";
                break;
            default:
                tipo = "INVÁLIDO!!!";
        }

        System.out.println(tipo);
    }
}
