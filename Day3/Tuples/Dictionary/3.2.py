students = [
            {"name":"Rita","marks":88},
            {"name":"sana","marks":91},
            {"name":"Aaliya","marks":87}
           ]
topper = students[0]

for s in students:
    if s["marks"]> topper["marks"]:
        topper = s
print(topper)