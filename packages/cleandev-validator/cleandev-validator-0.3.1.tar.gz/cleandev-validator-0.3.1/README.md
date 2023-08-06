# CleanDev Validator

Librería que tiene por objetivo cambiar ligeramente el comportamiento de las clases tipo `@dataclass` añadiendo
una forma de evitar y realizar una validación previa de sus atributos según necesidad

![diagrama](https://gitlab.com/cleansoftware/libs/public/cleandev-validator/-/raw/master/docs/diagram.png)

## @dataclass

Vamos a mostrar algunos ejemplos del uso de `@dataclass` en python de forma nativa y posteriormente lo compararemos con
los añadidos que se implementan con esta librería para que se note la intención de la misma.

### Ejemplo basico

La principal causa por la que uno quisiera usar `@dataclass` es crear las famosas clases de estructura de datos que
solo tienen la finalidad de agrupar ciertos atributos y trabajas con ellos de una forma muy concreta.

Si quisieramos una clase con atributos con el unico fin de hacer getter y setters sin usar `@dataclass` tendriamos algo
como esto.

```python
class Persona:
    edad: int
    altura: int
    apellidos: str
    peso: int
    nombre: str

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        self.edad = edad

    @property
    def altura(self):
        return self.altura

    @altura.setter
    def altura(self, altura):
        self.altura = altura

    @property
    def apellidos(self):
        return self.apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.apellidos = apellidos

    @property
    def peso(self):
        return self.peso

    @peso.setter
    def peso(self, peso):
        self.peso = peso

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
```

A continuación ejecutaremos el mismo ejemplo usando `@dataclass`

```python
from dataclasses import dataclass


@dataclass()
class Persona:
    edad: int
    altura: int
    apellidos: str
    peso: int
    nombre: str
```

Como se puede apreciar es mucho más compacto no obstante cuando queremos usar dicha clase tenemos que definir todos sus
atributos si no queremos un error, o como alternativa definir un metodo `__init__()` que sobreescriba el comportamiento
por defecto de `@dataclass` para permitirnos decidir que campos y cuales no queremos dar de alta.

Veamoslo en el siguiente ejemplo

```python
from dataclasses import dataclass


@dataclass()
class Persona:
    edad: int
    altura: int
    apellidos: str
    peso: int
    nombre: str


@dataclass()
class Animal:
    peso: int
    edad: int
    nombre: str

    def __init__(self, peso: int, edad: int):
        self.peso = peso
        self.edad = edad


if __name__ == '__main__':
    # Definiendo todos sus atributos para no tener un error
    persona: Persona = Persona(edad=18, altura=176, apellidos='Hernandez', peso=80, nombre='Daniel')

    # Para el caso de animal no estamos obligados a definirle un nombre por lo que estamos obligados a definir un método
    # __init__()
    animal: Animal = Animal(peso=20, edad=10)
```

Existe una forma compacta de hacer el ejemplo para la clase `Animal`

```python
from dataclasses import field
from dataclasses import dataclass


@dataclass()
class Animal:
    peso: int
    edad: int
    nombre: str = field(init=False)


if __name__ == '__main__':
    animal: Animal = Animal(peso=20, edad=10)

```

Ahora bien realmente pese a definir el tipo de dato realmente no se comprueba si el tipo de datos que se le asigna es
el correcto, veamos un ejemplo

```python
from dataclasses import field
from dataclasses import dataclass


@dataclass()
class Animal:
    peso: int
    edad: int  # Definimos como entero
    nombre: str = field(init=False)


if __name__ == '__main__':
    animal: Animal = Animal(peso=20, edad='tengo 10 años')  # ¿¿?? Le pasamos una string para edad
```

Ademas de esto no existe una forma sencilla de convertir la clase en `dict` y filtrarle algunos atributos cosa de
evitarme que crear el tipico DTO (DataTransferObject) para ese fin o cosas equivalente. Buscando sobre ese caso uno de
los mejores intentos de hacer esto lo
encontre [aquí](https://stackoverflow.com/questions/68722516/exclude-some-attributes-from-str-representation-of-a-dataclass/68722666)

Ni tampoco existe una forma facil de retornar unicamente el nombre de los atributos de mi clase.

## DataClass

Clase que añade dos metodos a toda clase que herede de ella que sirven para filtrar atributos de la clase y retornar
los nombres de los atributos de la misa.

### __fields__

La propiedad `__fields__` de esta clase retorna los atributos de la misma.

```python
from dataclasses import field
from dataclasses import dataclass
from cleandev_validator import DataClass


@dataclass
class Animal(DataClass):
    peso: int
    edad: int
    nombre: str = field(init=False)


if __name__ == '__main__':
    animal: Animal = Animal(peso=20, edad='tengo 10 años')
    animal.__fields__  # ['peso', 'edad', 'nombre']
```

### __filter__()

Recibe como parametro un `list` y un `bool` (default=True)
`bool`: Bandera que decide si queremos incluir o excluir los campos pasados por la lista
`list`: Dado una lista en funcion de `bool`, si es `True` solo mostrara (k,v) de los valores pasados por la lista
en caso contrario solo excluira dichos valores.

```python
from dataclasses import field
from dataclasses import dataclass
from cleandev_validator import DataClass


@dataclass
class Animal(DataClass):
    peso: int
    edad: int
    nombre: str = field(init=False)


if __name__ == '__main__':
    animal: Animal = Animal(peso=20, edad='tengo 10 años')
    animal.__filter__(['peso'])  # {'peso': 20}
    animal.__filter__(['peso'], False)  # {'edad': 'tengo 10 años'}

```

### validaciones de atributos

Para ejecutar la validación propuesta de atributos hay que definir un método `__constrains__` de esta manera ademas de

```python
from dataclasses import field
from dataclasses import dataclass
from cleandev_validator import DataClass, _DataClassConstrains


@dataclass()
class Animal(DataClass):
    peso: int
    edad: int
    active: bool
    nombre: str = field(init=False)

    @property
    def __constrains__(self):
        return {
            'edad': str(_DataClassConstrains.INT)
        }


```

Ademas de un método para que se mantegan las validaciones propias del `@dataclass`

```python
def __post_init__(self):
    super(Animal, self)._validate(**self.__dict__)
```

El resultado final

```python
from dataclasses import field
from dataclasses import dataclass

from cleandev_validator import DataClass, _DataClassConstrains

@dataclass()
class Animal(DataClass):
    peso: int
    edad: int
    active: bool
    nombre: str = field(init=False)

    def __post_init__(self):
        super(Animal, self)._validate(**self.__dict__)

    @property
    def __constrains__(self):
        return {
            'peso': str(_DataClassConstrains.INT),
            'edad': str(_DataClassConstrains.INT),
            'active': str(_DataClassConstrains.BOOL),
        }


if __name__ == '__main__':
    animal: Animal = Animal(peso=20, edad=20, active=True)
    animal.__filter__(['peso'])  # {'peso': 20}
    animal.__filter__(['peso'], False)  # {'edad': 'tengo 10 años'}
```

De esta forma estamos obligando a que realmente todos los campos son del tipo que se define y ademas de si hay que 
definirlo o no a la hora de crear la clase usando `field(init=False)`