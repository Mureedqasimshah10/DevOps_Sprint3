from datetime import datetime
import urllib3
from Cloudwatch_putMetrices import CloudwatchputMetric
import constants as constants

def lambda_handler(event, context):
    # Applying loop on the four urls to obtain availability and latency of the urls

    for url in constants.URL_TO_MONITOR:
        values_ = dict()
        availability = getavailability(url)
        latency = getLatency(url)
        values_.update({"Availability ":availability,"Latency ":latency})
        print(values_)
        # I would like to publish my matrices to cloud watch
        cw = CloudwatchputMetric()
        dimension = [{'Name': 'URL', 'Value': url}]
        
        
        responseAvail = cw.put_data(constants.URL_MONITOR_NAMESPACE , 
        constants.URL_MONITOR_METRIC_NAME_AVAILABILITY,
        dimension,
        availability)
        
        responselatency = cw.put_data(constants.URL_MONITOR_NAMESPACE , 
        constants.URL_MONITOR_METRIC_NAME_LATENCY,
        dimension,
        latency)

    

    # Defining the funciton to obtain the availability
def getavailability(url):
    http = urllib3.PoolManager()
    # Sending the get request to access the webpage
    response = http.request("GET", url)
    if response.status ==200:
        return 1.0
    else:
        return 0.0

    
    # Defining the funciton to obtain the latency
def getLatency(url):
    # Calculating the how much time it takes for the user to access webpage
    http = urllib3.PoolManager()
    # starting our timer
    start = datetime.now()
    # Sending a request to access the webpage
    response = http.request("GET", url)
    # Ending the timer
    end = datetime.now()
    # returing the latency in seconds
    delta = end - start
    latencySec = round(delta.microseconds * .000001, 6)
    return latencySec