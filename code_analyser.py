import ast

class AnalyseCode(object):
    """This will analyse the code and return if there is a
    specific construct used or not

    Attributes:
        code (str): the code that is provided as the argument to the class.
        attr2 (:obj:`int`, optional): Description of `attr2`.

        this is for ref and will be deleted later
        take the conventions from the google code conventions"""
    def __init__(self, code: str, _tree: str = ""):
        super(AnalyseCode, self).__init__()
        self.code = code
        self._tree = ast.parse(code)
        self._tree = ast.dump(self._tree)

    @property
    def tree(self) -> "str":
        return self._tree

    def has_list_append(self) -> bool:
        if self._tree.find("Call"):
            return "append" in self._tree
