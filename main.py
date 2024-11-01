import random
Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0

quiz = [
    {
        "question": "Un muggle se enfrenta a ti y te dice que está seguro de que eres una bruja o un mago. Vos si:",
        "options":[
            {
                "statement": "Pregúnteles qué les hace pensar eso",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Acepte y pregunte si les gustaría una muestra gratis de una maldición",
                "answer": "Gryffindor"
            },
            {
                "statement": "Acepta y aléjate, dejándolos preguntándose si estás fanfarroneando.",
                "answer": "Slytherin"
            },
            {
                "statement": "Dígales que está preocupado por su salud mental y ofrézcase a llamar a un médico.",
                "answer": "Hufflepuff"
            },
        ]
    },
  {
        "question": "Entras en un jardín encantado. ¿Qué sería lo que más le interesaría examinar primero?: ",
        "options":[
            {
                "statement": "La estatua de un viejo mago con un extraño centelleo en los ojos.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "El estanque burbujeante, en cuyas profundidades se arremolina algo luminoso",
                "answer": "Gryffindor"
            },
            {
                "statement": "El árbol de hojas de plata con manzanas doradas.",
                "answer": "Slytherin"
            },
            {
                "statement": "Las setas gordas rojas que parecen estar hablando entre sí",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "¿Cuál de las siguientes opciones le resulta más difícil de manejar?",
        "options":[
            {
                "statement": "Hambre",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Aburrimiento",
                "answer": "Gryffindor"
            },
            {
                "statement": "Soledad",
                "answer": "Slytherin"
            },
            {
                "statement": "Frío",
                "answer": "Hufflepuff"
            },
        ]
    },
    {
        "question": "Tú y dos amigos deben cruzar un puente custodiado por un troll del río que insiste en luchar contra uno de ustedes antes de que los deje pasar a todos. Vos si:",
        "options":[
            {
                "statement": "Intenta confundir al troll para que te deje pasar a los tres sin luchar.?",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Voluntario para luchar?",
                "answer": "Gryffindor"
            },
            {
                "statement": "Sugiera que los tres peleen (sin decirle al troll)?",
                "answer": "Slytherin"
            },
            {
                "statement": "Sugerir sorteo para decidir quién de ustedes peleará?",
                "answer": "Hufflepuff"
            },
        ]
    },
  
  
  
  
  
  
    # {
    #     "question" : "Entras en un jardín encantado. ¿Qué sería lo que más le interesaría examinar primero?",
    #     "options": [
    #         "Las setas gordas rojas que parecen estar hablando entre sí",
    #         "El estanque burbujeante, en cuyas profundidades se arremolina algo luminoso",
    #         "El árbol de hojas de plata con manzanas doradas",
    #         "La estatua de un viejo mago con un extraño centelleo en los ojos."
    #     ]
    # }
]
def options(list):
    numeral = 0
    plantilla = ""
    while numeral < 4:
        plantilla += f"""\t {numeral+1}. {list[numeral].get("statement")} \n"""
        numeral += 1
    return plantilla


for value in quiz:
    print(f""" 
    {value.get("question")}

       {options(value.get("options"))}
    """)
    number = int(input("\t Ingrese su prespuesta: "))
    match value.get("options")[number-1].get("answer"):
        case "Gryffindor":
            Gryffindor += 1
        case "Hufflepuff":
            Hufflepuff += 1
        case "Slytherin":
            Slytherin += 1
        case "Ravenclaw":
            Ravenclaw += 1
        case _:
            print(":(")



print("Gryffindor: ", Gryffindor)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)
print("Ravenclaw: ", Ravenclaw)

max_puntos = max(Gryffindor, Hufflepuff, Slytherin, Ravenclaw)
casas = []

if Gryffindor == max_puntos:
    casas.append("Gryffindor")
if Hufflepuff == max_puntos:
    casas.append("Huffl epuff")
if Slytherin == max_puntos:
    casas.append("Slytherin")
if Ravenclaw == max_puntos:
    casas.append("Ravenclaw")

if len(casas) > 1:
    casa_asignada = random.choice(casas)
else:
    casa_asignada = casas[0]

print(f"\n¡El Sombrero Seleccionador te ha asignado a: {casa_asignada}!")   