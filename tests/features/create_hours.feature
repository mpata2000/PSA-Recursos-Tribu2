Feature: Create Hours

  Background: some requirement of this test
    Given a running api

  Scenario: Create hours with all the information
    Given hours with "user_id","task_id","1","1","1","2020-10-10" and "note"
      And it isnt created already with "user_id","task_id" and "2020-10-10"
    When we request a create hours
    Then a hours is created correctly

  Scenario: Create hours with empty note
    Given hours with "user_id","task_id","1","1","1" and "2020-10-10"
      And it isnt created already with "user_id","task_id" and "2020-10-10"
    When we request a create hours
    Then a hours is created correctly

  Scenario: Create hours with empty note
    Given hours with "user_id","task_id","1","1","1" and "2020-10-10"
      And it is created already with "user_id","task_id" and "2020-10-10"
    When we request a create hours
    Then conlifct is thrown


  Scenario: Create hours with more than 23 hours
    Given hours with "user_id","task_id","24","1","1" and "2020-10-10"
    When we request a create hours
    Then hours arent created and error 422

  Scenario: Create hours with more than 59 minutes
    Given hours with "user_id","task_id","1","60","1" and "2020-10-10"
    When we request a create hours
    Then hours arent created and error 422

  Scenario: Create hours with more than 59 seconds
    Given hours with "user_id","task_id","1","1","60" and "2020-10-10"
    When we request a create hours
    Then hours arent created and error 422

  Scenario: Create hours with incorect date format(ISO 8601)
    Given hours with "user_id","task_id","1","1","60" and "10-10-2020"
    When we request a create hours
    Then hours arent created and error 422

  Scenario: Create hours with invalid date format(ISO 8601)
    Given hours with "user_id","task_id","1","1","60" and "2020-13-44"
    When we request a create hours
    Then hours arent created and error 422
