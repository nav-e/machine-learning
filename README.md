# machine-learning
A research repository for source code that implements machine learning methods to solve tasks related to navigation within the Greennav project

Current Contents:
### 1. Fuel prediction 
This module has three different functionalities namely:

1. Getting the Energy consumption
2. Getting the amount of CO2 that is saved from being emitted into the environment 	because of using an Electric vehicle
3. Getting the Rechargetime required for the journey.

The calcultions are shown in the Ipython Notebook and the data that is used is kept in the subdirectory /Fuel_consumption_dataset
Additionally I have used machine learning to calculate the CO2 that will be emitted per kilometer and created a dataset in CSV and JSON format that can be used by anyone.


### 2. Route Option:

This module focuses on leveraging human knowledge to get the best route. At a  given time due to certain circumstances (like rush hour) it is possible that a certain route may be faster than a route shown on the map. People who travel at those times or people who are residents of those areas have more knowledge about which route should be taken at what time. If every person entered which path to be taken based on their experience we could create a database that will help us to predict which path should be taken. The same has been done in this module

### 3. Trajectory:

Visualization of the route a car takes.
Still a work in progress.

### 4. Driving Simulator:

A simulator for cars to learn to drive themselves. Can be used for data generation. 
Still a work in progress.