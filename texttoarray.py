import shutil
import os
import urllib

input = open('input.txt','r') # file from which you're reading
output = open("output.js", "w") # file to which you'll write

output.write("var array = [") # start array tag

out_text = "" 
for line in input:
	out_text += "'" + line.strip("\n") + "', "
output.write(out_text[:-2]) # this takes out the last comma and space, thank you @ingridavendano

output.write("];") # end array tag

input.close()
output.close()