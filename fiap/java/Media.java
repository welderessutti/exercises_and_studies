package fiap.java;
import java.util.Scanner;

public class Media {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		//Declaração das variáveis
		float n1, n2, n3, n4, media;
		// Solicita quatro números ao usuário
		System.out.println("Digite 4 números:");

		n1 = entrada.nextFloat();
		n2 = entrada.nextFloat();
		n3 = entrada.nextFloat();
		n4 = entrada.nextFloat();
		// Calcula a média dos 4 números
		media = (n1 + n2 + n3 + n4) / 4;
		System.out.println("Média = " +  media);
		entrada.close();
	}
}
