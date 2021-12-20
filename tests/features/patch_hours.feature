Feature: patch Hours

  Background: A running api and database
    Given a running api

  Scenario: patch not existing hours
    Given a random hours url id
      And a patch body with "{}"
      And id doest return hours
    When patch is requested
    Then not found error is returned

  Scenario: patch existing hours
    Given an existing hours url id
      And a patch body with "{""}"
    When patch is requested
    Then not found error is returned
