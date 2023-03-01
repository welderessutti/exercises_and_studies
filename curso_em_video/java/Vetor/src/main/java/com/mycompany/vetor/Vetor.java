package com.mycompany.vetor;

public class Vetor {

    public static void main(String[] args) {
        int[] vetor = new int[5];
        int[] vetorDeclarado = {0, 1, 2, 3, 4};
        
        for (int c = 0; c < vetor.length; c++) {
            vetor[c] = c;
        }
        
        System.out.println(vetor[0] + " " + vetor[1] + " " + vetor[2] + " "
                + vetor[3] + " " + vetor[4]);
        
        System.out.println(vetorDeclarado[0] + " " + vetorDeclarado[1] + " "
                + vetorDeclarado[2] + " " + vetorDeclarado[3] + " "
                + vetorDeclarado[4]);
        
        System.out.println(vetor.length);
    }
}
