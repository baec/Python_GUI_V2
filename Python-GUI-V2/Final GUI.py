#!/usr/bin/python3
# This needs to be documented!!!!
from tkinter import *
from tkinter import ttk
from math import sqrt
from tkinter.filedialog import*
from rect import Rectangle

#Function for the code question is placed at the
# The second character is checked for having {
#The first character is checking if it is any lower case character within the ascii table
#The third character is checked for having any lower case character within the ascii table
#The fourth character is checked for not having a asterick *
#The fifth character is checked for not having any numbers
#The sixth character is checked if there is any lower case character within the ascii table
#The seventh character is checked if there are any lower case character within the ascii table
#The eight character is checking any lower case character within the ascii table
#The ninth character is checked if there is any lower case character within the ascii table
#The tenth character is checked if there is any lower case character within the ascii table


def checking(codeList):
    fcount=0
    for Rcode in codeList:
        if len(Rcode) !=10 \
           or Rcode[1] != '{'\
           or Rcode[0] in string.ascii_lowercase\
           or Rcode[3] != '*'\
           or Rcode[4] not in string.digits\
           or Rcode[5] in string.ascii_lowercase\
           or Rcode[6] in string.ascii_lowercase\
           or Rcode[9] in string.ascii_lowercase\
           or Rcode[8]  in string.ascii_lowercase\
           or Rcode[7] != '}' \
           or Rcode[2] in string.ascii_lowercase :
                fcount+=1
    return fcount


##The class RecCounter is able to hold a number of functions: _init_,reset add and all the working out for the questions that I used in stage One


class RecCounter():
   def __init__(self):
      self.reset()
#counter for each of the questions the line number is set to 0, each of these need to also have self. at the front of them
   def reset(self):
      self.count  = 0
      self.countq1=0
      self.maximum=0
      self.totalq3=0
      self.countq3=0
      self.formatcountq4=0
      self.totalq5=0
      self.countq6=0
      self.countq7=0
      
   def add(self, rectangle):

      self.count += 1  # every time I add a Rectangle I add 1

      #q1
      if rectangle.getStat()=="Fog":  #Fog is the word I want to find in the stat field
         self.countq1=self.countq1+1 #countq1 can now go into the print section
      #q2
      if rectangle.getValue()>self.maximum: # Finds the Maximum value in the column 
         self.maximum=rectangle.getValue()  #maximum can now go into the print section
      #q3
      self.totalq3=self.totalq3+1   # checks the rows to count the numbe of integars 
      if rectangle.getWidth()>=11 and rectangle.getWidth()<=20:   # uses the colum width to find the percentage between the values 11 and 20
         self.countq3=self.countq3+1    #increment line number

      #q4

      if checking(rectangle.getCode()) >1:        # checking if the characters do NOT match with the function checking (code)
         self.formatcountq4=self.formatcountq4+1
            
      #q5
      if rectangle.getQuant() >= 602 and rectangle.getQuant()<= 2075:  # the sum of the numbers in the column quant between 602 and 2075 and because it is inclusive we use the equal sign.
         self.totalq5 += rectangle.getQuant()
         
      #q6
      if rectangle.getSwitch()=="On":    # Checks the number of times On comes up within the switch column
         self.countq6=self.countq6+1
         
      #7
      if rectangle.getValue()>692.74 or rectangle.getStat()=="Cloud":  # Two columns are being used for this question at the same time: the value column needs to have a value more than 692.74 at the same time the stat column has to consis to the word cloud 
         self.countq7=self.countq7+1
         


   def myq1(self):
      return ("The number of times fog comes up is: %d " %(self.countq1))          #Returns the answer for question one with the string displaying the question

   def myq2(self):
      return("The maximum number in the field[value] is: %d " %(self.maximum))      #Returns the answer for question two with the string displaying the question

   def myq3(self):
      return("The percentage of the numbers in [width] lie between (11) and (20) inclusive : %6.2f " %((self.countq3/self.totalq3)*100))  #Returns the answer for question three with the string displaying the question

   def myq4(self):
       return("The values in the 'code' field do not match the format X{X*9XX}XX is: %d" %(self.formatcountq4))    #Returns the answer for question four with the string displaying the question
      
   def myq5(self):
       return("The sum of the numbers in field [quant] between (602) and (2075) inclusive : %d" %(self.totalq5))        #Returns the answer for question five with the string displaying the question      
   
   def myq6(self):
      return("The number of times On comes up is: %d " %(self.countq6))#Returns the answer for question six with the string displaying the question

   def myq7(self):
      return("The lines where value is more than 692.74 *or* stat's have the value (Cloud): %d " %(self.countq7))#Returns the answer for question seven with the string displaying the question



