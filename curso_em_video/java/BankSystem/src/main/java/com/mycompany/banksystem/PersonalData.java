package com.mycompany.banksystem;

public class PersonalData {
    
    // ATTRIBUTES:
    private String firstName;
    private String lastName;
    private String dateOfBirth;
    private String cpf;
    
    // CONSTRUCTOR:
    public PersonalData(
            String firstName, String lastName,
            String dateOfBirth, String cpf)
    {
        this.firstName = firstName.toUpperCase();
        this.lastName = lastName.toUpperCase();
        this.dateOfBirth = dateOfBirth;
        this.cpf = cpf;
    }
    
    // SETTERS:
    public void setFirstName(String firstName) {
        this.firstName = firstName.toUpperCase();
    }
    
    public void setLastName(String lastName) {
        this.lastName = lastName.toUpperCase();
    }
    
    public void setDateOfBirth(String dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    
    // GETTERS:
    public String getFirstName() {
        return this.firstName;
    }
    
    public String getLastName() {
        return this.lastName;
    }
    
    public String getDateOfBirth() {
        return this.dateOfBirth;
    }
    
    public String getCpf() {
        return this.cpf;
    }
}
