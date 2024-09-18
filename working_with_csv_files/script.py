import csv
hosts = [["localhost","127.0.0.1"],["webserver","127.0.0.2"]]
with open('hosts.csv',"w") as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)

with open('./software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users.".format(row['name'], row['user']))


users = [{"name":"Jhon", "email":"jhon@example.com"},
         {"name":"Anish","email":"anish@example.com"}]
keys = ["name","email"]

with open('./users.csv','w', newline='') as users:
    writer = csv.DictWriter(users,fieldnames=keys)
    writer.writeheader()
    # writer.writerows(users)