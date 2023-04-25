import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import statistics as st
import os


current_dir = os.getcwd()
file_list = os.listdir(current_dir)
csv_list = []
content = {}

# Pair bar plot
# def plot_pair(n):
#     t = plt.subplots(ncols=2, figsize=(14,6))
#     plt.subplots_adjust(wspace=0.5)
#     t[0].suptitle("Plot "+str(n), fontsize=24)
#     return list(t[1])

# Get the csv files
for f in file_list:
    if "speedtest" in f and ".csv" in f:
        with open(f, 'r') as file:
            content[f.replace("speedtest_", "").replace(".csv", "")] = file.readlines()[4:]

# Turn data in graph
for data in content:
    download = []
    upload = []
    ping = []
    ind = []
    sum = []
    avg_d = []
    avg_u = []
    for entry in content[data]:
        spl = entry.replace("\n", "").split(",")
        download += [float(spl[0])]
        upload += [float(spl[1])]
        ping += [float(spl[2])]
        sum += [float(spl[0]) + float(spl[1])]
    #print(download)
    for i in range(len(download)):
        ind += [f"Time {i}"]
        avg_d += [st.mean(download)]
        avg_u += [st.mean(upload)]

    down_data = Series(download, index=ind, name="Download Speed")
    up_data = Series(upload, index=ind, name="Upload Speed")
    sum_data = Series(sum, index=ind, name="Effective Speed")
    avg_d_data = Series(avg_d, index=ind, name="Average Download Speed")
    avg_u_data = Series(avg_u, index=ind, name="Average Upload Speed")

    df = DataFrame([down_data, up_data, sum_data, avg_d_data, avg_u_data])
    df = df.transpose()
    plt.rcParams['figure.figsize'] = [16, 10]

    plot = df[["Download Speed", "Upload Speed"]].plot.bar(color=["orange", "blue"])
    df["Effective Speed"].plot.line()
    df["Average Download Speed"].plot.line(linewidth = "3", linestyle = 'dashed')
    df["Average Upload Speed"].plot.line(linewidth = "3", linestyle = 'dashed')
    plot.set_ylabel('Mbps')
    plot.set_title(f"Average WiFi speed of {data}")
    # lf = DataFrame([sum_data])
    # lf = lf.transpose()
    # lf.plot.line()
    #plt.xticks(ind_val, ind)
    plt.legend(bbox_to_anchor=(1, 1.155), loc="upper right")
    #plt.show()
   
    plt.savefig(f"{data}.png")

            
    