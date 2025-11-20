student_info = []
first_id = 1

def student_information(name, course, form):
  global first_id
  ID = f"{first_id:04}"
  student_informations = {"name": name, "course": course, "form": form, "ID": ID}
  student_info.append(student_informations)
  first_id += 1
  return student_informations
student_information("Adom Bempong Franklin", "General Science", 22020618)
student_information("Mensah Kwame Moses", "General Science", 22127930)

print(student_info)
