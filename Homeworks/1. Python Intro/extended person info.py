name = input()
age = int(input())
town = input()
salary = float(input())

if age < 18:
    ageRange = "teen"
elif age < 70:
    ageRange = "adult"
else:
    ageRange = "elder"

if salary < 500:
    salaryRange = "low"
elif salary < 2000:
    salaryRange = "medium"
else:
    salaryRange = "high"

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Town: {town}')
print('Salary: ${:.2f}'.format(salary))
print(f'Age range: {ageRange}')
print(f'Salary range: {salaryRange}')
