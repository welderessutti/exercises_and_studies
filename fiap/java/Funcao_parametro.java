package fiap.java;
import java.util.Scanner;

public class Funcao_parametro {
	// Criação da função
	public static int maior2n(int num1, int num2) {
		int maior;

		if (num1 > num2) {
			maior = num1;
		} else {
			maior = num2;
		}
		return maior;
	}
	// Programa principal
	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		int n1, n2;

		System.out.println("Digite um número: ");
		n1 = teclado.nextInt();

		System.out.println("Digite outro número: ");
		n2 = teclado.nextInt();

		System.out.println("Maior numero = " + maior2n(n1, n2));
        teclado.close();
	}
}
