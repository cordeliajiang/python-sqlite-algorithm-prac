# workshop9 task2 - shell scripting, 19/09/21, Cordelia Jiang
# fetch the data from a provided climate.db
import sqlite3
import matplotlib.pyplot as plt    # import needed module to perform plot functions
connection = sqlite3.connect("climate.db")

# all access to the database is via the cursor object.
cursor = connection.cursor()

# fetch all data in the ClimateData table of the climate.db and save it in a data variable
# add the temperature data
cursor.execute('SELECT CO2, Year, Temperature FROM ClimateData')
climateData = cursor.fetchall()

# create a line graph of CO2 versus time, view the plot.
co2 = []    # empty list variable used to store appended co2 data
time = []    # empty list variable used to store appended time data
temperature = []    # empty list variable used to store appended temperature data

# go through all rows in climateData table, append all values of first column to co2 list,
# append all values of second column to time list, and append all values of third column to temperature list
for row in climateData:
    co2.append(row[0])
    time.append(row[1])
    temperature.append(row[2])

# the figure has 2 rows, 1 column, and this is the first plot
# plotting time as x and co2 as y values, and display as line graph.
# re-draw the graph with a blue dashed line.
plt.subplot(2, 1, 1)
plt.plot(time, co2, 'b--')

# add a title and axis titles to the plot.
plt.title('Time Versus CO2')
plt.xlabel('Time')
plt.ylabel('CO2')

# the figure has 2 rows, 1 column, and this is the second plot
# create a new plot with temperature data added
plt.subplot(2, 1, 2)
plt.plot(time, temperature)

# add a title and axis titles to the plot.
plt.title('Time Versus Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')

# adjusting spaces between plots
plt.tight_layout()    # only will work if execute this after plot code, but right before show()

# save the plot as an image file in code
plt.savefig('timeCO2TemperatureLineGraph.png')    # will only save the image when placed before plt.show()

# display line graphs
plt.show()

# close the connection to save changes
connection.close()
