houses = {
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
    }

houses ["Hermione"] = "Gryffindor"

if houses.get("Hermione") == houses.get("Harry") == "Gryffindor":
    print("True")