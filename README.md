# speedtest-analyzer
ECE 3600 final project conducted by Isaac Chia, Shaun Guo, Rafael Laury, Beaudly Leriche and Levi Tucker.

This repository includes the speedtester.py script, the process.py script used to generate the graphs for the presentation, the PowerPoint presentation, and the datasets used for analysis.

To run the speedtester, you will need to install the speedtest-cli package:

    pip install speedtest-cli

Once that is done, you can run,

    python speedtester.py
    
It will prompt you for your location, which will be printed in the file and in the file name.
The output will be a CSV file with the 20 trials.

These CSVs can then be processed into graphs using the process.py script.

The data used in the analysis presented in the PowerPoint can be found in the "datasets" directory. This contains the results from the six trials that were conducted as part of this project. These trials were conducted by running the speedtester at three different locations, once at a busy time and once at a not busy time. The aim of collecting this data was to better understand the inner workings and trends in WiFi speeds at different locations and times of day.
