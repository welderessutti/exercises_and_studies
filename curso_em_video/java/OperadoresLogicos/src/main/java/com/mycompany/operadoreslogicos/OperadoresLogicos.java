/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.operadoreslogicos;

/**
 *
 * @author welder
 */
public class OperadoresLogicos {

    public static void main(String[] args) {
        int x, y, z;
        String r;
        x = 4;
        y = 7;
        z = 12;
        
        r = (x < y && y < z) ? "SIM" : "NÃO";
        System.out.println(r);
        r = !(x < y && y < z) ? "SIM" : "NÃO";
        System.out.println(r);
        r = (x < y || y < z) ? "SIM" : "NÃO";
        System.out.println(r);
        r = (x < y ^ y < z) ? "SIM" : "NÃO";
        System.out.println(r);
    }
}
