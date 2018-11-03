from fz import fisbass
import pytest

def test_fissbass_takes_number_returns_string():
    result = fisbass(1)
    assert isinstance(result,str)

@pytest.mark.parametrize(("number", "expected"),[(1,"1"),(2,"2"),(4,"4"),(7,"7")])    
def test_fisbass_regular_returns_numbers(number,expected):
    result = fisbass(number)
    assert result == expected

@pytest.mark.parametrize("number", [3,6,9])    
def test_fiss_3_return(number):
    result = fisbass(number)
    assert result == "fizz"

@pytest.mark.parametrize("number", [5,10,55])    
def test_fiss_5_return(number):
    result = fisbass(number)
    assert result == "buzz"

@pytest.mark.parametrize("number", [15,30,300])    
def test_fiss_3__5_return(number):
    result = fisbass(number)
    assert result == "fizzbuzz"

def test_cannot_fizzbuzz_str():
    with pytest.raises(TypeError):
        fisbass("nope")

def test_cannot_fizzbuzz_none():
    with pytest.raises(TypeError):
        fisbass(None)

def test_cannot_fizzbuzz_float():
    with pytest.raises(TypeError):
        fisbass(5.5)

 # nepouzivat na otestovani, ze nevo nefunguje, rika se jim nekdy regresni testy
#@pytest.mark.xfail(strict=True)
#def test_xxx():
#    assert True
