tecnologias = ("Python", "JavaScript", "React", "PostgreSQL")


backend, *resto, base_datos = tecnologias
print(*resto)

lenguajes = {"Python", "JavaScript", "Python", "Java", "JavaScript"}
lenguajes.add("c++")
lenguajes.add("Python")
print(lenguajes)

flor = {"Python", "JavaScript", "React", "PostgreSQL"}
lucia = {"Python", "Java", "PostgreSQL", "Docker"}

tecnologias_en_comun = flor & lucia
todas_las_tecnologias = flor | lucia
diferencia_en_tecnologias = flor - lucia
diferencia_en_tecnologias2 = lucia - flor
print(tecnologias_en_comun, todas_las_tecnologias, diferencia_en_tecnologias, diferencia_en_tecnologias2)