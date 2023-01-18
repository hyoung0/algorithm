string = input()
print(string[:string.index("(")].count("@"), string[string.index("("):].count("@"))