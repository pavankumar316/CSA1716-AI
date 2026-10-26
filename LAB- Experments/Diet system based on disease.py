print("DIET SUGGESTION SYSTEM")
print("----------------------")
print("1. Diabetes")
print("2. High Blood Pressure")
print("3. Anemia")
print("4. Obesity")
print("5. Fever")

choice = int(input("Enter your disease choice (1-5): "))

if choice == 1:
    print("\nDisease: Diabetes")
    print("Diet Suggestions:")
    print("- Eat whole grains and vegetables.")
    print("- Choose whole fruits in moderate portions.")
    print("- Avoid sugary drinks and excess sweets.")

elif choice == 2:
    print("\nDisease: High Blood Pressure")
    print("Diet Suggestions:")
    print("- Reduce salt and high-sodium foods.")
    print("- Eat fruits and vegetables.")
    print("- Choose fresh foods instead of processed foods.")

elif choice == 3:
    print("\nDisease: Anemia")
    print("Diet Suggestions:")
    print("- Eat iron-rich foods such as beans and lentils.")
    print("- Include green leafy vegetables.")
    print("- Eat vitamin C-rich fruits with meals.")

elif choice == 4:
    print("\nDisease: Obesity")
    print("Diet Suggestions:")
    print("- Eat balanced meals with vegetables and protein.")
    print("- Limit sugary drinks and highly processed foods.")
    print("- Maintain regular physical activity as appropriate.")

elif choice == 5:
    print("\nDisease: Fever")
    print("Diet Suggestions:")
    print("- Drink enough fluids.")
    print("- Eat easily tolerated foods such as soup.")
    print("- Rest and monitor your symptoms.")

else:
    print("Invalid choice. Please enter a number from 1 to 5.")
