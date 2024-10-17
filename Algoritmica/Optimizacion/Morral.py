import random

def contador(i):
    return i + 1

def morral(tamano_morral, pesos, valores, n, i):
    i = contador(i)  # Actualizar el contador
    if n == 0 or tamano_morral == 0:
        return 0, i
    
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1, i)
    
    valor_con_item, i_con_item = morral(tamano_morral - pesos[n-1], pesos, valores, n-1, i)
    valor_sin_item, i_sin_item = morral(tamano_morral, pesos, valores, n-1, i)
    
    return max(valores[n-1] + valor_con_item, valor_sin_item), max(i_con_item, i_sin_item)

if __name__ == '__main__':
    for j in range(1, 15):
        valores = [random.randint(0, 100) for _ in range(j)]
        pesos = [random.randint(0, 100) for _ in range(j)]
        tamano_morral = 10 * j

        n = len(valores)
        i = 0  # Inicializar el contador

        resultado, llamadas = morral(tamano_morral, pesos, valores, n, i)
        print('Cuando N =', n, 'llama:', llamadas, '(2**(n+1)) - 1 =', (2**(n+1)) - 1)
        print('El valor máximo sería:', resultado)
