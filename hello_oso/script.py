from oso import Oso

oso = Oso()

oso.load_str("""allow("user", "can_use", "this_program");""")

if oso.is_allowed("user", "can_use", "this_program"):
    print("Hello from oso")
else:
    print("Access denied")
