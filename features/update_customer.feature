Feature: Update customer

  Scenario: An existing customer's name has changed
    Given customer "Joe Bloggs" with ID "2" exists
    When I update the surname of customer with ID "2" to "Smith"
    And I fetch customer "2"
    Then  I should see customer "Joe Smith"
