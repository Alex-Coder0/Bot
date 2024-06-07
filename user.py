def add_user(user):
    file = open("config.txt", "a")
    file.write(user + "\n")
    file.close()


def del_user(user):
    with open("config.txt", 'r') as file:
        lines = file.readlines()

    updated_lines = [line for line in lines if line.strip() != user]

    with open("config.txt", 'w') as file:
        file.writelines(updated_lines)





