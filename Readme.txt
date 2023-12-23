Mi proyecto se basa en una tienda de bicicletas. Para dar un poco de contexto dejé el la vista About. Intenté reutilizar lo más posible lo ya realizado y que tuviera coherencia con la idea que tenía de proyecto.

Voy describiendo el proyecto y luego abajo dejo detalle de los problemas que no pude resolver, citando con asteriscos.

Implementé 2 modelos relativos a la tienda, que fueron Accesorio y Modelo bicicleta, bajo appStock.
Dejé implementado la creación, listado, modificación, eliminación y búsqueda. Para ello tuve que hacer alguna diferencia con lo que vimos en la clase, xq no tengo atributos que sean identificadores únicos de cada instancia de mi clase, por lo que muchas veces es la combinación de 2 atributos.
Por lo tanto, para la búsqueda dejé implementado una busqueda con selección del parámetro/criterio a buscar, x ejemplo, rodado, y devolviendo todos los elementos que cumplieran con ese criterio. Reutilicé el listado para esto.

Tenía dos objetivos para los usuarios:

- Modificar las vistas y el base.html en funcion si estaba loggeado o no (para que fuese coherente los links de inicio de sesión, logout, vista de inventario) --> Sencillo, lo hice correctamente
- Modificar las vistas, base y funciones para que los usuarios solo si is_staff puedan acceder a acciones de altas de inventario, modificación de stock, modifiación de perfil de usuario --> No lo logré, no me reconoce a usuarios como staff*
- Generar algun cambio en mis modelos para que, el administrador pudiera cambiar a uno o varios usuarios a is_staff, pero que luego haya un tipo de perfil de usuario, que podría ser "Vendedor", que pueda otorgar a otros usuarios dicha capacidad, y por lo tanto, también modificar perfiles, etc. --> No llegué ni a programarlo xq no pude ni empezar a probar la situación anterior.


No logré implementar la mensajería, pero no entendí si era obligatorio o no.


Errores no solucionados:

Mi template base difería un poco de lo usado en clase. Me anuvo todo salvo el fondo, que lo toma de una URL. Cuando me di cuenta, lo más cercano que estuve de solucionarlo fue dejarlo funcionando en la vist de inicio y About. Por más que le dediqué mucho tiempo, no pude solucionar el problema de que al cambiar de vista, me modifica el path, y pierdo el fondo. Se ve muy fácil desde la consola cuando pasamos a una url de appStock o appUsuarios, que no puede resolver el archivo. Es un detalle, pero me gustaría si me pueden ayudar a solucionarlo.
* Para esto estuve buscando en linea y no encontré solución. Imprimo en consola y en la vista el atributo is_staff del usuario que estoy utilizando, en el momento que miro el condicional, y es True... No se que ocurre. Por ejemplo, para ver esto, no puedo ver los botones de editar y eliminar items de mi listado de stock. Ver lista_accesorios.html