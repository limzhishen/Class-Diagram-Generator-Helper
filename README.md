# Class-Diagram-Generator-Helper
This is a personal Interest Project

## Prerequisite library
        -customtkinter
        -mypy [contributing] -not affect the code running
    Python 
        -typing
        -os
## Start up
Run [ClassGenerator_startup.py](ClassGenerator_startup.py)


# Support programming language  
    - Python (Multi-Thread default(3) )
    - Java (Multi-Thread default(3)) 
    - C# (Multi-Thread default(3))  (On Testing)

# Export type
- Draw Io (since can be easily configure but meet the repeat problem may will solve when i lack of brain)

## MultiThread Support (5 woker almost save 10 plus times)
- Python Read
- Java Read
- C# Read
- Draw Io export (On Beta Testing)

### Create Reason (For newbie)
While going a new company is hard to link the code espacially thier using the dependency injection and dependency invesion

## Vision
To help every on to do a good experience while viewing code
To help Student easily to make the Class Diagram

### For the drawio Component
If got the same Class name :

-The Duplicate class name will mention in last component and font-color will change to red
-The class which extend Duplicate class name will mention in last component and font-color will change to red
'After export using Arrange->horizon or vertical to help you easy arrange'

If have same class name better folder by folder export that will help easily to create the diagram
## For Controtibute
### fileReader (other programming language)
-> Add file inside fileReader extend ThreadFileReader.py
-> ClassGenerator_startup.py add 

    #Add Reader here
    def get_class(self, *argv)->ReadFile:
        elif self.selected.get()==".xx":
            return xx(*argv)
    
     # Processing file type (java python)
      CTkRadioButton(self, text="xx", variable=self.selected,value=".xx").grid(row=4, column=x,sticky="w")

### Export type
-> Add file inside export extend exportThreading,py
-> ClassGenerator_startup.py add 

    #Add Export here
    def get_export_Type(self,*argv):
        if self.selected_export.get()=="xx":
            return xxx(*argv)

     # Export file type (drawio)
      CTkRadioButton(self, text="xxx", variable=self.selected_export,value="xxx").grid(row=8, column=x,sticky="w")
## Tips
    For Something cannot thread default thread to 1