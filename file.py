def greet(name):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


def check_admin(password):
    admin_password = "Admin@12345"

    if password == admin_password:
        return "Access granted"
    return "Access denied"


if __name__ == "__main__":
    print(greet("Student"))
    print("Sum:", add_numbers(10, 20))
    print(check_admin("Admin@12345"))
