# Dictionary in python
d1 = { }
print(d1)
d2 = {"Ram": "pasta","Shyam": "Maggi","Kohli": "Bathure","Rohit": {"B": "Poha", "L": "Dal roti","D": "Pav bhaji"}}
d2["Ankit"] = "Junk food"
d2["Sourav"] = "Dal tikad"
#print(d2["Rohit"])
#print(d2["Rohit"]["B"])
#del d2["Ram"]
#d3 = d2.copy()
#print(d2.get("Kohli"))
d2.update({"leena": "Coffee"})
print(d2.keys())
print(d2.items())