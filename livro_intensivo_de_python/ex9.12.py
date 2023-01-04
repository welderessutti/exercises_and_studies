from privilege_admin_classes import Admin

administrador = Admin("Welder", "Ressutti", 34, 1.80, 92)

print(administrador.privileges.show_privileges())

print(f"The admin privileges are: ", end="")
for privilege in range(len(administrador.privileges.privileges)):
    if privilege != len(administrador.privileges.privileges) - 1:
        print(administrador.privileges.privileges[privilege], end=", ")
    else:
        print(administrador.privileges.privileges[privilege], end=".")
