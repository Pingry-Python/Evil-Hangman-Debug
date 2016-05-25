def print_debug(families):
  ''' Prints the remaining possible words by family for debug mode.
      Retuns None'''
  
  total = 0
  print("\n\n[[DEBUG]]")
  for family in families:
    length = len(families[family])
    total += length
    print("\n{} ({} words)".format(family, length))
    print(families[family])
  print("\n[[DEBUG {} total words]]".format(total))
