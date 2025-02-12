import re

class Valid:
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def zip(input):
    #length?
    if (len(input) != 5):
      return False

    #digits?
    if (not re.match(r"^[0-9]{5}$", input)):
      return False
    
    return True
  
  """
  Validate a ZIP code. return true if the input is a valid ZIP, 
  false otherwise.

  input: string
  output: boolean

  TODO: implement a method to validate a ZIP code
  """
  @staticmethod
  def phone(input):
    if (input == None):
      return False

    #length?
    if (len(input) < 10 or len(input) > 50):
      return False

    #format?
    if (not re.match(r"^\+[\d]{1,3} \([0-9]{3}\) [0-9]{3}-[0-9]{4}$", input)):
      return False
    
    return True