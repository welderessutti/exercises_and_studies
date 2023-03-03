package com.mycompany.banksystem;

import java.util.Scanner;

public class BankSystem {
    
    public static void registerPerson() {
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("First Name: ");
        String firstName = input.nextLine();
        
        System.out.print("Last Name: ");
        String lastName = input.nextLine();
        
        System.out.print("Date of Birth: ");
        String dateOfBirth = input.nextLine();
        
        System.out.print("CPF: ");
        String cpf = input.nextLine();
        
        PersonalData welder = new PersonalData(
                firstName, lastName, dateOfBirth, cpf);
        
        createAccount(welder);
    }
    
    public static void createAccount(PersonalData person) {
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("Bank: ");
        int bank = input.nextInt();
        
        System.out.println("Agency: ");
        int agency = input.nextInt();
        
        System.out.println("Checking Account: ");
        int checkingAccount = input.nextInt();
        
        System.out.println("Balance: ");
        int balance = input.nextInt();
        
        System.out.println("Credit: ");
        int credit = input.nextInt();
        
        System.out.println("Password: ");
        int password = input.nextInt();
        
        BankAccount welder = new BankAccount(bank, agency, checkingAccount,
            balance, credit, password, person);
    }
    
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
        
        BankAccount[] accountsList = new BankAccount[10];
        
        boolean flag = true;
        
        while (flag) {
            flag = menu(flag);
        }
    }
}
