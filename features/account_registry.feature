Feature: Account registry

    Scenario: User is able to create a new account 
        Given Account registry is active
        When I create an account using name: "kurt", last name: "cobain", pesel: "89091209875"  
        Then Number of accounts in registry equals: "1"
        And Account with pesel "89091209875" exists in registry

    Scenario: User is able to create a second account
        #TODO

    Scenario: User is able to delete already created account
        Given Account with pesel "89091209875" exists in registry
        When I delete account with pesel: "89091209875"
        Then Account with pesel "89091209875" does not exists in registry

    Scenario: Admin user is able to clear the account registry
        When I clear the account reagistry
        #TODO add check that registry is empty

    Scenario: User is able to update last name saved in account
        #TODO