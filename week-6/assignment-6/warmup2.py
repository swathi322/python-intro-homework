 #Functions that Return Values
#Write two functions:

#celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
#fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
#Call each with a few test values and print the results. Use f-strings and round to one decimal place.

#Example output — your test values and wording might differ:


#c= float(input("Enter temperature in Celaius: "))


def celsius_to_fahrenheit(c):
    """converts celsius to fahrenheit using"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """converts Fahrenheit to Celsius using"""
    return(f - 32) * 5/9

celsius_test = [0]
#rint("celsius to fahrenheit")
for c in celsius_test:
    f_result = celsius_to_fahrenheit(c)
print(f"{c}°C = {f_result:.1f}°F")

celsius_test = [100]
#pri("celsius to fahrenheit")
for c in celsius_test:
    f_result = celsius_to_fahrenheit(c)
print(f"{c}°C = {f_result:.1f}°F")

fahrenheit_test = [72]
#rint("fahrenheit to celsius:")
for f in fahrenheit_test:
    c_result = fahrenheit_to_celsius(f)
print(f"\n{f}°F = {c_result:.1f}°C")
