import os
import os.path
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('\x1b[1;31;40m' + """                 
                         (                                      
    (          )  (         )\ )  (           (   (     (          
    )\   (    /(( )\  (    (()/( ))\    (  (  )(  )(   ))\ (  (    
    ((_)  )\ )(_))((_) )\    ((_))((_)   )\ )\(()\(()\ /((_))\ )\   
    | __|_(_/(_)((_|_)((_)   _| (_))    ((_|(_)((_)((_|_)) ((_|(_)  
    | _|| ' \)) V /| / _ \ / _` / -_)  / _/ _ \ '_| '_/ -_) _ (_-<  
    |___|_||_| \_/ |_\___/ \__,_\___|  \__\___/_| |_| \___\___/__/  @David Herrera
\x1b[0m""")

if os.path.isfile('password.txt'):
    archivo = open('password.txt', 'r')

    if archivo != "":
        print("\x1b[0;36;40m Cuenta iniciada: " + archivo.readline() +
              '\x1b[0m')
    archivo.close()

print("""Menu:
1) Crear cuenta nueva
2) Usar cuenta existente
""")

opcion = int(input(""))
if opcion == 1:

    me = input('\x1b[1;31;40m' + "Introduce tu correo: \x1b[0m")
    contra = getpass.getpass("\x1b[1;31;40mIntroduce tu contraseña: \x1b[0m")
    archivo = open('password.txt', 'w')
    archivo.write(me + '\n' + contra)
    archivo.close
    print('\x1b[1;32;40m' + "cuenta registrada con exito \x1b[0m")
    # datos de ambos
archivo = open('password.txt', 'r')
me = archivo.readline()
contra = archivo.readline()

destino = input('\x1b[1;31;40m' + "A quien quieres enviar el mensaje? \x1b[0m")
encabezado = input('\x1b[1;31;40m' + "introduce el asunto: \x1b[0m")
texto = input('\x1b[1;31;40m' + "introduce el texto del mensaje: \x1b[0m")

msg = MIMEMultipart()
msg['From'] = me
msg['To'] = destino
msg['Subject'] = encabezado

msg.attach(MIMEText(texto, 'plain'))

if (me[len(me) - 10] == 'g'):
    server = smtplib.SMTP('smtp.gmail.com', 25)
elif (me[len(me) - 7] == 'v'):
    server = smtplib.SMTP('smtp.live.com', 25)
elif (me[len(me) - 11] == 'h'):
    server = smtplib.SMTP('smtp.hotmail.com', 25)

print('\x1b[0;33;40m' + "El mensaje va ha ser enviado a: \x1b[0m" +
      "\x1b[1;36;40m" + destino + '\x1b[0m')
print('\x1b[0;33;40m' + 'El contenido del mensaje es el siguiente: \x1b[0m')
print('')
print("\x1b[1;36;40m" + "   " + texto + '\x1b[0m')
print("")
decision = input("Quieres enviarlo? ")
if (decision == 'si'):
    server.starttls()
    server.login(me, contra)
    text = msg.as_string()
    server.sendmail(me, destino, msg.as_string())
    server.quit()
    print('\x1b[1;32;40m' + 'Envio realizado correctamente \x1b[0m')
else:
    print('\x1b[1;31;40m' + 'Envio cancelado \x1b[0m')
archivo.close()
input("presiona enter para salir")