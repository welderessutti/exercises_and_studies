package fiap;
import java.util.Scanner;

public class Votos {
	public static void main(String[] args) {
		// Estancia o objeto Teclado para ler variáveis
		Scanner teclado = new Scanner(System.in);

		// Declaração das variáveis
		int hug, zez, lui, voto;

		// zera as variáveis dos candidatos
		hug = zez = lui = 0;
		System.out.println("1 - Huguinho: ");
		System.out.println("2 - Zezinho: ");
		System.out.println("3 - Luizinho: ");
		System.out.println("0 - Sair: ");

		// início do laço Faça-Enquanto
		do {
			System.out.println("Digite o voto:");
			voto = teclado.nextInt();
			switch(voto) {
                case 0 : System.out.println("Saindo..."); break;
				case 1 : hug++; break;
				case 2 : zez++; break;
				case 3 : lui++; break;
				default : System.out.println("Voto inválido, digite: 1, 2 ou 3");
			}
		} while(voto != 0);

        // Exibe o resultado da apuração
		System.out.println("1 - Huguinho: " + hug + "Votos");
		System.out.println("2 - Zezinho: " + zez + "votos");
		System.out.println("3 - Luizinho: " + lui + "votos");
        teclado.close();
	}
}
