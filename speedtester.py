# Speedtest Python Script

import speedtest
import csv
import datetime

TIME = (str((datetime.datetime.now())).replace(" ","@").replace(":","_"))[0:19]
print("Enter your location: ")
LOCATION = input()

servers = []
# If you want to test against a specific server
# servers = [1234]

# If you want to use a single threaded test
threads = 1
i = 0
data = []
s = speedtest.Speedtest()
s.get_servers(servers)
out_server = s.get_best_server()
print(out_server)
while i < 20:
    print("Iteration " + str(i))
    d = s.download(threads=threads)
    print(d)
    print(float(d))
    u = s.upload(threads=threads)
    print(u)
    print(float(u))
    results = s.results.dict()
    down = float(d)/1000000.0
    up = float(u)/1000000.0
    ping = results["ping"]
    data.append([down, up, ping])
    i = i + 1

server_fields = out_server.keys()
data_fields = ["Download [Mbps]", "Upload [Mbps]", "Ping [ms]"]
print(data)
with open("speedtest_{}_{}.csv".format(LOCATION.replace(" ","-"), TIME),'w', newline = '', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Location: ", LOCATION])
    writer.writerow(["Timedate: ", TIME])
    writer.writerow(["Server: ", out_server])
    writer.writerow(data_fields)
    a = []
    for a in data:
        writer.writerow(a)