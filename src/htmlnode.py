

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented.")

    def props_to_html(self):
        if not self.props: # Handles None or an empty dictionary
            return ""
        else:
            html_attributes_string = ''
            for prop in self.props:
                html_attributes_string = html_attributes_string + f' {prop}="{self.props[prop]}"'
            return html_attributes_string.lstrip()
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("INVALID: All leaf nodes MUST have a value")
        elif not self.tag:
            return str(self.value)
        else:
            props_string = ''
            for prop in self.props:
                props_string = props_string + f' {prop}="{self.props[prop]}"'
            return f'<{self.tag}{props_string}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("INVALID: All parent nodes MUST have a tag")
        elif not self.children:
            raise ValueError("INVALID: All parent nodes MUST have children. Otherwise they aren't parents. It's only logic bro.")
        else:
            props_string = ""
            for prop in self.props:
                props_string = props_string + f' {prop}="{self.props[prop]}"'
            
            children_string = ""
            for child in self.children:
                if child.children == None:
                    children_string = children_string + f'{child}'
                else:
                    children_string = child.to_html()
            return f'<{self.tag}{props_string}>{children_string}</{self.tag}>'
            