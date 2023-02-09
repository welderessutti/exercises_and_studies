package fiap.java;
import java.util.Scanner;

public class Funcao_notas {

	// Função que verifica se ma nota é válida
	public static boolean nota_valida(float nota) {
		if (nota >= 0 && nota <= 10){
			return true;
		} else {
			return false;
		}
	}

	// Função que retorna o menor entre 3 valores
	public static float menor3n(float n1, float n2, float n3) {
		// Verifica qual a menor nota
		float menor = n1;
		if (n2 < menor) {
			menor = n2;
		}
		if (n3 < menor)	{
			menor = n3;
		}
		return (menor);
	}

	// Função que retorna a média de 3 números
	private static float media2maiores(float n1, float n2, float n3) {
		float menor = menor3n(n1,n2,n3);
		return (n1 + n2 + n3 - menor) / 2;
	}

	// Procedimento que exibe a mensagem da media semestral
	private static void msg_media_semestral(float m) {
		System.out.println("A sua média semestral é " + m);
	}

	// Função que calcula a média de dois números
	public static float media2n(float n1, float n2) {
		return (n1 + n2) / 2;
	}

	// Função que retorna mensagem de aprovado ou não no exame
	public static String msg_aprovado_exame(float m) {
		if(m < 5) {
			return ("Reprovado em exame com media " + m);
		} else {
			return ("Aprovado em exame com media " + m);
		}
	}

	public static void main(String[] args) {
		// Estancia o objeto Teclado para ler variáveis
		Scanner teclado = new Scanner(System.in);

		// Declaração das variáveis
		float nota1, nota2, nota3, media_semestral, nota_exame, media_exame, menor_nota;

		System.out.print("Nota 1:");
		nota1 = teclado.nextFloat();
		// chamada da função 'nota_valida'
		if (nota_valida(nota1)) {
			System.out.print("Nota 2:");
			nota2 = teclado.nextFloat();

			if (nota_valida(nota2)) {
				System.out.print("Nota 3:");
				nota3 = teclado.nextFloat();

				if (nota_valida(nota3)) {
					// Chamada da função 'menor3n'
					menor_nota = menor3n(nota1, nota2, nota3);

					// chamada da função 'media2maiores' que calcula a media descartando a menor
					media_semestral = media2maiores(nota1, nota2, nota3);

					// chamada do procedimento que exibe a mensagem da media semestral
		  	  		msg_media_semestral(media_semestral);

		  	         // Verifica o status do aluno
					if (media_semestral < 4) {
						System.out.println("Você está reprovado direto");
					} else if (media_semestral >= 7) {
						System.out.println("Você está aprovado direto");
					} else {
						// Solicita uma nota em caso de exame
						System.out.println("VOCÊ FICOU EM EXAME");
						nota_exame = teclado.nextFloat();
						if(nota_valida(nota_exame)) {
							// chamada da função media_exame que calcula a media
							media_exame = media2n(media_semestral, nota_exame);

							// chamada da função msg_aprovado_exame
							System.out.println(msg_aprovado_exame(media_exame));
						} else {
							System.out.println("Nota de exame" + nota_exame + "Inválida");
						}
					}
				} else {
					System.out.println("Nota 3 " + nota3 + " - É inválida");
				}
			} else {
				System.out.println("Nota 2 " + nota2 + " - É inválida");
			}
		} else {
			System.out.println("Nota 1 " + nota1 + " - É inválida");
		}
        teclado.close();
	}
}
