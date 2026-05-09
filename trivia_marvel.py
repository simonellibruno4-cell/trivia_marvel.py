import streamlit as st
import time
import base64

# Configuración de estilo original
st.set_page_config(page_title="Quiz de Marvel", page_icon="🛡️")

# --- FUNCIÓN PARA AUDIO AUTOMÁTICO ---
def autoplay_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true" loop="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ No se pudo cargar 'vengadores.mp3'. Verificá que esté en la raíz.")

autoplay_audio("vengadores.mp3")

st.title("🛡️ Quiz de Marvel")
st.write("---")

# --- LÓGICA DE NAVEGACIÓN (Session State) ---
if "indice" not in st.session_state:
    st.session_state.indice = 1
if "score" not in st.session_state:
    st.session_state.score = 0

def siguiente_pregunta():
    time.sleep(3) # El tiempo de 3 segundos original
    st.session_state.indice += 1
    st.rerun()

# --- PREGUNTAS (Contenido Original) ---

# Pregunta 1
if st.session_state.indice == 1:
    st.info("Pregunta 1: ¿Cuál es el nombre del superhéroe conocido como 'El Hombre Araña'?")
    st.write("a) Tony Stark | b) Peter Parker | c) Steve Rogers")
    respuesta1 = st.text_input("Tu respuesta 1:", key="r1").lower()
    if st.button("Enviar", key="b1"):
        if respuesta1 == "b":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es b) Peter Parker.")
        siguiente_pregunta()

# Pregunta 2
elif st.session_state.indice == 2:
    st.info("Pregunta 2: ¿Cuál es el nombre del villano principal en la película 'Avengers: Infinity War'?")
    st.write("a) Thanos | b) Loki | c) Ultron")
    respuesta2 = st.text_input("Tu respuesta 2:", key="r2").lower()
    if st.button("Enviar", key="b2"):
        if respuesta2 == "a":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es a) Thanos.")
        siguiente_pregunta()

# Pregunta 3
elif st.session_state.indice == 3:
    st.info("Pregunta 3: ¿Quien mato a vision?")
    st.write("a) Wanda Maximoff | b) Thanos | c) Loki")
    respuesta3 = st.text_input("Tu respuesta 3:", key="r3").lower()
    if st.button("Enviar", key="b3"):
        if respuesta3 == "a":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es a) Wanda Maximoff.")
        siguiente_pregunta()

# Pregunta 4
elif st.session_state.indice == 4:
    st.info("Pregunta 4: ¿Cuál es el nombre del actor que interpreta a Iron Man?")
    st.write("a) Robert Downey Jr. | b) Robert dawney Jr. | c) Robert Downei jr.")
    respuesta4 = st.text_input("Tu respuesta 4:", key="r4").lower()
    if st.button("Enviar", key="b4"):
        if respuesta4 == "a":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es a) Robert Downey Jr.")
        siguiente_pregunta()

# Pregunta 5
elif st.session_state.indice == 5:
    st.info("Pregunta 5: ¿En el universo paralelo de what if, en que se convierte tony stark?")
    st.write("a) Doctor Strange | b) Iron Man | c) Star Lord | d) Se muere | e) Doctor Doom")
    respuesta5 = st.text_input("Tu respuesta 5:", key="r5").lower()
    if st.button("Enviar", key="b5"):
        if respuesta5 == "d":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es d) Se muere.")
        siguiente_pregunta()

# Pregunta 6
elif st.session_state.indice == 6:
    st.info("Pregunta 6: ¿En la pelicula de antman y la avispa quantumania, a donde viaja el protagonista?")
    st.write("a) Wakanda | b) El reino cuántico | c) Asgard | d) El espacio | e) El inframundo | f) Kang el conquistador")
    respuesta6 = st.text_input("Tu respuesta 6:", key="r6").lower()
    if st.button("Enviar", key="b6"):
        if respuesta6 == "b":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es b) El reino cuántico.")
        siguiente_pregunta()

# Pregunta 7
elif st.session_state.indice == 7:
    st.info("pregunta 7: ¿En la pelicula de capitan america: el primer vengador, en que se convierte el protagonista?")
    st.write("a) Un super soldado | b) El primer soldado | c) Un mega soldado | d) Un soldado mejorado | e) Un soldado mutante | f) Un super soldado de hydra")
    respuesta7 = st.text_input("Tu respuesta 7:", key="r7").lower()
    if st.button("Enviar", key="b7"):
        if respuesta7 == "a":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es a) Un super soldado.")
        siguiente_pregunta()