class RecReader():
   def __init__(self, filename, counter, recgui):
     
      self.gui = recgui
      self.counter = counter
      self.infile = open(filename, 'r')   #This opens up the file and reads the contents of it
      if not self.infile:
         self.gui.fileNotFound()    # this leads to studying exceptions
      else:
         self.run()         
         #run is defined, open the file, set the file 
   def run(self):
        #for all the lines in the file first line is set to true                 
      firstline = True
      for line in self.infile:
         if firstline:
            firstline = False
            continue

        

         line = line.strip ()               # line.strip() removes the end of the line character that is stuck in the end of each line as it is read
         fields = line.split (",")           #mapping each of the columns in the excel spreadsheet to their field name this makes it easier for me to type their column name instead of their position again 
         stat = str( fields [0])           #The stat column is mapped out to be the first column and identified as a string
         value = float(fields [1])         #The fields column is mapped out as the second column and identified as a float
         width = int(fields [2])           #The width column is mapped out as the third column and identidfied as a number
         code = fields [3]                  #The code column is mapped out as the fourth column 
         quant = int(fields [4])            # The quant column is mapped out as the fifth column and identified as a string
         switch =  str(fields [5])          #The switch column is mapped out as the fifth column and identified as a string
             # then I pass a complete Rectangle to the counter object 
         self.counter.add( Rectangle(stat, value, width, code, quant, switch))
         
         #The file in the GUI needs to be closed after
      self.infile.close()
      self.gui.notify()
      

class RecGUI():
   def __init__(self, root):
      self.ok = False # indicate if there has been a valid read
      self.counter = RecCounter()


#This was the code from before the scenario, I removed this because I implented a new button which was able to open up the file directory directly 
      #Label(root, text="Enter Filename: ", width=12).grid(row=3, column=0, sticky=E)

      #self.flname = Entry(root, width=15, bg="white")
      #self.flname.grid(row=3, column=1, stick=W)



#This is the part of the code where we position each of the questions onto the GUI
#Label is used to place each of the question names in.
#Text is used to place the whatever number the question is
#Width dictates the length in which your label is, if it is too small then it would not show up
#The next row down with the self. are the answers for the questions and they are mapped using the grid feature
#There are three main columns and I have placed the 'question X' in the first column ([0]) while the answers to the question have been placed in column 1
#The width of the self answers have been set to 80 because they need a lot fo space to display on the GUI     
#q1
      Label(root, text="Question 1:", width=10).grid(row=4, column=0, sticky=E)
      self.q1= Label(root, width=80)
      self.q1.grid(row=4,column=1, sticky=W)
#q2
      Label(root, text="Question 2:", width=10).grid(row=5, column=0, sticky=E)
      self.q2=Label(root, width=80)
      self.q2.grid(row=5,column=1, sticky=W)
#q3
      Label(root, text="Question 3:", width=10).grid(row=6, column=0, sticky=E)
      self.q3=Label(root, width=80)
      self.q3.grid(row=6,column=1, sticky=W)
#q4
      Label(root, text="Question 4:", width=10).grid(row=7, column=0, sticky=E)
      self.q4= Label(root, width=80)
      self.q4.grid(row=7,column=1, sticky=W)
