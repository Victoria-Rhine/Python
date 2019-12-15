from encode import encode

def test_empty_string():
    assert encode("") == ""

def test_single_nonrepeating_character():
    assert encode("a") == "a"
    assert encode("B") == "B"

def test_return_original_string_if_compressed_is_not_shorter():
    assert encode("ABC") == "ABC"
    assert encode("AaBbCc") == "AaBbCc" 

def test_three_or_more_nonrepeating_characters():
    assert encode("abcdef") == "abcdef"
    assert encode("hIj") == "hIj"

def test_multiple_characters_with_repetition():
    assert encode("AAbbbbb") == "A2b5"
    assert encode("aaa") == "a3"
