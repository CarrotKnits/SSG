


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None): # tag is str, value is str, chidren is list, props is dictionary
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Function not yet implemented")
    
    def props_to_html(self):
        if self.props is None or {}:
            return ""
        else:
            formatted_string = ''
            for key in self.props:
                formatted_string = formatted_string + f' {key}="{self.props[key]}"'
            print(formatted_string)
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