# --find the item name, ex: god_conf 
# --for that item name,
#	--identify what sentence it is (string compare: split on first space,
#	  save to string, stringcompare to actual sentences 
#	--match that to a category:decl, exclam, conf. try catch loop?
#	--in the try catch loop, if it matches one of the sentences,
#	  then change the name appropriately: "god_conf" + "+decl"
#
# -> the tricky part is that we have to change all of the tags within
#    a given QuestionFrame; the number of items in this varies.

import scipy
import pydub
import os

pathResults = "results_27Dec.txt"
pathSaveAs = "cleaned_results27Dec.txt"
parts = ["Huh", "God", "Oh", "What"]

def tryAndSee(sent):
	emotion = "error"
	if str(sent) in ["we're out of flour", "I put the toolbox in the shed", "I'm on the phone", "another pile of papers to grade"]:
		emotion = "decl" 
	elif str(sent) in ["you don't know how to tango", "I thought apples were in the sunflower family", "she's never done that before", "I've never heard that before"]:
		emotion = "conf"
	elif str(sent) in ["he really likes it", "a package arrived for you" , "you can't be serious right now", "there are a lot of cakes to choose from"]:
		emotion = "exclam"
	return emotion
		

a = open(pathSaveAs, "a")

with open(pathResults, "rt") as b:
	lines = b.read().split("\n")

for i, line in enumerate(lines):
	if line and line[0] != "#":
		array = line.split(',')
		print line + ": " + str(len(array)) + " elements."
		if ' ' in array[7] and array[7].split(' ')[0] in parts:
			otherArray = array[7].split(' ')
			temp = " ".join(array[7].split(" ")[1:]) 
			print temp + "\n"
			emot2 = tryAndSee(temp)
			a.write(",".join(array[0:5]) + "," + str(array[5] + "+" + emot2 + ",") + ",".join(array[6:]) + "\n")
a.close()

		



def checkCol(array):
	return NULL