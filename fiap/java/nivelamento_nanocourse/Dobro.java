package fiap.java;
import java.util.Scanner;

public class Dobro {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, dobro;

        System.out.print("Digite um número: ");
        num = entrada.nextInt();
        dobro = num + num;
        System.out.print("Dobro = " + dobro);
        entrada.close();
    }
}
