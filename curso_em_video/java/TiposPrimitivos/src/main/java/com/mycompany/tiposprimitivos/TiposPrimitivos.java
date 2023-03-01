/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package com.mycompany.tiposprimitivos;

import java.util.Scanner;

/**
 *
 * @author welder
 */
public class TiposPrimitivos {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        boolean logico = true;
        char a = 'A';
        String abc = "ABC";
        byte num1 = 1;
        short num2 = 2;
        int num3 = 3;
        long num4 = 4;
        float num5 = 5.5f;
        double num6 = 6.6;
        
        System.out.print("Digite seu nome: ");
        String nome = teclado.nextLine();
        
        System.out.printf("%s, %b, %s, %s, %d, %d, %d, %d, %.2f, %.2f",
                nome, logico, a, abc, num1, num2,
                num3, num4, num5, num6);
    }
}
