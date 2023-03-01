/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.testetipos;

/**
 *
 * @author welder
 */
public class TesteTipos {

    public static void main(String[] args) {
        int num1 = 1;
        int num2 = 1;
        String numeroString1 = Integer.toString(num1);
        String numeroString2 = Integer.toString(num2);
        
        String palavra1 = "1";
        String palavra2 = "1";
        int palavraNum1 = Integer.parseInt(palavra1);
        int palavraNum2 = Integer.parseInt(palavra2);
        
        System.out.println(num1 + num2);  // Somando dois "int".
        System.out.println(numeroString1 + numeroString2);  // Concatenando duas "Strings".
        System.out.println(num1 + numeroString1);  // Concatenando "int" com "String".
        System.out.println("Isso é um inteiro " + num1 + " e isso também "
                + num2 + ".\n" + "Isso é uma String "
                + numeroString1 + " e isso também " + numeroString2 + ".");
        
        System.out.printf("Isso é um inteiro %d e isso também %d.\n"
                + "Isso é uma String %s e isso também %s."
                , num1, num2, numeroString1, numeroString2);
    }
}
