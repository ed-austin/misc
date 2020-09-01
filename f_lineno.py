def f_lineno (): 
   """Returns the current line number in program"""
   import inspect
   return inspect.currentframe().f_back.f_lineno
