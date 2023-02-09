package fiap;
import java.util.Scanner;

public class Fatorial {
	public static void main(String[] args) {
		// Estancia o objeto Teclado para ler variáveis
		Scanner teclado = new Scanner(System.in);

		// Declaração das variáveis
		int n, fat;

		System.out.println("Digite um número: ");
		n = teclado.nextInt();

		fat = 1;

		while(n > 1) {
			fat *= n;
			n--;
		}

		System.out.println("Fatorial = " + fat);
        teclado.close();
	}
}
