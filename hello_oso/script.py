from oso import Oso

oso = Oso()

oso.load_str("""allow("user", "can_use", "this_program");""")

if oso.is_allowed("user", "can_use", "this_program"):
    print("Hello from oso")
else:
    print("Access denied")

if oso.is_allowed("user-123", "can_run", "this_program"):
    print("Hello again, but you probably can't run this line.")
else:
    print("You weren't authorized by the rules!")
