class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"] = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        text_props = ""
        if self.props is None:
            return text_props
        for k, v in self.props.items():
            text_props += f' {k}="{v}"'
        return text_props
    
    def __eq__(self, value):
        return (
            self.tag == value.tag and
            self.value == value.value and
            self.children == value.children and
            self.props == value.props
        )
    
    def __repr__(self):
        return f'''HTMLNode Object Details:
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props_to_html()}
        '''