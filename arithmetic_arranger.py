def arithmetic_arranger(problems,calc = False):
  if 5 < len(problems):
    return "Error: Too many problems."
  sOperand1 =  sOperand2 = sDashes = sResults = ""
  separator = "    "
  for i in range(len(problems)):
    words = problems[i].split()
    if(not (words[1] == "+" or words[1] =="-")):
      return "Error: Operator must be '+' or '-'."
    if( not words[0].isnumeric() or not words[2].isnumeric()):
      return "Error: Numbers must only contain digits."
    if(4 < len(words[0] ) or 4 < len(words[2])):
      return "Error: Numbers cannot be more than four digits."    
    lengthOp = max(len(words[0]),len(words[2]))
    sOperand1 += words[0].rjust(lengthOp+2)
    sOperand2 += words[1]+ " " + words[2].rjust(lengthOp) 
    sDashes += "-"*(lengthOp + 2)
    if calc:
      if words[1] == "+":
        sResults += str(int(words[0])+int(words[2])).rjust(lengthOp+2)    
      else:
        sResults += str(int(words[0])-int(words[2])).rjust(lengthOp+2)        
    if i < len(problems)-1:
      sOperand1 += separator
      sOperand2 += separator
      sDashes += separator
      sResults += separator 
  arranged_problems = sOperand1 + "\n" + sOperand2 + "\n" + sDashes 
  if calc:
    arranged_problems += "\n" + sResults
  return arranged_problems