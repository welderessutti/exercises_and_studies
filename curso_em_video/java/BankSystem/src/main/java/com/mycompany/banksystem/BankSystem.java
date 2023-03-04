package com.mycompany.banksystem;

import java.util.ArrayList;

public class BankSystem {

    public static ArrayList<BankAccount> accountsList = new ArrayList<>();
    public static Menu menuOptions = new Menu();

    public static void main(String[] args) {

        boolean flag = true;

        while (flag) {
            flag = menuOptions.mainMenu(flag);
        }
    }
}
