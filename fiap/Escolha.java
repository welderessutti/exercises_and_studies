package fiap;
import java.util.Scanner;

public class Escolha
{
	public static void main(String[] args)
	{
		Scanner entrada = new Scanner(System.in);
		int n;
		System.out.println("Digite um número:");
		n = entrada.nextInt();
	    // Verifica qual número foi digitado.
	    switch (n)
	    {
	    	case 1:
	    		System.out.println("Domingo"); break;
	    	case 2:
	    		System.out.println("Segunda-feira"); break;
	    	case 3:
	    		System.out.println("Terça-feira"); break;
	    	case 4:
	    		System.out.println("Quarta-feira"); break;
	    	case 5:
	    		System.out.println("Quinta-feira"); break;
	    	case 6:
	    		System.out.println("Sexta-feira"); break;
	    	case 7:
	    		System.out.println("Sábado"); break;
	    	default:
	    		System.out.println("Dia inválido");
	    }
	}
}
