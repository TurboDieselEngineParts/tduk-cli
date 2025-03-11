Feature: Hello Command

    Scenario: Running the hello command with a name
        Given I have a CLI application
        When I run the hello command with the name Behave
        Then the output should contain "Hello Behave"

    Scenario: Running the hello command with default
        Given I have a CLI application
        When I run the hello command with no name
        Then the output should contain "Hello World"

