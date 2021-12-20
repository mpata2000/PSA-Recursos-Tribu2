# Created by Martin at 19/12/2021
Feature: # Enter feature name here

  Background: A running api and database
    Given a running api

  Scenario: Get hours
    When get hours is requested
    Then All existing hours are returned

  Scenario: Get hours by id
    When get hours is requested with "json"
