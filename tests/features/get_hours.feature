# Created by Martin at 19/12/2021
Feature: Get Hours

  Background: A running api and database
    Given a running api

  Scenario: Get hours
    When get hours is requested
    Then All existing hours are returned

  Scenario: Get hours by with all info
    Given a created hour
    When get hours is requested with created data
    Then only one existing hour is return

  Scenario: Get hours by id
    Given a created hour
    When get hours is requested with id
    Then only one existing hour is return

  Scenario: Get hours with no existing id
    Given a created hour
    When get hours is requested with "{"ids":"test_get_no_id"}"
    Then get is succesful and empty
