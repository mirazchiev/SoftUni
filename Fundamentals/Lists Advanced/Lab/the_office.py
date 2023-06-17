def office(happiness: list, improvement: int):
    employees_happiness = []
    happy_count = 0
    unhappy_count = 0
    for employee in happiness:
        eh = employee * improvement
        employees_happiness.append(eh)
    for employee in employees_happiness:
        if employee > sum(employees_happiness) // len(employees_happiness):
            happy_count += 1
        else:
            unhappy_count += 1
    if happy_count > unhappy_count:
        return f"Score: {happy_count}/{len(employees_happiness)}. Employees are happy!"
    return f"Score: {happy_count}/{len(employees_happiness)}. Employees are not happy!"


rates_of_happiness = list(map(int, (input().split())))
happiness_improvement_factor = int(input())
result = office(rates_of_happiness, happiness_improvement_factor)
print(result)
