import ast

class AnalyseCode(object):
    """This will analyse the code and return if there is a
    specific construct used or not

    Attributes:
        code (str): the code that is provided as the argument to the class.
        attr2 (:obj:`int`, optional): Description of `attr2`.

        this is for ref and will be deleted later
        take the conventions from the google code conventions

    TODO:
        fix mypy errors:
            code_analyser.py: note: In member "__init__" of class "AnalyseCode":
code_analyser.py:17: error: Incompatible types in assignment (expression has type "str", variable has type "AST")
code_analyser.py: note: In member "tree" of class "AnalyseCode":
code_analyser.py:21: error: Incompatible return value type (got "AST", expected "str")"""
    def __init__(self, code: str, _tree: str = "") -> None:
        super(AnalyseCode, self).__init__()
        self.code = code
        self._tree = ast.parse(code)
        self._tree = ast.dump(self._tree)

    @property
    def tree(self) -> "str":
        return self._tree

    def has_list_append(self) -> bool:
        t = str(self._tree)
        if t.find("Call"):
            return "append" in t

    def has_proper_classes(self):
        pass


if __name__ == '__main__':
    code='''
my_list=['raindrops n roses', 'whiskers on kittens']
my_list.append('bright copper kettles')'''
    ac = AnalyseCode(code)
    print(ac.has_list_append())