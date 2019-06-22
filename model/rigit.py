import tkinter
import argparse
import cv2
import os
from math import sqrt,pow
from os.path import relpath
import numpy as np
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

class MainWindow():

    def __init__(self, main):
        self.frame = Frame(main)
        self.frame.grid(row=0, column=0)
        self.frame2 = Frame(main)
        self.frame2.grid(row=1,column=0)
        self.frame3 = Frame(main)
        self.frame3.grid(row=2,column=0)
        self.canvas = Canvas(self.frame, width=780, height=640)
        self.canvas.grid(row=0,column=0)
        self.scroll_x = Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set,scrollregion=self.canvas.bbox("all"))
        # button to change image
        self.openbutton = Button(self.frame2, text="New Image", command=self.openImage)
        self.openbutton.grid(row=0,column=0)
        self.loadbutton = Button(self.frame2, text="Load project",command=self.openSaved)
        self.loadbutton.grid(row=0,column=1)
        self.editbutton = Button(self.frame2, text="Edit skeleton", command=self.onEdit)
        self.editbutton.grid(row=0,column=2)
        self.savebutton = Button(self.frame2, text="Save skeleton", command=self.onSave)
        self.savebutton.grid(row=0,column=3)
        # self.textspace = Text(self.frame)
        self.edges=[]
        self.keypoints=[]
        self.color = [255,0 , 0]
        self.colorcircle = [0, 0, 255]
        self.mode = ""
        self.inputfile = ""
        self.outputfile = ""
        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = ImageTk.PhotoImage(file="hi.png"))

    def tkinter_display(self,the_message):
        try:
            self.textspace.grid_remove()
        except(NameError, AttributeError):
            pass
        self.textspace = Label(self.frame3, text=the_message)
        self.textspace.grid(row=0)

    def loadSkeleton(self):
        filename = self.source
        ipimg = cv2.imread(filename)
        self.srcheight,self.srcwidth,_ = ipimg.shape
        for edge in self.edges:
            a,b = edge[0],edge[1]
            x_a,y_a = self.keypoints[a][0],self.keypoints[a][1]
            x_b,y_b = self.keypoints[b][0],self.keypoints[b][1]
            cv2.circle(ipimg, (int(x_a), int(y_a)), 8, self.colorcircle, -1)
            cv2.circle(ipimg, (int(x_b), int(y_b)), 8, self.colorcircle, -1)
            cv2.line(ipimg, (int(x_a), int(y_a)), (int(x_b), int(y_b)), self.color, 3)
        self.photo2 = ImageTk.PhotoImage(image = Image.fromarray(ipimg))
        self.canvas.itemconfig(self.image_on_canvas,image=self.photo2)
        # self.canvas.configure(scrollregion=canvas.bbox("all"))
        self.tkinter_display('Displaying skeleton. Click on edit to make changes to skeleton')

    def onSave(self):
        writefile = open(self.outputfile,"w")
        writefile.write(self.inputfile+"\n")
        for kpt in self.keypoints:
            writefile.write(str(kpt[0])+","+str(kpt[1])+",0.0\n")
        for edge in self.edges:
            writefile.write(str(edge[0])+","+str(edge[1])+"\n")
        writefile.close()
        print("File saved as ",self.outputfile)
        self.tkinter_display('File saved as '+self.outputfile)

    def loadSaved(self):
        filename = self.outputfile
        opfile = open(filename)
        for aline in opfile:
            args = aline.split(',')
            if(len(args) == 1):
                self.inputfile = args[0]
            elif(len(args)==2):
                self.edges.append((int(float(args[0])),int(float(args[1].split('/')[0]))))
            elif(len(args)==3):
                self.keypoints.append((int(float(args[0])),int(float(args[1]))))
        opfile.close()
        self.inputfile = self.inputfile.split('\n')[0]
        self.source = relpath(self.inputfile,os.getcwd())
        self.loadSkeleton()

    def openSaved(self):
        filename = askopenfilename(title="Select an skl file")
        if filename != "" and filename.split('.')[-1] == "skl":
            self.tkinter_display("Openinng file "+filename)
            self.outputfile = filename
            self.loadSaved()
        else:
            self.tkinter_display("Please select a .skl file")

    def resetflags(self):
        self.flag = 0
        self.pivot1 = -1
        self.pivot2 = -1

    def addmode(self):
        self.mode = "add"
        self.tkinter_display("Select the nodes to add a node between them")
        self.resetflags()

    def movemode(self):
        self.mode = "move"
        self.tkinter_display("Select a node and Click anywhere to it to that position")
        self.resetflags()

    def deletemode(self):
        self.mode = "delete"
        self.tkinter_display("Select a node to delete it")
        self.resetflags()

    def printcoords(self,event):
        if(event.x >= 0 and event.x <= self.srcwidth and event.y >= 0 and event.y <= self.srcheight):
            if(self.mode == "move"):
                if self.flag == 0:
                    #If first node, search for the point
                    for i in range(len(self.keypoints)):
                        kpx = int(self.keypoints[i][0])
                        kpy = int(self.keypoints[i][1])
                        dist = sqrt(pow((kpx-event.x),2)+pow((kpy-event.y),2))
                        if(dist<=8):
                            break;
                    self.pivot1 = i
                    self.flag = 1
                elif self.flag == 1:
                    i = self.pivot1
                    self.keypoints[i] = (event.x,event.y)
                    self.loadSkeleton()
                    self.resetflags()
            elif self.mode == "add":
                if self.flag == 0:
                    for i in range(len(self.keypoints)):
                        kpx = int(self.keypoints[i][0])
                        kpy = int(self.keypoints[i][1])
                        dist = sqrt(pow((kpx-event.x),2)+pow((kpy-event.y),2))
                        if(dist<=8):
                            break;
                    self.pivot1 = i
                    self.flag = 1
                elif self.flag == 1:
                    for i in range(len(self.keypoints)):
                        kpx = int(self.keypoints[i][0])
                        kpy = int(self.keypoints[i][1])
                        dist = sqrt(pow((kpx-event.x),2)+pow((kpy-event.y),2))
                        if(dist<=8):
                            break;
                    self.pivot2 = i
                    self.flag = 2
                elif self.flag == 2:
                    self.keypoints.append((event.x,event.y))
                    # indextoremove = self.edges.index((self.pivot1,self.pivot2))
                    self.edges.remove((self.pivot1,self.pivot2))
                    self.edges.append((self.pivot1,len(self.keypoints)-1))
                    self.edges.append((len(self.keypoints)-1,self.pivot2))
                    self.loadSkeleton()
                    self.resetflags()
            elif self.mode == "delete":
                if self.flag == 0:
                    for i in range(len(self.keypoints)):
                        kpx = int(self.keypoints[i][0])
                        kpy = int(self.keypoints[i][1])
                        dist = sqrt(pow((kpx-event.x),2)+pow((kpy-event.y),2))
                        if(dist<=8):
                            break;
                    self.pivot1 = i
                    self.flag = 1
                    neighbors = []
                    for i in range(len(self.edges)):
                        if self.edges[i][0] == self.pivot1:
                            neighbors.append(self.edges[i][1])
                        elif self.edges[i][1] == self.pivot1:
                            neighbors.append(self.edges[i][0])
                    for i in range(len(self.edges)):
                        if self.edges[i][0] == self.pivot1:
                            for j in range(len(neighbors)):
                                if(neighbors[j] != self.edges[i][1]):
                                    if (neighbors[j],self.edges[i][1]) not in self.edges and (self.edges[i][1],neighbors[j]) not in self.edges:
                                        self.edges.append((self.edges[i][1],neighbors[j]))
                        elif self.edges[i][1] == self.pivot1:
                            for j in range(len(neighbors)):
                                if(neighbors[j] != self.edges[i][0]):
                                    if (neighbors[j], self.edges[i][0]) not in self.edges and (self.edges[i][0],neighbors[j]) not in self.edges:
                                        self.edges.append((self.edges[i][0],neighbors[j]))
                    edgelength = len(self.edges)
                    kk = 0
                    while(kk < edgelength):
                        if self.edges[kk][0] == self.pivot1 or self.edges[kk][1] == self.pivot1:
                            self.edges.remove(self.edges[kk])
                            kk-=1
                            edgelength-=1
                        kk+=1
                    self.loadSkeleton()
                    self.resetflags()


    def onEdit(self):
        self.addbutton = Button(self.frame2, text="Add point", command=self.addmode)
        self.addbutton.grid(row=1,column=1)
        self.movebutton = Button(self.frame2, text="Move point", command=self.movemode)
        self.movebutton.grid(row=1,column=2)
        self.deletebutton = Button(self.frame2, text="Delete Point", command=self.deletemode)
        self.deletebutton.grid(row=1,column=3)
        self.resetbutton = Button(self.frame2, text="Reset prediction",command=self.onPredict)
        self.resetbutton.grid(row=1,column=4)
        self.canvas.bind("<Button 1>",self.printcoords)

    def openImage(self):
        try:
            self.addbutton.grid_remove()
            self.movebutton.grid_remove()
            self.deletebutton.grid_remove()
            self.resetbutton.grid_remove()
        except(NameError, AttributeError):
            pass
        filename = askopenfilename(title="Select an image")
        if filename != "":
            self.inputfile = filename
            cvimg = cv2.imread(filename)
            self.srcheight,self.srcwidth,_ = cvimg.shape
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(cvimg))
            self.canvas.itemconfig(self.image_on_canvas,image=self.photo)
            # self.canvas.configure(scrollregion=canvas.bbox("all"))
            self.predictbutton = Button(self.frame2, text="Predict Skeleton", command=self.onPredict)
            self.predictbutton.grid(row=1,column=0)

    def onPredict(self):
        # Predict skeleton
        self.tkinter_display('Predicting image')
        filename = self.inputfile
        self.inputfile = filename.split('\n')[0]
        print("Predicting skeleton")
        mycmd = "./rundemo.sh "+filename
        os.system(mycmd)
        filename = filename.split('/')[-1]
        self.outputfile = "output/"+(filename.split('.')[0])+".skl"
        self.loadSaved()

#----------------------------------------------------------------------

root = Tk()
root.title("Rig a sketch")
MainWindow(root)
root.mainloop()