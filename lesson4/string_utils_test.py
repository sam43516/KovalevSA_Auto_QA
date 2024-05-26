from string_utils import StringUtils
import pytest


#capitilize - Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст.

@pytest.mark.parametrize("str, result", [("ivan","Ivan"), ("Ivan","Ivan" ), ("a","A"), ("иван","Иван")])
def test_capitilize_positive(str, result):
    string = StringUtils()
    res = string.capitilize(str)
    assert res == result

@pytest.mark.parametrize("str, result", [("1","1"), ("%","%"), ("🍑","🍑"), (" "," ")])
def test_capitilize_negative(str, result):
    string = StringUtils()
    res = string.capitilize(str)
    assert res == result   



# trim - Принимает на вход текст и удаляет пробелы в начале, если они есть.
    
@pytest.mark.parametrize("str, result", [ (" test","test"), ("   0","0"),("abc","abc"),("tes     t","tes     t"),("", "")])
def test_trim_positive_and_negative(str, result):
    string = StringUtils()
    res = string.trim(str)
    assert res == result



# to_list - Принимает на вход текст с разделителем и возвращает список строк. Параметры: `string` - строка для обработки, `delimeter` - разделитель строк. По умолчанию запятая (",").

@pytest.mark.parametrize("str, result", [("a,b,c,d", ["a", "b", "c", "d"]), ("1,2,3,4", ["1", "2", "3", "4"]), (":,:,:,:", [":", ":", ":", ":"]),(",", ["",""])])
def test_to_list_delimeter_comma(str, result):
    string = StringUtils()
    res = string.to_list(str)
    assert res == result

@pytest.mark.parametrize("str, delimeter, result", [("a*b*c*d", "*", ["a", "b", "c", "d"]), ("1:2:3", ":", ["1", "2", "3"]), ("П.П.П", ".", ["П", "П", "П"]), ("@;#;$;%", ";", ["@", "#", "$", "%"])])
def test_to_list_positive(str, delimeter, result):
    string = StringUtils()
    res = string.to_list(str, delimeter)
    assert res == result
    
@pytest.mark.parametrize("str, delimeter, result", [("abc", ",", ["abc"]), ("1 2 3", " ", ["1", "2", "3"]), (" ", " ", [])])
def test_to_list_negative(str, delimeter, result):
    string = StringUtils()
    res = string.to_list(str, delimeter)
    assert res == result




# contains - Возвращает `True`, если строка содержит искомый символ и `False` - если нет. Параметры:`string` - строка для обработки, `symbol` - искомый символ.

@pytest.mark.parametrize("str, symbol, result", [("SkyPro", "S", True), ("SkyPro", "Sky", True),("SkyPro", "SkyPro", True),("SkyPro", "G", False),("А", "A", False)] )
def test_contains_positive(str, symbol, result):
    string = StringUtils()
    res = string.contains(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result", [("SkyPro", "", True), ("", "", True), (" ", " ", True)] )
def test_contains_negative(str, symbol, result):
    string = StringUtils()
    res = string.contains(str, symbol)
    assert res == result




# delete_symbol - Удаляет все подстроки из переданной строки. Параметры:`string` - строка для обработки, `symbol` - искомый символ для удаления. 
  
@pytest.mark.parametrize("str, symbol, result", [("SkyPro", "k", "SyPro"), ("SkyPro", "SkyPro", ""), ("SkyPro", "Skypro", "SkyPro")] )
def test_delete_symbol_postive(str, symbol, result):
    string = StringUtils()
    res = string.delete_symbol(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result", [("SkyPro", "", "SkyPro"), ("SkyPro", " ", "SkyPro"), ("SkyPro", "g", "SkyPro")] )
def test_delete_symbol_negative(str, symbol, result):
    string = StringUtils()
    res = string.delete_symbol(str, symbol)
    assert res == result


        
# starts_with - Возвращает `True`, если строка начинается с заданного символа и `False` - если нет. Параметры:`string` - строка для обработки, `symbol` - искомый символ.
    
@pytest.mark.parametrize("str, symbol, result", [("Семен", "С", True), ("Семен", "H", False), (" Семен", " ", True), ("Семен", "C", False)])
def test_starts_with_positive(str, symbol, result):
    string = StringUtils()
    res = string.starts_with(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result", [("Семен", "", False ), ("", "", True ), ("     ", "     ", True )] )
def test_starts_with_negative(str, symbol, result):
    string = StringUtils()
    res = string.starts_with(str, symbol)
    if symbol == "" and str != "":
        pytest.xfail(reason= 'за неимением спецификации - считаю багом')
    assert res == result



# end_with - Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет. Параметры:`string` - строка для обработки, `symbol` - искомый символ.

@pytest.mark.parametrize("str, symbol, result", [("Семен", "н", True), ("Семен", "H", False), ("Семен", " ", False), ("Петр", "p", False)])
def test_end_with_positive(str, symbol, result):
    string = StringUtils()
    res = string.end_with(str, symbol)
    assert res == result

@pytest.mark.parametrize("str, symbol, result", [("Семен", "", False), ("Семен", " ", False), ("", "", True), (" ", " ", True)])
def test_end_with_negative(str, symbol, result):
    string = StringUtils()
    res = string.end_with(str, symbol)
    if symbol == "" and str != "":
        pytest.xfail(reason= 'за неимением спецификации - считаю багом')
    assert res == result



# is_empty - Возвращает `True`, если строка пустая и `False` - если нет.
   
@pytest.mark.parametrize("str, result", [("", True), (" ", True), ("тест", False)])
def test_is_empty_positive(str, result):
    string = StringUtils()
    res = string.is_empty(str)
    assert res == result

@pytest.mark.parametrize("str, result", [("______", False), (" " " ", True)])
def test_is_empty_negative(str, result):
    string = StringUtils()
    res = string.is_empty(str)
    assert res == result


# list_to_string - Преобразует список элементов в строку с указанным разделителем. Параметры: `lst` - список элементов, `joiner` - разделитель элементов в строке. По умолчанию запятая (", ").

@pytest.mark.parametrize("list, result", [([1,2,3], "1, 2, 3"), (["1", 1], "1, 1"), ([True, 1.2], "True, 1.2"), ([[1, 2], (1, 2)], "[1, 2], (1, 2)")])
def test_list_to_string_joiner_comma(list, result):
    lst = StringUtils()
    res = lst.list_to_string(list)
    assert res == result

@pytest.mark.parametrize("list, joiner, result", [([1,True,"str"], ":", "1:True:str"), ([3.14, [1], "(abc)"], "-", "3.14-[1]-(abc)"), ([{"Имя":"Семен"},2], "@", "{'Имя': 'Семен'}@2")])
def test_list_to_string_positive(list, joiner, result):
    lst = StringUtils()
    res = lst.list_to_string(list, joiner)
    assert res == result

@pytest.mark.parametrize("list, joiner, result", [([], ",", ""), ([",",","], ",", ",,,"), ([123], "", "123")])
def test_list_to_string_negative(list, joiner, result):
    lst = StringUtils()
    res = lst.list_to_string(list, joiner)
    assert res == result