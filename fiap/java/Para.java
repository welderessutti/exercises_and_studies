package fiap.java;
import java.util.Scanner;

public class Para {
	public static void main(String[] args) {
		// Estancia o objeto Teclado para poder ler variáveis
		Scanner teclado = new Scanner(System.in);

		// Declaração das variáveis
		float i, n, soma = 0;
		System.out.println("Digite 10 números: ");
		
		for (i = 1; i <= 10; i++) {
			n = teclado.nextFloat();
			soma += n;
		}
		
		System.out.println("Somatória = " + soma);
	}
}
