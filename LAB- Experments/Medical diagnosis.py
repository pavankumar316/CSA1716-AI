print("MEDICAL DIAGNOSIS SYSTEM")
print("-----------------------")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()
sore_throat = input("Do you have sore throat? (yes/no): ").lower()

print("\nDIAGNOSIS RESULT")

if fever == "yes" and cough == "yes" and sore_throat == "yes":
    print("Symptoms may be consistent with a respiratory infection.")

elif fever == "yes" and headache == "yes":
    print("Fever with headache can have several causes. Medical evaluation may be needed.")

elif cough == "yes" and sore_throat == "yes":
    print("Symptoms may be associated with a respiratory illness.")

elif headache == "yes":
    print("Headache has many possible causes. Monitor symptoms.")

else:
    print("Insufficient information for a suggestion.")

print("\nThis program is for educational purposes only.")
print("Consult a healthcare professional for medical advice.")
