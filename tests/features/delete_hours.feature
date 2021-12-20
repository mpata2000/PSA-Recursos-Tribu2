Feature: Delete Hours

  Background: A running api and database
    Given a running api

  Scenario: Delete existing hours
    Given an existing hours url id
    When delete is requested
    Then hours are deleted

  Scenario: Delete not existing hours
    Given a random hours url id
      And id doest return hours
    When delete is requested
    Then not found error is returned
