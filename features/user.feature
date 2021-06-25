Feature: User has a profile
    Scenario: Restrict profile access user
    Given user object
    When user accesses profile
    Then user can view and edit individual profile. 
    
    I should not be able to view or edit anyone else's profile