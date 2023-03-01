/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.fatorial;

import java.util.Scanner;

/**
 *
 * @author welder
 */
public class Fatorial {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int fat = 1;
        
        System.out.print("Fatorial de: ");
        int cont = entrada.nextInt();
        
        while (cont >= 1) {
            fat *= cont;
            if (cont > 1) {
                System.out.printf("%d x ", cont);
            } else {
                System.out.printf("%d = ", cont);
            }            
            cont--;
        }
        System.out.println(fat);
    }
}
