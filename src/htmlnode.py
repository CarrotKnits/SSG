


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None): # tag is str, value is str, chidren is list, props is dictionary
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Function not yet implemented")
    
    def props_to_html(self):
        if (self.props is None) or (self.props is {}):
            return ""
        else:
            formatted_string = ''
            for key in self.props:
                formatted_string = formatted_string + f' {key}="{self.props[key]}"'
            return formatted_string

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return str(self.value)
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
    
        else:
            final_string = f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                final_string = final_string + f'{child.to_html()}'
            return final_string + f'</{self.tag}>'
