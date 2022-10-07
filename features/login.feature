Feature: Login
#  Scenario: Standard user login
#    Given  the Login page is open
#    When the user logs in with username and password
#    And  clicks button login
#    Then the message "PRODUCTS" is shown

#      Scenario: Successful Standard user logout
#    Given  the Login page is open
#    When the user logs in with username and password
#    And  clicks button login
#    Then the message "PRODUCTS" is shown
#    And  the user clicks on the menu and click on logout


#  Scenario: Locked out user login
#    Given the Login page is open
#    When the user logs in with "locked_out_user" username and "secret_sauce" password
#    And  clicks button login
#    Then the message "Epic sadface: Sorry, this user has been locked out." is shown
##
#  Scenario: Problem user login
#    Given  the Login page is open
#    When the user logs in with "problem_user" username and "secret_sauce" password
#    And  clicks button login
#     Then the message "PRODUCTS" is shown

#  Scenario: Performance glitch user login
#    Given  the Login page is open
#    When the user logs in with "performance_glitch_user" username and "secret_sauce" password
#    And  clicks button login
#     Then the message "PRODUCTS" is shown

#
  Scenario Outline: All login
    Given  the Login page is open
    When the user logs in with "<username>" username and "<password>" password
    And  clicks button login
     Then the message "<message>" is shown


    Examples: Usernames and Password
      |username  | password | message |
#      | standard_user        |alizwa | Epic sadface: Username and password do not match any user in this service |
      | standard_user  |secret_sauce | PRODUCTS|
#      | locked_out_user  |secret_sauce | Epic sadface: Sorry, this user has been locked out. |
      | problem_user        |secret_sauce | PRODUCTS |
      | performance_glitch_user  |secret_sauce | PRODUCTS |




#    Scenario: Incorrect username or password user login
#    Given the Login page is open
#    When the user logs in with "Alizwa" username and "secret_sauce" password
#    And  clicks button login
#    Then the message "Epic sadface: Username and password do not match any user in this service" is shown
