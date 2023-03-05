**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

#### MonitoringInstallation.PNG

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

#### Grafana.PNG 

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

#### FirstSimpleDashboardAsPrometheusAsDataSource.PNG

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

#### SLI for SLO of "monthly uptime" : The application is fully functional 99% of the time over a period of 30 days.
#### SLI for SLO of "request response time" : The time taken by an application to return a response for a request is less than or equal to 200 ms. 

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

##### 1. Availability
        A percentage of time a service or application is fully functional and available to user over a time interval. Example - 99.9% of uptime over 30 days.
##### 2. Latency
        The time taken an API of service or application to process a request an return a reponse. Example - 200 ms.
##### 3. Error rate
        The percentage of requests that a service or application is failed process (or resulted in an error) over a time interval. Example - 0.5% of requests resulted in error 500 in 30 days.
##### 4. Througput
        The number of requests handled/process by an API of a service or application per unit of time, usually measured as request per minute (RPM). 
##### 5. MTBF (mean time between failures)
        The average amount of time between two consecutive failures. Example - 5 days 4 hrs.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

#### DashboardForCLIs.PNG

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

#### Jaeger span screenshot : JaegerSpan.PNG
#### Sample python code screenshot: SamplePyCodeForTracing.PNG

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

#### GrafanaDashboardWithJaegerTraces.PNG

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Jay

Date: 5th Jan 2023

Subject: Adding start and distance takes longer.

Affected Area: Backend service /start api

Severity: High

Description: The backend-service's /start api response is slower, it takes more than 200 ms on averrage with p99 280 ms


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

#### SLIs to achieve SLOs to gaurantee 99.95% uptime
     - Track number of total requests over year
     - Track number of 400 errors over a year 
     - Track number of 500 errors
     - Total downtime over year

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.
    
#### KPIs for metrics
     - Total number of request over year
     - Total number of 400 errors over year - to check how many requests failed due to this error which indicates downtime
     - Total number of 500 errors over year - to check how many request failed  due to this error which indicates the services is not functions
     - Total downtime over year - to check total downtime for maintenance or other such activities.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

#### Graphs
     - Backend service API stats graph shows 
                - the API calls (each point on the graph represents an API call)
                - time taken for each call the 
                - total number of API call within a year (5th Mar 2023 to 29th Apr 2024)
                - max reponse time
                - min response time
                - mean response time
     - Backend Service API Status graph shows - to monitor health of API 
     - Backend Service Error Stat. graph shows - occurrences of any error 
     The above 3 graphs together shall help to monotor the SLI of number of request per year, number of failure per year, and if any downtime over an year. Please refer the dashboard mentioned below.
##### GrafanaDashboardWithJaegerTraces.PNG
