class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        html = ""
        if self.props is None:
            return ""

        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value} {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leafnode requires a value")
        if self.children:
            raise ValueError("Leafnode has no children")
        if self.tag is None:
            return self.value
        html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        if self.children is None:
            raise ValueError("ParentNode requires children")
        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

