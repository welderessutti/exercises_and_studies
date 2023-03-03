package com.mycompany.banksystem;

import static com.mycompany.banksystem.BankSystem.accountsList;
import java.util.Scanner;

public class Login {
    
    public static int userIndex;
    
    public boolean validateLogin() {
        
        int userAgency;
        int userChekingAccount;
        int userPassword;
        Scanner input = new Scanner(System.in);
        
        System.out.println("Digit your agency number: ");
        userAgency = input.nextInt();
        
        System.out.println("Digit your checking account number: ");
        userChekingAccount = input.nextInt();
        
        if (findAccount(userAgency, userChekingAccount)) {
            
            System.out.println("Digit your password: ");
            userPassword = input.nextInt();
            
            if (verifyPassword(userIndex, userPassword)) {                
                return true;
                
            } else {                
                System.out.println("Invalid password.");
                return false;
            }  
            
        } else {            
            System.out.println("Agency number or "
                    + "checking account number ivalid.");             
            return false;
        }
    }
    
    public static boolean findAccount(int userAgency, int userChekingAccount) {
        
        for (int count = 0; count < accountsList.length; count++) {  
            
            if (userAgency == accountsList[count].getAgency() && 
                    userChekingAccount == accountsList[count].getCheckingAccount()) 
            {
                userIndex = count;
                return true;
            }
        }
        return false;
    }
    
    public static boolean verifyPassword(int userIndex, int userPassword) {        
        return accountsList[userIndex].getPassword() == userPassword;
    }
}
