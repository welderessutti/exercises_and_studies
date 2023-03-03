package com.mycompany.banksystem;

import java.util.Scanner;

public class Menu {
    
    public static CreateAccount newAccount = new CreateAccount();
    public static Login newLogin = new Login();
    
    public boolean mainMenu(boolean flag) {
        
        boolean flag2 = true;
        Scanner input = new Scanner(System.in);

        System.out.println(
                "== MENU ==\n"
              + "1 - CREATE ACCOUNT\n"
              + "2 - ACCESS ACCOUNT\n"
              + "3 - SHOW ACCOUNT DETAILS\n"
              + "4 - SHOW REGISTERED ACCOUNTS\n"
              + "5 - DELETE ACCOUNT\n"
              + "0 - EXIT\n");
        System.out.print("Choose an option: ");
        int option = input.nextInt();

        switch (option) {
            case 1:
                newAccount.creator();
                break;
            case 2:
                if (newLogin.validateLogin()) {                    
                    while (flag2) {                        
                    flag2 = accountMenu(flag2);
                    }
                }                
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                break;
            case 0:
                flag = false;
                break;
            default:
                System.out.println("Invalid Option!");
        }
        return flag;
    }
    
    public boolean accountMenu(boolean flag2) {
        
        Scanner input = new Scanner(System.in);

        System.out.println(
                "== MENU ==\n"
              + "1 - DEPOSIT\n"
              + "2 - WITHDRAW\n"
              + "3 - TRANSFER\n"
              + "4 - SHOW FUNDS\n"
              + "0 - EXIT\n");
        System.out.print("Choose an option: ");
        int option = input.nextInt();

        switch (option) {
            case 1:
                break;
            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
            case 0:
                flag2 = false;
                break;
            default:
                System.out.println("Invalid Option!");
        }
        return flag2;
    }
}
