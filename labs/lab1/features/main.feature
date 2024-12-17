Feature: Solving Bi-Quadratic Equations

  Scenario: No real roots for bi-quadratic equation
    Given the coefficients a = 1, b = 0, c = 1
    When I solve the bi-quadratic equation
    Then the result should be "Корней нет"

  Scenario: One real root for bi-quadratic equation
    Given the coefficients a = 1, b = 0, c = 0
    When I solve the bi-quadratic equation
    Then the result should contain "Один корень: 0"

  Scenario: Four real roots for bi-quadratic equation
    Given the coefficients a = 1, b = -5, c = 4
    When I solve the bi-quadratic equation
    Then the result should contain "Четыре корня: 2.0 и -2.0 и 1.0 и -1.0"