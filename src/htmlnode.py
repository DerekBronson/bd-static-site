class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

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
