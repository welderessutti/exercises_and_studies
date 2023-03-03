package com.mycompany.banksystem;

public class BankAccount {
    
    // ATTRIBUTES:
    private int bank;
    private int agency;
    private int chekingAccount;
    private int fund;
    private int credit;
    private PersonalData data;
    private int password;
    
    // CONSTRUCTOR:
    public BankAccount(
            int bank, int agency, int checkingAccount,
            int fund, int credit, int password,
            PersonalData data
            )
    {
        this.bank = bank;
        this.agency = agency;
        this.chekingAccount = checkingAccount;
        this.fund = fund;
        this.credit = credit;
        this.data = data;
        this.password = password;
    }
    
    // SETTERS:
    public void setBank(int bank) {
        this.bank = bank;
    }
    
    public void setAgency(int agency) {
        this.agency = agency;
    }
    
    public void setCheckingAccount(int checkingAccount) {
        this.chekingAccount = checkingAccount;
    }
    
    public void setFund(int fund) {
        this.fund = fund;
    }
    
    public void setCredit(int credit) {
        this.credit = credit;
    }
    
    public PersonalData setData() {
        return this.data;
    }
    
    public void setPassword(int password) {
        this.password = password;
    }
    
    
    // GETTERS:
    public int getBank() {
        return this.bank;
    }
    
    public int getAgency() {
        return this.agency;
    }
    
    public int getCheckingAccount() {
        return this.chekingAccount;
    }
    
    public int getFund() {
        return this.fund;
    }
    
    public int getCredit() {
        return this.credit;
    }
    
    public PersonalData getData() {
        return this.data;
    }
    
    public int getPassword() {
        return this.password;
    }

    // METHODS:
    public boolean checkFund(int amount) {
        return amount <= this.fund;
    }
    
    public void deposit(int amount) {
        this.fund += amount;
    }
    
    public boolean withdraw(int amount) {
        if (checkFund(amount)) {
            this.fund -= amount;
            return true;
        } else {
            System.out.println(
                    "Sorry, there aren´t enough funds for this amount."
            );
            return false;
        }
    }
    
    public void transfer(int amount, BankAccount account) {
        if (withdraw(amount)) {
            account.deposit(amount);
        }
    }
}
