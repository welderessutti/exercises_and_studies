package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import static com.mycompany.banksystem.Transaction.destinyIndex;
import static com.mycompany.banksystem.Login.userIndex;
import java.util.Scanner;

public class Menu {
    
    public static CreateAccount newAccount = new CreateAccount();
    public static Login newLogin = new Login();
    public static Transaction newTransaction = new Transaction();
    
    public boolean mainMenu(boolean flag) {
        
        boolean flag2 = true;
        int option;
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
        option = input.nextInt();

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

        int destinyAgency;
        int destinyCheckingAccount;
        int amount;
        int option;
        Scanner input = new Scanner(System.in);

        System.out.println(
                "== MENU ==\n"
              + "1 - DEPOSIT\n"
              + "2 - WITHDRAW\n"
              + "3 - TRANSFER\n"
              + "4 - SHOW FUNDS\n"
              + "0 - EXIT\n");
        System.out.print("Choose an option: ");
        option = input.nextInt();

        switch (option) {
            case 1:
                System.out.println("Agency: ");
                destinyAgency = input.nextInt();
                
                System.out.println("Checking Account: ");
                destinyCheckingAccount = input.nextInt();
                
                if (newTransaction.findDestinyAccount(destinyAgency, destinyCheckingAccount)) {                    
                    
                    System.out.println("Deposit amount: ");
                    amount = input.nextInt();
                    
                    newTransaction.deposit(accountsList[destinyIndex], amount);
                    
                } else {
                    System.out.println("Agency number or "
                    + "checking account number ivalid.");
                }                
                break;
            case 2:
                System.out.println(userIndex);
                System.out.println("Withdraw Amount: ");
                amount = input.nextInt();
                newTransaction.withdraw(amount);
                break;
            case 3:
                System.out.println("Agency: ");
                destinyAgency = input.nextInt();
                
                System.out.println("Checking Account: ");
                destinyCheckingAccount = input.nextInt();
                
                if (newTransaction.findDestinyAccount(destinyAgency, destinyCheckingAccount)) {                    
                    
                    System.out.println("Tranfer amount: ");
                    amount = input.nextInt();
                    
                    newTransaction.transfer(accountsList[destinyIndex], amount);
                    
                } else {
                    System.out.println("Agency number or "
                    + "checking account number ivalid.");
                }
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
