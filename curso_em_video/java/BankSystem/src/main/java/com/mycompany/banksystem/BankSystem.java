package com.mycompany.banksystem;

public class BankSystem {
    
    public static BankAccount[] accountsList = new BankAccount[2];
    public static Menu menuOptions = new Menu();

    public static void main(String[] args) {
        
        boolean flag = true;
        
        while (flag) {
            flag = menuOptions.mainMenu(flag);
        }
        
        System.out.println(accountsList[0].getData().getFirstName());
    }
}
