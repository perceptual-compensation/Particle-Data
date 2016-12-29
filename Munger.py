# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:39:33 2016

@author: PWillis
"""
import os
import json

try:
	filePath = os.path.split(__file__)[0] + "/"
except:
	filePath = ""

with open(filePath + "results", "rt") as f:
    results = f.read().split("\n")
outFile = open(filePath + "results.json", "wt")

struc = {}
for line in results:
    if line and line[0] != "#":
        spl = line.split(",")
        if spl[2] == "Form":
        	struc[spl[1]] = {"Time" : int(spl[0]), spl[7] : spl[8], "Items" : {}}
        else:
        	if not struc[spl[1]]["Items"].get(spl[3]):
        		struc[spl[1]]["Items"][spl[3]] = {"Type" : spl[5], "Playback" : {}, "Responses" : {}}
        	if len(spl) == 10:
        		struc[spl[1]]["Items"][spl[3]]["Playback"][spl[9]] = {"Action" : spl[7], "Location" : float(spl[8])}
        	elif len(spl) == 8:
        		struc[spl[1]]["Items"][spl[3]]["Stimulus"] = spl[7]
        	elif len(spl) == 9:
        		struc[spl[1]]["Items"][spl[3]]["Scenario"] = spl[7]
        	elif len(spl) == 11:
        		if spl[7] != "NULL":
        			struc[spl[1]]["Items"][spl[3]]["Responses"][spl[7]] = {"Answer" : spl[8], "Time" : int(spl[10])}

outFile.write(json.dumps(struc, sort_keys=True, indent=4))
outFile.close()


