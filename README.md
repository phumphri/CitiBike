# Citi Bike Analytics

## Summary

![Citi-Bikes](images/citi-bike-station-bikes.jpg)

Based on bike trip data provided by citibike, the data was analyzed, searching for answers for the following questions.

* How many trips have been recorded total during the chosen period?

* By what percentage has total ridership grown? 

* How has the proportion of short-term customers and annual subscribers changed?

* What are the peak hours in which bikes are used during summer months? 

* What are the peak hours in which bikes are used during winter months?

* Today, what are the top 10 stations in the city for starting a journey? (Based on data, why do you hypothesize these are the top locations?)

The answers were derived in a a four-step process.
* Data Acquisition
* Data Modeling
* Data Access
* Data Visualization

These four steps are described in this document.

## Data Acquisition
![Data Acquisition](images/acquisition.png)

There are 60 archive files that yielded 60 csv files.  

The resulting citibike.trips table contains nearly 60 million rows.

All files were processed that were in C:/citibike directory.  

Assumming all files were type csv, the ever evolving naming scheme for the files had no effect.

Some of the data cleansing done were:
* Data that would normally hold type integer data where converted to type integer.  If the cast failed, the value None was assigned.
* Data that would normally hold text that had the value "NULL" were assigned the value None.
* Key values for start_time and bike_id were required.  
* Records with duplicate keys were ignored.

