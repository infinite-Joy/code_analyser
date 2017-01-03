from code_analyser import AnalyseCode


def test_has_list_append_ifthere():
    code='''
my_list=['raindrops n roses', 'whiskers on kittens']
my_list.append('bright copper kettles')'''
    ac = AnalyseCode(code)
    assert ac.has_list_append() == True


def test_has_list_append_ifnotthere():
    code='''
my_list=['raindrops n roses', 'whiskers on kittens']'''
    ac = AnalyseCode(code)
    assert ac.has_list_append() == False


def test_check_properties():
    code = "a"
    ac = AnalyseCode(code)
    assert ac.tree == "Module(body=[Expr(value=Name(id='a', ctx=Load()))])"
