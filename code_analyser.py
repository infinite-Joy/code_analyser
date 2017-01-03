import ast

class AnalyseCode(object):
    """This will analyse the code and return if there is a
    specific construct used or not

    Attributes:
        code (str): the code that is provided as the argument to the class.
        attr2 (:obj:`int`, optional): Description of `attr2`.

        this is for ref and will be deleted later
        take the conventions from the google code conventions"""
    def __init__(self, code):
        super(AnalyseCode, self).__init__()
        self.code = code
        self.tree = ast.parse(code)
        self.tree = ast.dump(self.tree)

    def has_list_append(self) -> bool:
        if self.tree.find("Call"):
            return "append" in self.tree


# import pprint

# original_code='''
# my_list=['raindrops n roses', 'whiskers on kittens']
# my_list.append('bright copper kettles')
# '''

# print(original_code)

# import ast

# tree = ast.parse(original_code)

# pp = pprint.PrettyPrinter(indent=4)

# des = ast.dump(tree)

# pp.pprint(des)

# print(des.find("Call"))

# print(des.find("append"))
