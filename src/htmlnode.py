class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or not isinstance(self.props, dict):
            return ""
        prop_list = [f'{key}="{value}"' for key, value in self.props.items()]
        return " ".join(prop_list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super(LeafNode, self).__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("Node value must be provided")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_output = super().props_to_html()
            return f"<{self.tag} {props_output}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super(ParentNode, self).__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node tag must be provided")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Node children must be provided")
        if self.props is None:
            converted_string = f"<{self.tag}>"
        else:
            props_output = super().props_to_html()
            converted_string = f"<{self.tag} {props_output}>"
        for child in self.children:
            converted_string += child.to_html()
        converted_string += f"</{self.tag}>"
        return converted_string
