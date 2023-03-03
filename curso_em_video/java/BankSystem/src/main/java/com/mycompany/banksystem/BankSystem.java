package com.mycompany.banksystem;

import static com.mycompany.banksystem.Login.userIndex;

public class BankSystem {
    
    public static BankAccount[] accountsList = new BankAccount[2];
    public static Menu menuOptions = new Menu();

    public static void main(String[] args) {
        
        boolean flag = true;
        
        while (flag) {
            flag = menuOptions.mainMenu(flag);
        }
        
        System.out.println(accountsList[userIndex].getFund());
    }
}
