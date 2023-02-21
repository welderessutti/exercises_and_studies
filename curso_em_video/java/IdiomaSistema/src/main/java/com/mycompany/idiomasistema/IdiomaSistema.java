package com.mycompany.idiomasistema;

import java.util.Locale;

public class IdiomaSistema {

    public static void main(String[] args) {
        Locale localAtual;
        String idioma;
        
        localAtual = Locale.getDefault();
        idioma = localAtual.getDisplayLanguage();
        
        System.out.println("Seu sistema está em: " + idioma);
    }
}
