#!/usr/local/bin/python3.6

# change above line to point to local 
# python executable

from __future__ import absolute_import, division, print_function, unicode_literals
                                                                                  
import logging

import sys

import pygenie
  
logging.basicConfig(level=logging.ERROR)                                          
                                        
LOGGER = logging.getLogger(__name__)    
                                        
pygenie.conf.DEFAULT_GENIE_URL = "http://130.211.114.111:8080"
                                                              
# Create a job instance and fill in the required parameters   
job = pygenie.jobs.HadoopJob().job_name('Genie Demo HDFS Job').genie_username('root').job_version('3.0.0')                                     
                                                              
# Set cluster criteria which determine the cluster to run the job on
job.cluster_tags(['sched:' + str('sla'), 'type:yarn'])        
                                                                    
# Set command criteria which will determine what command Genie executes for the job
job.command_tags(['type:hdfs'])                                                    
                                                                                   
# Any command line arguments to run along with the command. In this case it holds  
# the actual query but this could also be done via an attachment or file dependency.
job.command("dfs -cat credit.csv")                                                        
                                                                                    
# Submit the job to Genie                                                           
running_job = job.execute()                                                      
                                                                                    
print('Job {} is {}'.format(running_job.job_id, running_job.status))                
print(running_job.job_link)                                                         
                                                                    
# Block and wait until job is done                                  
running_job.wait()    

print(running_job.stdout_url)

import csv
import urllib
import sys
import os

import urllib.request

page = urllib.request.urlopen(running_job.stdout_url)

f = open("data.csv", "wb")
content = page.read()
f.write(content)
f.close()

print(content)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
    
#with open('data.csv', "rt") as csvfile:
#    csv = csv.reader(csvfile)  # with the appropriate encoding
#    data = [row for row in csv]
#    print (data)
                                                                   
print('Job {} finished with status {}'.format(running_job.job_id, running_job.status))



