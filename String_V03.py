# ReType's Make string kerning lists for MetricsMachine 3.0

# Set the title
title = 'MetricMachine_kerning_block'

# Tweak / Comment from line 7 to 10 if you are using a PC.
import sys
sys.dont_write_bytecode = True
f = open(title + '.txt', 'w')
sys.stdout = f

print '#KPL:W: ' + title


def makeString(string):
    list = string.split()
    for x in range(len(list) - 1):
        list.insert(x + 1, ' ')
        print ''.join(list)
        list.pop(x + 1)


# Example: format your string in this way (space separated)
makeString('/slash /one.lf /slash /two.lf /slash /three.lf /slash /four.lf /slash /five.lf /slash /six.lf /slash /seven.lf /slash /eight.lf /slash /nine.lf /slash')
makeString('/slash /one /slash /two /slash /three /slash /four /slash /five /slash /six /slash /seven /slash /eight /slash /nine /slash')
