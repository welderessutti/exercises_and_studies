package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import static com.mycompany.banksystem.Login.userAccount;

public class Transaction {

    public static BankAccount destinyAccount;

    public boolean checkFund(int amount) {
        return amount <= userAccount.getFund();
    }

    public void deposit(BankAccount destinyAccount, int depositAmount) {
        destinyAccount.setFund(destinyAccount.getFund() + depositAmount);
    }

    public boolean withdraw(int withdrawAmount) {

        if (checkFund(withdrawAmount)) {
            userAccount.setFund(userAccount.getFund() - withdrawAmount);
            return true;

        } else {
            System.out.println(
                    "Sorry, there aren´t enough funds for this amount."
            );
            return false;
        }
    }

    public void transfer(BankAccount destinyAccount, int transferAmount) {
        if (withdraw(transferAmount)) {
            deposit(destinyAccount, transferAmount);
        }
    }

    public boolean findDestinyAccount(int destinyAgency, int destinyCheckingAccount) {

        for (BankAccount thisAccount : accountsList) {

            if (thisAccount != null) {
                if (destinyAgency == thisAccount.getAgency()
                        && destinyCheckingAccount == thisAccount.getCheckingAccount()) {
                    destinyAccount = thisAccount;
                    return true;
                }
            }
        }
        return false;
    }
}
