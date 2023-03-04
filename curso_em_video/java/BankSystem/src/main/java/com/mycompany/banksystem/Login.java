package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import java.util.Scanner;

public class Login {

    public static BankAccount userAccount;

    public boolean validateLogin() {

        int userAgency;
        int userChekingAccount;
        int userPassword;
        Scanner input = new Scanner(System.in);

        System.out.println("Digit your agency number: ");
        userAgency = input.nextInt();

        System.out.println("Digit your checking account number: ");
        userChekingAccount = input.nextInt();

        if (findLoginAccount(userAgency, userChekingAccount)) {

            System.out.println("Digit your password: ");
            userPassword = input.nextInt();

            if (verifyPassword(userAccount, userPassword)) {
                return true;

            } else {                
                System.out.println("Invalid password.");
                userAccount = null;
                return false;
            }

        } else {
            System.out.println("Agency number or "
                    + "checking account number ivalid.");
            return false;
        }
    }

    public static boolean findLoginAccount(int userAgency, int userChekingAccount) {

        for (BankAccount thisAccount : accountsList) {

            if (thisAccount != null) {
                if (userAgency == thisAccount.getAgency()
                        && userChekingAccount == thisAccount.getCheckingAccount()) {
                    userAccount = thisAccount;
                    return true;
                }
            }

        }
        return false;
    }

    public static boolean verifyPassword(BankAccount userAccount, int userPassword) {
        return userAccount.getPassword() == userPassword;
    }
}
