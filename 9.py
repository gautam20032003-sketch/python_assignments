nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
nested_student_dict["class"]["student"]["name"]="jasse"
print(nested_student_dict["class"]["student"]["name"])
print(nested_student_dict)