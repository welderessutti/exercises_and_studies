package fiap.java;

public class Procedimento_parametro {
	// Criação do Procedimento
	public static void saudacao2(String usuario, int hora) {
		String msg;

		if (hora < 12) {
			msg = "bom dia!";
		} else if (hora < 18) {
			msg = "boa tarde!";
		} else {
			msg = "boa noite!";
		}

		System.out.println("Ola "+ usuario + ", " + msg + " Você está logado.");
	}

	// Chamada do Procedimento - Programa Principal
	public static void main(String[] args) {
		saudacao2("Welder", 16);
	}
}
