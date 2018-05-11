#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cite: www.zetcode.com
"""

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
import csv
import tkinter
import os
import sys



class ReviewMiner(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Review Miner--trending feature analyzer")

        self.style = Style()
        self.style.theme_use("default")


def switch_table(root,value):
    if value == 'Camera' :
        with open("data/features/cameras.csv", newline = "") as file:
            reader = csv.reader(file)
            r = 1
            for col in reader:
                c = 1
                for row in col:
                    label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)

                    label.grid(row = r, column = c)
                    c += 1
                r += 1
    if value == 'TV' :
        with open("data/features/TVs.csv", newline = "") as file:
            reader = csv.reader(file)
            r = 1
            for col in reader:
                c = 1
                for row in col:
                    label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)

                    label.grid(row = r, column = c)
                    c += 1
                r += 1

    if value == 'Tablet' :
        with open("data/features/tablets.csv", newline = "") as file:
            reader = csv.reader(file)
            r = 1
            for col in reader:
                c = 1
                for row in col:
                    label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)

                    label.grid(row = r, column = c)
                    c += 1
                r += 1
    if value == 'Mobilephone' :
        with open("data/features/mobilephones.csv", newline = "") as file:
            reader = csv.reader(file)
            r = 1
            for col in reader:
                c = 1
                for row in col:
                    label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)

                    label.grid(row = r, column = c)
                    c += 1
                r += 1
    if value == 'Video Surveillance' :
        with open("data/features/videosurveillance.csv", newline = "") as file:
            reader = csv.reader(file)
            r = 1
            for col in reader:
                c = 1
                for row in col:
                    label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)

                    label.grid(row = r, column = c)
                    c += 1
                r += 1
    if (len(sys.argv) > 1):
        with open("data/features/" + sys.argv[1] + ".csv", newline = "") as file:
            reader = csv.reader(file)
            r = 1
            for col in reader:
                c = 1
                for row in col:
                    label = tkinter.Label(root, width = 10, height = 2, \
                                   text = row, relief = tkinter.RIDGE)

                    label.grid(row = r, column = c)
                    c += 1
                r += 1

def main():

    root = Tk()
    root.geometry("850x600+300+300")
    app = ReviewMiner()
    mainframe = Frame(root)

    variable = StringVar(root)
    variable.set("Product")
    variable.trace_add('write', lambda *args: switch_table(root, variable.get()))


    optionList = ["Camera", "TV", "Tablet", "Mobilephone", "Video Surveillance"]
    if(len(sys.argv) > 1):
        optionList.append(sys.argv[1])
    w = OptionMenu(root, variable,  *optionList)
    w.grid(row = 0, column = 0, padx = 10, pady = 10)
    w.config(width=15)

    root.mainloop()


if __name__ == '__main__':
    main()
