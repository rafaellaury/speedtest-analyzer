# speedtest-analyzer
ECE 3600 final project, this repository includes the speedtester.py script and the graph maker

To run the speedtester, you will need to install the speedtest-cli package:

    pip install speedtest-cli

Once that is done, you can run,

    python speedtester.py
    
It will prompt you for your location, which will be printed in the file and in the file name.
The output will be a CSV file with the 20 trials.

These CSVs can then be processed into graphs using the process.py script.

Have fun!

