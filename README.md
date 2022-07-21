# Distribution Generator

This repository was created to make available a method that build a distribution with all the possible scenarios given the possibilities input. This method can be very interesting for unit tests or data analysis that consider all the possible scenarios.


The method works from a list of lists in the input. 

Example: 

What's all the possible mix with 2 of the 4 main primary colors (red, green, yellow, blue)?

colors = ['red', 'green', 'yellow', 'blue']

print(distribution_generator([colors, colors]))

output:
[['red', 'red'], ['red', 'green'], ['red', 'yellow'], ['red', 'blue'],
['green', 'red'], ['green', 'green'], ['green', 'yellow'], ['green', 'blue'],
['yellow', 'red'], ['yellow', 'green'], ['yellow', 'yellow'], ['yellow', 'blue'],
['blue', 'red'], ['blue', 'green'], ['blue', 'yellow'], ['blue', 'blue']]


The method is simple and the time complexity was reduced comparing with standard methods. It can be used with all data type.  
