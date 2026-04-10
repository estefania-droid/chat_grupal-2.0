# Chat Grupal - Paso de Mensajes

## Integrantes

* Estefania Guadalupe Alvarez Guevara - Servidor
* Enrique Silva Sanchez - Cliente

---

## Descripción

Este proyecto es una aplicación de chat en consola que permite la comunicación entre múltiples clientes conectados a un servidor.

El servidor permanece activo esperando conexiones y distribuye los mensajes a todos los clientes conectados.

---

## Tecnologías utilizadas

* Python
* Sockets
* Git

---

## Cómo ejecutar el programa

### 1. Ejecutar el servidor

Abrir una terminal y ejecutar:

python server.py

---

### 2. Ejecutar los clientes

Abrir una o más terminales y ejecutar:

python cliente.py

Después ingresar el nombre de usuario.

---

## Conexión entre computadoras

Para conectarse desde otra computadora:

1. Obtener la IP del servidor (192.168.1.209)
2. Cambiar en cliente.py:

HOST = '192.168.1.209'

3. Ejecutar el cliente normalmente

---

## Funcionalidades

* Permite múltiples clientes conectados al mismo tiempo
* Envío de mensajes en tiempo real
* Recepción de mensajes de todos los usuarios
* Notificación cuando un usuario entra o sale

---

## Ejemplo de uso

Juan se unió al chat
Ana se unió al chat

Juan: Hola
Ana: Qué tal

---

## Estructura del proyecto

chat_grupal/
│
├── server.py
├── cliente.py
├── README.md

---

## Control de versiones

El proyecto fue desarrollado utilizando Git, donde cada integrante trabajó en su propia rama y posteriormente se integraron los cambios.

---

## Notas importantes

* El servidor debe ejecutarse antes que los clientes
* Todos los dispositivos deben estar en la misma red
* El puerto utilizado es 5000
