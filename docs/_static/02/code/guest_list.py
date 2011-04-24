allowed_guest_1 = "Mir Nazim"
allowed_guest_2 = "Owais Lone"
allowed_guest_3 = "John Doe"
allowed_guest_4 = "George Bush"

print "Enter guest's name: ",
guest_at_gate = raw_input()

if guest_at_gate == allowed_guest_1:
    print "Allow"
elif guest_at_gate == allowed_guest_2:
    print "Allow"
elif guest_at_gate == allowed_guest_3:
    print "Allow"
elif guest_at_gate == allowed_guest_4:
    print "Allow"
else:
    print "Do Not Allow"
