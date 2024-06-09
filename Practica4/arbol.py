from positional_binary_tree import PositionalBinaryTree


def suma_arbol_binario(arbol):
    """Calcula la suma de todos los valores almacenados en un árbol binario."""
    if arbol.is_empty():
        return 0
    else:
        suma_izquierda = suma_arbol_binario(arbol.left_child())
        suma_derecha = suma_arbol_binario(arbol.right_child())
        return arbol.root_element() + suma_izquierda + suma_derecha
    
# Ejemplo de uso
arbol = PositionalBinaryTree(1,
                   PositionalBinaryTree(2, PositionalBinaryTree(4), PositionalBinaryTree(5)),
                   PositionalBinaryTree(3, PositionalBinaryTree(6), PositionalBinaryTree(7)))

print("La suma de todos los valores en el árbol es:", suma_arbol_binario(arbol))
