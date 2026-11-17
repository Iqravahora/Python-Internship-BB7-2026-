salaries = {"zayan":4000, "aaman":6000,"sahil":5000,"raj":7000}
sorted_emp = sorted(salaries.items(), key=lambda x:x[1], reverse=True)
print(sorted_emp[:3])
