package fiap.java;
import java.util.Scanner;

public class Matriz {

	public static void main(String[] args) {
		// Estancia o objeto Teclado para ler variáveis
		Scanner teclado = new Scanner(System.in);

		int [][] matriz = new int[3][4];

		// 1 - PREENCHER A MATRIZ
		System.out.println("PREENCHENDO A MATRIZ:");
		for(int l = 0; l < 3; l++){
			for(int c = 0; c < 4; c++){
				System.out.print("Matriz["+ l + "]["+ c + "]=");
				matriz[l][c] = teclado.nextInt();
			}
		}

		// 2 - EXIBIR A MATRIZ
		System.out.println("EXIBINDO A MATRIZ:");
		for(int l = 0; l < 3; l++){
			for(int c = 0; c < 4; c++){
				System.out.print("["+ l + "]["+ c + "] = " + matriz[l][c] +"	");
			}
			System.out.println();
		}

		// 3 - SOMAR OS ELEMENTOS DA MATRIZ
		int soma = 0;
		for(int l = 0; l < 3; l++){
			for(int c = 0; c < 4; c++){
				soma += matriz[l][c];
			}
			System.out.println();
		}
		System.out.println("Somatória da Matriz = " + soma);

		// 4 - BUSCAR UM ELEMENTO NO VETOR
		boolean achou = false;
		int elem;

		// Digitação do elemento que será procurado
		System.out.print("Digite o elemento: ");
		elem = teclado.nextInt();
        int linha = 0;
        int coluna = 0;

		for(int l = 0; l < 3; l++){
			for(int c = 0; c < 4; c++){
				// Caso encontre o elemento, interrompe a busca
				if (matriz[l][c] == elem) {
					achou = true;
                    linha = l;
                    coluna = c;
					break;
				}
			}
		}
		// Analisa se encontrou ou não o elemento
		if (achou) {
			System.out.println("Elemento "+ elem +" encontrado na linha "+ linha +" coluna "+ coluna +" da matriz.");
        } else {
			System.out.println("Elemento "+ elem +" NÃO encontrado na matriz.");
        }
        teclado.close();
	}
}
