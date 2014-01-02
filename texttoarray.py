import shutil
import os
import urllib

input = open('input.txt','r') # file from which you're reading
output = open("output.js", "w") # file to which you'll write

output.write("var array = [") # start table tag

for line in input:
	output.write(line + ", ") # writing the list to array
	
output.write("];") # end table tag

input.close()
output.close()