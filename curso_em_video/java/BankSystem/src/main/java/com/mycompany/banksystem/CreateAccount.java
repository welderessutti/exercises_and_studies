package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import java.util.Scanner;

public class CreateAccount {
    
    public static int blankIndex;
    
    public void creator() {

        if (findBlankIndex()) {

            Scanner input = new Scanner(System.in);

            System.out.print("First Name: ");
            String firstName = input.nextLine();

            System.out.print("Last Name: ");
            String lastName = input.nextLine();

            System.out.print("Date of Birth: ");
            String dateOfBirth = input.nextLine();

            System.out.print("CPF: ");
            String cpf = input.nextLine();

            System.out.println("Bank: ");
            int bank = input.nextInt();

            System.out.println("Agency: ");
            int agency = input.nextInt();

            System.out.println("Checking Account: ");
            int checkingAccount = input.nextInt();

            System.out.println("Fund: ");
            int fund = input.nextInt();

            System.out.println("Credit: ");
            int credit = input.nextInt();

            System.out.println("Password: ");
            int password = input.nextInt();
            
            accountsList[blankIndex] = new BankAccount(bank, agency,
            checkingAccount, fund, credit, password, firstName, lastName,
            dateOfBirth, cpf);  
            
        } else {            
            System.out.println("List of account is full. Remove an account.");
        }
    }
    
    public static boolean findBlankIndex() {

        for (int count = 0; count < accountsList.length; count++) {
            if (accountsList[count] == null) {
                blankIndex = count;
                return true;
            }
        }
        return false;
    }
}
