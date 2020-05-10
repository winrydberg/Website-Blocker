import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# hosts_temp = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", ]

currentYear = dt.now().year
currentMonth = dt.now().month
currentDay = dt.now().day

while True:
    if dt(currentYear, currentMonth, currentDay, 8) < dt.now() < dt(currentYear, currentMonth, currentDay, 17):
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
