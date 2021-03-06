### Space Apps Challenge 2019

#### For Part 1 

*   Organize by latitude/longitude (probably through mapping).
*   Sub Compare each of them, check for anomalies. 
	*   Need location, time, and, reliability of data.

#### Objective 1: 
*   Create a script that identifies parasitic geomagnetic activity and assigns a degree of reliability based on a suggested value to the erroneous data.

#### Process 1: 
*   The dataset1 is provided. It contains magnetic variation data from 26 measurement sites over 31 days in one-hour increments. Participants must create a script that reports the falsified data in a report.

#### Final Product 1: 
*   Participants must present their report of the data deemed geomagnetically implausible, including location, time (DD-HH) and reliability of the aforementioned measurement. The format of this report is left to the discretion of the participants.
*   Required:
	*    Number of actual error predictions
	*   The degree of reliability attributed to errors/ The suggestion for error replacement
	*   Ease of understanding and the use of the minutes
	*   Accessibility of the report format.
		*   Report format must contain a dataset of the sites in which there was an anomaly, and the date (DD/HH) and the reliability of the measurement.

#### Algorithm:
*   Background: 
*   There are 26 measurement sites over 31 days in one-hour increments. We must differentiate between the magnetic fluctuations between Solar storms and variations in Earth's magnetic field due to false geomagnetic fluctuations caused by
	*   human activity: increase
	*   thunderstorms: heavy increase for a short period of time (a few hours at most)
	*    instrument failure: heavy decrease (hours of none to little change)
	*   instrument overheating: heavy ?
	*   power failure: heavy decrease (hours of none to little change)
	*   data transmission problems: heavy decrease 
*   A solar storm is seen as a rapid drop in the Earth's magnetic field strength. This decrease lasts about 6 to 12 hours, after which the magnetic field gradually recovers over a period of several days. 
*   Earth's magnetic field at its surface ranges from 25 to 64 microteslas. (not relevant?)
		
*   Claim: 
	*   Differentiate magnetic fluctuations due to Solar storms versus magnetic fluctuations due to false geomagnetic fluctuations. Determine which of the data entries are solar storms and which are false entries.

*   Potential solutions: 
	*   Note that two locations relatively close locations will have similar swings in magnetic fluctuation when affected by solar storms.
	*    We can examine the standard deviation of a given column, and note that outliers are potentially false geomagnetic fluctuations.
	*   Potentially map location as the key, and list of geomagnetic fluctuations as the values.
		*   § 31 * 24 = 744 total inputs
		*   § We compare the geomagnetic fluctuation of each value to the mean - the standard deviation, mean + the standard deviation.
		*   § If it doesn't fall within this range, then it is an outlier. 
			*   We can determine the day and hour using the same method of recursion.
		*   § How do we differentiate between outliers and solar storms?
	*   ○ Necessary functions:
		*   § mean of a location
		*   § standard deviation of a location
			*   at 99.7 confidence interval
		*   § min range of a location
		*   § max range of a location
		*   § day of anomaly
		*   § hour of anomaly
	*   ○ Export as a csv file?
		*   § Map SITE IDs to latitude/longitudes


Rozario: 
### Part 2:
*   Objective: 
	*   Create a script to estimate the variation in magnetic field at a measurement site where the data is erroneous/lost
*   Process: 
	*   The files dataset2_full.txt (117 KB) and dataset2_holed.txt (116 KB) are available to participants for this challenge. The objective of the participants is to estimate the magnetic field variations for the missing site. They will be able to use the dataset2_full.txt dataset to measure the accuracy of different mapping methods.
*   Final product: 
	*   Participants must submit a text file (.txt) containing the estimate of magnetic field variations over the given period as well as a visual representation of the geomagnetic mapping (image/video).

*   Required:
	*   The accuracy of their estimate
	*   The quality of the mapping (visual support)
	*   The originality and ingenuity of the method used.

	
*   Ideas: 
	*   1) Well obviously we must extract both datas from both csv files to compare both of them.
		*   So we need a get file content method
	*   2) Once we have the file we will need to compare both to estimate the magnetic field variation. Will probably need to play around with it to get a good feel for the variations in the missing sites.
		*   compare the differences between data method
	*   3) Once that is done we will need to create a visual representation probably with one of the resources that they provided.
		*   Create chart method

*   class':
	*   Site:
		*   Site Id
		*   List of Geomagnetic variation
*   NEEDED FUNCTIONS:
	*   find missing data. Return site id of which one
	*   get estimate go through the data 
