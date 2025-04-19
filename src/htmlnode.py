class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
    
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
    
        return props_str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(self, tag, value, props)
    def to_html(self):
        if LeafNode.value == None:
            raise ValueError()
        if LeafNode.tag == None:
            return LeafNode.value
        else:
            pass
    
    