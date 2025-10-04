try:
    doc= open(r"C:\Users\oanas\OneDrive\Desktop\eSchool1.txt")
except FileNotFoundError as e : 
    print(f"File Not Found {e}")

else:
   print(doc.readlines())

