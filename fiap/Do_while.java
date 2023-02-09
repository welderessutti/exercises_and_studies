package fiap;
import java.util.Scanner;

public class Do_while {
	public static void main(String[] args) {
		// Estancia o objeto Teclado para ler variáveis
		Scanner teclado = new Scanner(System.in);

		// Declaração das variáveis
		int num, mult, volta;

		System.out.println("Digite um número: ");
		num = teclado.nextInt();

		volta = 1;

		do {
			mult = num * volta;
			System.out.println(volta + "X" + num + "="+ mult);
			volta++;
		} while(volta <= 10);
        teclado.close();
	}
}
