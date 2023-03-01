package com.mycompany.banksystem;

import java.util.Scanner;

public class BankSystem {
    
    /*public static void registerPerson() {
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("First Name: ");
        String firstName = input.nextLine();
        
        System.out.print("Last Name: ");
        String lastName = input.nextLine();
        
        System.out.print("Date of Birth: ");
        String dateOfBirth = input.nextLine();
        
        System.out.print("CPF: ");
        String cpf = input.nextLine();
        
        PersonalData welder = new PersonalData(firstName, lastName, dateOfBirth, cpf);
    }*/
    
    public static void menu() {
        
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
                break;
            default:
                System.out.println("Invalid Option!");
        }
    }

    public static void main(String[] args) {
        menu();
    }
}
