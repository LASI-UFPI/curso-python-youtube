dic = {
    "Nome": ["João","Marcos"],
    "Idade": [20,23],
    "Número": ["99882-5575","99999999"]
}

print(dic)

dic["Nome"].append("Maria")

dic["Idade"][0] = 22

print(dic)

dic.pop("Número")

print(dic)