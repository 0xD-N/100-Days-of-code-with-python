from prettytable import PrettyTable

p = PrettyTable()

p.field_names = ["Pokemon name", "Type"]

p.add_row(["Pikachu", "Electric"])
p.add_row(["Squirtle", "Water"])
p.add_row(["Charmander", "Fire"])

p.preserve_internal_border = True
p.align = "l"

print(p)