### Input Files
Files provided by citibike (https://www.citibikenyc.com/system-data):
<table>
    <tr>
        <th>Name</th>
        <th>Date Modified</th>
        <th>Size</th>
        <th>Type</th>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201306-citibike-tripdata.zip">201306-citibike-tripdata.zip</a></td>
        <td>Apr 30th 2018, 06:18:55 am</td>
        <td>16.79 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201307-201402-citibike-tripdata.zip">201307-201402-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:25 pm</td>
        <td>178.26 MB</td>
        <td>ZIP file</td>
    </tr>  
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201307-citibike-tripdata.zip">201307-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:27 pm</td>
        <td>27.07 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201308-citibike-tripdata.zip">201308-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:27 pm</td>
        <td>32.09 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201309-citibike-tripdata.zip">201309-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:27 pm</td>
        <td>33.16 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201310-citibike-tripdata.zip">201310-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:28 pm</td>
        <td>33.07 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201311-citibike-tripdata.zip">201311-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:28 pm</td>
        <td>21.62 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201312-citibike-tripdata.zip">201312-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:28 pm</td>
        <td>14.31 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201401-citibike-tripdata.zip">201401-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:29 pm</td>
        <td>9.70 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201402-citibike-tripdata.zip">201402-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:29 pm</td>
        <td>7.25 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201403-citibike-tripdata.zip">201403-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:29 pm</td>
        <td>14.13 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201404-citibike-tripdata.zip">201404-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:29 pm</td>
        <td>21.41 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201405-citibike-tripdata.zip">201405-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:29 pm</td>
        <td>27.59 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201406-citibike-tripdata.zip">201406-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:29 pm</td>
        <td>29.90 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201407-citibike-tripdata.zip">201407-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:30 pm</td>
        <td>30.89 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201408-citibike-tripdata.zip">201408-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:30 pm</td>
        <td>30.63 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201409-citibike-tripdata.zip">201409-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:30 pm</td>
        <td>30.25 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201410-citibike-tripdata.zip">201410-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:30 pm</td>
        <td>26.15 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201411-citibike-tripdata.zip">201411-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:31 pm</td>
        <td>16.83 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201412-citibike-tripdata.zip">201412-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:31 pm</td>
        <td>12.72 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201501-citibike-tripdata.zip">201501-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:31 pm</td>
        <td>7.01 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201502-citibike-tripdata.zip">201502-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:31 pm</td>
        <td>4.82 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201503-citibike-tripdata.zip">201503-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:31 pm</td>
        <td>8.42 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201504-citibike-tripdata.zip">201504-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:31 pm</td>
        <td>20.74 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201505-citibike-tripdata.zip">201505-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:32 pm</td>
        <td>30.34 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201506-citibike-tripdata.zip">201506-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:32 pm</td>
        <td>22.89 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201507-citibike-tripdata.zip">201507-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:32 pm</td>
        <td>34.52 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201508-citibike-tripdata.zip">201508-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:33 pm</td>
        <td>38.04 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201509-citibike-tripdata.zip">201509-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:33 pm</td>
        <td>43.62 MB</td>
        <td>ZIP file</td>
    </tr>  
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201510-citibike-tripdata.zip">201510-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:34 pm</td>
        <td>41.82 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201511-citibike-tripdata.zip">201511-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:34 pm</td>
        <td>34.35 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201512-citibike-tripdata.zip">201512-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:35 pm</td>
        <td>23.15 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201601-citibike-tripdata.zip">201601-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:35 pm</td>
        <td>17.79 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201602-citibike-tripdata.zip">201602-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:35 pm</td>
        <td>19.67 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201603-citibike-tripdata.zip">201603-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:36 pm</td>
        <td>26.45 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201604-citibike-tripdata.zip">201604-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:36 pm</td>
        <td>35.50 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201605-citibike-tripdata.zip">201605-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:36 pm</td>
        <td>42.46 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201606-citibike-tripdata.zip">201606-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:37 pm</td>
        <td>51.46 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201607-citibike-tripdata.zip">201607-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:38 pm</td>
        <td>48.81 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201608-citibike-tripdata.zip">201608-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:39 pm</td>
        <td>56.05 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201609-citibike-tripdata.zip">201609-citibike-tripdata.zip</a></td>
        <td>Jan 18th 2017, 02:23:40 pm</td>
        <td>60.82 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201610-citibike-tripdata.zip">201610-citibike-tripdata.zip</a></td>
        <td>Jan 23rd 2017, 06:25:28 am</td>
        <td>52.92 MB</td>
      <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201611-citibike-tripdata.zip">201611-citibike-tripdata.zip</a></td>
        <td>Jan 23rd 2017, 06:25:18 am</td>
        <td>40.31 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201612-citibike-tripdata.zip">201612-citibike-tripdata.zip</a></td>
        <td>Jan 23rd 2017, 06:25:24 am</td>
        <td>27.55 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201701-citibike-tripdata.csv.zip">201701-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:05 pm</td>
        <td>24.25 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201702-citibike-tripdata.csv.zip">201702-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:14 pm</td>
        <td>26.35 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201703-citibike-tripdata.csv.zip">201703-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:25 pm</td>
        <td>24.17 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201704-citibike-tripdata.csv.zip">201704-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:16:58 am</td>
        <td>45.08 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201705-citibike-tripdata.csv.zip">201705-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:17:14 am</td>
        <td>52.67 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201706-citibike-tripdata.csv.zip">201706-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:17:25 am</td>
        <td>60.39 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201707-citibike-tripdata.csv.zip">201707-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:17:42 am</td>
        <td>60.55 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201708-citibike-tripdata.csv.zip">201708-citibike-tripdata.csv.zip</a></td>
        <td>Oct 3rd 2017, 08:52:50 am</td>
        <td>63.28 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201709-citibike-tripdata.csv.zip">201709-citibike-tripdata.csv.zip</a></td>
        <td>Oct 3rd 2017, 08:52:58 am</td>
        <td>65.88 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201710-citibike-tripdata.csv.zip">201710-citibike-tripdata.csv.zip</a></td>
        <td>Jan 31st 2018, 01:14:57 pm</td>
        <td>67.61 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201711-citibike-tripdata.csv.zip">201711-citibike-tripdata.csv.zip</a></td>
        <td>Jan 31st 2018, 01:15:07 pm</td>
        <td>47.77 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
      <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201712-citibike-tripdata.csv.zip">201712-citibike-tripdata.csv.zip</a></td>
        <td>Jan 31st 2018, 01:15:13 pm</td>
        <td>32.10 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201801-citibike-tripdata.csv.zip">201801-citibike-tripdata.csv.zip</a></td>
        <td>Apr 30th 2018, 08:56:01 am</td>
        <td>28.01 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201802-citibike-tripdata.csv.zip">201802-citibike-tripdata.csv.zip</a></td>
        <td>Apr 30th 2018, 08:56:34 am</td>
        <td>32.89 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201803-citibike-tripdata.csv.zip">201803-citibike-tripdata.csv.zip</a></td>
        <td>Apr 30th 2018, 08:56:54 am</td>
        <td>38.14 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201804-citibike-tripdata.csv.zip">201804-citibike-tripdata.csv.zip</a></td>
        <td>May 11th 2018, 01:49:18 pm</td>
        <td>50.87 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/201805-citibike-tripdata.csv.zip">201805-citibike-tripdata.csv.zip</a></td>
        <td>Jun 8th 2018, 08:29:41 am</td>
        <td>70.91 MB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201509-citibike-tripdata.csv.zip">JC-201509-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:34 pm</td>
        <td>125 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201510-citibike-tripdata.csv.zip">JC-201510-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:35 pm</td>
        <td>357 KB</td>
      <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201511-citibike-tripdata.csv.zip">JC-201511-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:37 pm</td>
        <td>281 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201512-citibike-tripdata.csv.zip">JC-201512-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:38 pm</td>
        <td>222 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201601-citibike-tripdata.csv.zip">JC-201601-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:38 pm</td>
        <td>141 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201602-citibike-tripdata.csv.zip">JC-201602-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:38 pm</td>
        <td>156 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201603-citibike-tripdata.csv.zip">JC-201603-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:39 pm</td>
        <td>253 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201604-citibike-tripdata.csv.zip">JC-201604-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:39 pm</td>
        <td>304 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201605-citibike-tripdata.csv.zip">JC-201605-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:40 pm</td>
        <td>361 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201606-citibike-tripdata.csv.zip">JC-201606-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:40 pm</td>
        <td>442 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201607-citibike-tripdata.csv.zip">JC-201607-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:41 pm</td>
        <td>455 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201608-citibike-tripdata.csv.zip">JC-201608-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:41 pm</td>
        <td>651 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201609-citibike-tripdata.csv.zip">JC-201609-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:42 pm</td>
        <td>637 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201610-citibike-tripdata.csv.zip">JC-201610-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:42 pm</td>
        <td>568 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201611-citibike-tripdata.csv.zip">JC-201611-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:43 pm</td>
        <td>424 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201612-citibike-tripdata.csv.zip">JC-201612-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:43 pm</td>
        <td>298 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201701-citibike-tripdata.csv.zip">JC-201701-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:43 pm</td>
        <td>255 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201702-citibike-tripdata.csv.zip">JC-201702-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:44 pm</td>
        <td>275 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201703-citibike-tripdata.csv.zip">JC-201703-citibike-tripdata.csv.zip</a></td>
        <td>Apr 6th 2017, 02:01:44 pm</td>
        <td>241 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201704-citibike-tripdata.csv.zip">JC-201704-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:20:54 am</td>
        <td>432 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201705-citibike-tripdata.csv.zip">JC-201705-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:20:55 am</td>
        <td>529 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201706-citibike-tripdata.csv.zip">JC-201706-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:20:56 am</td>
        <td>647 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201707-citibike-tripdata.csv.zip">JC-201707-citibike-tripdata.csv.zip</a></td>
        <td>Aug 1st 2017, 09:20:57 am</td>
        <td>676 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201708 citibike-tripdata.csv.zip">JC-201708 citibike-tripdata.csv.zip</a></td>
        <td>Oct 3rd 2017, 08:52:49 am</td>
        <td>711 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201709-citibike-tripdata.csv.zip">JC-201709-citibike-tripdata.csv.zip</a></td>
        <td>Oct 3rd 2017, 08:52:49 am</td>
        <td>667 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201710-citibike-tripdata.csv.zip">JC-201710-citibike-tripdata.csv.zip</a></td>
        <td>Jan 31st 2018, 01:15:18 pm</td>
        <td>703 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201711-citibike-tripdata.csv.zip">JC-201711-citibike-tripdata.csv.zip</a></td>
        <td>Jan 31st 2018, 01:15:19 pm</td>
        <td>477 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201712-citibike-tripdata.csv.zip">JC-201712-citibike-tripdata.csv.zip</a></td>
        <td>Jan 31st 2018, 01:15:19 pm</td>
        <td>324 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201801-citibike-tripdata.csv.zip">JC-201801-citibike-tripdata.csv.zip</a></td>
        <td>Apr 30th 2018, 08:56:11 am</td>
        <td>273 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201802-citibike-tripdata.csv.zip">JC-201802-citibike-tripdata.csv.zip</a></td>
        <td>Apr 30th 2018, 08:59:51 am</td>
        <td>326 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201803-citibike-tripdata.csv.zip">JC-201803-citibike-tripdata.csv.zip</a></td>
        <td>Apr 30th 2018, 08:56:45 am</td>
        <td>370 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201804-citibike-tripdata.csv.zip">JC-201804-citibike-tripdata.csv.zip</a></td>
        <td>May 11th 2018, 01:49:58 pm</td>
        <td>512 KB</td>
        <td>ZIP file</td>
    </tr>
    <tr>
        <td><i class="icon-file i-file-or-folder" style="margin-left:calc((1 * 16px) + 4px);"></i>
        <a href="https://s3.amazonaws.com/tripdata/JC-201805-citibike-tripdata.csv.zip">JC-201805-citibike-tripdata.csv.zip</a></td>
        <td>Jun 8th 2018, 08:29:50 am</td>
        <td>744 KB</td>
        <td>ZIP file</td>
    </tr>

</table>

## Data Modeling
![Data Modeling](images/modeling.png)

Loading the 60 csv files into a database allows access to all data.  However, the database has nearly 60 million rows.

Materialized views aggregate and store the data, thus greatly reducing the amount of data transmitted to a client and avoiding processing time.

Not all aggregation is done with SQL.  However, the "heavy lifting" is done in advance in the database to allow the client to do further discovery.

The advantages of using materialized in Postgres:
* Fast perfomance, since the data is already aggregated.
* Reduce the number of records to be transmitted to a client.
* Use of the aggregation, windowing, and analytical functions in Postgres.

## Data Access
![Data Access](images/access.png)

An Application Programming Interface (API) was developed.

This API would read either a materialized view or a view and format a OData/JSON payload.  
The view objects applied Postgres windowing to calculate percentages or eliminate duplicates.

A typical API would provision a JSON package with or without embedded metadata.

However, Tableau is different.  It requires Open Data Protocol (OData).  This a combination of a JSON payload and an XML payload describing the JSON.

## Visualization
![Data Visualization](images/visualization.png)

All Tableau views were created using OData resources. 
 
These OData resources were JSON payloads with the number of rows ranging from a low of 10 rows 
to as many as 3,814 rows.  Since the data was already aggregated, response is immediate.

The Postgres database contained nearly sixty million rows.  The system would fail if that much data were to be pushed out to Tableau
and having Tableau do the aggregation.

