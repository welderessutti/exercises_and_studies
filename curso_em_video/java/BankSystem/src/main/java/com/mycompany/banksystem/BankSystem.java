package com.mycompany.banksystem;

import java.util.Scanner;

public class BankSystem {
    
    public static BankAccount[] accountsList = new BankAccount[10];
    public static boolean flag = true;
    
    public static boolean menu(boolean flag) {
        
        Scanner input = new Scanner(System.in);
        
        System.out.println(
                "== MENU ==\n"
              + "1 - CREATE ACCOUNT\n"
              + "2 - DEPOSIT\n"
              + "3 - WITHDRAW\n"
              + "4 - TRANSFER\n"
              + "5 - SHOW ACCOUNT DETAILS\n"
              + "6 - SHOW REGISTERED ACCOUNTS\n"
              + "7 - DELETE ACCOUNT\n"
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
            case 5:
                break;
            case 6:
                break;
            case 7:
                break;
            case 0:
                flag = false;
                break;
            default:
                System.out.println("Invalid Option!");
        }
        return flag;
    }

    public static void main(String[] args) {
        
        /*while (flag) {
            flag = menu(flag);
        }*/
                
        System.out.println(CreateAccount.fullListChecker());
    }
}
