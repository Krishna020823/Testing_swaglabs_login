Feature: E-commerce checkout process

  Scenario: Successful checkout
    Given I am on the login page
    When I enter valid credentials
    And I add an item to the cart
    And I go to checkout
    And I fill out the checkout details
    Then I complete the checkout process
    And I should logout
