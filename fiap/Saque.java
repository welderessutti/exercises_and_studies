package fiap;
import java.util.Scanner;

public class Saque {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
		  //Declaração de variáveis
		  int quantia, ced50, ced20, ced10;
		  // Solicita a quantia
		  System.out.println("Digite a quantia: ");
		  quantia = entrada.nextInt();
		  // Efetua o cálculo das quantias de cédulas
		  ced50 = quantia / 50;
		  quantia = quantia % 50;
		  ced20 = quantia / 20;
		  quantia = quantia % 20;
		  ced10 = quantia / 10;
		  quantia = quantia % 10;
		  // Exibe as quantidades de cédulas
		  System.out.println("Quantidade das cédulas 50: " + ced50);
	  System.out.println("Quantidade das cédulas 20: " + ced20);
	  System.out.println("Quantidade das cédulas 10: " + ced10);
	  entrada.close();
    }
}
