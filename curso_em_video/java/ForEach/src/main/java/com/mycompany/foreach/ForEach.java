package com.mycompany.foreach;

public class ForEach {

    public static void main(String[] args) {
        int[] vetor = new int[5];
        int[] vetorDeclarado = {4, 1, 3, 0, 2};
        
        for (int valor: vetorDeclarado) {
            System.out.print(valor);
        }
    }
}
