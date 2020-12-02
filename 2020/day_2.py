def read_passwords(file):
    """
    Reading a file with a list of dictionaries 
    with password policy, letter and password.
    """
    list_of_passwords = []
    for line in f:
        conditions = line.split(" ")
        password_policy = [int(conditions[0].split("-")[0]),
                           int(conditions[0].split("-")[1]) + 1]
        letter = conditions[1][0]
        password = conditions[2].split("\n")[0]
        list_of_passwords.append({"password_policy": password_policy,
                                  "letter": letter, 
                                  "password": password})
    return list_of_passwords


def count_valid_passwords_first(list_of_passwords):
    """
    Count the number of passwords that have a given password policy numbers of letters.
    """
    result = [1 for line in list_of_passwords if line["password"].count(line["letter"]) in range(*line["password_policy"])]
    return sum(result)


def count_valid_passwords_second(list_of_passwords):
    """
    Count the number of passwords that have only one letter in indices of password policy.
    """
    result = [1 for line in list_of_passwords if (line["password"][line["password_policy"][0]-1] == line["letter"])^
              (line["password"][line["password_policy"][1]-2] == line["letter"])]
    return sum(result)

f = open('day_2.txt')
list_of_passwords = read_passwords(f)
print(count_valid_passwords_second(list_of_passwords))