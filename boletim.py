lista = [{'nome': 'Sophia Ahart', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 55, 'portugues': 70, 'ciencias': 95, 'historia': 95, 'geografia': 60, 'ingles': 75}}, {'trimestre': 2, 'disciplinas': {'matematica': 90, 'portugues': 85, 'ciencias': 95, 'historia': 65, 'geografia': 90, 'ingles': 55}}, {'trimestre': 3, 'disciplinas': {'matematica': 50, 'portugues': 70, 'ciencias': 55, 'historia': 65, 'geografia': 90, 'ingles': 80}}]}, {'nome': 'Michael Tobias', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 90, 'portugues': 80, 'ciencias': 80, 'historia': 50, 'geografia': 60, 'ingles': 90}}, {'trimestre': 2, 'disciplinas': {'matematica': 85, 'portugues': 65, 'ciencias': 90, 'historia': 55, 'geografia': 90, 'ingles': 85}}, {'trimestre': 3, 'disciplinas': {'matematica': 90, 'portugues': 75, 'ciencias': 85, 'historia': 75, 'geografia': 50, 'ingles': 65}}]}, {'nome': 'Paul Asakura', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 85, 'portugues': 50, 'ciencias': 75, 'historia': 90, 'geografia': 90, 'ingles': 60}}, {'trimestre': 2, 'disciplinas': {'matematica': 55, 'portugues': 80, 'ciencias': 55, 'historia': 95, 'geografia': 70, 'ingles': 50}}, {'trimestre': 3, 'disciplinas': {'matematica': 75, 'portugues': 50, 'ciencias': 95, 'historia': 75, 'geografia': 80, 'ingles': 90}}]}, {'nome': 'Leon Mcthay', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 65, 'portugues': 60, 'ciencias': 80, 'historia': 50, 'geografia': 65, 'ingles': 85}}, {'trimestre': 2, 'disciplinas': {'matematica': 75, 'portugues': 95, 'ciencias': 50, 'historia': 65, 'geografia': 60, 'ingles': 70}}, {'trimestre': 3, 'disciplinas': {'matematica': 55, 'portugues': 75, 'ciencias': 75, 'historia': 55, 'geografia': 95, 'ingles': 60}}]}, {'nome': 'Linda Flowers', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 50, 'portugues': 65, 'ciencias': 80, 'historia': 60, 'geografia': 90, 'ingles': 80}}, {'trimestre': 2, 'disciplinas': {'matematica': 50, 'portugues': 50, 'ciencias': 90, 'historia': 85, 'geografia': 80, 'ingles': 80}}, {'trimestre': 3, 'disciplinas': {'matematica': 55, 'portugues': 70, 'ciencias': 60, 'historia': 65, 'geografia': 55, 'ingles': 95}}]}, {'nome': 'Jonathan Smith', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 50, 'portugues': 60, 'ciencias': 60, 'historia': 90, 'geografia': 90, 'ingles': 80}}, {'trimestre': 2, 'disciplinas': {'matematica': 70, 'portugues': 80, 'ciencias': 85, 'historia': 85, 'geografia': 65, 'ingles': 95}}, {'trimestre': 3, 'disciplinas': {'matematica': 90, 'portugues': 55, 'ciencias': 90, 'historia': 60, 'geografia': 90, 'ingles': 65}}]}, {'nome': 'Carlos Russo', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 75, 'portugues': 80, 'ciencias': 95, 'historia': 60, 'geografia': 80, 'ingles': 50}}, {'trimestre': 2, 'disciplinas': {'matematica': 75, 'portugues': 85, 'ciencias': 55, 'historia': 80, 'geografia': 85, 'ingles': 55}}, {'trimestre': 3, 'disciplinas': {'matematica': 95, 'portugues': 60, 'ciencias': 95, 'historia': 70, 'geografia': 85, 'ingles': 80}}]}, {'nome': 'Vita Smith', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 70, 'portugues': 60, 'ciencias': 90, 'historia': 60, 'geografia': 55, 'ingles': 60}}, {'trimestre': 2, 'disciplinas': {'matematica': 55, 'portugues': 95, 'ciencias': 75, 'historia': 80, 'geografia': 70, 'ingles': 85}}, {'trimestre': 3, 'disciplinas': {'matematica': 70, 'portugues': 90, 'ciencias': 75, 'historia': 75, 'geografia': 70, 'ingles': 75}}]}, {'nome': 'Joyce Sabb', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 95, 'portugues': 80, 'ciencias': 60, 'historia': 60, 'geografia': 65, 'ingles': 50}}, {'trimestre': 2, 'disciplinas': {'matematica': 50, 'portugues': 85, 'ciencias': 90, 'historia': 75, 'geografia': 95, 'ingles': 95}}, {'trimestre': 3, 'disciplinas': {'matematica': 85, 'portugues': 95, 'ciencias': 50, 'historia': 65, 'geografia': 55, 'ingles': 65}}]}, {'nome': 'Ernest Broussard', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 70, 'portugues': 85, 'ciencias': 80, 'historia': 60, 'geografia': 65, 'ingles': 55}}, {'trimestre': 2, 'disciplinas': {'matematica': 50, 'portugues': 55, 'ciencias': 75, 'historia': 85, 'geografia': 65, 'ingles': 50}}, {'trimestre': 3, 'disciplinas': {'matematica': 95, 'portugues': 90, 'ciencias': 95, 'historia': 60, 'geografia': 75, 'ingles': 90}}]}]



