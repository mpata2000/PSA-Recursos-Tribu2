Feature: patch Hours

  Background: A running api and database
    Given a running api

  Scenario: patch not existing hours
    Given a random hours url id
      And a patch body with "{}"
      And id doest return hours
    When patch is requested
    Then not found error is returned

  Scenario: patch existing hours only user_id
    Given an existing hours url id
      And a patch body with "{"user_id":"test_patch"}"
    When patch is requested
    Then hours is updated

  Scenario: patch existing hours all information
    Given an existing hours url id
      And a patch body with "{"user_id": "1","task_id": "1","day": "2021-05-25","hours": 3,"minutes": 45,"seconds": 10,"note": "Descripcion"}"
    When patch is requested
    Then hours is updated
