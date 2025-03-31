import pytest

def fix_phone_num(phone_num_to_fix):
  # given "5125558823". Split the parts, then recombine and return
  #to raise character value error
  number = "".join(char for char in phone_num_to_fix if char.isdigit())

  #to raise length value error
  if len(phone_num_to_fix) != 10:
    raise ValueError("Phone number must be exactly 10 digits long!")
  area_code = phone_num_to_fix[0:3] # 512 (first three digits)
  three_part = phone_num_to_fix[3:6] # 555 (next three digits)
  four_part = phone_num_to_fix[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_lastFix():
  with pytest.raises(ValueError):
    fix_phone_num("555-442-98761")
  assert fix_phone_num("(321) 654 3333") == "(321) 654 3333"

def test_fix_phone_num_v2():
  # given "5125558823". Split the parts, then recombine and return (try again)
  assert fix_phone_num("555-442-98761") == "(555) 442 9876"
  assert fix_phone_num("321-654-3333") == "(321) 654 3333"

def test_raiseError_wrongChar():
  with pytest.raises(ValueError):
    fix_phone_num("sun-yay-dirt")

def test_raiseError_wrongNum():
  with pytest.raises(ValueError):
    fix_phone_num("5125558")




  

  
