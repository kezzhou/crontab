# crontab
HHA 507 // Week 6 // Assignment 6

## In this repo, the focus is an introduction to crontab, which is useful for automating tasks via terminal or cmd prmpt and is usually installed with OS by default. Cron allows users to automate tasks dictated by scripts such as py or sh files.

## In order to activate cron, one must type the prompt: crontab -e. If it is the first activation of cron, it will ask the user to select an editor of choice. In this repo we use nano.

## subsequent activations of cron will allow the user to input five stars followed by a command. The five stars all correspond to a specific date-time value. The first star is minute, the second is hour, the third is day of the month, the fourth is month, and the fifth is day of the week. 

## In this example we want to pull down data from an API during given intervals: once a day at a random time, every sunday night at 10:00 PM, and once at the end of every quarter.

## We can begin by writing our pulldown.py file. We choose to import os, sys and time for timestamping the txts that we will create. We import requests to pull down data from the API and json to visualize that data. Finally, we use pandas to put the data into a dataframe for csv importing into the local machine. Technically speaking, we could run the pandas section without the timestamps, but it is useful to have a log of each cron job run.

## The data API we have used can be found at: https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data

## We have written pulldown.py so that the txt file created will have the time it was created in its name, and the API data pulled as its contents when nanoed in.

## Now we can take to a virtual/testing environment to test the file out on cron. In this case we have chosen to use Azure. We can then use 'rm -r' to remove any outdated crontab directories that we have and use 'git clone https://github.com/kezzhou/crontab.git' to clone our directory into the venv.

## Once we have created the crontab dir, we can then type 'crontab -e' and populate the document with the necessary scripts.

## For once a day at a random time, we write:
## '30 17 * * * /usr/bin/python3 /home/kevin/crontab/pulldown.py'
## technically speaking, this will pull api data and create a new txt file every day of the week, every day of the month, every month at 17:30 or 5:30 PM.

## For every Sunday at 10:00 PM, we write:
## '00 22 * * 7 /usr/bin/python3 /home/kevin/crontab/pulldown.py'

## For the end of the quarter, we write:
## '59 23 31 3,12 * /usr/bin/python3 /home/kevin/crontab/pulldown.py'
## '59 23 30 6,9 * /usr/bin/python3 /home/kevin/crontab/pulldown.py'
## we can separate the end of quarters into two commands. March and December both have 31 days whereas June and September have 30 days. We can leave days of the week as * as the end of the quarters may land on different days annually. we can automate the process to pull the data right before the start of the new day and quarter.

## It is useful to find the path of python3 with 'which python3' and the path of various files in directories with 'pwd' after cding into them. 

## In the case that there is a stray print command in the py file we are working with, we must provide a path for a new txt file to be created to execute that print command. For example, had we used a stray print command somewhere in our script, such as 'print('Hello')', a working cron script would look something like this: '00 22 * * 7 /usr/bin/python3 /home/kevin/crontab/pulldown.py > log.txt 2>&1 &'. Every time that the job was run based on the time we set, we would also generate a txt called log.txt with our executed print command in it ('Hello'). This is also helpful as if your code does not work, it will transcribe the error on the log.txt for you to troubleshoot.

## IMPORTANT: be sure to pip/pip3 install all requirements from the requirements.txt as your venv may not come with it.