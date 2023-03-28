# Notas

# Para crear un working directory, se usa 'git init' en la carpeta donde esta el/los archivo/s a trabajar.

# Se puede corroborar el estado de los archivos en el working directory usando 'git status'

# Para agregar un archivo a la staging area desde el working directory, se usa 'git add' y el nombre del archivo. Si se quiere agregar
# todo, se usa 'git add'.

# NO siempre que se guarda con ctrl + S se guarda el cambio a la staging area.
# Para mandar un cambio a la staging area, se hace 'git add'.

# Staged Changed son los archivos que ya estan en la zona de staging.

# Para pasar del staging al repository, se usa 'git commit -m "Mensaje descriptivo del cambio"'. El mensaje es util para saber
# que modificacion se realizo.

# 'git log' genera un listado de los commit que se realizaron. Cuantas 'versiones viejas' hay.

# Para ver el log resumido, se usa 'git log --oneline'.

# Para crear una rama nueva, se usa 'git branch nombre_rama'. Se puede ver las ramas creadas con 'git branch'. La rama en la que
# estamos ubicados va a aparecer en color.

# Para moverme entre ramas, se usa 'git checkout nombre_rama'.

# Para borrar una rama, se usa 'git branch -d nombre_rama_eliminar'.

# Para movernos a un commit, usamos 'git checkout primeros_7_num_id'. Con esto podemos pasar a una version anterior de una misma rama,
# en caso de que queramos volver hacia atras.

# Con 'git merge' me traigo lo que este en una rama a la rama en la que estoy.