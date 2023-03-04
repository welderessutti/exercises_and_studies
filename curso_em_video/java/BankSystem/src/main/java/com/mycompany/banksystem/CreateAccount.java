package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import java.util.Scanner;

public class CreateAccount {

    public void creator() {

        Scanner input = new Scanner(System.in);

        System.out.print("First Name: ");
        String firstName = input.nextLine();

        System.out.print("Last Name: ");
        String lastName = input.nextLine();

        System.out.print("Date of Birth: ");
        String dateOfBirth = input.nextLine();

        System.out.print("CPF: ");
        String cpf = input.nextLine();

        System.out.print("Bank: ");
        int bank = input.nextInt();

        System.out.print("Agency: ");
        int agency = input.nextInt();

        System.out.print("Checking Account: ");
        int checkingAccount = input.nextInt();

        System.out.print("Fund: ");
        int fund = input.nextInt();

        System.out.print("Credit: ");
        int credit = input.nextInt();

        System.out.print("Password: ");
        int password = input.nextInt();

        accountsList.add(new BankAccount(bank, agency,
                checkingAccount, fund, credit, password, firstName, lastName,
                dateOfBirth, cpf));
    }
}
