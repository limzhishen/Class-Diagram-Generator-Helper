from data.datatype import class_type,method_type,attributes_access_type
# """
# <mxCell id="2" value="Person" style="swimlane;fontStyle=1;childLayout=stackLayout;" parent="1" vertex="1">
#     <mxGeometry x="330" y="280" width="160" height="164" as="geometry" />
# </mxCell>
# """
_interface="&lt;&lt;interface&gt;&gt;&#xa;"
_abstarct="&lt;&lt;Abstract&gt;&gt;&#xa;"
class titleText:
    def __init__(self,id,name,type):
        self.id=id
        self.name=name
        self.check_type(type)
    def get_back(self):
        return(f"""<mxCell id="{self.id}" value="{self.name}" style="swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;" parent="1" vertex="1">
                        <mxGeometry x="330" y="280" width="160" height="164" as="geometry" />
                    </mxCell>
               """)
    def check_type(self,type):
        if type==class_type.Interface.value:
            self.name=_interface+self.name
        elif type==class_type.Abstract.value:
            self.name=_abstarct+self.name
        elif type==class_type.Class.value:
            pass
       

# <mxCell id="hHCIbGpsmqmkXR4JZTMh-3" value="child" style="text;" parent="2" vertex="1">
#     <mxGeometry y="26" width="160" height="26" as="geometry" />
# </mxCell>
class subText:
    def __init__(self,id,name,parent,y_axis):
        self.id=id
        self.name=name
        self.parent=parent
        self.y_axis=y_axis
        
        
    
    def method_process(self,**kwargs):
         for key,value in kwargs.items():
            if key=="parameter" and value!="":
                self.name=f"{self.name} ({', '.join(value)})"
            if key=="type":
                if value==method_type.Private.value:
                    self.name="- "+self.name
                    continue
                elif value==method_type.Public.value:
                    self.name="+ "+self.name
                    continue
                elif value == method_type.Protected.value:
                    self.name="# "+self.name
                    continue
                else:
                    self.name="+ "+self.name
                
                
    def attributes_process(self,**kwargs):
        for key,value in kwargs.items():
            if key=="type" and value!="" :
                self.name=self.name+": "+value
            if key=="access_type":
                if value==attributes_access_type.Private.value:
                    self.name="- "+self.name
                    continue
                elif value==attributes_access_type.Public.value:
                    self.name="+ "+self.name
                    continue
                elif value == attributes_access_type.Protected.value:
                    self.name="# "+self.name
                    continue
                else:
                    self.name="+ "+self.name
                
        
    def get_back(self):
        return(f""" <mxCell id="{self.id}" value="{self.name}" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" parent="{self.parent}" vertex="1">
                    <mxGeometry y="{self.y_axis}" width="160" height="26" as="geometry" />
                </mxCell>
                """)
# <mxCell id="2IQ6KFNbmM4y4lDrINHY-4" value="" style="line;strokeWidth=1;" vertex="1" parent="2IQ6KFNbmM4y4lDrINHY-2">
#     <mxGeometry y="52" width="160" height="8" as="geometry" />
# </mxCell>

class middle_line:
    def __init__(self,id,parent,y_axis):
        self.id=id
        self.parent=parent
        self.y_axis=y_axis

    def get_back(self):
        return( f"""<mxCell id="{self.id}" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;" vertex="1" parent="{self.parent}">
                        <mxGeometry y="{self.y_axis}" width="160" height="8" as="geometry" />
                    </mxCell>
                    """)
    