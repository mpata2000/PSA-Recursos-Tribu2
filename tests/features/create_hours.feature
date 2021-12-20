Feature: Create Hours

  Background: some requirement of this test
    Given a running api

  Scenario: Create hours with all the information
    Given hours with "user_id","task_id","1","1","1","2020-10-10" and "note"
      And it isnt created already with "user_id","task_id" and "2020-10-10"
    When we request a create hours
    Then a hours is created correctly



