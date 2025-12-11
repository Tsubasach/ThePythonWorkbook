mass=input("Enter mass")
temp=input("Enter the Temp")
energy=4.186 * float(mass) * float(temp)
print(f"The energy you need is: {energy:.2f} jolues")
kilowolt=float(energy) / 3.6e6
costs=float(kilowolt) * 8.9
print(f"the energ you need is: {kilowolt:.2f} kw/h which costs {costs:.2f} cents" )