# Pregunta 8
elif st.session_state.indice == 8:
    st.info("Pregunta 8: ¿En la pelicula de doctor strange, que es el ojo de agamotto?")
    st.write("a) Un amuleto | b) Un anillo | c) Un reloj | d) Un collar | e) Un brazalete")
    respuesta8 = st.text_input("Tu respuesta 8:", key="r8").lower()
    if st.button("Enviar", key="b8"):
        if respuesta8 == "a":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es a) Un amuleto.")
        siguiente_pregunta()

# Pregunta 9
elif st.session_state.indice == 9:
    st.info("Pregunta 9: ¿En la pelicula de black panther, cual es el nombre del metal que se encuentra en wakanda?")
    st.write("a) Vibranium | b) Adamantium | c) Uru | d) Unobtanium | e) Mithril")
    respuesta9 = st.text_input("Tu respuesta 9:", key="r9").lower()
    if st.button("Enviar", key="b9"):
        if respuesta9 == "a":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es a) Vibranium.")
        siguiente_pregunta()

# Pregunta 10
elif st.session_state.indice == 10:
    st.info("pregunta 10: ¿En la mini serie de moon knight, cual es el nombre del dios egipcio que le da sus poderes al protagonista?")
    st.write("a) Anubis | b) Osiris | c) Khonshu | d) Ra | e) Horus")
    respuesta10 = st.text_input("Tu respuesta 10:", key="r10").lower()
    if st.button("Enviar", key="b10"):
        if respuesta10 == "c":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es c) Khonshu.")
        siguiente_pregunta()

# Pregunta 11
elif st.session_state.indice == 11:
    st.info("Pregunta 11: ¿En la mini serie de moon knight, cuantas personalidades tiene el protagonista?")
    st.write("a) 2 | b) 3 | c) 4 | d) 5 | e) 6")
    respuesta11 = st.text_input("Tu respuesta 11:", key="r11").lower()
    if st.button("Enviar", key="b11"):
        if respuesta11 == "b":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es b) 3.")
        siguiente_pregunta()

# Pregunta 12
elif st.session_state.indice == 12:
    st.info("Pregunta 12: ¿En la miniserie de loki, cual es el nombre quien lo ayuda para que deje de trabarse en el tiempo?")
    st.write("a) Mobius M. Mobius | b) Sylvie | c) Ravonna Renslayer | d) Hunter B-15 | e) Miss Minutes | f) Ouroboros OB")
    respuesta12 = st.text_input("Tu respuesta 12:", key="r12").lower()
    if st.button("Enviar", key="b12"):
        if respuesta12 == "f":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es f) Ouroboros OB.")
        siguiente_pregunta()

# Pregunta 13
elif st.session_state.indice == 13:
    st.info("Pregunta 13: ¿En la pelicula de los eternos, cual es el nombre del personaje interpretado por Angelina Jolie?")
    st.write("a) Sersi | b) Thena | c) Ajak | d) Makkari | e) Sprite")
    respuesta13 = st.text_input("Tu respuesta 13:", key="r13").lower()
    if st.button("Enviar", key="b13"):
        if respuesta13 == "b":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es b) Thena.")
        siguiente_pregunta()

# Pregunta 14
elif st.session_state.indice == 14:
    st.info("Pregunta 14: ¿En la pelicula de los 4 fantasticos primeros pasos, quien aparece al final de la pelicula?")
    st.write("a) Galactus | b) Silver Surfer | c) Doom | d) El vigilante | e) Kang el conquistador")
    respuesta14 = st.text_input("Tu respuesta 14:", key="r14").lower()
    if st.button("Enviar", key="b14"):
        if respuesta14 == "c":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es c) Doom.")
        siguiente_pregunta()

# Pregunta 15
elif st.session_state.indice == 15:
    st.info("Pregunta 15: ¿En la pelicula de endgame, quien es el unico personaje que se queda en el pasado?")
    st.write("a) Tony Stark | b) Steve Rogers | c) Natasha Romanoff | d) Clint Barton | e) Bruce Banner")
    respuesta15 = st.text_input("Tu respuesta 15:", key="r15").lower()
    if st.button("Enviar", key="b15"):
        if respuesta15 == "b":
            st.success("¡Correcto!")
            st.session_state.score += 1
        else:
            st.error("Incorrecto. La respuesta correcta es b) Steve Rogers.")
        siguiente_pregunta()

# PUNTUACIÓN FINAL
elif st.session_state.indice > 15:
    st.balloons()
    st.success(f"Tu puntuación final es: {st.session_state.score} de 15.")
    st.write("¡Gracias por jugar al Quiz de Marvel, Bruno!")
    if st.button("Reiniciar Quiz"):
        st.session_state.indice = 1
        st.session_state.score = 0
        st.rerun()