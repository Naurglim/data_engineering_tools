
Los commits pueden referenciarse con los primeros números de su hash (5 o 6 suelen bastar)
También se pueden referenciar por su distancia con el último:
    [HEAD] El último commit
    [HEAD~X] El commit a X distancia del último
En algunos comandos en los que se puede obviar el commit, se utiliza [--] para saltear el parámetro y tomar el default (HEAD)

**Comandos:**

git checkout
    [-b 'nombre_de_rama'] Crea una nueva rama y se posiciona en ella.
    [#commit] recupera los archivos de un commit en particular. Se puede usar [--] para apuntar al ultimo (HEAD).
    [file] recupera solo ese archivo.

git add 
    [file] Un archivo particular
    [.] Todos los archivos del directorio con modificaciones

git commit -m "mensaje"

git status

git log 
    [-X] Sólo los últimos X commits
    [file] Sólo de un archivo en particular
    [--since='Apr 2 2024'] Desde qué fecha
    [--until='Apr 11 2024'] Hasta qué fecha

git show

git diff

git revert
    
git clean
    [-n] muestra la lista de archivos que no se están trackeando 
    [-f] elimina los archivos que no se están trackeando (no se puede deshacer)

