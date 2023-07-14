class Departamento:
    def __init__(depa, tipo, piso):
        depa.tipo = tipo
        depa.piso = piso
        depa.estado = 'Disponible'
        depa.comprador = None


class DepartamentosManager:
    def __init__(depa):
        depa.departamentos = []
        depa.precios_venta = {'A': 3800, 'B': 3000, 'C':2800 , 'D': 3500}
        depa.compradores = {}

    def agregar_departamento(depa, tipo, piso):
        departamento = Departamento(tipo, piso)
        depa.departamentos.append(departamento)

    def mostrar_estado_departamentos(depa):
        for departamento in depa.departamentos:
            if departamento.estado == 'Disponible':
                print(f'{departamento.tipo}{departamento.piso}: Disponible')
            if departamento.estado == 'Vendido':
                print(f'{departamento.tipo}{departamento.piso}: Vendido')
            

    def mostrar_listado_compradores(depa):
        for comprador in sorted(depa.compradores.keys()):
            print(comprador)

    def mostrar_ventas_totales(depa):
        ventas_totales = {}
        for departamento in depa.departamentos:
            if departamento.estado == 'Vendido':
                precio = depa.precios_venta.get(departamento.tipo, 0)
                if departamento.tipo in ventas_totales:
                    ventas_totales[departamento.tipo]['cantidad'] += 1
                    ventas_totales[departamento.tipo]['total'] += precio
                else:
                    ventas_totales[departamento.tipo] = {'cantidad': 1, 'total': precio}
        
        print('Tipo de departamento, cantidad, total')
        for tipo, datos in ventas_totales.items():
            print(f'{tipo} {depa.precios_venta.get(tipo, 0)} UF, {datos["cantidad"]}, {datos["total"]} UF')
        print(f'Total, {sum([datos["cantidad"] for datos in ventas_totales.values()])}, {sum([datos["total"] for datos in ventas_totales.values()])} UF')

    def realizar_operacion(depa, tipo_operacion, tipo_departamento, piso_departamento, run_comprador):
        departamento_seleccionado = None
        for departamento in depa.departamentos:
            if departamento.tipo == tipo_departamento and departamento.piso == piso_departamento:
                departamento_seleccionado = departamento
                break

        if departamento_seleccionado is None or departamento_seleccionado.estado != 'Disponible':
            print('El departamento seleccionado no está disponible.')
            return

        elif tipo_operacion == 'C':
            departamento_seleccionado.estado = 'Vendido'
            departamento_seleccionado.comprador = run_comprador
            depa.compradores[run_comprador] = tipo_departamento + piso_departamento
            print('La operación de compra se ha realizado correctamente.')
        
        else:
            print('Tipo de operación inválida.')


departamentos_manager = DepartamentosManager()

# Agregar departamentos disponibles
for piso in range(1, 11):
    for tipo in ['A', 'B', 'C', 'D']:
        departamentos_manager.agregar_departamento(tipo, piso)

while True:
    print('--- MENÚ ---')
    print('1. Comprar departamento ')
    print('2. Mostrar departamentos disponibles')
    print('3. Ver listado de compradores')
    print('4. Mostrar ventas totales')
    print('5. Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        print('----- Comprar departamento -----')
        piso_departamento = int(input('Ingrese el número del piso: '))
        tipo_departamento = input('Ingrese el tipo de departamento (A, B, C, D): ')
        tipo_operacion = input('¿Desea comprar el departamento? (C para comprar): ')
        run_comprador = input('Ingrese el RUN del comprador (sin puntos ni guiones): ')
        departamentos_manager.realizar_operacion(tipo_operacion, tipo_departamento, piso_departamento, run_comprador)
    elif opcion == '2':
        print('--- Mostrar departamentos disponibles ---')
        departamentos_manager.mostrar_estado_departamentos()
    elif opcion == '3':
        print('--- Ver listado de compradores ---')
        departamentos_manager.mostrar_listado_compradores()
    elif opcion == '4':
        print('--- Mostrar ventas totales ---')
        departamentos_manager.mostrar_ventas_totales()
    elif opcion == '5':
        print("Gracias por utilizar el sistema ")
        break
    else:
        print('Opción inválida. Por favor, seleccione una opción válida.')

    print()  

import datetime
fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
nombre = input("Soledad Ojeda: ")
mensaje_salida = f"{nombre}. La fecha actual es {fecha_actual} y la hora actual es {hora_actual}."
print(mensaje_salida)