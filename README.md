# Parallel Data Processing System

## Overview

This is your capstone project for the instructional module. Your goal is to parse a large datset of web server logs and extract useful information from it. For information on generating the data, refer to the [Data Generation](#data-generation) section.

## Tasks

### Metrics Calculation (MetricsCalculator.java)

1. Calculate daily statistics including the total number of requests, the number of succesfful requests (200 Status code), number of client error requests (400 status codes), and the number of server error requests (500 status codes).
2. Determine the most requested URLs.
3. Determine the most frequent referrers.

### Anomaly Detection (AnomalyDetector.java)

1. Identify potential security threats by detecting patterns indicative of attacks, like a high number of requests from the same IP or a bunch of 404 error codes in quick succession.
2. Identify sudden surges in traffic which could be indicative of a DDoS attack.

## Suggested Approach

1. Data Ingestion: Implement a multithreaded parser to read the log file concurrently, divide the file into chunks and pass each chunk to a separate thread for processing. A naive version is in LogProcessor.java, but you can definitelyimprove on this.
2. Data Processing: Implement a metrics calculator and anomaly detector to process the data. Utilize thread-safe collections and synchronization to ensure that the data is processed correctly and to aggregate the results.
3. Data Aggregation: Combine the results from the metrics calculator and anomaly detector to generate a report summarizing the findings.
4. Optimization: Multithreading is not the only way to speed this up! You can also consider writing parsers completely from scratch taking advantage of the specific format of the log files to see if you can shave off some milliseconds. Try different number of threads, is there an optimal number of threads that gives you the best performance? Maybe implement a thread pool to manage the threads more efficiently, what if you HAD only 4 threads to work with, how would you design your system then?

## Expected Outcomes
- Performance improvements in the data processing pipeline.
- Scalability of the system to handle larger datasets.
- Accuracy in detecting anomalies and calculating metrics.

## Data Generation

In `src/data` we have included a python script called `data_gen.py` which will generate a log file called `web_server_logs.txt` with logs that look like:

```204.20.167.240 - - [14/Feb/2024:21:52:13 +0000] "GET /products HTTP/1.1" 500 4877 "https://harris.org/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"```

In general the format is:

```<ip> - - [<date>] "<method> <url> <protocol>" <status_code> <response_size> "<referrer>" "<user_agent>"```.

Make sure to run the script in the `src/data` directory to generate the log file, and make sure to put the log file in the `src/data` directory. We've included a sample log file, but it has only 10000 records which is not enough to test the performance of your system. You can generate a larger log file by running the script with a larger number of records by modifying the last line of the script, we suggest about 10 million records at the least.
