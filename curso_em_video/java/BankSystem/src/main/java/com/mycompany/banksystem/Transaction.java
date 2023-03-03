package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import static com.mycompany.banksystem.Login.userIndex;

public class Transaction {
    
    public static int destinyIndex;

    public boolean checkFund(int amount) {        
        return amount <= accountsList[userIndex].getFund();
    }
    
    public void deposit(BankAccount destinyAccount, int depositAmount) {
        destinyAccount.setFund(destinyAccount.getFund() + depositAmount);
    }
    
    public boolean withdraw(int withdrawAmount) {

        if (checkFund(withdrawAmount)) {            
            accountsList[userIndex].setFund(accountsList[userIndex].getFund() - withdrawAmount);
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

        for (int count = 0; count < accountsList.length; count++) {  
            
            if (accountsList[count] != null){
                if (destinyAgency == accountsList[count].getAgency()
                        && destinyCheckingAccount == accountsList[count].getCheckingAccount()) {
                    destinyIndex = count;  // TESTAR FAZENDO A VARIÁVEL "DESTINYINDEX" RECEBENDO O OBJETO, E NÃO SOMENTE O ÍNDICE.
                    return true;
                }
            }
        }
        return false;
    }
}
