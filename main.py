import os
import funcion_n

def main():
    # Usar las funciones
    print(f"La suma de 10 + 5 es: {funcion_n.suma(10, 5)}")
    print(f"La resta de 10 - 5 es: {funcion_n.resta(10, 5)}")
    
    # Crear carpeta de resultados y archivos simulados
    os.makedirs('resultados', exist_ok=True)
    
    with open('resultados/imagen.png', 'w') as f:
        f.write("Simulación de imagen PNG")
    
    with open('resultados/grafica.eps', 'w') as f:
        f.write("Simulación de imagen EPS")
        
    print("Archivos generados exitosamente en la carpeta resultados/")

if __name__ == "__main__":
    main()
    #xd
