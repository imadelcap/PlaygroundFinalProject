Mi proyecto se basa en una tienda de bicicletas. Para dar un poco de contexto dejé el la vista About. Intenté reutilizar lo más posible lo ya realizado y que tuviera coherencia con la idea que tenía de proyecto.

Voy describiendo el proyecto y luego abajo dejo detalle de los problemas que no pude resolver, citando con asteriscos.

Implementé 2 modelos relativos a la tienda, que fueron Accesorio y Modelo bicicleta, bajo appStock.
Dejé implementado la creación, listado, modificación, eliminación y búsqueda. Para ello tuve que hacer alguna diferencia con lo que vimos en la clase, xq no tengo atributos que sean identificadores únicos de cada instancia de mi clase, por lo que muchas veces es la combinación de 2 atributos.
Por lo tanto, para la búsqueda dejé implementado una busqueda con selección del parámetro/criterio a buscar, x ejemplo, rodado, y devolviendo todos los elementos que cumplieran con ese criterio. Reutilicé el listado para esto.

Para los usuarios discrimine la vista en base.html dependiendo de:
	- Si está loggeado:
		- Ver stock y crear/ver perfil
		- Loggearse
	- Si tiene perfil:
		- Crear perfil
		- Ver perfil

También discrimino y restrinjo la capacidad de acción del usuario dependiendo si es miembro del staff:
	- Dar altas de inventario: Mediante el ingreso de bicicletas o accesorios
	- Modificar o eliminar de los listados.
	## Ver otros usuarios
	## Modificar o eliminar otros usuarios.
#Probar ingresar directamente a las páginas que no permito por staff, en views.py> @staff_member_required//if al comienzo de la funcion.


###REVISAR###
Tenía dos objetivos para los usuarios:

- Modificar las vistas y el base.html en funcion si estaba loggeado o no (para que fuese coherente los links de inicio de sesión, logout, vista de inventario) --> Sencillo, lo hice correctamente
- Modificar las vistas, base y funciones para que los usuarios solo si is_staff puedan acceder a acciones de altas de inventario, modificación de stock, modifiación de perfil de usuario --> No lo logré, no me reconoce a usuarios como staff*
- Generar algun cambio en mis modelos para que, el administrador pudiera cambiar a uno o varios usuarios a is_staff, pero que luego haya un tipo de perfil de usuario, que podría ser "Vendedor", que pueda otorgar a otros usuarios dicha capacidad, y por lo tanto, también modificar perfiles, etc. --> No llegué ni a programarlo xq no pude ni empezar a probar la situación anterior.

