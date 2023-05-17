from flask import Flask, render_template, request ,jsonify
from flask_cors import CORS
app = Flask(__name__, template_folder='templates')
CORS(app)

conversacion = []  # Lista para almacenar los mensajes de la conversación

nombre_usuario = '' 

@app.route('/')
def chatbot():
    return render_template('index.html')

@app.route('/guardar-nombre', methods=['POST'])
def guardar_nombre():
    global nombre_usuario
    data = request.get_json()
    nombre = data.get('name', '')
    nombre_usuario = nombre
    print(f"Nombre recibido: {nombre}")
    return "OK"

@app.route('/respuesta', methods=['GET', 'POST'])

def respuesta():
    if request.method == 'GET':
        return render_template('chatbot.html', conversacion=conversacion)
    
    if request.method == 'POST':
        mensaje_usuario = request.form['mensaje'].lower()
       
    
          # Lógica del chatbot para procesar el mensaje del usuario y generar una respuesta

    if mensaje_usuario == "hola" or mensaje_usuario == "ola" or mensaje_usuario == "holas":
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "hola como estas"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "bien y vos?" or mensaje_usuario == "bien" or mensaje_usuario == "muy bien":
         
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "me alegro, yo genial por charlar contigo"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "que haces?" or mensaje_usuario == "que haces" or mensaje_usuario == "que cuentas?" or mensaje_usuario == "contame algo":
        
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "no tengo mucho que hacer, cual es tu color favorito azul rojo o verde?"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "rojo" or  mensaje_usuario == "el rojo" or  mensaje_usuario == "es el rojo" or  mensaje_usuario == "el color rojo":
         
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "El color rojo, el color de la pasion, hermoso color"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "verde" or  mensaje_usuario == "el verde" or  mensaje_usuario == "es el verde" or  mensaje_usuario == "el color verde" :
         
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "El color verde, el color de la esperanza, hermoso color relajante"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "azul" :
         
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "El color azul, el color de la victoria, hermoso color del cielo"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "adios" or mensaje_usuario == "chau" or mensaje_usuario == "me voy" or mensaje_usuario == "hasta luego":
        
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "Adios Nos estamos viendo, Vuelve cuando quieras!"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    elif mensaje_usuario == "":
          
        
        mensaje_respuesta = "Vamos escribe algo, no seas timido"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    
    else :
        conversacion.append((nombre_usuario, mensaje_usuario))  # Agregar mensaje del usuario a la conversación
        mensaje_respuesta = "Lo lamento no comprendo, recuerda que soy un prototipo de prueba muy limitado"
        conversacion.append(('Chatbot', mensaje_respuesta))# Agregar respuesta del chatbot a la conversación
    return render_template('chatbot.html', conversacion=conversacion)
    """return jsonify({'response': mensaje_respuesta}) #PARA HACER POST CON JSON DESDE POSTMAN /THUNDERCLIENT
 """
if __name__ == '__main__':
    app.run(threaded=True)  #(threaded=True) para multiples peticiones

