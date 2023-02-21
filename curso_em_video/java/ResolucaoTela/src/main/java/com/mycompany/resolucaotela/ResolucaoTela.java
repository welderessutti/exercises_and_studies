package com.mycompany.resolucaotela;

import java.awt.*;

public class ResolucaoTela {

    public static void main(String[] args) {
        Dimension size = Toolkit.getDefaultToolkit().getScreenSize();
        
        int width = (int)size.getWidth();        
        int height = (int)size.getHeight();
        
        System.out.println("Sua tela tem resolução: " + width + " x " + height);
    }
}
