Mi proyecto se basa en una tienda de bicicletas. Para dar un poco de contexto dejé la vista About. Intenté reutilizar lo más posible lo ya realizado y que tuviera coherencia con la idea que tenía de proyecto.

Implementé 2 modelos relativos a la tienda, que fueron Accesorio y Modelo bicicleta, bajo appStock.
Dejé implementado la creación, listado, modificación, eliminación y búsqueda. Para ello tuve que hacer alguna diferencia con lo que vimos en la clase, xq no tengo atributos que sean identificadores únicos de cada instancia de mi clase, por lo que muchas veces es la combinación de 2 atributos. 
Por lo tanto, para la búsqueda dejé implementado una busqueda con selección del parámetro/criterio a buscar, x ejemplo, rodado, y devolviendo todos los elementos que cumplieran con ese criterio. Reutilicé el listado para esto.
Valió la pena aprender cómo realizar esto.

Luego implementé el modelo Usuario, cómo lo vimos en clase.

Las imágenes las implementé para las imágenes de usuario.

Los tiempos los implemente para fecha de creación y de modificación de objetos de appStock. Se pueden apreciar en los listados.

Para los usuarios discrimine la vista en base.html dependiendo de:
	- Si no está loggeado puede:
		- Inciar sesión o registrarse.
	- Si está loggeado puede:
		- Ver Listar modelos de appStock
		- Crear un perfil de usuario
		- Cerrar sesión
	- Si está loggeado y además tiene perfil de usuario
		- Ver su perfil
	- Si es staff puede:
		- Ver otros perfiles y asignar capacidades de Staff.
		- Crear objetos de appStock
		- Editar o eliminar objetos de appStock a través de los listados.


El template base está adecuado para discriminar estas situaciones, así como las vistas están protegidas para que no se puedan ingresar directamente.

Espero que sea fácil de revisar.

Saludos!