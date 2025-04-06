"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Maria Freixas Solé
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other

    

    def __mul__(self, otro):
        """
        Método que permite multiplicar un vector por otro vector o constante.
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v1 * v2
        Vector([4, 10, 18])
        """
        if isinstance(otro, (int, float, complex)):
            return Vector([elemento * otro for elemento in self])
        else :
          # zip permite recorrer 2 iterables al mismo tiempo
            return Vector([num1*num2 for num1, num2 in zip(self, otro)]) 
        
    __rmul__ = __mul__ 

    def __matmul__(self, otro):
        """
        Permite calcular el producto matricial de dos vectores.
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32
        """
        if not isinstance(otro, Vector):
            raise TypeError("El producto matricial solo se puede realizar entre dos vectores")
        else:
            return sum([num1*num2 for num1, num2 in zip(self, otro)])
    
    def __rmatmul__(self, otro):
        """
        Metodo que permite calcular el producto matricial de dos vectores.
        """
        if not isinstance(otro, Vector): 
            raise TypeError("El producto matricial solo se puede realizar entre dos vectores")


    def __floordiv__(self, otro): 
        """
        Este metodo permite obtener el vector la componente paralela de v1 a v2, si v1 // v2.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        if not isinstance(otro, Vector):
            raise TypeError("No se puede proyectar un escalar sobre un vector.")
        
        else: 
            producto_escalar = self @ otro
            modulo = sum(a**2 for a in otro)
            factor = producto_escalar / modulo
            return Vector([num1 * factor for num1 in otro])
    
    def __rfloordiv__(self, otro):
        """
        Si se utiliza // de un vector por un escalar da error.
        """
        if not isinstance(otro, Vector):
            raise TypeError("No se puede proyectar un escalar sobre un vector.")
        
    def __mod__(self, otro):
        """
        Metodo que permite obtener el vector perpendicular de un vector sobre otro.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """

        if not isinstance(otro, Vector):
            raise TypeError("No se puede proyectar un escalar sobre un vector.")
        else: 
            tangencial = self // otro
            return Vector([num1 - num2 for num1, num2 in zip(self, tangencial)])
        
    def __rmod__(self, otro): 
        """
        Sucede el mismo error que en __rfloordiv__()
        """
        if not isinstance(otro, Vector): 
            raise TypeError("No se puede proyectar un escalar sobre un vector.")
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()