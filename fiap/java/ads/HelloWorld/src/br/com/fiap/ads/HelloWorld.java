package br.com.fiap.ads;

public class HelloWorld {

	public static void main(String[] args) {
		
		int idade = 34;
		double preco = 10.5;
		char sexo = 'M';
		boolean temFilhos = true;
		String hello = "Hello, World!";
		
		int x = 2000;
		float y = x;  //Dependendo do tamanho do int, não dá para converter para float.
		
		double z = 200.20;
		int w = (int) z;  //Converter double para int somente com cast e perde informação.
		
		System.out.println(hello + temFilhos + sexo + preco + idade);
		System.out.println(y + w);
	}
}
