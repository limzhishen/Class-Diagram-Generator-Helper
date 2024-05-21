from enum import Enum

# """
# <mxCell id="arrow2" value="" style="endArrow=block;html=1;rounded=0;endFill=0;edgeStyle=orthogonalEdgeStyle;dashed=0" parent="1" target="2" edge="1" source="3">
#     <mxGeometry width="50" height="50" relative="1" as="geometry" />
# </mxCell>
# """
class arrow_type(Enum):
    normal="classic"
    extend="block"
    implement="open"

class arrow_drawio:
    def __init__(self,id,arrow:arrow_type,source,target,width=50,height=50):
        self.id=id
        self.arrow=arrow.value
        self.dash=0
        self.source=source
        self.target=target
        self.width=width
        self.height=height
        self.check_dashed()
    def get_back(self):
        return (f"""<mxCell id="arrow_{self.id}" value="" style="endArrow={self.arrow};html=1;rounded=0;endFill=0;edgeStyle=orthogonalEdgeStyle;dashed={self.dash}" parent="1" target="{self.target}" edge="1" source="{self.source}">
    <mxGeometry width="{self.width}" height="{self.height}" relative="1" as="geometry" />
</mxCell>""")
    def check_dashed(self):
        value= self.arrow
        if value=="open":
            self.dash=1