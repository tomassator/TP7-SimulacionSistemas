
#Estados Zapatero

libre = "L"
atendiendo_pedido = "AP"
atendiendo_retiro = "AR"
reparando = "R"

#Estados cliente

siendo_at_pedido = "SAP"
siendo_at_retiro = "SAR"
esperando_retiro = "EAR" #Se cambio EPR POR EAR
esperando_pedido = "EAP" #SE CAMBIO EPP POR EAP    EA-> Esperando atencion
abandono_sin_zapato = "ASZ"
abandono_cierre_local = "ACL"


#Estados Zapatos

siendo_reparados = "SR"
reparados = "RT"  #Reparacion terminada
esperando_reanudacion_reparacion = "ERR"
esperando_reparo = "ER"



#Estado cuando se van del sistema

fuera_sistema = "-"


#Acciones del cliente

retirar = "Retirar"
pedido = "Pedido"


#Nombre eventos

eventoInicializacion = "#######inicializacion#######"
eventoLlegadaClientes = "llegada_cliente"
eventoFinAtencionCliente = "fin_atencion_cliente"
eventoFinReparacion = "fin_reparacion"
eventoLlegadaInterrupcion = "#CIERRE#_zapateria"
eventoFinInterrupcion = "#APERTURA#_zapateria"


#RungeKutta

rk4_secado = None    #Esta varibale se asigna al iniciar la simulacion