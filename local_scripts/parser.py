from prettytable import PrettyTable

x = PrettyTable()

csvfile = "logins.csv"


def parse_file(file):
    x.field_names = ["URL", "USERNAME", "PASSWORD"]
    rfile = open(file, "r", encoding="utf-8")
    for l in rfile.readlines():
        line = l.split(",")
        username = line[0]
        url = line[1]
        password = line[2]
        x.add_row([username, url, password])
        # print(f"{line[0]} {line[1]} {line[2]}")

    print(x)

parse_file(csvfile)