#q5
      Label(root, text="Question 5:", width=10).grid(row=8, column=0, sticky=E)
      self.q5= Label(root, width=80)
      self.q5.grid(row=8,column=1, sticky=W)
#q6
      Label(root, text="Question 6:", width=10).grid(row=9, column=0, sticky=E)
      self.q6= Label(root, width=80)
      self.q6.grid(row=9,column=1, sticky=W)
#q7
      Label(root, text="Question 7:", width=10).grid(row=10, column=0, sticky=E) #displays question on 9th row
      self.q7= Label(root, width=80)
      self.q7.grid(row=10,column=1, sticky=W)  #displays answer on 9th row

#The upload button allows for the user to open up the file directory,the code below is used to map the position of where that upload button gets placed
#The command code is used from the previous stage of pressing the go button, here I have implemented it into the upload button the process to display the results

      B2=Button(root,text="UPLOAD",command=self.process_file).grid(row=5,column=0,sticky=N)
      self.q8= Label(root, width=10)
      self.q8.grid(row=11,column=0, sticky=N)

      #self.maxDgLbl.grid(row=4,column=2, sticky=W)
      #self.mssg=Label(root)
      #self.mssg.grid(row=5,column=0,columnspan=3)

# This function calls the opening directory function and calls it filename      
   def process_file(self,):

      filename = askopenfilename()
      
      
      if len(filename) > 4:    #The filename has to match the specification set other wise it will not work
        self.ok = True
        self.counter.reset()
        self.reader=RecReader(filename, self.counter, self)
      
   def fileNotFound(self):
      self.ok = False
      
   def message(self, amssg):
      self.mssg['text']=amssg

# This displays the text as strings 
      
   def notify(self):
      if self.ok:
         self.q1['text'] = str(self.counter.myq1())
         self.q2['text'] = str(self.counter.myq2())
         self.q3['text'] = str(self.counter.myq3())
         self.q4['text'] = str(self.counter.myq4())
         self.q5['text'] = str(self.counter.myq5())
         self.q6['text'] = str(self.counter.myq6())
         self.q7['text'] = str(self.counter.myq7())







         
 
   ##########################
   ### It all starts here ###
   ##########################


# I have dedicated the end of the code to do many things primarily it is just for athestics such as adding picture      
if __name__ == "__main__":
   def CloseWindow(event):
    top.destroy()
    
   top = Tk()
   top.geometry("800x490")# This sets out the size of the window, The first value is the width while the second value is the height of the box
   top.iconbitmap(default='transparent.ico')# make the status bar at the top transparent for a more minimalist look
# the picutre has to be in gif frormat  has to be used when placing an image in a canvas and it also has to be in the same directory as the python file that is currently being run
   photo=PhotoImage(file="logo.png")
   areaDraw = Canvas(top,width=260,height=120)#Sets what column and row the image goes into
   areaDraw.create_image(140,60,image=photo)#left/right#up/down
   areaDraw.grid(row=0,column=0)

   photo1=PhotoImage(file="man.gif")
   areaDraw1 = Canvas(width=152,height=200)#Sets what column and row the image goes into
   areaDraw1.create_image(70,96,image=photo1)#left/right#up/down
   areaDraw1.grid(row=1,column=0)
##
   photo2=PhotoImage(file="Information.png")
   areaDraw2 = Canvas(width=700,height=100)#Sets what column and row the image goes into
   areaDraw2.create_image(170,60,image=photo2)#left/right#up/down
   areaDraw2.grid(row=1,column=1, sticky=N)

   areaDraw3=Canvas(width=100,height=100)#The size of the canvas
   photo3=PhotoImage(file="quit.gif")
   areaDraw3.grid(row=0,column=1,sticky="N")#Sets what column and row the image goes into
   quit1=areaDraw3.create_image(65,35, image= photo3)#left/right#up/down
   areaDraw3.tag_bind(quit1, '<ButtonPress-1>', CloseWindow)




   
   top.title("")
   top.grid()

   app = RecGUI(top)
   
   top.mainloop()
      