for i in range(len(lista)):
   print(f"Aluno:           | Disciplina |1º Trim. |2º Trim. |3º Trim. | Média | Situação")
   mediac = (int(lista[i]['boletim'][0]['disciplinas']['ciencias'])
             + int(lista[i]['boletim'][1]['disciplinas']['ciencias'])
             + int(lista[i]['boletim'][2]['disciplinas']['ciencias']))/3
   if mediac >= 70:
       situacao = 'Aprovado'
   else:
       situacao = 'Reprovado'
   print(f"{lista[i]['nome']:<16}",
         f"|Ciências    "
         f"|{lista[i]['boletim'][0]['disciplinas']['ciencias']:^8} "
         f"| {lista[i]['boletim'][1]['disciplinas']['ciencias']:^7} "
         f"| {lista[i]['boletim'][2]['disciplinas']['ciencias']:^7} "
         f"| {int(mediac):^5} "
         f"| {situacao}")
   mediag = (int(lista[i]['boletim'][0]['disciplinas']['geografia']) +
             int(lista[i]['boletim'][1]['disciplinas']['geografia']) +
             int(lista[i]['boletim'][2]['disciplinas']['geografia']))/3
   if mediag >= 70:
       situacao = 'Aprovado'
   else:
       situacao = 'Reprovado'
   print(f"                 |Geografia   "
         f"|{lista[i]['boletim'][0]['disciplinas']['geografia']:^8} "
         f"| {lista[i]['boletim'][1]['disciplinas']['geografia']:^7} "
         f"| {lista[i]['boletim'][2]['disciplinas']['geografia']:^7} "
         f"| {int(mediag):^5} "
         f"| {situacao}")
   mediah = (int(lista[i]['boletim'][0]['disciplinas']['historia']) +
             int(lista[i]['boletim'][1]['disciplinas']['historia']) +
             int(lista[i]['boletim'][2]['disciplinas']['historia']))/3
   if mediah >= 70:
       situacao = 'Aprovado'
   else:
       situacao = 'Reprovado'
   print(f"                 |História    "
         f"|{lista[i]['boletim'][0]['disciplinas']['historia']:^8} "
         f"| {lista[i]['boletim'][1]['disciplinas']['historia']:^7} "
         f"| {lista[i]['boletim'][2]['disciplinas']['historia']:^7} "
         f"| {int(mediah):^5} "
         f"| {situacao}")
   mediai = (int(lista[i]['boletim'][0]['disciplinas']['ingles']) +
             int(lista[i]['boletim'][1]['disciplinas']['ingles']) +
             int(lista[i]['boletim'][2]['disciplinas']['ingles']))/3
   if mediai >= 70:
       situacao = 'Aprovado'
   else:
       situacao = 'Reprovado'
   print(f"                 |Inglês      "
         f"|{lista[i]['boletim'][0]['disciplinas']['ingles']:^8} "
         f"| {lista[i]['boletim'][1]['disciplinas']['ingles']:^7} "
         f"| {lista[i]['boletim'][2]['disciplinas']['ingles']:^7} "
         f"| {int(mediai):^5} "
         f"| {situacao}")
   mediam = (int(lista[i]['boletim'][0]['disciplinas']['matematica']) +
             int(lista[i]['boletim'][1]['disciplinas']['matematica']) +
             int(lista[i]['boletim'][2]['disciplinas']['matematica']))/3
   if mediam >= 70:
       situacao = 'Aprovado'
   else:
       situacao = 'Reprovado'
   print(f"                 |Matemática  "
         f"|{lista[i]['boletim'][0]['disciplinas']['matematica']:^8} "
         f"| {lista[i]['boletim'][1]['disciplinas']['matematica']:^7} "
         f"| {lista[i]['boletim'][2]['disciplinas']['matematica']:^7} "
         f"| {int(mediam):^5} "
         f"| {situacao}")
   mediap = (int(lista[i]['boletim'][0]['disciplinas']['portugues']) +
             int(lista[i]['boletim'][1]['disciplinas']['portugues']) +
             int(lista[i]['boletim'][2]['disciplinas']['portugues']))/3
   if mediap >= 70:
       situacao = 'Aprovado'
   else:
       situacao = 'Reprovado'
   print(f"                 |Português   "
         f"|{lista[i]['boletim'][0]['disciplinas']['portugues']:^8} "
         f"| {lista[i]['boletim'][1]['disciplinas']['portugues']:^7} "
         f"| {lista[i]['boletim'][2]['disciplinas']['portugues']:^7} |"
         f" {int(mediap):^5} | {situacao}")
   print('{message:{fill}{align}{width}}'.format(message='-', fill='-', align='^', width=80))

