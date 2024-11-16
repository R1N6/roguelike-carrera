#Definicion de personajes 
define chico = Character("[nombre]", color="#0FD2A9")
define chica = Character("[nombre]", color="#9951C2")
define amiga = Character("Luna", color="#5c0668")
define amigo = Character("Sebastián",color="#02C743")
define maestro = Character("Carlos",color="#aa1d1d")
define maestra = Character("Vanesa",color="#d845b8")
define desconocido = Character("???",color="#88828a")
define misterioso = Character("?",color="#161616")
define explicacion = Character("Explicacion",color="#e66700")
# barras de estres
default estres = 0  # Nivel inicial de estrés

#Resultados de minijuegos
default minijuegos_ganados = 0
default minijuegos_perdidos = 0
# Definición de sprites
image Estado_chico_normal = "Estado_chico_normal.png"
image Estado_chico_cansado = "Estado_chico_cansado.png"
image Estado_chico_estresado = "Estado_chico_estresado.png"

image Estado_chica_normal = "Estado_chica_normal.png"
image Estado_chica_cansada = "Estado_chica_cansada.png"
image Estado_chica_estresada = "Estado_chica_estresada.png"

# Variables de estado
default cansancio = False  # Estado de desvelo
default estado_estresado = False  # Estado activado cuando el estrés > 50
default ruta_normal = False

#Definir videos a imagen para pantalla de game over
image gameoverchico = Movie(play="Gameoverchico.webm", size=(1920, 1080))
image gameoverchica = Movie(play="Gameoverchica.webm", size=(1920, 1080))
image gameoverchico_img = "gameoverchico.png"
image gameoverchica_img = "gameoverchica.png"
# Función para actualizar el estado estresado cada vez que cambie el estrés
init python:
    def actualizar_estado_sprite():
        global estado_estresado, cansancio
        if estres >= 50:
            estado_estresado = True
            cansancio = False
            ruta_normal = False      
        else:  # Menor a 50 es normal
            estado_estresado = False
            cansancio = False
            ruta_normal = True
      


#pantalla de gameover
label game_over():
    window hide
    hide screen barra_estres
    hide screen personaje_sprite

    # Variable para controlar si mostrar el video o la imagen estática
    $ mostrar_imagen = False  

    # Verifica el género para elegir el video adecuado
    if genero == "chico":
        show gameoverchico  # Muestra el video para el chico
        $ renpy.pause(6)  # Duración del video
        hide gameoverchico  # Oculta el video después de la pausa
        show gameoverchico_img  # Muestra la imagen estática para el chico

    elif genero == "chica":
        show gameoverchica  # Muestra el video para la chica
        $ renpy.pause(6)  # Duración del video
        hide gameoverchica  # Oculta el video después de la pausa
        show gameoverchica_img  # Muestra la imagen estática para la chica

    # Reproduce la música después de que el video haya terminado
    play music "gameover.mp3"

    # Muestra la pantalla de Game Over que tiene el mensaje y el botón de regreso al menú
    show screen game_over_screen

    # Detiene el flujo del juego hasta que el jugador elija regresar al menú
    $ renpy.pause()


screen game_over_screen():
    tag menu

    

    # Fondo de la pantalla de Game Over (puedes agregar una imagen o color sólido si deseas)
    #add Solid("#000000")  # Fondo negro para la pantalla de Game Over

    # Mensaje de Game Over principal
    text "¡Has alcanzado el nivel máximo de estrés!" xalign 0.5 ypos 0.4 size 50 color "#ffffff" bold True

    # Mensaje de ánimo personalizado
    text "[nombre], no te rindas. Cada error es una oportunidad para aprender. ¡Vuelve a intentarlo con más fuerza!" xalign 0.5 ypos 0.5 size 30 color "#ffffff"

    # Indicador del progreso en el juego (opcional)
    text "Recuerda: La calma y las buenas decisiones serán tus mejores aliados." xalign 0.5 ypos 0.6 size 25 color "#ffffff"

    # Botón para regresar al menú principal, centrado
    textbutton "Regresar al Menú Principal" action MainMenu() xalign 0.8 ypos 0.8

screen barra_estres:
    frame:
        align (0.02, 0.98)  # Ajusta la posición de la barra (0.02, 0.98) es cerca de la esquina inferior izquierda
        
        # Cambiar la imagen de la barra de estrés según el nivel de estrés
        if estres <= 0:
            add "estres_0.png"  # Imagen para 0% de estrés
        elif estres <= 5:
            add "estres_5.png"  # Imagen para 5% de estrés 
        elif estres <= 10:
            add "estres_10.png"  # Imagen para 10% de estrés    
        elif estres <= 15:
            add "estres_15.png"  # Imagen para 15% de estrés    
        elif estres <= 20:
            add "estres_20.png"  # Imagen para 20% de estrés      
        elif estres <= 25:
            add "estres_25.png"  # Imagen para 25% de estrés 
        elif estres <= 30:
            add "estres_30.png"  # Imagen para 30% de estrés                    
        elif estres <= 35:
            add "estres_35.png"  # Imagen para 35% de estrés 
        elif estres <= 40:
            add "estres_40.png"  # Imagen para 40% de estrés 
        elif estres <= 45:
            add "estres_45.png"  # Imagen para 45% de estrés                          
        elif estres <= 50:
            add "estres_50.png"  # Imagen para 50% de estrés 
        elif estres <= 55:
            add "estres_55.png"  # Imagen para 55% de estrés
        elif estres <= 60:
            add "estres_60.png"  # Imagen para 60% de estrés 
        elif estres <= 65:
            add "estres_65.png"  # Imagen para 65% de estrés
        elif estres <= 70:
            add "estres_70.png"  # Imagen para 70% de estrés 
        elif estres <= 75:
            add "estres_75.png"  # Imagen para 75% de estrés 
        elif estres <= 80:
            add "estres_80.png"  # Imagen para 80% de estrés                
        elif estres <= 85:
            add "estres_85.png"  # Imagen para 85% de estrés 
        elif estres <= 90:
            add "estres_90.png"  # Imagen para 90% de estrés 
        elif estres <= 95:
            add "estres_95.png"  # Imagen para 95% de estrés 
        else:
            add "estres_100.png"  # Imagen para 100% de estrés


screen personaje_sprite:
    if genero == "chico":
        if ruta_normal:
            add "Estado_chico_normal.png" xpos 0.9 ypos 0.75  # Estado normal fijo en rutas D y B
        elif estado_estresado:
            add "Estado_chico_estresado.png" xpos 0.9 ypos 0.75  # Estado estresado
        elif cansancio:
            add "Estado_chico_cansado.png" xpos 0.9 ypos 0.75  # Estado cansado
        else:
            add "Estado_chico_normal.png" xpos 0.9 ypos 0.75  # Estado normal en otras rutas

    elif genero == "chica":
        if ruta_normal:
            add "Estado_chica_normal.png" xpos 0.9 ypos 0.75  # Estado normal fijo en rutas D y B
        elif estado_estresado:
            add "Estado_chica_estresada.png" xpos 0.9 ypos 0.75  # Estado estresado
        elif cansancio:
            add "Estado_chica_cansada.png" xpos 0.9 ypos 0.75  # Estado cansado
        else:
            add "Estado_chica_normal.png" xpos 0.9 ypos 0.75  # Estado normal en otras rutas


#ajustar video            
define config.screen_width = 1920
define config.screen_height = 1080       

#label para cambiar escenas
transform move_in_left:
    xalign -1.0
    yalign 1.0  # Alinea el personaje en la parte inferior de la pantalla
    linear 0.5 xalign 0.0  # Ajusta el tiempo (0.5) según la velocidad deseada

transform move_in_right:
    xalign 2.0
    yalign 1.0  # Alinea el personaje en la parte inferior de la pantalla
    linear 0.5 xalign 1.0  # Ajusta el tiempo (0.5) según la velocidad deseada



label start:
    stop music
    # Pantalla de selección de género
    menu:
        
        "Alumno":
            $ genero = "chico"
            $ personaje = "Protagonista"
            jump elegir_nombre
        "Alumna":
            $ genero = "chica"
            $ personaje = "Protagonista"
            jump elegir_nombre

label elegir_nombre:
    
    # Pantalla para elegir el nombre del personaje
    $ nombre = renpy.input("¿Cuál es tu nombre?") 
    $ nombre = nombre.strip()  # Elimina los espacios adicionales

    if nombre == "":
        $ nombre = "Estudiante"  # Nombre por defecto si no introducen ninguno

    jump introduccion

label introduccion:
    #play music "cancioncuarto.mp3"
    "¡Finalmente! Terminé la preparatoria. Ese examen de admisión para la universidad fue algo difícil. Me pregunto qué me deparará esta nueva etapa..."
    "Al día siguiente."
    "Te levantas temprano, te espera un nuevo comienzo."
   
    scene cuarto with slideleft
    # Mostrar la barra de estrés en la parte inferior izquierda
    show screen barra_estres 

    # Mostrar al personaje correspondiente
    if genero == "chico":
        show screen personaje_sprite 
        show chico at center with dissolve
        chico "*bostezo* Ya es hora de levantarme para ir a mi primer día de universidad."
        chico "¡Espero que todo salga bien!"
    elif genero == "chica":
        show screen personaje_sprite 
        show chica at center with dissolve
        chica "*bostezo* Ya es hora de levantarme para ir a mi primer día de universidad. No se me vaya a hacer tarde."
        chica "Espero que todo salga bien."

    if genero == "chico":
        scene wc with slideleft
        "..."
        scene chico_normal with dissolve
        chico "Espero no tener problemas como en la preparatoria."    
        chico "Me cuesta un poco socializar."
        chico "Vamos, nuevo comienzo, nuevas personas."
        chico "Además, pude entrar a la carrera que quería: Ingeniería en Computación."
        scene cocina with slideleft   
        "Cualquier cosa servirá de desayuno."
        "Hoy mis padres están lejos por temas de trabajo, así que estaré solo estos días."
    elif genero == "chica":
        scene wc with slideleft
        "..."
        scene chica_normal with dissolve
        chica "Espero no tener problemas como en la preparatoria."    
        chica "Me cuesta un poco socializar."
        chica "Vamos, nuevo comienzo, nuevas personas."
        chica "Además, pude entrar a la carrera que quería: Ingeniería en Computación."
        scene cocina with slideleft   
        "Cualquier cosa servirá de desayuno."
        "Hoy mis padres están lejos por temas de trabajo, así que estaré sola estos días."

    #stop music
    scene negro with dissolve
    "¿Debería tomar el autobús o el tren?"
    menu:
        "Tomar Tren":
            $ transporte = "tren"
            jump Tren

        "Tomar Autobús":
            $ transporte = "autobus"
            jump Autobus    

    label Tren:
        image treen = Movie(play="Tren.webm", size=(1920, 1080))
        show treen 
        "El tren es rápido y llega directo a la universidad."  
        jump universidad

    label Autobus:
        image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
        show aautobus 
        "El autobús es más económico y hace varias paradas."
        jump universidad

label universidad:
    #play music "salonclase.mp3"
    scene escuela with slideleft
    "Por fin llegué a la Universidad School Link."
    if transporte == "tren":
        "Parece que fue una buena elección tomar el tren, fue rápido y tranquilo."
    elif transporte == "autobus":
        "El autobús fue algo más lento, pero al menos ahorré algo de dinero."

    "¿Qué clase de compañeros tendré? ¡Seguro que puedo hacer algún amigo!"
    "Hora de encontrar mi salón de clases."
    scene salon with slideleft

if genero == "chico":
        chico "Este es mi salón."    
        chico "Bueno, me sentaré aquí."
        desconocido "Hola, ¿cómo estás?"
        chico "Hola, bien. ¿Y tú?"
        show amiga at move_in_left
        desconocido "Bien también, soy Luna."
        chico "Un gusto, yo soy [nombre]."
        "Espero ser su amigo."
        amiga "El gusto es mío."
        "A lo lejos veo a un chico acercándose."
        desconocido "Qué onda."
        amiga "Hola Sebastián, ¿elegiste la misma carrera?"
        show amigo at move_in_right
        amigo "Sí, eso parece. ¿Y tú, cómo te llamas?"
        chico "[nombre]."
        amigo "Te ves pálido, ¿estás bien?"
        chico "Sí, estoy bien."
        hide amigo with dissolve
        hide amiga with dissolve
        "Debo controlarme, sé que es difícil para mí socializar, pero está saliendo bien."
        play sound "mas.mp3"
        $ estres += 20
        $ renpy.restart_interaction()
        explicacion "De aquí en adelante, las decisiones que tomes afectarán tu barra de estrés."
        explicacion "Recuerda mantenerla baja, si sube al límite, perderás la partida."
        explicacion "Un estrés muy alto puede hacer que aumente la dificultad de los minijuegos."
        explicacion "Así que cuida tu barra de estrés."
        "Veo al maestro entrar al salón de clases, y todos guardan silencio."
        show maestro at center with dissolve
        maestro "Buenos días, alumnos. Soy el profesor Carlos, y yo les impartiré la materia de Redes."
        maestro "Empezaremos viendo la primera sesión."
        hide maestro with dissolve
        chico "Bueno, aquí vamos."
        chico "Espero no tener dificultades."

        #agregar minijuego
        #$ Minijuego = "Gano"
        #if juego == "gana":
            #$ minijuegos_ganados += 1
            #play sound "menos.mp3"
            # $ estres -= 5
            # $ renpy.restart_interaction()
        chico "Eso estuvo fácil."

        #$ Minijuego = "perdio"
        #elif juego == "pierde":
            #$ minijuegos_perdidos += 1
            #play sound "mas.mp3"
            #$ estres += 5
            # $ renpy.restart_interaction()
            #chico "¡Uf! Menos mal que no me fue tan mal."

        chico "Debería practicar para mejorar en la siguiente."
        show amigo at move_in_right
        amigo "Oye [nombre], ¿quieres acompañarnos al billar?"
        show amiga at move_in_left
        amiga "No lo sé… creo que deberíamos repasar un poco para la siguiente clase, [nombre]."
        hide amigo with dissolve
        hide amiga with dissolve

        # Reflexión Interna
        "Me siento un poco indeciso. Por un lado, sé que socializar es importante para hacer amigos en esta nueva etapa, y no quiero perderme la oportunidad de acercarme a Sebastián."
        "Por otro lado, sé que estudiar con Luna podría aliviar algo de la ansiedad que siento por mis clases. Quizás dedicarle tiempo al estudio me ayude a manejar mejor el estrés."
        explicacion "Esta es la primera decisión que puede afectar tu barra de estrés."
        explicacion "Recuerda no llenarla."

        menu:
            "Claro, vámonos al billar":
                jump billar

            "Me quedaré a repasar con Luna":
                jump Estudiar  




        # Decisión Sebastián
        label billar:
            show amigo at center with dissolve
            amigo "Bien dicho, [nombre]. ¡Vamos!"
            hide amigo with dissolve
            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction()
            scene negro with dissolve
            "Vas al billar con Sebastián."
            "Fue divertido, pero una pequeña voz en tu cabeza te dice que mañana pagarás el precio."
            "Regresas a casa algo cansado."
            #stop music
            #play music "cancioncuarto.mp3"
            scene cuartonoche with slideright
            chico "Fue un buen primer día."
            "¿Debería dormirme ya o jugar videojuegos un rato?"
            menu:
                "Dormir.":
                    jump descansado

                "Jugar videojuegos.":
                    jump cansado     

        # Ruta D
        label descansado:
            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction()
            scene cuartonoche with slideright
            chico "Bueno, lo mejor será descansar para mañana y tener energía."
            scene negro with dissolve
            "Te acuestas a dormir temprano, recuperando energía para el siguiente día."
            scene cuarto with slideleft
            "Te despiertas con energía y una mentalidad optimista."
            scene wc with slideleft
            "Te sientes con mucha energía, ansioso de ver qué pasará hoy."   
            scene chico_normal with dissolve
            chico "Descansé bien. Es un buen momento para comenzar con la mentalidad correcta."    
            chico "Hoy quiero enfocarme en enfrentar cualquier desafío que venga."    
            scene cocina with slideleft
            "Desayunas lo primero que encuentras y sales corriendo para tomar el transporte." 
            scene negro with dissolve
            #stop music
            "¿Qué debería tomar ahora?"
            menu:
                "Tomar Tren":
                    jump Tren2

                "Tomar Autobús":
                    jump Autobus2  

        label Tren2:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren, ya que el autobús fue más lento."
            jump RutaD

        label Autobus2:
            if transporte == "tren": 
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento, es el más económico."
            jump RutaD   

        # Ruta D
        label RutaD:   
            #play music "salonclase.mp3" 
            scene escuela with slideleft
            "Aquí vamos de nuevo."
            scene salon with slideleft
            chico "Parece que Luna no está muy convencida."
            show amigo at center with dissolve
            amigo "No te preocupes, hablaremos con ella después para que se una a nosotros."
            chico "Sí, creo que es lo mejor."
            amigo "Bueno, es hora de ver cómo nos va, seguro que nos irá bien."
            chico "Espero que todo salga bien."
            hide amigo with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase, vamos a repasar lo que vimos en la clase anterior."
            hide maestro with dissolve

            # Agregar segundo minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # chico "Me fue muy bien"
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ renpy.restart_interaction()
            chico "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            show amigo at center with dissolve
            amigo "No estuvo mal después de todo."
            chico "Sí, me siento aliviado de que haya terminado bien."
            amigo "Pasemos a la siguiente materia."
            chico "Seguro que en esta nos irá todavía mejor."
            hide amigo with dissolve
            "Nunca había tenido la oportunidad de salir con un amigo."
            "Siempre solía volver solo a casa."
            "Veo que llega la maestra, Sebastián se nota preocupado. ¿Será que le gusta Luna?"
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            "Después le pregunto, ahora, a poner atención."
            hide maestra with dissolve

            # Agregar tercer minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # show amigo at center with dissolve
                # amigo "Muy fácil."
                # chico "Es cierto."
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ renpy.restart_interaction()
            show amigo at center with dissolve
            amigo "Esto no estuvo tan mal."
            chico "Sí, tienes razón."
            chico "Oye, Sebastián, te veo preocupado. ¿Todo bien?"
            amigo "Me preocupa porque Luna siempre ha sido mi amiga y no quisiera que se quedara sola."
            "Tenía razón, sí le gusta."
            chico "Podemos quedarnos esta vez."
            amigo "Sí, aunque hoy habrá un festival, podemos convencerla de que venga con nosotros y ya después practicamos con ella."
            chico "Veré qué puedo hacer."
            hide amigo with dissolve

            # Reflexión Interna
            "Me preocupa que Luna se quede estudiando sola, pero también sé que ella tiene sus propias prioridades. Tal vez quiera venir con nosotros, pero no quiero presionarla."
            "Me pregunto si convencerla será lo mejor o si debo respetar su decisión. En momentos como estos, parece que siempre hay algo que perder o ganar."

            menu:
                "Convencerla de que se una.":
                    jump ConvencerlaD

                "No hacer nada.":
                    jump NadaLD




            # Ruta D
            label ConvencerlaD:
                chico "Luna, Sebastián y yo vamos a ir a un festival. ¿Quieres unirte?"
                show amiga at center with dissolve
                amiga "Yo les recomendaría quedarse a estudiar, pero prefiero repasar. Diviértanse."
                chico "Gracias por la preocupación, te veré mañana."
                amiga "Hasta mañana."
                hide amiga with dissolve
                "Bueno, lo intenté, pero espero mañana estar con ella. No me gusta que esté sola, me recuerda a mí en la preparatoria."
                play sound "mas.mp3"
                $ estres += 10
                $ renpy.restart_interaction()
                #stop music
                # Continuación de Ruta
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "Gracias por acompañarme."
                chico "Está bien relajarse de vez en cuando."
                #play music "Sebastian.mp3"
                amigo "No sé por qué, pero me siento como un tonto ahora mismo."
                chico "¿Qué te preocupa?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio. Aun así, pasábamos tiempo juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que algo anda mal, así que decido preguntarle."
                chico "¿Todo bien, Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Para mí, Luna es mi mejor amiga. En mi casa, mi padre siempre está decepcionado de mí, tanto por mi conducta como por mi rendimiento en la escuela."
                amigo "Nunca conocí a mi madre, pues cuando nací ella tuvo problemas de salud... pero aquí sigo."
                amigo "He sido fuerte gracias a Luna. Me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián. Su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy poco, así que sé cómo se siente."
                "Le doy un fuerte abrazo a Sebastián."
                amigo "Gracias, [nombre]. Lo necesitaba. Sé que la escuela es importante, pero a veces no se tienen fuerzas para continuar."
                chico "Sé lo que se siente no tener fuerzas para seguir, pero debemos continuar adelante."
                hide amigo_triste with dissolve
                #stop music
                show amigo at center with dissolve
                amigo "Mejor regresemos y nos vemos mañana."
                chico "Muy bien."
                hide amigo with dissolve
                scene negro with dissolve
                "Sientes un dolor profundo al saber que no sufres solo."
                "Regresas a casa pensando en todo lo que pasó hoy."
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 
                
                # Siguiente Día
                scene cuartonoche with slideright
                "Intento dormir, pero mi mente no deja de pensar en Luna."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Recuerda que no todas las decisiones serán fáciles, y eso está bien."
                misterioso "A veces, tomar el camino más difícil es lo que nos permite crecer y conocernos mejor."
                misterioso "No huyas de las situaciones que te incomodan, enfréntalas y verás que puedes salir fortalecido."
                misterioso "La universidad no es solo un lugar para estudiar, también es una oportunidad para aprender a conocerte a ti mismo."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confuso, pero sigues pensando en Luna."
                chico "Conocerme a mí mismo..."
                
                if estres >= 50:
                    scene chico_estres with dissolve
                    $ renpy.restart_interaction()
                    $ actualizar_estado_sprite() 
                    chico "Vamos, ánimo. Si Sebastián está bien, yo también puedo estarlo. Resolveré esto con Luna."
                else:
                    scene chico_normal with dissolve
                    chico "Vamos, ánimo. Si Sebastián está bien, yo también puedo estarlo. Resolveré esto con Luna."
                
                scene cocina with slideleft
                "Te preparas un desayuno rápido antes de salir a la universidad."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                
                menu:
                    "Tomar Tren":
                        jump Tren10

                    "Tomar Autobús":
                        jump Autobus10  

            label Tren10:
                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Es el más rápido."  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
                
                jump DiaD

            label Autobus10:
                if transporte == "tren":  
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El tren es rápido, pero aún tengo tiempo para llegar."  
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "Bueno, aunque es más lento es el más económico."
                
                jump DiaD








        label DiaD:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "Vamos anímate debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon with slideleft
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo at center with dissolve
            amigo "Hola [nombre]."
            "Miro como los 2 estamos mejor que ayer, pero decidí contarle mi pasado."
            chico "Sobre lo de ayer yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chico "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chico "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chico "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien esta vez iremos los 2."
            chico "De acuerdo."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra with dissolve

            # agregra cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Muy facil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovechamos el tiempo para ir a hablar con luna."
            chico "Hola Luna."
            show amiga at move_in_left
            amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
            chico "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
            show amigo at move_in_right
            amigo "Como en los viejos tiempos."
            amiga "Claro encantada de ir con ustedes."
            chico "Entonces nos vemos allá."
            hide amigo with dissolve
            hide amiga with dissolve
            "Nos regresamos a nuestros lugares."
            "Se termina el tiempo y continúa la siguiente clase."


            # agregra quinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "Salió bien la verdad."
            show amigo at center with dissolve
            amigo "Sí tienes razón este fin será inolvidable. "   
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro with dissolve
            # agregra sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Sin problemas."
                #amigo "Pues claro."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                # play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo with dissolve

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo at center with dissolve
            amigo "Así es."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            show amiga at center with dissolve
            amiga "Adiós [nombre] nos vemos allá entonces."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Estoy ansioso de que llegue este fin de semana." 

            "Pasa el tiempo llegando el fin de semana."

            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Afrontas bien las consecuencias recuerda no rendirte."
            "Te sientes confuso."
            "Bueno gracias a él todo fue mejor y resolví las cosas."
            "Ahora sólo debo concentrarme en pasarla bien con ellos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chico "Hola Sebastián."
            show amigo at move_in_left
            amigo "Hola [nombre]."
            amigo "¿Estás listo para pasarla bien?"
            chico "Si estoy listo."
            " Luna aparece con un material para estudiar."
            show amiga at move_in_right
            amiga "Hola chicos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga with dissolve
            hide amigo with dissolve
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chico "¿Qué pasa? "
            chico "¿Te sientes bien?"
            show amigo_triste at center with dissolve
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            chico " Deberías decirle lo que sientes por ella."
            amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
            # Reflexión Interna
            "Escuchar a Sebastián me hace recordar mis propias dudas y temores. Entiendo lo que es sentirse inseguro, y quizá, si lo apoyo, le ayude a ganar la confianza que necesita."
            "Si le doy ese empujón para que hable con Luna, podría ser lo mejor para ambos. Pero también me pregunto si debería respetar su ritmo y su espacio."

            hide amigo_triste with dissolve

            menu:
                "Darle apoyo para que se confiese.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalD1

                "Respetar sus sentimientos de preocupación.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalD2





                    
            label finalD1:
                chico "Se cómo te sientes, pero es mejor decirle lo que sientes por ella veo que ella quiere que le digas eso."
                show amigo at center with dissolve
                amigo "¿Estás seguro de esto?"
                chico "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo with dissolve
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at move_in_left
                amigo "Luna…"
                show amiga at move_in_right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga with dissolve
                show amiga_triste at right with dissolve

                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo with dissolve
                hide amiga_triste with dissolve
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at move_in_left
                show amiga at move_in_right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella. "
                hide amigo with dissolve
                hide amiga with dissolve
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                stop music
                hide screen barra_estres 
                hide screen personaje_sprite 
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Ayudar a tus amigos desinteresadamente te da propósito y fortalece tus lazos. No subestimes el poder de una mano amiga."
                misterioso "En la vida universitaria y más allá, no temas ofrecer tu apoyo. A veces, el simple hecho de estar presente hace una gran diferencia."
                misterioso "Nunca dudes en expresar tus emociones a quienes te importan. El camino de la amistad se nutre de la autenticidad y la empatía."
                stop music


                scene negro with dissolve
                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music
                return


            

            label finalD2:
                chico "Si es lo que sientes, te apoyaré en cualquier decisión que tomes, Sebastián."
                chico "Sé lo que se siente no poder expresarte, así que cuentas conmigo en lo que sea."
                show amigo at center with dissolve
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chico "De acuerdo."
                hide amigo with dissolve
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo."
                show amigo at move_in_left
                amigo "Volvimos."
                show amiga at move_in_right
                amiga "¿Todo bien?"
                chico "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chico "Continuemos."
                hide amigo with dissolve
                hide amiga with dissolve
                "Luna parece tranquila al pasar tiempo con Sebastián, pero  puedes notar que le hubiera gustado que él le confesara sus sentimientos."
                "Aun así, respetastes  su decisión de Sebastián."
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."               
                stop music
                hide screen barra_estres 
                hide screen personaje_sprite 
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Respetar los sentimientos de tus amigos también muestra madurez. A veces, darles espacio es el mejor apoyo."
                misterioso "Recuerda, [nombre], la verdadera fortaleza está en saber cuándo apoyar y cuándo dar un paso atrás, confiando en el proceso de los demás."
                misterioso "La universidad puede ser desafiante, pero enfrentarlo acompañado de amigos hace el camino más llevadero. No te rindas, y apóyate en quienes te rodean."
                misterioso "Confía en tus decisiones, y recuerda que la vida es un constante aprendizaje."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return

            

            














            #Ruta D,D
            label NadaLD:
                "Decides no hacer nada, pero Sebastián parece preocupado."
                # Reflexión Interna
                "Un extraño malestar se instala en mí al ver que decidí no invitarla. Algo en mí me dice que pude haber hecho más."
                "¿Por qué no di ese paso? Quizás fue el miedo de interferir o simplemente el temor a equivocarme."
            
                chico "Lo siento, Sebastián."
                show amigo_triste at center with dissolve
                amigo "No te preocupes. Vámonos entonces."
                hide amigo_triste with dissolve
                "¿Qué me sucede? Ver a Luna sola me recuerda a mí, y no puedo hacer nada."
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                #stop music
                # Continuación de Ruta
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "Gracias por acompañarme, aunque deberíamos haberla invitado."
                chico "Está bien relajarse de vez en cuando, y de verdad lo siento... no sé por qué no me animé."
                amigo "Anímate, yo soy quien debió convencerla, no tú."
                #play music "Sebastian.mp3"
                amigo "Me siento como un idiota ahora mismo."
                chico "¿Por qué lo dices?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio. Aun así, pasábamos tiempo juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que algo anda mal, así que decido preguntar."
                chico "¿Todo bien, Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna es mi mejor amiga, pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como por mi desarrollo en la escuela."
                amigo "A mi madre nunca la conocí, pues cuando nací tuvo problemas... pero aquí sigo."
                amigo "He sido fuerte gracias a Luna. Me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián, su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces, así que sé lo que siente Sebastián."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias, [nombre]. Lo necesitaba. Sé que la escuela es importante, pero a veces uno no puede reunir fuerzas para continuar."
                chico "Sé lo que se siente no tener fuerzas para seguir, pero debemos continuar adelante."
                hide amigo_triste with dissolve
                #stop music
                show amigo at center with dissolve
                amigo "Mejor regresemos, y nos vemos mañana."
                chico "Muy bien."
                hide amigo with dissolve
                scene negro with dissolve
                "Sientes un dolor profundo al saber que no sufres solo, pero te sientes peor por no haber invitado a Luna."
                "Regresas a casa pensando en todo lo que pasó hoy."
                play sound "mas.mp3"
                $ estres += 20
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()    
                # Continuar
                scene cuartonoche with slideright
                "Sientes que pudiste haber hecho más por Luna, y te acuestas a dormir."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, el mayor desafío es enfrentar nuestros propios miedos y limitaciones, ¿verdad, [nombre]?"
                misterioso "Recuerda que la vida nos da varias oportunidades. El arrepentimiento no debe ser un peso, sino una motivación para actuar diferente la próxima vez."
                misterioso "Si sientes que pudiste hacer más, considera esta reflexión como una promesa a ti mismo de intentarlo mejor en el futuro."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confuso, pero sigues pensando en Luna."
                chico "¿Enfrentar mis miedos?"
                if estres >= 50:
                    scene chico_estres with dissolve
                    $ actualizar_estado_sprite()
                    chico "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                    "Esa voz me dijo que debo enfrentar mis miedos."
                else:
                    scene chico_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chico "Me siento muy mal de no haber hecho nada por Sebastián y Luna, pero al menos voy bien en mis estudios."
                    "Esa voz me dijo que debo enfrentar mis miedos."

                scene cocina with slideleft 
                "Te preparas un desayuno con mayor esfuerzo para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"

                menu:
                    "Tomar Tren":
                        jump Tren12

                    "Tomar Autobús":
                        jump Autobus12  

            label Tren12:
                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Es el más rápido."  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
                        
                jump DiaDD








        label DiaDD:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "No es hora de pensar en eso debo de dar lo mejor de mí. "
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon with slideleft
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo_preocupado at center with vpunch
            amigo "Hola [nombre] ¿te sientes bien?"
            chico "Si estoy bien."
            hide amigo_preocupado with dissolve
            "Miro como los 2 estamos mejor que ayer, pero decidí contarle mi pasado."
            chico "Sobre lo de ayer yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            show amigo at center with dissolve
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chico "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chico "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chico "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien esta vez iremos los 2 pero yo le diré que te veo un poco desanimado."
            chico "De acuerdo."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra with dissolve

            # agregra cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "fue facil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovechamos el tiempo para ir a hablar con luna."
            chico "Hola Luna."
            show amiga at move_in_left
            amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
            chico "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
            show amigo at move_in_right
            amigo "Como en los viejos tiempos."
            amiga "Claro encantada de ir con ustedes."
            hide amiga with dissolve
            show amiga_preocupada at left with vpunch
            "Luna me observa preocupada "
            amiga "¿Estás bien [nombre]?"
            chico "Si estoy bien no te preocupes Luna."
            amiga "Si tu lo dices."
            chico "Entonces nos vemos allá."
            hide amigo with dissolve
            hide amiga_preocupada with dissolve
            "Nos regresamos a nuestros lugares."
            "Se termina el tiempo y continúa la siguiente clase."


            # agregra quinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "Salió bien la verdad."
            show amigo at center with dissolve
            amigo "Sí tienes razón este fin será inolvidable. "   
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro with dissolve
            # agregra sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Sin problemas."
                #amigo "Pues claro."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo with dissolve

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo at center with dissolve
            amigo "Así es."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            show amiga at center with dissolve
            amiga "Adiós [nombre] nos vemos allá entonces."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Estoy ansioso de que llegue este fin de semana." 
            "Y sobre todo cambiar mi destino."
            "Pasa el tiempo llegando el fin de semana."

            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "No importa que decisión tomes solo se consciente. "
            "Te sientes confuso."
            "¿Ser consciente? Creo que he hecho bien en planear este día."
            "Mejor no pensar en ello y pasarla bien."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chico "Hola Sebastián."
            show amigo at move_in_left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros."    
            amigo "Vamos amigo mucho ánimo ¿vale?"
            chico "Está bien, pero sigo pensando que esto pudo cambiar al decirle desde un principio, pero estoy preocupado de cómo está ella."
            amigo "No te dejaré solo en esto."
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chico "¿Mejor?"
            amigo "Mucho mejor."
            "Luna aparece con un material para estudiar."
            show amiga at move_in_right
            amiga "Hola chicos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga with dissolve
            hide amigo with dissolve
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chico "¿Qué pasa? "
            chico "¿Te sientes bien?"
            show amigo_triste at center with dissolve
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            amigo "Te dije que todo está bien [nombre]."
            chico " Aun así quiero apoyarte Sebastián y ayudarte con Luna."
            amigo "Muchas gracias amigo."
            # Reflexión Interna
            "Sé lo que es tener dudas, especialmente cuando los sentimientos están involucrados. ¿Debo motivarlo a actuar o debería respetar su cautela y dejar que decida su propio camino?"
            "Quizás lo que él necesita es un empujón... o quizás sólo un amigo que entienda su silencio."
            hide amigo_triste with dissolve

            menu:
                "Darle apoyo para que se confiese.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalDD1

                "Respetar sus sentimientos de preocupación.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalDD2





                    
            label finalDD1:
                chico "No pude convencerla en un principio, pero quiero ayudarte a que le confieses tus sentimientos a ella."
                show amigo at center with dissolve
                amigo "No te preocupes más por eso."
                amigo "¿Y estás seguro de esto?"
                chico "Esta vez te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo with dissolve
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at move_in_left
                amigo "Luna…"
                show amiga at move_in_right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga with dissolve
                show amiga_triste at right with dissolve

                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo with dissolve
                hide amiga_triste with dissolve
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at move_in_left
                show amiga at move_in_right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella, y se siente más apoyado. "
                hide amigo with dissolve
                hide amiga with dissolve
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos, aunque tuvimos dificultades."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia."
                stop music
                hide screen barra_estres 
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, ayudar a quienes amamos es motivarlos a enfrentar sus propios temores. Lo has hecho bien."
                misterioso "No temas en expresar lo que piensas y en buscar siempre el bienestar de los demás, incluso cuando implique un riesgo."
                stop music


                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label finalDD2:
                chico "No pude convencerla en un principio, pero tampoco quiero presionarte y respeto tu decisión."
                chico "Te daré el apoyo que necesites con Luna."
                show amigo at center with dissolve
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chico "De acuerdo."
                hide amigo with dissolve
                "Regresamos con Luna."
                "Volvemos con Luna Sebastián parece más calmado sabiendo que cuenta conmigo para lo que sea y me siento mejor al darle mi apoyo que no pude darle antes."
                show amigo at move_in_left
                amigo "Volvimos."
                show amiga at move_in_right
                amiga "¿Todo bien?"
                chico "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chico "Continuemos."
                hide amiga with dissolve
                hide amigo with dissolve
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia y sobre todo respetar decisiones."               
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Respetar las decisiones de otros es también una forma de apoyo. La vida nos enseña que, a veces, acompañar sin presionar es el mejor camino."
                misterioso "Recuerda que no siempre se trata de tomar decisiones por los demás, sino de estar ahí cuando nos necesiten."
                stop music 
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


                







        # Ruta C        
        label cansado:
            $ cansancio = True
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction()
            scene cuartonoche with slideright
            chico "Bueno, una partida no hará daño..."
            "Sé que debería dormir para estar en mi mejor forma mañana... pero necesito una distracción. Solo una partida más."
            scene negro with dissolve
            "Juegas unas cuantas partidas y pierdes la noción del tiempo."
            scene cuarto with slideleft
            "Despiertas con dificultad, sintiendo el peso de tus malas decisiones."
            scene wc with slideleft
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chico_normal with dissolve
            "El cansancio es evidente. Me miro al espejo y no reconozco al reflejo. ¿Valió la pena el desvelo? Quizás esté escapando de algo..."
            chico "Creo que me sobrepasé un poco…"
            "Suspiro."
            chico "Bueno, diría que demasiado... Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina with slideleft
            "Desayunas lo primero que encontraste y vas corriendo para tomar el transporte." 
            scene negro with dissolve
            #stop music
            "¿Ahora qué debería tomar?"
            
            menu:
                "Tomar Tren":
                    jump Tren3

                "Tomar Autobús":
                    jump Autobus3  

        label Tren3:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
                    
            jump RutaC

        label Autobus3:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento, es el más económico."
                    
            jump RutaC   

        # Ruta C
        label RutaC:
            #play music "salonclase.mp3"
            scene escuela with slideleft
            "Aquí vamos de nuevo."
            scene salon with slideleft
            "Luna parece decepcionada, y Sebastián se muestra pensativo."
            amiga "Bueno... supongo que estudiaré sola entonces."
            
            # Reflexión Interna 
            "La decepción en los ojos de Luna es evidente, y aunque Sebastián intenta animarme, siento una carga en mis hombros que no se va."
            "¿Por qué siempre evito enfrentar estos momentos de frente? Quizás temo a lo que pueda descubrir de mí mismo."
            "Quería que fuéramos juntos… pero no puedo estar en dos lugares a la vez."
            "Veo cómo Luna se sienta en su lugar, intentando concentrarse en sus apuntes, pero su mirada se desvía hacia mí."
            "Hay un silencio incómodo que parece durar una eternidad."
            chico "Me siento mal por ella."
            show amigo at center with dissolve
            amigo "No te preocupes por Luna, luego hay que convencerla de que venga con nosotros."
            chico "Sí, tienes razón... aunque algo en su mirada me dice que ya la decepcioné."
            "Sebastián se queda en silencio por un momento."
            amigo "¿Dormiste bien? Te ves cansado."
            chico "No te preocupes, estaré bien... o al menos eso espero."
            hide amigo with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase, vamos a repasar lo que vimos en la clase anterior."
            hide maestro with dissolve
            "Durante la clase, el cansancio comienza a hacer mella en ti."
            "Te cuesta concentrarte, y cada palabra del profesor se siente como un peso más sobre tus hombros."

            # Agregar Minijuego 2
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ renpy.restart_interaction()
                #chico "Me fue muy bien."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 10
                #$ renpy.restart_interaction()
            
            chico "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            amigo "¿Seguro que estás bien?"
            chico "Sí, estoy bien... sólo tuve dificultades, pero la próxima vez lo haré mejor, lo prometo."
            amigo "Si tú lo dices... solo recuerda que tenemos otra clase, dormilón."
            chico "Lo sé, Sebastián... pero tú también estabas en las mismas."
            "A pesar de sus palabras de ánimo, sabes que algo en ti está cambiando."
            "Te preguntas si realmente vale la pena seguir así."
            "Veo entrar a la maestra para dar inicio a la siguiente clase."
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            chico "Bueno, a empezar con la siguiente materia."
            "Aunque sigo con sueño."
            hide maestra with dissolve

            # Minijuego 3 agregar 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #amigo "Muy fácil."
                #chico "Es cierto."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 10
                #$ renpy.restart_interaction()

            show amigo at center with dissolve
            amigo "Bueno, esta estuvo fácil, ¿a que sí, dormilón?"
            chico "Sí, y deja de decirme dormilón."
            amigo "Tranquilo, está bien."
            "Sebastián y tú están en clase, pero tu mente está en otro lugar."
            "Cada palabra que Sebastián menciona sobre Luna hace que te sientas más culpable."
            amigo "Siempre he sido cercano a Luna, pero últimamente no hemos pasado tiempo juntos como antes."
            chico "Podemos quedarnos esta vez, intentar recuperar el tiempo."
            amigo "Sí, aunque hoy hay un festival... Tal vez podamos convencerla de que venga con nosotros."
            chico "Haré lo que pueda..."
            
            # Reflexión Interna 
            "Sé que tengo la oportunidad de invitarla, y tal vez sea lo correcto... Pero, ¿y si prefiero quedarme en mi zona de confort?"
            "¿Estoy evitando el esfuerzo emocional por miedo, o realmente no deseo involucrarme?"
            hide amigo with dissolve
            $ estres = 30 # Ajustar después de revisar minijuegos 
            $ renpy.restart_interaction()
            
            menu:
                "Convencerla de que se una.":
                    jump ConvencerlaC

                "No hacer nada.":
                    jump NadaLC
            
            
            
            #Ruta C
            label ConvencerlaC:
                "Estás muy cansado y estresado, pero aun así intentas convencer a Luna."
                chico "¿Luna, Sebastián y yo vamos a ir a un festival, quieres unirte?"
                show amiga at center with dissolve
                amiga "Deberías mejor descansar por hoy, pero diviértanse. Yo prefiero quedarme a repasar."
                chico "Gracias por la preocupación, te veré mañana."
                amiga "Hasta mañana."
                hide amiga with dissolve
                #Reflexión Interna
                "Sus palabras me afectan más de lo que esperaba. Verla tan concentrada en el estudio, tan ajena a nosotros... Me recuerda a mis propios días en la preparatoria."
                "¿Estaré buscando su aprobación o solo tratando de evitar enfrentarme a mí mismo?"
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()    
                #stop music
                #Continuar Historia
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "En serio, te ves muy cansado, pero gracias por acompañarme."
                chico "Estaré bien, no te preocupes."
                #play music "Sebastian.mp3"
                amigo "Me siento como un idiota ahora mismo."
                chico "¿Por qué lo dices?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que algo anda mal, así que decido preguntarle."
                chico "¿Todo bien, Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna para mí es mi mejor amiga, pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "A mi madre nunca la conocí, pues cuando nací tuvo problemas... pero aquí sigo."
                amigo "He sido fuerte gracias a Luna. Me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Intento consolar a Sebastián pues su vida es muy dura."
                #Reflexión Interna
                "Escuchar su historia me recuerda la soledad que yo mismo siento en casa, con padres que apenas veo. A veces, el vacío es más profundo cuando parece que todo está bien."
                "Le doy un abrazo fuerte a Sebastián."
                amigo "Gracias, [nombre]. Lo necesitaba. Sé que la escuela es importante, pero a veces uno no puede agarrar fuerzas para continuar."
                chico "Sé lo que se siente, no poder agarrar fuerzas para seguir, pero debemos continuar adelante."
                hide amigo_triste with dissolve
                #stop music
                show amigo at center with dissolve
                amigo "Mejor regresemos y nos vemos mañana."
                chico "Muy bien."
                hide amigo with dissolve
                scene negro with dissolve
                "Sientes un dolor profundo y no tienes ánimos de continuar, pero la vida sigue adelante."
                "Regresas a casa pensando en todo lo que pasó hoy."
                play sound "mas.mp3"
                $ estres += 20
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()
            
                scene cuartonoche with slideright
                #Reflexión Interna
                "Hoy me he dado cuenta de que el cansancio físico no es lo único que me afecta. El peso de mis decisiones se siente cada vez más, y no sé si estoy listo para enfrentarlo."
                "Te sientes muy cansado y te acuestas a dormir, pero no puedes dejar de pensar en Luna."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Cada paso que das tiene un impacto, [nombre]. Recuerda que no puedes cambiarlo todo en un solo día."
                misterioso "El cansancio y la frustración pueden ser tus maestros. Aprende a escuchar lo que te dicen, en lugar de evitarlos."
                misterioso "La próxima vez que tengas una decisión en tus manos, pregúntate: ¿Es esto realmente lo que quiero, o estoy evitando enfrentarme a algo más profundo?"
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confuso, pero sigues pensando en Luna."
                chico "¿Evitar algo más profundo? ¿Lo que realmente quiero?"
                if estres >= 50:
                    scene chico_estres with dissolve
                    $ actualizar_estado_sprite()
                    chico "Me llevo bien con Sebastián, ¿pero por qué me siento asi?"
                    chico "Pensar tanto en la Luna y la situación de Sebastián hace que no pueda concentrarme."
                    chico "Vamos tú puedes con esto."
                else:
                    scene chico_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chico "Me llevo bien con Sebastián, ¿pero por qué me siento asi?"
                    chico "Pensar tanto en la Luna y la situación de Sebastián hace que no pueda concentrarme."
                    chico "Vamos tú puedes con esto."

                
                scene cocina with slideleft
                "Muy apenas te preparas algo para comer."
                #stop music
                scene negro with dissolve
                "¿No sé qué transporte tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren14

                    "Tomar Autobus":
                        jump Autobus14  
        label Tren14:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Llegare temprano aunque no se que hacer..."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "así tengo mas tiempo de pensar que hare... "
             
            jump DiaC
        
        label Autobus14:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero quiero primero estar bien antes de verlos..."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Así tengo tiempo de pensar muy bien todo..."
             
            jump DiaC








        label DiaC:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "Vamos anímate debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon with slideleft
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo_preocupado at center with vpunch
            amigo "¡¡wow!! ¿estas bien [nombre]?"
            amigo "Te veo un poco mal."
            chico "Estoy bien no te preocupes."
            amigo "Oye deberías sacarlo todo yo lo hice ayer y me sentí mejor así que puedes decirme que pasa."
            chico "Yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado with dissolve
            show amigo at center with dissolve
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chico "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chico "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chico "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo un poco mal para que no se preocupe."
            chico "Tienes razón gracias."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra with dissolve

            # agregra cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con luna mientras los observo."
            "Espero que todo esté bien entre ellos."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno jóvenes comencemos la siguiente clase."
            hide maestra
            "Sebastián Regresa a su asiento, después le preguntare como le fue."


            # agregra quinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "¿Cómo te fue con ella?"
            show amigo at center with dissolve
            amigo "Aceptó así que nos veremos con ella este fin."
            chico "Me alegra oír eso."   
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro with dissolve
            # agregra sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Sin problemas."
                #amigo "Pues claro."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo with dissolve

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo at center with dissolve
            amigo "Así es y recuerda tranquilo vale."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            show amiga at center with dissolve
            amiga "Adiós [nombre] te veré allá entonces con Sebastián."
            chico "Te veo ahí."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Me retiro a mi casa a descansar esperando el fin de semana." 

            "Pasa el tiempo llegando el fin de semana."

            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Afrontar bien las consecuencias sigue así."
            "Te sientes confuso."
            "Aun no entiendo el propósito de esa sombra."
            "No importa, hoy la pasaré bien con mis amigos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chico "Hola Sebastián."
            show amigo at move_in_left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros"
            amigo "Vamos amigo mucho ánimo ¿vale?"
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chico "¿Mejor?"
            amigo "Mucho mejor."
            " Luna aparece con un material para estudiar."
            show amiga at move_in_right
            amiga "Hola chicos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga with dissolve
            hide amigo with dissolve
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chico "¿Qué pasa? "
            chico "¿Te sientes bien?"
            show amigo_triste at center with dissolve
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            chico " Deberías decirle lo que sientes por ella."
            amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
            "La soledad no es una buena opción." 
            #Reflexión Interna
            "Sé que sería lo correcto animarlo a sincerarse con Luna, pero ¿realmente es lo que necesita ahora? A veces, la prudencia es más importante que la acción inmediata."

            hide amigo_triste with dissolve

            menu:
                "Darle apoyo para que se confiese.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalC1

                "Respetar sus sentimientos de preocupación.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalC2





                    
            label finalC1:
                chico "Mira, la soledad no es buena y no es excusa puedes pasar más tiempo con ella estudiando juntos conociéndote más."
                chico "Es difícil Estudiar cuando uno está estresado y Solo, así que siempre es bueno tener a alguien en quien apoyarse."
                show amigo at center with dissolve
                amigo "¿Estás seguro de esto?"
                chico "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo with dissolve
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at move_in_left
                amigo "Luna…"
                show amiga at move_in_right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga with dissolve
                show amiga_triste at right with dissolve

                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo with dissolve
                hide amiga_triste with dissolve
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at move_in_left
                show amiga at move_in_right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Ayudar a otros a expresar sus sentimientos requiere de gran sensibilidad."
                misterioso "No olvides, [nombre], que las relaciones se fortalecen cuando actuamos con sinceridad y cuidado."
                misterioso "Recuerda, cada palabra y cada gesto tienen peso. Las conexiones pueden ser una fortaleza o un desafío, dependiendo de cómo las manejemos."
                stop music

                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label finalC2:
                chico "Si sientes eso en verdad te apoyo sea cual sea la decisión que tomes Sebastián."
                show amigo at center with dissolve
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chico "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo para lo que sea."
                show amigo at move_in_left
                amigo "Volvimos."
                show amiga at move_in_right
                amiga "¿Todo bien?"
                chico "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chico "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has mostrado respeto y comprensión, permitiendo que los sentimientos evolucionen con el tiempo."
                misterioso "A veces, ser paciente y escuchar es la mayor ayuda que puedes ofrecer."
                misterioso "No permitas que el miedo o las dudas te frenen, pero respeta el ritmo de las personas. Cada silencio tiene su valor, y cada palabra su lugar."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return






            #Ruta Egoista
            label NadaLC:
                "Decides no hacer nada, el cansancio y la falta de energía te paralizan."
                chico "Lo siento, Sebastián... simplemente no puedo."
                show amigo_triste at center with dissolve
                amigo "No te preocupes, vámonos entonces."
                hide amigo_triste
                #Reflexión Interna
                "Ver a Luna sola… Me hace ver mi propio reflejo. Tal vez esté proyectando mis propios miedos y fracasos en ella, pero ahora mismo no tengo la fuerza para actuar."
                "Algo en tu interior grita que actúes, pero el peso de tus malas decisiones te hunde más."
                play sound "mas.mp3"
                $ estres += 25
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()   
                #stop music
                #Continuar Historia
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "Te ves muy cansado... pero gracias por acompañarme."
                amigo "Aunque, la verdad, deberíamos haberla invitado."
                chico "Estaré bien... lo siento, Sebastián, de verdad lo siento."
                amigo "No te castigues tanto, debí ser yo quien la convenciera, no tú."
                "Mientras caminan por el festival, notas que Sebastián está más callado que de costumbre. Decides preguntarle qué le sucede."
                chico "¿Qué pasa, Sebastián?"
                #play music "Sebastian.mp3"
                "Sebastián se detiene y te mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna es mi mejor amiga."
                amigo "Siempre ha estado ahí para mí, incluso cuando mi padre estaba decepcionado conmigo o cuando no tenía a nadie más."
                amigo "Ella me daba fuerzas... y ahora siento que la estoy perdiendo."
                #Reflexión Interna
                "La historia de Sebastián me golpea. Me doy cuenta de que mis malas decisiones no solo me han afectado a mí. No estoy solo en esto, pero ¿por qué sigo sintiéndome tan atrapado?"
                hide amigo_triste with dissolve
                show amigo_preocupado at center with vpunch
                chico "Sebastián... no estás solo. Lo que sea que necesites, estoy aquí."
                "Lo abrazas con fuerza, sintiendo la presión de las expectativas y la culpa arremolinándose dentro de ti."
                hide amigo_preocupado with dissolve
                show amigo_triste at center with dissolve
                amigo "Gracias, [nombre]. A veces es difícil continuar, pero al menos sé que te tengo a ti."
                hide amigo_triste with dissolve
                #stop music
                scene negro with dissolve
                #Reflexión Interna
                "La culpa me consume. Siento el peso de no haber sido mejor amigo, de no haber hecho lo suficiente… ¿Podré soportarlo o terminaré huyendo de todo?"
                "Debo resistir por mis amigos..."
                "Regresas a casa intentando despejar tu mente."
                #cambio para comprobar el game over 
                play sound "mas.mp3"
                $ estres += 25
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()     
                #Continuar 
                scene cuartonoche with slideright
                "Te sientes más agotado que nunca."
                "La culpa de no haber hecho más por Luna y Sebastián te pesa enormemente."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "¿Realmente crees que has tomado las mejores decisiones, [nombre]?"
                misterioso "Las elecciones que hacemos llevan consigo consecuencias, y escapar de ellas solo te llevará a enfrentarte a un mayor peso más adelante."
                misterioso "Pregúntate: ¿Estás evitando enfrentar tus miedos, o simplemente estás huyendo del dolor?"
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas con el corazón acelerado y el estrés a tope."
                "Las palabras de la voz resuenan en tu mente."
                chico "No puedo seguir así..."
                scene chico_estres with dissolve
                chico "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                chico "Pensar tanto en Luna y la situación de Sebastián hace que no pueda concentrarme."
                chico "Vamos, tú puedes con esto."
                scene cocina with slideleft
                "Apenas te preparas algo para comer."
                #stop music
                scene negro with dissolve
                "¿No sé qué transporte tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren16

                    "Tomar Autobús":
                        jump Autobus16  

        label Tren16:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Llegaré temprano, aunque no sé qué hacer..."
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así tengo más tiempo de pensar qué haré..."
            jump DiaCC

        label Autobus16:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero quiero estar bien antes de verlos..."
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Así tengo tiempo de pensar muy bien en todo..."
            jump DiaCC








        label DiaCC:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "No es hora de pensar en eso, debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la universidad."
            scene salon with slideleft
            "Veo que Sebastián aún no llega y observo a Luna estudiando. No quisiera molestarla después de no hablar con ella ayer."
            "Después de un tiempo, Sebastián aparece."
            chico "Hola, Sebastián."
            show amigo_preocupado at center with vpunch
            amigo "¡¡Wow!! ¿Estás bien, [nombre]?"
            amigo "Te ves peor que ayer."
            chico "Estoy bien, no te preocupes."
            amigo "¿Seguro?"
            chico "Sí."
            amigo "Oye, deberías sacarlo todo. Yo lo hice ayer y me sentí mejor, así que dime qué pasa."
            chico "Yo también tuve problemas en la preparatoria, solo que nunca tuve un amigo como tú hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado with dissolve
            show amigo at center with dissolve
            amigo "Ya veo. No te preocupes por nosotros. Siempre hemos sido así desde la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla bien los dos."
            chico "Entiendo, pero aun así debí apoyarte. Sé que ella es importante para ti."
            amigo "No solo eso... sin ella, mi vida no tendría sentido. Cuando estoy con ella, me siento vivo."
            chico "Tengo una idea: ¿qué tal si la invitamos un fin de semana? Nos reunimos y hablas con ella."
            amigo "No suena mal. Estoy seguro de que le gustaría pasar un rato con nosotros y estudiar como antes."
            chico "Muy bien, entonces terminando la clase hay que decirle."
            amigo "Me parece bien. Aunque yo le diré, porque sigues viéndote muy mal, y no quiero que se preocupe."
            chico "Tienes razón. Gracias."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Anímate, todo saldrá bien."
            hide maestra with dissolve

            # Agregar cuarto minijuego
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Estuvo bien."
                #amigo "Ves, sí se pudo."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
            #if estres >= 100:
                #call game_over
            #else:
                #$ actualizar_estado_sprite()    
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Esto es muy difícil."
                #amigo "Sí."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con Luna mientras lo observo."
            "Espero que todo esté bien entre ellos. No quiero arruinar esto y quedarme solo otra vez."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve
            "Sebastián regresa a su asiento. Después le preguntaré cómo le fue."

            # Agregar quinto minijuego
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Estuvo bien."
                #amigo "Ves, sí se pudo."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Esto es muy difícil."
                #amigo "Muy cierto."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra "Bueno, clase, estudien porque la siguiente semana será de exámenes. Estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que inicia la siguiente clase." 
            chico "¿Cómo te fue con ella?"
            show amigo at center with dissolve
            amigo "Aceptó, así que nos veremos con ella este fin."
            chico "Me alegra oír eso."
            amigo "También noto que te ves mal. Intenta descansar para que este fin de semana sea agradable."
            chico "Lo intentaré..."
            amigo "No te esfuerces mucho."
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase. Hoy veremos un nuevo tema. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Fue fácil."
                #amigo "Ves que sí."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chico "Esto es muy difícil."
                #amigo "Tienes razón, pero ya terminó."
                #hide amigo with dissolve

            "Termina la clase, dando por finalizado este día."    
            chico "Bueno, nos reuniremos en un parque para pasar tiempo los dos."
            show amigo at center with dissolve
            amigo "Así es, y recuerda: tranquilo, ¿vale?"
            chico "Muy bien, entonces nos vemos, Sebastián."
            amigo "Cuídate, [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós, Luna."
            "Observo su preocupación en mi cara, pero aun así decido sonreírle."
            show amiga at center with dissolve
            amiga "Adiós, [nombre]. Te veré allá entonces con Sebastián."
            chico "Te veo ahí."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Me retiro a mi casa a descansar, esperando el fin de semana." 
            "Espero que todo salga bien, la verdad."

            "Pasa el tiempo, llegando el fin de semana."
            play music "parque.mp3"
            scene parque with slideleft
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Recuerda, tus decisiones te han llevado hasta aquí."
            "Te sientes confuso y abrumado."
            "Vaya, esa voz... ¿será mi conciencia?"
            "En fin, hoy solo me divertiré con mis amigos."
            scene parque with slideleft
            "Te sientas a esperar a Luna y Sebastián, sintiendo el peso de lo que está por venir."
            "Sebastián llega primero, y te saluda con su habitual energía."
            chico "Hola Sebastián."
            show amigo at move_in_left
            amigo "¡Hola [nombre]! Vamos, ánimo, amigo."
            "Intentas poner tu mejor cara, pero el dolor de cabeza te traiciona."
            amigo "Tranquilo, no te esfuerces tanto."
            amigo "Todo saldrá bien."
            "Agachas la mirada, apenas esbozando una sonrisa."
            "¿Será este el camino del que hablaba esa sombra?"
            "Sebastián, preocupado, me abraza."
            amigo "Estamos contigo." 
            amigo "No estás solo, ¿vale?"
            chico "Eso espero..."
            "Luna llega y nos observa con preocupación."
            show amiga_preocupada  at right with vpunch
            amiga "¿Están bien los dos?"
            "Sebastián le da un pulgar arriba, ocultando la verdad de tu estado."
            amigo "Solo le duele la cabeza a [nombre], no es nada grave."
            "Me susurra al oído."
            amigo "Te apoyo en lo que decidas."
            chico "Gracias, Sebastián..."
            "Te das cuenta de que, aunque ellos se preocupan por ti, tú no has hecho nada por ellos."
            #Reflexión Interna
            "Mirando a mis amigos, siento una mezcla de culpa y alivio. Son lo mejor que tengo aquí, pero no estoy seguro de si podré cambiar. ¿Debería darme otra oportunidad, o es mejor dejar todo atrás?"
            hide amiga_preocupada with dissolve
            hide amigo with dissolve
            

            menu:
                "Hacer un último esfuerzo.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalCC1

                "Retirarse de la Universidad.":
                    play sound "menos.mp3"
                    $ estres -= 10
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalCC2
                    




                    
            label finalCC1:
                "Agarras el mayor coraje para enmendar tus errores."
                chico "Amigos..."
                chico "Quiero empezar de nuevo, Ustedes son lo mejor que me ha pasado."
                chico "Nunca pude tener amigos en la preparatoria..."
                chico "Y ahora que los tengo a ustedes."
                "Agachas mas la cabeza y aprietas los puños fuertemente sintiendo un peso enorme"
                chico "He sido un mal amigo y ustedes han sido buenos conmigo."
                "Ambos me abrazan fuertemente."
                chico "Quiero pasarla bien con ustedes y no volverlos a decepcionar."
                show amiga_preocupada at left with vpunch
                amiga "Tranquilo no nos has decepcionado y me alegra que me hayas dicho cómo te sientes."
                hide amiga_preocupada with dissolve
                show amiga at move_in_left
                amiga "Gracias Sebastián por estar al pendiente como siempre estuviste de mi"
                show amigo at move_in_right
                amigo "Una amistad grande jamás abandona a sus amigos en las buenas o en las malas."
                chico "Gracias amigos."
                "Sientes un peso menos, pero la culpa no se irá fácilmente."
                "Me abrazan más fuerte y correspondiendo regresando un abrazo más fuerte."
                amiga "Toda ira bien ya lo veras."
                amigo " si te apoyaremos en lo que sea."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los 3 nos quedamos estudiando, aunque no me preocupaba el examen, pero si estar con mis amigos y no volver a decepcionarlos."
                "Las decisiones que tome tardaran en sanar pues lo que hice no fue bueno ahora se a que se refería esa sombra."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Afrontar las consecuencias y enmendar los errores es un acto de valentía, [nombre]."
                misterioso "Reconocer nuestras fallas y buscar el apoyo de quienes nos importan es el primer paso para un verdadero cambio."
                misterioso "Las amistades son una fuente de fortaleza, y los errores nos hacen más sabios. Nunca olvides que siempre puedes contar con otros para ayudarte en los momentos más oscuros."
                stop music 

                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label finalCC2:
                stop music
                #play music "Sebastian.mp3"
                "Con lágrimas y un fuerte dolor en el pecho, decides decirles que te vas de la universidad."
                " Sebastián y Luna me miran preocupados, la sorpresa se refleja en sus rostros."
                show amiga_preocupada at left with vpunch
                show amigo_preocupado at right with vpunch
                amigo "Amigo, no tires la toalla tan rápido."
                amigo "Todos pasamos por momentos difíciles, pero siempre hay una salida."
                amiga "[nombre], no te rindas aún."
                amiga "Tienes un futuro por delante y nosotros estamos aquí para ayudarte..."
                "Me agarro el pecho, incapaz de levantar la mirada."
                "Las palabras se me escapan, el peso de la situación me aplasta."
                "La cabeza me pesa, el estómago se revuelve, el pecho me duele."
                "Siento que las paredes se cierran y las voces en mi cabeza se vuelven ensordecedoras."
                " El pánico me paraliza."
                chico "No puedo… no puedo seguir…"
                hide amiga_preocupada with dissolve
                hide amigo_preocupado with dissolve
                show amiga_triste at left with dissolve
                show amigo_triste at right with dissolve

                "Luna y Sebastián, con expresiones tristes, se acercan y me abrazan, intentando transmitirme fuerzas."
                amigo "Respetamos tu decisión, pero por favor, regresa pronto." 
                amigo"Sabes que te estaremos esperando."
                amiga "Te extrañaremos mucho, aunque no convivimos tanto, aprecio el tiempo que pasamos juntos."
                amiga "Prométeme que cuidarás de ti y que regresarás."
                amigo " Y que no estamos enojados ni decepcionados contigo."
                amigo "Todos tenemos momentos así."
                "Con un gran esfuerzo, apenas logró responderles."
                chico "Lo prometo… haré lo mejor que pueda."
                "Me sueltan y, con una sonrisa llena de esfuerzo, me despido de ellos."
                hide amiga_triste with dissolve
                hide amigo_triste with dissolve
                show amiga at move_in_left
                show amigo at move_in_right
                "Ambos me devuelven la sonrisa, aunque se nota la tristeza en sus ojos."               
                "Sebastián y Luna" "Adios [nombre] cuidate mucho."
                hide amigo
                hide amiga
                "Me alejo de ellos, regresando solo a mi casa, sintiendo el vacío en cada paso."
                #stop music
                scene cuarto with slideleft
                play music "latidos.mp3"
                "Te acuestas en la cama, reflexionando sobre lo sucedido."
                chico "No pude con la presión."
                chico "Este peso es insoportable, pero no puedo huir para siempre."
                chico "Esta ansiedad es horrible."
                chico "Volveré…" 
                "Luna, Sebastián… les prometo volver."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, el peso de nuestras decisiones nos lleva a un punto de ruptura. No es una señal de debilidad, sino una oportunidad para aprender."
                misterioso "Rendirse puede parecer una derrota, pero es mejor buscar apoyo que enfrentar todo solo."
                misterioso "Recuerda que siempre puedes volver a intentarlo. Las decisiones difíciles son inevitables, pero nunca olvides que hay personas dispuestas a ayudarte, y la puerta siempre está abierta para regresar."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


        #Decisión Luna
        label Estudiar:
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction()
            show amigo at center with dissolve
            amigo "Como gustes."
            hide amigo with dissolve
            "Te quedas estudiando con Luna. Fue estresante, pero al menos aprendiste."
            show amiga at center with dissolve
            amiga "Gracias por quedarte."
            hide amiga with dissolve
            scene negro with dissolve
            "Regresas a casa algo cansado."
            #stop music
            #play music "cancioncuarto.mp3"
            scene cuartonoche with slideright
            #Reflexión Interna
            "Hoy fue un buen primer día, pero siento una inquietud. Sé que debería descansar, pero la tentación de distraerme jugando videojuegos también es fuerte."
            "¿Será que estoy buscando una manera de escapar de la presión que siento por las expectativas en la universidad?"
        menu:
            "Dormir.":
                jump descansado2

            "Jugar videojuegos.":
                jump cansado2

        # Ruta B
        label descansado2:
            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction()
            scene cuartonoche with slideright
            chico "Bueno, lo mejor será descansar para mañana y tener energía."
            scene negro with dissolve
            "Te acuestas a dormir temprano, recuperando energía para el siguiente día."
            image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
            show misteriosoo
            misterioso "Descansar fue una buena elección, [nombre]."
            misterioso "No subestimes el poder del descanso. En momentos de estrés, a veces lo mejor que puedes hacer es recuperar tu energía."
            misterioso "Recuerda, mantener un equilibrio entre el esfuerzo y el descanso será fundamental en tu camino."
            scene cuarto with slideleft
            "Te despiertas con energía y descansado."
            scene wc with slideleft
            "Te sientes con mucha energía por lo que pasará hoy."   
            scene chico_normal with dissolve
            chico "¡Ahhh! Qué bien me siento."
            chico "Hora de ir a la universidad."    
            scene cocina with slideleft
            "Desayunas lo primero que encuentras y vas corriendo para tomar el transporte."
            scene negro with dissolve
            #stop music
            "¿Qué debería tomar ahora?"
        menu:
            "Tomar Tren":
                jump Tren4

            "Tomar Autobús":
                jump Autobus4

        label Tren4:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren, ya que el autobús fue más lento."
            jump RutaB

        label Autobus4:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento, es el más económico."
            jump RutaB

        # Ruta B
        label RutaB:
            #play music "salonclase.mp3"
            scene escuela with slideleft
            "Aquí vamos de nuevo."
            scene salon with slideleft
            show amiga at center with dissolve
            amiga "¿Listo para continuar?"    
            chico "Claro que sí."
            amiga "Te ves muy concentrado. Esto va a ser muy fácil."
            chico "Sí, gracias por ayudarme a practicar."
            hide amiga with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase. Vamos a repasar lo que vimos en la clase anterior."
            hide maestro with dissolve
            chico "Estoy preparado."
            # Agregar Minijuego 2
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
            chico "Eso fue fácil. Muchas gracias, Luna."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ renpy.restart_interaction()
                #chico "Esta clase fue estresante, pero logré salir adelante."
            show amiga at center with dissolve
            amiga "Sabes, estamos para apoyarnos."
            amiga "Estuviste excelente, [nombre]."
            chico "Todo gracias a ti, Luna, por ayudarme a practicar."
            amiga "Un placer. Es mejor para mí practicar con alguien."
            hide amiga with dissolve
            "Quién sabe cómo me habría ido si no hubiera dormido temprano."
            # Reflexión Interna
            "Es agradable saber que tengo a alguien como Luna para apoyarme. A veces, la universidad parece abrumadora, pero me doy cuenta de que no estoy solo en esto."
            "Tal vez este sea el tipo de amistad que me hace falta para seguir adelante."
            "Oh, aquí viene la nueva maestra."
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            chico "Bueno, a empezar con la siguiente materia."
            hide maestra with dissolve
            # Minijuego 3 agregar
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
            show amiga at center with dissolve
            amiga "Bueno, bueno, explica muy bien la maestra."
            chico "Sí, tienes razón."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ renpy.restart_interaction()
                #chico "Estuvo complicado."
            amiga "Sigo preocupada por Sebastián. Seguro tuvo problemas en la clase anterior."
            chico "Tienes razón. Ahora hay que convencerlo de que practique con nosotros."
            amiga "Buena suerte con eso."
            # Reflexión Interna
            "Sebastián ha estado algo distante últimamente... Siento que debería acercarme más y apoyarlo, pero me pregunto si estoy siendo demasiado insistente."
            "¿Debería tomar la iniciativa e intentar convencerlo de unirse o simplemente respetar su espacio?"
            hide amiga with dissolve
            $ estres = 5 # Eliminar después de ajustar los minijuegos
            $ renpy.restart_interaction()

            menu:
                "Convencerlo de que se una":
                    jump ConvencerB

                "No hacer nada":
                    jump NadaB
            
            
            
            
            #Ruta B
            label ConvencerB:
                chico "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo at center with dissolve
                amigo "Pero habrá un festival…"
                chico "Vamos, hazlo por mí y por Luna."
                amigo "Está bien, el festival puede esperar."
                chico "No te arrepentirás."
                hide amigo with dissolve
                play sound "mas.mp3"
                $ estres += 5
                $ renpy.restart_interaction()
                # Continuar Guion
                "Nos quedamos con Luna, quien parecía muy feliz."
                # Reflexión Interna
                "Convencer a Sebastián de estudiar con nosotros me hace sentir un poco más confiado. Tal vez estar aquí para mis amigos también me ayude a mantenerme enfocado y recordar que no estoy solo en esta experiencia."
                show amiga at move_in_left
                amiga "Gracias por acompañarme, chicos."
                show amigo at move_in_right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto, nos va a servir mucho."
                hide amigo with dissolve
                hide amiga with dissolve
                "Pasa el tiempo y estudiamos un rato más con Luna."
                "Observo cómo Sebastián se retira para ir al festival, pero decido acompañar a Luna un rato más."
                show amiga at center with dissolve
                amiga "[nombre], ¿puedo decirte algo?"
                chico "Claro, Luna."
                #stop music
                #play music "Luna.mp3"
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "De verdad lo aprecio mucho, [nombre]. Gracias por estar conmigo."
                chico "Sé cómo te sientes, Luna, y te comprendo."              
                # Reflexión Interna
                "Ver a Luna vulnerable me hace darme cuenta de que todos llevamos una carga, incluso cuando intentamos mantenerla oculta."
                "Es fácil olvidar que cada uno enfrenta sus propias batallas, y a veces el mejor apoyo es estar ahí, escuchar y ser alguien en quien puedan confiar."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chico "Nos vemos, Luna."
                amiga "Cuídate mucho, [nombre]."
                hide amiga with dissolve
                play sound "menos.mp3"
                $ estres -= 5
                $ renpy.restart_interaction()
                # Continuar
                scene cuartonoche with slideright
                "Te acuestas a dormir feliz por las amistades que has hecho."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Vas por buen camino, [nombre]. Estar ahí para los demás también ayuda a fortalecer tu propio sentido de propósito."
                misterioso "Recuerda que la universidad es un momento de desafíos, pero tener amigos para apoyarse mutuamente te hará más fuerte."
                misterioso "No subestimes el impacto positivo que puedes tener en la vida de los demás. Los pequeños gestos de apoyo pueden hacer una gran diferencia."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confuso pero calmado a la vez."
                chico "¿Qué o quién era esa voz?"
                chico "¿Buen camino?"
                scene chico_normal with dissolve
                chico "Nunca pensé estar tan calmado desde lo de la preparatoria."
                scene cocina with slideleft
                "Te preparas un desayuno para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren18

                    "Tomar Autobús":
                        jump Autobus18

        label Tren18:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día más, ¡qué emoción!"  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego más rápido."
            jump DiaB

        label Autobus18:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aún tengo tiempo."
            jump DiaB


        label DiaB:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chico "Hoy espero volver a pasar tiempo con Luna y Sebastián."
            scene salon with slideleft
            chico "Hola, amigos, ¿cómo están?"
            show amiga at move_in_right 
            amiga "Hola, me siento mucho mejor, gracias. Espero que tú también, [nombre]."
            show amigo at move_in_left
            amigo "Bien también, ¿y tú cómo estás, [nombre]?"
            chico "Muy bien. ¿Hoy vamos a quedarnos a repasar, verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Sí, será lo mejor."
            "Empieza la clase."
            chico "¿Hoy tendremos tres clases, verdad?"
            amiga "Según el horario, sí."
            chico "Vale, gracias, Luna."
            hide amigo with dissolve
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos, hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra with dissolve

            # Agregar cuarto minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # show amiga at center with dissolve
                # chico "Fue fácil."
                # amiga "Eso es verdad."
                # hide amiga with dissolve
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ renpy.restart_interaction()
                # show amiga at center with dissolve
                # chico "Vaya que sí tuve dificultades."
                # amiga "Deberías practicar un poco más."
                # hide amiga with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDiaB

                "Quedarse callado.":
                    $ Luna = "callarse"
                    jump cDiaB

        label cDiaB:
            if Luna == "preguntar":
                chico "Luna, ¿cómo has estado?"
                "Decido abrazarla por lo que pasó ayer."
                show amiga at move_in_right
                amiga "Me he sentido mejor, gracias por preguntar."
                show amigo at move_in_left
                amigo "¿Aún preocupada, Luna? Eres lista y puedes con todo."
                amiga "Gracias a ambos por el apoyo."
                amiga "Sin ustedes no sé qué haría."
                hide amiga with dissolve
                hide amigo with dissolve

            elif Luna == "callarse":  
                "Te quedas callado, pero permaneces cerca de ella."
                chico "No tengo palabras ahorita, pero tienes mi apoyo, Luna."
                show amiga at move_in_right
                amiga "Gracias, lo aprecio mucho."  
                show amigo at move_in_left
                amigo "También estoy aquí y me quedaré contigo, Luna."
                amiga "Gracias a ambos, de verdad."
                hide amiga with dissolve
                hide amigo with dissolve

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase." 
            hide maestra with dissolve

            # Agregar quinto minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # show amiga at center with dissolve
                # chico "Genial, muy fácil."
                # amiga "Practicando, todo se logra."
                # hide amiga with dissolve
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ renpy.restart_interaction()
                # show amiga at center with dissolve
                # chico "Vaya que sí tuve dificultades."
                # amiga "Deberías practicar un poco más, [nombre]."
                # hide amiga with dissolve

            show maestra at center with dissolve
            maestra "Bueno, clase, estudien porque la próxima semana habrá exámenes, pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve 
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at move_in_left
            amigo "Vaya, un fin de semana y ya tendremos exámenes."
            show amiga at move_in_right
            amiga "Lo sé, pero esto ya es la universidad. Siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno, ya lo veremos el fin de semana."
            chico "Apuesto a que será divertido, quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chico "Entonces no se diga más, nos veremos en el parque."
            hide amigo with dissolve
            hide amiga with dissolve
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase, hoy veremos un nuevo tema. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # show amiga at center with dissolve
                # chico "Estuvo bien."
                # amiga "Te lo dije."
                # hide amiga with dissolve
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                # show amiga at center with dissolve
                # chico "Eso estuvo difícil."
                # amiga "No te rindas, [nombre]."
                # hide amiga with dissolve

            "Termina la clase, finalizando el día de hoy."
            chico "Bueno, nos reuniremos en un parque para pasar tiempo los dos."
            show amiga at move_in_right
            amiga "Muy bien, los veré ahí."
            show amigo at move_in_left
            amigo "Igual, nos veremos allí."
            hide amiga with dissolve
            hide amigo with dissolve
            scene cuarto with slideleft
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            #stop music
            scene negro with dissolve
            "Es la primera vez que estoy muy relajado. Estudiar con amigos es mejor que solo, ya que aprendes más."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana, donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Recuerda, vas por buen camino."
            "Te sientes confuso, pero calmado."
            chico "¿Buen camino, eh?"
            "Mejor me concentro en pasarla bien con mis amigos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chico "Hola, Luna."
            amiga "Hola, [nombre]."
            amiga "Veo que aún no llega Sebastián."
            chico "Sí, creo que no tarda en llegar. Veo que trajiste material para estudiar."
            amiga "Sí, es para estudiar para el examen."
            chico "Perfecto. Esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos a estudiar los tres."

            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarlo juntos. ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas, [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, pero tampoco conozco los sentimientos de Sebastián."

            # Reflexión Interna
            "Este es el tipo de situación que temía enfrentar desde que entré a la universidad. No quiero perder a mis amigos, pero también quiero hacer las cosas bien para ambos."
            "Quizás eligiendo bien ahora, pueda evitar el tipo de soledad que experimenté en la preparatoria. Tal vez puedo ser el amigo que ambos necesitan."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalB1
                    

                "Quedarse con Luna.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalB2

            label finalB1:
                show amiga at move_in_right
                show amigo at move_in_left
                #Reflexión Interna
                "Saber que convencí a Sebastián de quedarse me da una sensación de logro. Me doy cuenta de que, en lugar de separarnos, esta experiencia nos está uniendo aún más."
                chico "Sebastián, podemos dejarlo para otro fin de semana."
                chico "Hoy hay que darle todo el apoyo a Luna."
                amigo "Tienes razón, es momento de saber cuándo hay que divertirse y cuándo hay que apoyar en momentos difíciles."
                amiga "Gracias por quedarte, Sebastián."
                amiga "Y a ti, [nombre], por ayudarme."
                chico "Quiero decirles que al principio no creí que haría buenos amigos."
                chico "El miedo a quedarme solo me aterraba, pero cuando los conocí, sentí más emoción, y es más divertido estudiar con amigos."
                "Sebastián y Luna me abrazan."
                amiga "Para eso están los amigos, [nombre]."
                amigo "Así es, estamos para apoyarnos en las buenas y en las malas."
                hide amigo with dissolve
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga with dissolve


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tomaste una decisión valiente al acercarte a tus amigos, [nombre]."
                misterioso "A veces, apoyar a otros requiere que nos pongamos en su lugar y reconozcamos la importancia de estar juntos en los momentos difíciles."
                misterioso "Recuerda que la amistad genuina no solo aligera las cargas de otros, sino que también te fortalece a ti."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            label finalB2:
                chico "Yo prefiero quedarme a estudiar un poco más."
                "No puedo dejar a Luna sola es mejor darle mi apoyo."
                show amigo at move_in_left
                amigo "Entiendo, bueno, no importa, los veré después."
                show amiga at move_in_right
                amiga "No tienes que irte ahora puedes quedarte."
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián me susurra."
                amigo "Cuida de ella, [nombre], ¿vale? Haz la diferencia por mí vale."
                "Lo miras directamente, haciendo un gesto de afirmación."
                hide amigo with dissolve
                hide amiga with dissolve
                "Sebastián se retira dejándonos solos a Luna y a ti."
                #Reflexión Interna
                "Aunque Sebastián se fue, sé que me quedé aquí por una razón importante. Estar aquí para Luna me hace sentir que, por una vez, puedo ser alguien en quien los demás confíen."
                chico "Tranquila, Luna, tienes mi apoyo."
                chico "Después de esto lo veremos y te ayudaré, ¿vale? Debemos permanecer juntos."
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chico "Gracias Luna."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga with dissolve
                "Ambos nos quedamos estudiando, pero debí convencerlo para que luna estuviera mejor."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, las elecciones que hacemos nos muestran lo que realmente valoramos."
                misterioso "Quedarte y apoyar a Luna fue un acto de empatía. Recuerda que tu presencia tiene un impacto importante en aquellos que valoran tu amistad."
                misterioso "La universidad es un viaje donde aprenderás a equilibrar tus decisiones, el apoyo mutuo será clave para sobrellevar los momentos difíciles."
                stop music 
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return













            #Ruta B,B
            label NadaB:
                "Decides no hacer nada y seguir practicando con Luna, quien parece aún preocupada."
                chico "Lo siento, Luna."
                show amiga_preocupada at center with vpunch
                amiga "No pasa nada, [nombre]."
                hide amiga_preocupada with dissolve
                play sound "mas.mp3"
                $ estres += 10
                $ renpy.restart_interaction()
                # Continuar Guion
                "Me quedo con Luna mientras observo cómo Sebastián se va al festival."
                # Reflexión Interna
                "Ver a Sebastián marcharse mientras me quedo con Luna me hace sentir una mezcla de alivio y culpa. Quiero ayudarla, pero ¿habrá sido suficiente? Tal vez dejé ir una oportunidad de unirnos más los tres."
                show amiga at center with dissolve
                amiga "Gracias por quedarte, [nombre]."
                chico "A ti, Luna, por ayudarme."
                amiga "[nombre], ¿puedo decirte algo?"
                chico "Claro, Luna."
                #stop music
                #play music "Luna.mp3"
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "De verdad lo aprecio mucho, [nombre]. Gracias por estar conmigo."
                chico "Sé cómo te sientes, Luna, y te comprendo."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                # Reflexión Interna
                "Ver a Luna luchar contra sus propias expectativas y la soledad me recuerda que todos tenemos cargas pesadas que no siempre mostramos."
                "Quizá, en lugar de preocuparme solo por cómo me ven mis amigos, debería centrarme en cómo puedo ser un mejor amigo para ellos."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chico "Nos vemos, Luna."
                amiga "Cuídate mucho, [nombre]."
                hide amiga with dissolve
                "Me siento mal porque sé que pude haber convencido a Sebastián."
                play sound "mas.mp3"
                $ estres += 10
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()     
                # Continuar
                scene cuartonoche with slideright
                chico "Pude haberlo convencido."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Las personas que confían en ti son un reflejo de lo que valoras, [nombre]."
                misterioso "Tener amigos es una oportunidad y una responsabilidad. Asegúrate de responder a esa confianza siendo honesto y solidario."
                misterioso "La duda y el miedo pueden evitar que actúes, pero reconocer tus propias emociones y las de los demás es el primer paso para acercarte y hacer una verdadera diferencia."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas con un sentimiento de culpa."
                chico "Tranquilízate, solo fue un sueño."
                scene chico_normal with dissolve
                chico "Solo fue un sueño. Hoy veré que Luna esté bien."
                scene cocina with slideleft
                "Te preparas un desayuno para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren19

                    "Tomar Autobús":
                        jump Autobus19  

        label Tren19:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día más, ¡qué emoción!"  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego más rápido."
            
            jump DiaBB

        label Autobus19:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aún tengo tiempo."
            
            jump DiaBB

        







        label DiaBB:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chico "Sé que pude haber convencido a Sebastián."
            chico "No quisiera ser responsable de que Luna se distancie de él."
            scene salon with slideleft
            "Veo a Luna preocupada aún."
            chico "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga at center with dissolve
            amiga "No te preocupes, Sebastián siempre sale desde la preparatoria, así que estoy acostumbrada."
            chico "Sé que es importante estudiar, pero también es bueno salir con personas."
            chico "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar solo."
            amiga "¿Estás bien, [nombre]?"
            chico "Sí, estoy bien, gracias."
            "Veo a Sebastián saludarnos de lejos, pero no se ve feliz."
            "Hoy tendremos 3 clases." 
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra with dissolve

            # Agregar cuarto minijuego 
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #    $ minijuegos_ganados += 1
            #    play sound "menos.mp3"
            #    $ estres -= 5
            #    $ actualizar_estado_sprite()
            #    $ renpy.restart_interaction()
            # show amiga at center with dissolve
            # chico "Salió bien."
            # amiga "Sí."
            # hide amiga with dissolve
            # elif juego == "pierde":
            #    $ minijuegos_perdidos += 1
            #    play sound "mas.mp3"
            #    $ estres += 5
            #    $ actualizar_estado_sprite()
            #    $ renpy.restart_interaction()
            # show amiga at center with dissolve
            # chico "Pudo ser peor."
            # amiga "Práctica más."
            # hide amiga with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."

            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDiaBB

                "Quedarse callado.":
                    $ Luna = "callarse"
                    jump cDiaBB

        label cDiaBB:
            if Luna == "preguntar":
                chico "Luna, ¿estás bien?"
                show amiga at center with dissolve
                amiga "Solo estoy preocupada. No quiero que Sebastián piense que lo dejé atrás, él sabe mi situación."
                "Decido abrazarla fuerte."      
                chico "Todo estará bien, ya lo verás."
                amiga "Eso espero."
                hide amiga with dissolve

            elif Luna == "callarse":  
                "Un incómodo silencio nos invadió a ambos."
                "Intentas calmar a Luna."
                chico "Cualquier cosa, aquí estaré, Luna."
                show amiga at center with dissolve
                amiga "Lo sé…"  
                hide amiga with dissolve
                "Decido darle ánimo a Luna."

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase." 
            hide maestra with dissolve

            # Agregar quinto minijuego 
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #    $ minijuegos_ganados += 1
            #    play sound "menos.mp3"
            #    $ estres -= 5
            #    $ actualizar_estado_sprite()
            #    $ renpy.restart_interaction()
            # show amiga at center with dissolve
            # chico "Genial, muy fácil."
            # amiga "Me alegro por ti."
            # hide amiga with dissolve
            # elif juego == "pierde":
            #    $ minijuegos_perdidos += 1
            #    play sound "mas.mp3"
            #    $ estres += 5
            #    $ actualizar_estado_sprite()
            #    $ renpy.restart_interaction()
            # show amiga at center with dissolve
            # chico "Vaya, que sí tuve dificultades."
            # amiga "Deberías practicar más."
            # hide amiga with dissolve

            show maestra at center with dissolve
            maestra "Bueno clase, estudien porque la próxima semana será de exámenes, pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará el tema de una manera diferente para que lo refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            "Pero notas que Luna está cada vez más desanimada."
            chico "Ánimo, Luna. Este fin de semana hay que reunirnos con Sebastián en el parque para que te animes. ¿Qué te parece?"
            show amiga at center with dissolve
            amiga "No es mala idea. Gracias por preocuparte mucho por mí, [nombre]."
            chico "Entonces este fin iremos al parque."
            amiga "Muy bien."

            hide amiga with dissolve
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase, hoy veremos nuevo tema. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego 
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #    $ minijuegos_ganados += 1
            #    play sound "menos.mp3"
            #    $ estres -= 5
            #    $ actualizar_estado_sprite()
            #    $ renpy.restart_interaction()
            # show amiga at center with dissolve
            # chico "Estuvo bien."
            # amiga "Te lo dije."
            # hide amiga with dissolve
            # elif juego == "pierde":
            #    $ minijuegos_perdidos += 1
            #    play sound "mas.mp3"
            #    $ estres += 5
            #    $ actualizar_estado_sprite()
            #    $ renpy.restart_interaction()
            # show amiga at center with dissolve
            # chico "Eso estuvo difícil."
            # amiga "Tienes mi apoyo."
            # hide amiga with dissolve

            "Termina la clase, finalizando el día de hoy."
            chico "Bueno, nos reuniremos en un parque para pasar tiempo los dos."
            show amiga at move_in_right
            amiga "Muy bien, los veré allí."
            hide amiga with dissolve
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chico "Hola, Sebastián. Luna y yo nos vamos a reunir este fin de semana. ¿Te unes?"
            show amigo at center with dissolve
            amigo "Claro que sí. Los veré a los dos entonces."
            hide amigo with dissolve
            "Me despido de él, regresando a mi casa."
            #stop music
            scene cuarto with slideleft
            "Al final salió bien. Espero que todo salga bien este fin de semana."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso " Ella aún confía en ti."
            "Te sientes menos culpable ya que conviviste con ambos."
            chico "¿Seguiré Dormido?"
            "No creo mejor no pensar en ello y concentrarme para pasarla bien con ellos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chico "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chico "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chico "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Gracias por organizar esto."
            chico "Te la debo Luna."
            "Veo a Luna más tranquila que antes."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            #Reflexión Interna
            "Me encuentro entre dos personas a las que quiero ayudar, pero me siento atrapado por mis propias inseguridades."
            "¿Cómo puedo ser un buen amigo si siempre temo que mis acciones no sean suficientes? Hoy quiero hacer lo correcto, aunque no sé qué significa exactamente."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalBB1

                "Quedarse con Luna.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalBB2

            label finalBB1:
                show amiga at move_in_right
                show amigo at move_in_left
                chico "Sebastián esta vez quiero decirte que te quedes con nosotros, la vez del festival no sé por qué no pude hacerlo."
                amigo "No te preocupes se lo que se siente no poder decidir."
                chico "Aun así lo siento, Luna necesita apoyo así que esta vez acompáñanos."
                amigo " Está bien y no te preocupes es hora de pasar tiempo con ustedes esta vez."
                amiga "Gracias a ambos por quedarse conmigo y más en estos tiempos."
                #Reflexión Interna
                "Convencer a Sebastián de quedarse me da esperanza. Quizá por fin estoy logrando unir a mis amigos y demostrarles que pueden contar conmigo cuando más lo necesitan."
                "Los junto a los 2 para estar más juntos."
                chico "La soledad nunca es buena."
                "Sebastián y Luna" "Estamos de acuerdo contigo."
                hide amigo with dissolve
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga with dissolve


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos, aunque me costó trabajo."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Elegir ser un punto de unión es una decisión de fortaleza, [nombre]."
                misterioso "Cuando decides apoyar a tus amigos, también te estás apoyando a ti mismo, creando un vínculo que te ayudará a superar los momentos difíciles."
                misterioso "La verdadera amistad implica tomar decisiones que beneficien al grupo. Sigue adelante con confianza y la seguridad de que no estás solo."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            label finalBB2:
                "Me vuelvo a quedar sin palabras para convencerle."
                chico "Yo prefiero quedarme a estudiar un poco más."
                "Luna necesita apoyo ahora más que nunca ahora que se su pasado."
                show amigo at move_in_left
                amigo "Entiendo bien, no importa los veré después…"
                show amiga at move_in_right
                amiga "Sebastián…"
                amigo "No te preocupes es como en los viejos tiempos diviértanse los 2."
                "Sebastián me susurra."
                amigo "Si de verdad somos amigos cuidaras bien de ella ¿Vale?"
                "Decido abrazarlo por la culpa que cargo y le susurro también."
                chico " Lo siento no te fallare te lo prometo."
                "Sebastián corresponde el abrazo y más calmado se retira."
                hide amigo with dissolve
                #Reflexión Interna
                "Sentí que debía quedarme con Luna. Aunque no convencí a Sebastián, espero poder compensarlo con mi dedicación. A veces, ser un buen amigo es estar ahí para quien más lo necesita en ese momento."
                chico "Lo siento Luna te he vuelto a fallar."
                amiga "No te preocupes, pero me ayudaras a convivir más con el."
                chico "Te lo prometo."
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez Luna."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chico "Gracias Luna."
                    chico "No te fallare."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga with dissolve
                "Ambos nos quedamos estudiando."
                "Debo cumplir con estas promesas."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Elegiste quedarte con alguien que confía en ti, lo cual muestra tu empatía y determinación."
                misterioso "No siempre puedes cumplir con todos, pero dar lo mejor en cada situación es una muestra de tu crecimiento."
                misterioso "Recuerda que la amistad es una oportunidad para aprender, mejorar y equilibrar decisiones. Sigue buscando ese equilibrio, y nunca dudes de tu capacidad de impactar positivamente en la vida de los demás."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


        
        # Ruta A               
        label cansado2:
            $ cansancio = True
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction()
            scene cuartonoche with slideright
            chico "Bueno, una partida no hará ningún daño."
            scene negro with dissolve
            "Juegas unas cuantas partidas y pierdes la noción del tiempo."
            scene cuarto with slideleft
            "Despiertas con dificultad, sintiendo mucho sueño."
            scene wc with slideleft
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chico_normal with dissolve
            # Reflexión Interna
            "Miro mi reflejo, apenas reconociéndome. Esto no es lo que imaginé para mí en la universidad."
            "¿Es que realmente vale la pena seguir así, sacrificando el descanso y la salud por distracciones que al final solo me dejan agotado?"
            chico "Creo que me sobrepasé un poco…"
            "Suspiro."
            chico "Bueno, diría que demasiado... Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina with slideleft
            "Desayunas lo primero que te hallaste y vas corriendo para tomar el transporte."
            scene negro with dissolve
            #stop music
            "¿Ahora qué debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren9

                "Tomar Autobús":
                    jump Autobus9  

        label Tren9:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
            jump RutaA

        label Autobus9:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento, es el más económico."
            jump RutaA   

        # Ruta A
        label RutaA:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "Aquí vamos de nuevo."
            scene salon with slideleft
            show amiga at center with dissolve
            amiga "¿Listo para continuar?"    
            chico "Claro que sí."
            amiga "¿Te sientes bien? Te ves un poco cansado."
            amiga "Sabes, [nombre], tal vez podrías descansar un poco más. Aunque estudiar es importante, si estás muy cansado no puedes concentrarte igual."
            chico "Tienes razón... creo que debería planear mejor mis horas de descanso."
            hide amiga with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase. Vamos a repasar lo que vimos la clase anterior."
            hide maestro with dissolve
            "Oh no, tengo mucho sueño."

            #Minijuego 2
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                #chico "Eso fue fácil muchas gracias Luna."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 10
                #$ renpy.restart_interaction()
            chico "Rayos, casi no me pude concentrar bien, pero gracias a Luna no fue tan mal."
            # Reflexión Interna
            "El sueño me invade y, aunque intento enfocarme, la clase se vuelve una lucha constante contra mis propios párpados."
            "¿Por qué no me detuve a descansar? Esto no solo me afecta a mí, también a Luna, que está aquí apoyándome."           
            show amiga at center with dissolve
            amiga "Vamos, anímate. No estuvo tan mal."
            chico "Bueno, si tú lo dices, esperemos que en la siguiente vaya mejor."
            amiga "Ya verás que sí."
            hide amiga with dissolve
            "Sigo un poco cansado, pero veo que entra la maestra."
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            chico "Bueno, a empezar con la siguiente materia."
            hide maestra with dissolve

            # Minijuego 3
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
            show amiga at center with dissolve
            amiga "Bueno, bueno explica muy bien la maestra. "
            chico "Sí, tienes razón."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 10
            #if estres >=50:
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #chico "Estuvo complicado."
            amiga "Sigo preocupada por Sebastián, seguro tuvo problemas en la anterior."
            chico "Tienes razón, ahora hay que convencerlo de que practique con nosotros."
            amiga "Buena suerte con eso."
            # Reflexión Interna 
            "Sebastián podría beneficiarse de estudiar juntos, y Luna seguramente lo apreciaría, pero siento que el cansancio sigue pesando sobre mí."
            "¿Debería hacer el esfuerzo y convencerlo o simplemente dejarlo pasar esta vez?"

            hide amiga with dissolve
            $ estres = 15 # Eliminar después de ajustar los minijuegos
            $ renpy.restart_interaction()
            menu:
                "Convencerlo de que se te una.":
                    jump ConvencerA

                "No hacer nada.":
                    jump NadaA









        label ConvencerA:
            chico "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
            show amigo at center with dissolve
            amigo "Pero habrá un festival."
            chico "Vamos, hazlo por mí y por Luna."
            amigo "Te ves muy cansado, pero está bien, me uniré a ustedes."
            amigo "El festival puede esperar."
            chico "No te arrepentirás."
            
            # Reflexión Interna
            "Ver a Sebastián quedarse me hace pensar que tomar la iniciativa fue lo correcto. Puede que el cansancio me afecte, pero saber que estoy ayudando a mis amigos también me da energía."
            "Tal vez si mantengo este equilibrio entre el estudio y el descanso, podré enfrentar mejor los desafíos de la universidad."
            
            hide amigo with dissolve
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction()

            # Continuar guion
            "Nos quedamos con Luna. Parecía muy feliz."
            show amiga at move_in_left
            amiga "Gracias por acompañarme, chicos."
            show amigo at move_in_right
            "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto. Nos va a servir mucho."
            hide amigo with dissolve
            hide amiga with dissolve
            "Pasa el tiempo y estudiamos un rato más con Luna."
            "Observo cómo Sebastián se retira para ir con lo que quedó del festival, pero decido acompañar un rato más a Luna."
            
            show amiga at center with dissolve
            amiga "[nombre], ¿puedo decirte algo?"
            chico "Claro, Luna."
            #stop music
            #play music "Luna.mp3"
            amiga "Muchas gracias por acompañarme. Aprecio mucho esto."
            "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
            chico "¿Estás bien, Luna?"
            amiga "Sí, es solo que siempre me he sentido sola."
            amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
            amiga "Mis padres esperan que sea perfecta, sin margen de error."
            hide amiga with dissolve
            
            "Observas cómo comienza a llorar, por lo que decides abrazarla."
            show amiga_triste at center with dissolve
            amiga "De verdad lo aprecio mucho, [nombre]. Gracias por estar conmigo."
            chico "Sé cómo te sientes, Luna, y te comprendo."
            "Secas sus lágrimas y te despides de ella, regresando a casa."
            hide amiga_triste with dissolve
            #stop music
            show amiga at center with dissolve
            chico "Nos vemos, Luna."
            amiga "Cuídate mucho, [nombre]."
            hide amiga with dissolve

            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction()

            # Continuar
            scene cuartonoche with slideright
            "Te acuestas a dormir porque te sentías muy cansado, pero a pesar de todo, el día salió bien."
            "Mientras tus ojos se cierran, tu mente repasa las últimas horas... algo se siente fuera de lugar, pero decides no pensar demasiado en ello."
            play music "sueñom.mp3"
            image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
            show misteriosoo
            misterioso "A veces, el esfuerzo que hacemos para apoyar a nuestros amigos nos da la fuerza que pensamos que no tenemos."
            misterioso "Recuerda que, en la universidad, tanto el apoyo mutuo como el descanso son esenciales para mantenerse firme ante los desafíos."
            misterioso "Aprende a dosificar tu energía, y nunca subestimes la importancia de rodearte de personas que te fortalezcan."
            stop music
            scene cuarto with slideleft
            #play music "cancioncuarto.mp3"
            "Te despiertas sobresaltado y con la mente llena de preguntas, pero te das cuenta de que ya no te sientes cansado."
            chico "¿Qué habrá sido eso?"

            if estres >= 50:
                scene chico_estres with dissolve
                $ actualizar_estado_sprite() 
                chico "Hoy va a ser un buen día. Mejor dejar atrás esos pensamientos extraños."
            else:        
                scene chico_normal with dissolve
                $ actualizar_estado_sprite() 
                chico "Hoy va a ser un buen día. Mejor dejar atrás esos pensamientos extraños."

            scene cocina with slideleft
            "Te preparas un desayuno para ir a la escuela."
            #stop music
            scene negro with dissolve
            "¿Qué transporte tomo hoy?"
            menu:
                "Tomar Tren":
                    jump Tren20

                "Tomar Autobús":
                    jump Autobus20
        label Tren20:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump DiaA
        
        label Autobus20:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump DiaA            

        label DiaA:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chico "Hoy espero volver a pasar tiempo con Luna y Sebastián."
            scene salon with slideleft
            "Veo a Luna y a Sebastián reunidos y me decido a saludarlos."
            chico "Hola amigos, ¿cómo están?"
            show amiga at move_in_right
            amiga "Hola, [nombre], te ves mejor que ayer. Espero que tú también estés bien."
            show amigo at move_in_left
            amigo "Sí, opino lo mismo. ¿Y tú, cómo estás?"
            chico "Muy bien. ¿Hoy vamos a quedarnos a repasar, verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Sí, será lo mejor."

            "Empieza la clase."
            chico "¿Hoy tendremos tres clases, verdad?"
            amiga "Según el horario, sí."
            chico "Vale, gracias, Luna."
            hide amigo with dissolve
            hide amiga with dissolve

            show maestra at center with dissolve
            maestra "Muy bien, alumnos, hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra with dissolve

            # Agregar cuarto minijuego (placeholder)
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chico "¡Fue fácil!"
            #     amiga "Eso es verdad."
            #     hide amiga with dissolve
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chico "Vaya, sí tuve dificultades."
            #     amiga "Deberías practicar un poco más."
            #     hide amiga with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."

            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDiaA

                "Quedarse callado.":
                    $ Luna = "callarse"
                    jump cDiaA

        label cDiaA:
            if Luna == "preguntar":
                chico "Luna, ¿cómo has estado?"
                "Decido abrazarla por lo que pasó ayer."
                show amiga at move_in_right
                amiga "Me he sentido mejor. Gracias por preguntar."
                show amigo at move_in_left
                amigo "¿Aún preocupada, Luna? Eres lista y puedes con todo."
                amiga "Gracias a ambos por el apoyo."
                amiga "Sin ustedes no sé qué haría."
                hide amiga with dissolve
                hide amigo with dissolve

            elif Luna == "callarse":
                "Te quedas callado, pero permaneces cerca de ella."
                chico "No tengo palabras ahora, pero tienes mi apoyo, Luna."
                show amiga at move_in_right
                amiga "Gracias, lo aprecio mucho."
                show amigo at move_in_left
                amigo "Yo también estoy aquí y me quedaré contigo, Luna."
                amiga "Gracias a ambos, de verdad."
                hide amiga with dissolve
                hide amigo with dissolve

            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve

            # Agregar quinto minijuego (placeholder)
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chico "¡Genial, fue muy fácil!"
            #     amiga "Practicando todo se logra."
            #     hide amiga with dissolve
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chico "Vaya, sí tuve dificultades."
            #     amiga "Deberías practicar más, [nombre]."
            #     hide amiga with dissolve

            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at move_in_left
            amigo "¡Vaya, un fin de semana y ya tenemos exámenes!"
            show amiga at move_in_right
            amiga "Lo sé, pero esto es la universidad. Siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno, ya lo veremos el fin de semana."
            chico "Apuesto a que será divertido. Quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chico "Entonces no se diga más, nos veremos en el parque."
            hide amigo with dissolve
            hide amiga with dissolve

            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase. Hoy veremos un nuevo tema. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego (placeholder)
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()

            "Termina la clase, finalizando el día de hoy."
            chico "Bueno, nos reuniremos en un parque para pasar tiempo los tres."
            show amiga at move_in_right
            amiga "Muy bien, los veré ahí."
            show amigo at move_in_left
            amigo "Igual, nos veremos allí."
            hide amiga with dissolve
            hide amigo with dissolve
            scene cuarto with slideleft
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            #stop music
            scene negro with dissolve
            "Es la primera vez que estoy muy relajado. Estudiar con amigos es mejor que hacerlo solo, ya que aprendes más."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Recuerda vas muy bien."
            "Te sientes confuso."
            chico "¿Otra vez?"
            "Bueno no importa debo estar concentrado."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chico "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chico "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chico "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalA1

                "Quedarse con Luna.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalA2

            label finalA1:
                show amiga at move_in_right
                show amigo at move_in_left
                chico "Sebastián, podemos dejarlo para otro fin de semana."
                chico "Hoy hay que darle todo el apoyo a Luna."
                amigo "Tienes razón, es momento de saber cuándo hay que divertirse y cuándo hay que apoyar en momentos difíciles."
                amiga "Gracias por quedarte esta vez Sebastián."
                amiga "Y a ti, [nombre], por ayudarme."
                hide amigo with dissolve
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga with dissolve


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos."
                #Reflexión Interna
                "Estudiar junto a Luna y Sebastián me hace sentir que estoy en el camino correcto. La compañía de amigos no solo ayuda a sobrellevar el estrés académico, sino que también aporta una paz que no se puede encontrar estudiando solo."
                "Quizás la universidad no solo sea un desafío académico, sino también una oportunidad para aprender a apoyarnos mutuamente."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has hecho buenos amigos que te apoyarán en esta etapa de tu vida. No olvides que el apoyo mutuo fortalece las amistades y también tu espíritu."
                misterioso "Aprender a equilibrar tus esfuerzos y compartirlos con personas en quienes confías es esencial en este camino."
                misterioso "Recuerda, la universidad te ofrece no solo conocimiento académico, sino también una lección sobre el valor de las relaciones y el apoyo en los momentos difíciles."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return

                

            label finalA2:
                chico "Yo prefiero quedarme a estudiar un poco más."
                "Recuerdo lo que Luna me contó sobre su pasado, y sé que necesita apoyo ahora más que nunca."
                show amigo at move_in_left
                amigo "Entiendo... no importa, los veré después."
                show amiga at move_in_right
                amiga "Sebastián…"
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián se acerca y me susurra al oído."
                amigo "Cuida de ella, [nombre], ¿vale?"
                "Lo miras directamente, haciendo un gesto de afirmación, sintiendo el peso de su petición."
                hide amigo with dissolve
                hide amiga with dissolve
                "Al verlo marcharse, me quedo pensando si realmente tomé la decisión correcta."
                "Pero no quiero que Luna se sienta sola, así que dejo esos pensamientos de lado."
                chico "Tranquila, Luna, tienes mi apoyo."
                chico "Después de esto lo veremos y te ayudaré, ¿vale?"
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chico "Gracias Luna."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga with dissolve
                "Aunque me quedo con Luna para estudiar, no puedo evitar que, en el fondo de mi mente, una pequeña duda me siga preguntando por qué no convencí a Sebastián de quedarse también."
                #Reflexión Interna
                "Quedarme con Luna me da la certeza de que, a veces, priorizar a quienes nos importan es el camino correcto."
                "Quizá este pequeño gesto no cambie el mundo, pero fortalece nuestra amistad y me hace sentir en paz."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Cuidar de tus amigos cuando lo necesitan demuestra tu madurez y crecimiento."
                misterioso "Recuerda que en la vida y en la universidad, construir relaciones sólidas te ayudará a sobrellevar los momentos difíciles."
                misterioso "El bienestar emocional de las personas que nos importan puede ser un refugio en tiempos de estrés y desafíos."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return    






            #Ruta A,A
            label NadaA:
                "Decides no hacer nada y seguir practicando con Luna, quien parece estar preocupada aún."
                chico "Lo siento, Luna."  
                show amiga_preocupada at center with vpunch
                amiga "No pasa nada, [nombre]."
                hide amiga_preocupada with dissolve
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 

                #Continuar guion 
                "Decides quedarte con Luna mientras observas cómo Sebastián se va al festival."
                "Te sientes realmente cansado."

                #Reflexión Interna
                "El cansancio me supera, y aunque sé que pude haber intentado convencer a Sebastián, no tuve las fuerzas para hacerlo. ¿Es este el tipo de persona en la que me estoy convirtiendo?"
                show amiga at center with dissolve
                amiga "Gracias por quedarte, [nombre]."
                chico "A ti, Luna, por ayudarme."
                amiga "[nombre], ¿puedo decirte algo?"
                chico "Claro, Luna."
                #stop music
                #play music "Luna.mp3"
                amiga "Quería agradecerte por acompañarme."
                amiga "Esto significa mucho para mí."
                "Ves a Luna un poco triste y decides preguntar qué le sucede."
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "De verdad lo aprecio mucho, [nombre]."
                amiga "Gracias por estar aquí."
                chico "Entiendo cómo te sientes, Luna."
                chico "Estoy aquí para ti."

                #Reflexión Interna
                "Luna confía en mí, y aquí estoy, sintiéndome agotado y culpable. Tal vez ella no lo sabe, pero siento que he fallado al no hacer más por nuestros amigos. ¿Por qué no puedo reaccionar?"
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chico "Nos vemos, Luna."
                amiga "Cuídate mucho, [nombre]."
                hide amiga with dissolve
                "Te sientes mal porque sabes que pudiste haber convencido a Sebastián, pero el cansancio te supera."

                #Reflexión Interna
                "Si solo hubiera tenido un poco más de energía... Quizás esto habría terminado de otra forma. Siento que esta carga de arrepentimiento se hace cada vez más pesada."
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 

                #Continuar historia
                scene cuartonoche with slideright
                chico "Pude haberlo convencido, pero estaba muy cansado..."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, nuestras decisiones son reflejo de nuestro estado emocional, [nombre]."
                misterioso "Cuando estamos agotados, nuestras acciones pueden parecer ajenas a nosotros, pero cada una deja una huella."
                misterioso "La próxima vez que enfrentes una decisión importante, pregúntate: ¿Es esto lo que realmente quiero, o es solo una respuesta a cómo me siento en el momento?"
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas nervioso."
                chico "¿Solo fue un sueño?"
                "Aún te sientes culpable, pero ya no estás agotado."

                if estres >= 50:
                    scene chico_estres with dissolve
                    $ actualizar_estado_sprite() 
                    chico "Espero que Luna esté bien..."
                else:    
                    scene chico_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chico "Espero que Luna esté bien."
                #stop music    
                scene cocina with slideleft
                "Te preparas un desayuno para ir a la escuela."
                
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren21

                    "Tomar Autobús":
                        jump Autobus21  

            label Tren21:
                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Otro día más. ¡Qué emoción!"  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Así llego más rápido."
                
                jump DiaAA

            label Autobus21:
                if transporte == "tren":  
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El tren es rápido, pero aún tengo mucho tiempo."  
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "Aún tengo tiempo."
                
                jump DiaAA








        label DiaAA:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chico "Sé que pude haber convencido a Sebastián."
            chico "No quisiera ser responsable de que Luna se distancie de él."
            scene salon with slideleft
            "Veo a Luna preocupada aún."
            chico "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga at center with dissolve
            amiga "No te preocupes, [nombre]. Sebastián siempre sale desde la preparatoria, así que estoy acostumbrada."
            chico "Sé que es importante estudiar, pero también es bueno salir con personas."
            chico "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar solo."
            amiga "¿Estás bien, [nombre]?"
            chico "Sí, estoy bien, gracias."
            "Veo a Sebastián saludarnos de lejos, pero no se ve feliz."
            "Hoy tendremos tres clases."
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra with dissolve

            # Minijuego 4
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chico "Salió bien."
                #amiga "Sí."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chico "Esto salió fatal."
                #amiga "Práctica más."
                #hide amiga with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDiaAA

                "Quedarse callado.":
                    $ Luna = "callarse"
                    jump cDiaAA

        label cDiaAA:
            if Luna == "preguntar":
                chico "Luna, ¿estás bien?"
                show amiga at center with dissolve
                amiga "Solo estoy preocupada. No quiero que Sebastián piense que lo dejé atrás, aunque él sabe mi situación."
                "Decido abrazarla fuerte."
                chico "Todo estará bien, ya lo verás."
                amiga "Eso espero."
                hide amiga with dissolve

            elif Luna == "callarse":  
                "Un incómodo silencio nos invadió a ambos."
                "Intento calmar a Luna."
                chico "Cualquier cosa, aquí estaré, Luna."
                show amiga at center with dissolve
                amiga "Lo sé…"
                hide amiga with dissolve
                "Decido darle ánimo a Luna."

            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve

            # Placeholder Minijuego 5
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                # play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chico "Genial, muy fácil."
                #amiga "Me alegro por ti."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chico "Vaya que sí tuve dificultades."
                #amiga "Deberías practicar más."
                #hide amiga with dissolve

            show maestra at center with dissolve
            maestra "Bueno, clase, estudien porque la próxima semana será de exámenes."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento mientras inicia la siguiente clase."
            "pero notas que Luna está cada vez más desanimada."
            chico "Animo Luna este fin de semana hay que reunirnos con Sebastián en el parque para que te animes ¿qué te parece?"
            show amiga at center with dissolve
            amiga "No es mala idea, gracias por preocuparte mucho por mi [nombre]."
            chico "Entonces este fin iremos al parque."
            amiga "Muy bien."
            hide amiga with dissolve
            "Observó cómo Luna se veía más calmada."
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro with dissolve
            #agregar sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chico "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
            #if estres >= 100:
                #call game_over
            #else:    
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chico "Eso estuvo difícil."
                #amiga "Tienes mi apoyo."
                #hide amiga with dissolve 
            "Termina la clase, finalizando el día de hoy."
            chico "Bueno, nos reuniremos en el parque para pasar tiempo juntos."
            show amiga at move_in_right
            amiga "muy bien los veré ahí."
            hide amiga with dissolve
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chico "Hola Sebastián, Luna y yo nos vamos a reunir este fin de semana ¿te unes?"
            show amigo at center with dissolve
            amigo "Claro que sí los veré a los 2 entonces."
            hide amigo with dissolve
            "Me despido de él regresando a mi casa."
            #stop music
            scene cuarto with slideleft
            "Al final salió bien, espero que todo salga bien este fin de semana."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Ahora puedes hacer la diferencia."
            "Te sientes menos culpable, pero confuso."
            chico "¿Otra vez el?"
            "Bueno, debo estar concentrado."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chico "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chico "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chico "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Gracias por organizar esto."
            chico "Te la debo Luna."
            #Reflexión Interna
            "Me quedo al lado de Luna, pero no puedo evitar sentir un peso en el pecho. Sigo pensando en cómo pude haber intentado más, en lo fácil que sería mejorar esta situación si tan solo tuviera la energía para ello."
            "Veo a Luna más tranquila que antes."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez, debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            #Reflexión Interna
            "Me encuentro en la misma encrucijada, pero esta vez debo dar un paso adelante. No puedo seguir dejando que el cansancio y la culpa me controlen. Es momento de decidir qué clase de amigo quiero ser."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalAA1

                "Quedarse con Luna.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump finalAA2

            label finalAA1:
                show amiga at move_in_right
                show amigo at move_in_left
                chico "Sebastián, esta vez quiero decirte que te quedes con nosotros."
                chico "Aquella vez no pude convencerte porque me sentía mal y cansado."
                amigo "oh no lo sabía."
                amigo "Lo siento..."
                chico "No pasa nada, Sebastián."
                chico "Pero me preocupé mucho por Luna aquella vez."
                amigo " Entiendo..."
                "Ves que Sebastián finalmente decide quedarse con ustedes."
                amiga "Gracias, [nombre], por convencer a Sebastián."
                chico "No hay problema. "
                chico "Sé que te preocupa estar sola."
                hide amigo with dissolve
                hide amiga with dissolve
                "Pasan la tarde juntos, disfrutando del tiempo como amigos y estudiando. "
               
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."

                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga with dissolve

                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos, aunque me costó trabajo."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Reconocer las propias limitaciones y aun así encontrar la fuerza para actuar es un acto de valentía, [nombre]."
                misterioso "Nunca subestimes el poder de pequeños esfuerzos, porque son esos momentos los que fortalecen las amistades."
                misterioso "Hoy, elegiste no permitir que el cansancio te definiera, y ese es un paso hacia adelante."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            label finalAA2:
                "Me siento mal al no volver a convencer a Sebastián, pero con pocos ánimos respondo."
                chico "Lo siento, Sebastián."
                chico "Creo que esta vez me quedaré con Luna. "
                "No quiero que se quede sola."
                show amigo at move_in_left
                amigo "Lo entiendo, no te preocupes."
                amigo "Me reuniré con otros amigos entonces."
                show amiga at move_in_right
                amiga "Sebastián…"
                hide amigo with dissolve
                "Ves cómo Sebastián se va, dejándote con Luna."              
                amiga "Gracias por quedarte conmigo, [nombre]."
                chico "Lo haré siempre que lo necesites, Luna."
                hide amiga with dissolve
                "Pasan la tarde estudiando juntos, aunque sientes un poco de tristeza por no haber salido con Sebastián."
                "Luna parece estar un poco más tranquila, pero sabes que aún queda mucho por superar."
                "Decides tomar un descanso después de un largo día de estudio."
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez Luna."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se..."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    amiga "Así que no te sientas culpable."
                    chico "Gracias Luna."
                    chico "No te volvere a fallar."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía y el apoyo que me das."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    chico "Lo mejor sera darle espacio."
                    amiga "Si tiene razón [nombre]."
                    hide amiga with dissolve
                
                "Estás satisfecho de haber apoyado a Luna, pero también sabes que aún hay retos por enfrentar."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "La culpa puede ser una carga, pero también una señal de que tienes el deseo de mejorar."
                misterioso "No te castigues demasiado, en la universidad y en la vida, habrá oportunidades de redención."
                misterioso "Recuerda, [nombre], que las decisiones que tomas hoy son solo el comienzo de un camino en el que siempre podrás evolucionar."
                stop music 
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return







# Division Chica
elif genero == "chica":
        
        chica "Este es mi salón."
        chica "Bueno, me sentaré aquí."
        desconocido "Hola, ¿cómo estás?"
        chica "Hola, bien. ¿Y tú, cómo estás?"
        show amiga at move_in_left
        desconocido "Bien también. Soy Luna."
        chica "Un placer, me llamo [nombre]."
        "Espero ser su amiga."
        amiga "El gusto es mío."
        "A lo lejos, veo a un chico acercándose."
        desconocido "Hola."
        amiga "Hola, Sebastián, ¿elegiste la misma carrera?"
        show amigo at move_in_right
        amigo "Sí, eso parece. ¿Y tú cómo te llamas?"
        chica "Hola, me llamo [nombre], mucho gusto."
        amigo "El gusto es mío. Te ves pálida, ¿estás bien?"
        chica "Sí, estoy bien."
        hide amigo with dissolve
        hide amiga with dissolve
        "Debo controlarme. Sé que es difícil para mí socializar, pero está saliendo bien."
        play sound "mas.mp3"
        $ estres += 20
        $ renpy.restart_interaction()
        
        explicacion "De aquí en adelante, las decisiones que tomes afectarán tu barra de estrés."
        explicacion "Recuerda mantenerla baja. Si sube al límite, perderás la partida."
        explicacion "Un estrés muy alto puede aumentar la dificultad de los minijuegos."
        explicacion "Así que cuida tu barra de estrés."
        
        "Veo al maestro entrando al salón de clases mientras todos se quedan en silencio."
        show maestro at center with dissolve
        maestro "Buenos días, alumnos. Soy el profesor Carlos y les impartiré la materia de Redes."
        maestro "Empezaremos con la primera sesión."
        hide maestro with dissolve
        
        chica "Bueno, aquí vamos."
        chica "Espero no tener dificultades."

        # Minijuego (comentado para futuras implementaciones)
        # $ Minijuego = "Gano"
        # if juego == "gana":
            #$ minijuegos_ganados += 1
            #play sound "menos.mp3"
            #$ estres -= 5
            #$ renpy.restart_interaction()        
        chica "Eso estuvo fácil."        
        # $ Minijuego = "Perdio"
        # elif juego == "pierde":
            #$ minijuegos_perdidos += 1
            #play sound "mas.mp3"
            #$ estres += 5
            #$ renpy.restart_interaction()
            #chica "¡Uf! Menos mal no me fue tan mal."
        
        chica "Pero debería practicar para mejorar en la siguiente clase."
        
        show amigo at move_in_right
        amigo "Oye, [nombre], ¿quieres acompañarnos al billar?"
        show amiga at move_in_left
        amiga "No lo sé... creo que deberíamos repasar un poco para la siguiente clase, [nombre]."
        
        hide amigo with dissolve
        hide amiga with dissolve
        
        # Reflexión interna
        "Me siento un poco indecisa. Por un lado, sé que socializar es importante para hacer amigos en esta nueva etapa, y no quiero perderme la oportunidad de acercarme a Sebastián."
        "Por otro lado, sé que estudiar con Luna podría aliviar algo de la ansiedad que siento por mis clases. Quizás dedicarle tiempo al estudio me ayude a manejar mejor el estrés."
        
        explicacion "Esta es la primera decisión que puede afectar tu barra de estrés."
        explicacion "Recuerda no llenarla."

        menu:
            "Claro, vámonos al billar":
                jump billar2

            "Me quedaré a repasar con Luna":
                jump estudiar2

    # Decisión Sebastián
        label billar2:
            show amigo at center with dissolve
            amigo "Bien dicho, [nombre]. ¡Vamos!"
            hide amigo with dissolve
            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction()
            scene negro with dissolve
            #stop music
            #play music "cancioncuarto.mp3"
            "Vas al billar con Sebastián."
            "Fue divertido, pero una pequeña voz en tu cabeza te dice que mañana pagarás el precio."
            "Regresas a tu casa algo cansada."
            
            scene cuartonoche with slideright
            chica "Fue un buen primer día."
            "¿Debería dormirme ya o leer un libro?"

        menu:
            "Dormir":
                jump descansada

            "Leer libro":
                jump cansada
     



        # ChicaD
        label descansada:
            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction()            
            scene cuartonoche with slideright
            chica "Lo mejor será descansar para tener energía mañana."
            scene negro with dissolve
            "Te acuestas temprano y recuperas energías para el siguiente día."
            scene cuarto with slideleft
            "Te despiertas llena de energía y bien descansada."
            scene wc with slideleft
            "Hoy me siento con mucha vitalidad. Me pregunto qué pasará."
            scene chica_normal with dissolve
            chica "¡Aaahhh! Qué bien me siento."
            chica "Hora de ir a la universidad."
            scene cocina with slideleft
            "Desayunas lo primero que encuentras y sales corriendo para tomar el transporte."
            scene negro with dissolve
            #stop music
            "¿Qué debería tomar hoy?"
            menu:
                "Tomar el tren":
                    jump Tren5

                "Tomar el autobús":
                    jump Autobus5

        label Tren5:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "El tren es la opción más rápida."
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren, ya que el autobús fue más lento la última vez."
            
            jump ChicaD

        label Autobus5:
            if transporte == "tren":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero hoy tengo tiempo de sobra, así que tomaré el autobús."
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aunque el autobús es más lento, es la opción más económica."
            
            jump ChicaD
  



        #Chica D
        label ChicaD:    
            scene escuela with slideleft
            #play music "salonclase.mp3" 
            "Aquí vamos de nuevo."
            scene salon with slideleft
            chica "Parece que Luna no está muy convencida."
            show amigo at center with dissolve
            amigo "No te preocupes, hablaremos con ella después para que se una a nosotros."
            chica "Sí, creo que es lo mejor."
            amigo "Bueno, es hora de ver cómo nos va. Seguro que nos irá bien."
            chica "Eso espero."
            hide amigo with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase, vamos a repasar lo que vimos la sesión anterior."
            hide maestro with dissolve
            
            # Agregar segundo minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # chica "Me fue muy bien"
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ renpy.restart_interaction()
            
            chica "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            
            show amigo at center with dissolve
            amigo "No estuvo mal después de todo."
            chica "Sí, me siento aliviada de que haya terminado bien."
            amigo "Pasemos a la siguiente materia."
            chica "Seguro que en esta nos irá todavía mejor."
            amigo "Si tú lo dices."
            hide amigo with dissolve
            
            "Nunca había tenido la oportunidad de salir con un amigo."
            "Siempre solía volver sola a casa."
            "Veo que llega la maestra. Sebastián parece preocupado, ¿será que le gusta Luna?"
            
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            "Después le pregunto... ahora a poner atención."
            hide maestra with dissolve

            # Minijuego 3 agregar
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # show amigo at center with dissolve
                # amigo "Muy fácil."
                # chica "Es cierto."
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 5
                # $ renpy.restart_interaction()
            
            show amigo at center with dissolve
            amigo "Esto no estuvo tan mal."
            chica "Sí, tienes razón."
            chica "Oye, Sebastián, te veo preocupado. ¿Todo bien?"
            amigo "Me preocupa que Luna siempre ha sido mi amiga, y no quisiera que se quedara sola."
            "Mi instinto no me falla aún."
            chica "Podemos quedarnos con ella esta vez."
            amigo "Sí, aunque hoy habrá un festival. Podemos convencerla de que venga con nosotros, y después practicamos con ella."
            chica "Veré qué puedo hacer."
            hide amigo with dissolve

            # Reflexión Interna
            "Me preocupa que Luna se quede estudiando sola, pero también sé que tiene sus propias prioridades. Quizás quiera venir con nosotros, pero no quiero presionarla."
            "Me pregunto si convencerla será lo mejor o si debería respetar su decisión. En momentos como estos, parece que siempre hay algo que perder o ganar."
            
            
            
            menu:
                "Convencerla de que se una.":
                    jump ConvencerlaD_Chica

                "No hacer nada.":
                    jump NadaLD_Chica




            #Chica D
            label ConvencerlaD_Chica:
                chica "Luna, Sebastián y yo vamos a ir a un festival. ¿Quieres unirte?"
                show amiga at center with dissolve
                amiga "Les recomendaría quedarse a estudiar, pero prefiero repasar por mi cuenta. De todos modos, diviértanse."
                chica "Gracias por la preocupación. Espero verte mañana, amiga."
                amiga "Hasta mañana, [nombre]."
                hide amiga with dissolve
                "Intenté convencerla, pero fallé. Espero que mañana pueda pasar tiempo con ella. No me gusta que esté sola... me recuerda a mí en la preparatoria."
                "También solía quedarme sola estudiando..."
                play sound "mas.mp3"
                $ estres += 10
                $ renpy.restart_interaction()
                #stop music
                # Continuación de la Ruta
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "Gracias por acompañarme."
                chica "Está bien relajarse de vez en cuando."
                #play music "Sebastian.mp3"
                amigo "No sé por qué, pero me siento como un tonto ahora mismo."
                chica "¿Te preocupa algo?"
                amigo "Luna siempre fue mi mejor amiga. Aunque ella estaba más enfocada en el estudio, siempre encontrábamos tiempo para estar juntos."
                "Veo tristeza en su rostro y decido preguntarle directamente."
                chica "¿Estás bien, Sebastián?"
                "Sebastián se detiene y me mira con melancolía."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna es muy importante para mí. En casa, mi padre siempre está decepcionado por mi desempeño en la escuela y mi conducta."
                amigo "Nunca conocí a mi madre... falleció cuando nací. Pero aquí estoy, tratando de ser fuerte gracias a Luna."
                amigo "Me gustaría invitarla a salir algún día y volver a pasar tiempo con ella como antes."
                "Intento consolarlo. Su vida parece estar llena de dificultades, y empatizo con él."
                "Mis padres también trabajan todo el tiempo, y los veo muy poco. Entiendo lo que siente Sebastián al querer hacerlos sentir orgullosos..."
                chica "Entiendo cómo te sientes, Sebastián. Pero no debemos rendirnos. Tenemos que seguir adelante."
                "Lo abrazo con fuerza, transmitiéndole todo mi apoyo."
                amigo "Gracias, [nombre]. Lo necesitaba. Sé que la escuela es importante, pero a veces es difícil encontrar fuerzas para continuar."
                hide amigo_triste with dissolve
                #stop music
                show amigo at center with dissolve
                amigo "Será mejor que regresemos. Nos vemos mañana."
                chica "Muy bien. Hasta mañana."
                amigo "Gracias por acompañarme. Me recuerdas mucho a ella."
                chica "¿En serio? Espero llevarme muy bien con ella entonces."
                hide amigo with dissolve
                scene negro with dissolve
                "Siento un dolor profundo al saber que no soy la única que enfrenta estas luchas."
                "Regreso a casa, reflexionando sobre todo lo que ocurrió hoy."
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()     
                scene cuartonoche with slideright
                "Intento dormir, pero mi mente no deja de pensar en Luna."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Recuerda que no todas las decisiones serán fáciles, y eso está bien."
                misterioso "A veces, tomar el camino más difícil es lo que nos permite crecer y conocernos mejor."
                misterioso "No huyas de las situaciones que te incomodan. Enfréntalas, y verás que puedes salir fortalecida."
                misterioso "La universidad no es solo un lugar para estudiar, también es una oportunidad para aprender a conocerte a ti misma."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confusa, pero decidida a resolver la situación con Luna y Sebastián."
                chica "Conocerme a mí misma... Tal vez es hora de intentarlo."

                if estres >= 50:
                    scene chica_estres with dissolve
                    $ actualizar_estado_sprite() 
                    chica "Vamos, ánimo. Si Sebastián está bien, yo también puedo estarlo. Resolveré esto con Luna."
                else:
                    scene chica_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chica "Vamos, ánimo. Si Sebastián está bien, yo también puedo estarlo. Resolveré esto con Luna."

                scene cocina with slideleft
                "Te preparas un desayuno rápido para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren11

                    "Tomar Autobus":
                        jump Autobus11  
               
            label Tren11:
            
                
                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Es el más rápido."  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
                    
                jump Dia_chicaD
                
            label Autobus11:

                if transporte == "tren":  
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El tren es rápido, pero aún tengo tiempo para llegar  ."  
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "Bueno, aunque es más lento es el más económico."
                    
                jump Dia_chicaD

            label Dia_chicaD:
                scene escuela with slideleft
                #play music "salonclase.mp3"
                "Vamos anímate debo dar lo mejor de mí."
                "No debo rendirme ahora que por fin entré a la Universidad."
                scene salon with slideleft
                "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
                "Después de un tiempo veo llegar a Sebastián."
                chica "Hola Sebastián."
                show amigo at center with dissolve
                amigo "Hola [nombre]."
                "Miro como los 2 estamos mejor que ayer, pero decidí contarle mi pasado."
                chica "Sobre lo de ayer yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
                chica "No quisiera que entre tú y Luna tengan problemas."
                amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
                amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
                chica "Entonces ella te gusta verdad."
                amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
                chica "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
                amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
                chica "muy bien entonces terminando hay que decirle."
                amigo "Me parece bien esta vez iremos los 2."
                chica "De acuerdo."
                hide amigo with dissolve
                "Comienza la clase."
                show maestra  at center with dissolve
                maestra "Muy bien Alumnos hoy les impartiré 2 clases."
                amigo "Podemos con esto."
                hide maestra with dissolve

                # agregra cuarto minijuego 
                #$ Minijuego = "Gano"
                #if juego == "gana":
                    #$ minijuegos_ganados += 1
                    #play sound "menos.mp3"
                    # $ estres -= 5
                    # $ actualizar_estado_sprite()
                    # $ renpy.restart_interaction()
                    #show amigo at center with dissolve
                    #chica "Muy facil."
                    #amigo "Tienes razon."
                    #hide amigo with dissolve
                #$ Minijuego = "perdio"
                #elif juego == "pierde":
                    #$ minijuegos_perdidos += 1
                    #play sound "mas.mp3"
                    #$ estres += 5
                    # $ actualizar_estado_sprite()
                    #$ renpy.restart_interaction()
                    #show amigo at center with dissolve
                    #chica "Soy pésima en esto."
                    #amigo "Yo también."
                    #hide amigo with dissolve

                "Termina la primera clase, pero la maestra nos da un tiempo libre."
                "Aprovechamos el tiempo para ir a hablar con luna."
                chica "Hola Luna."
                show amiga at move_in_left
                amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
                chica "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
                show amigo at move_in_right
                amigo "Como en los viejos tiempos."
                amiga "Claro encantada de ir con ustedes."
                chica "Entonces nos vemos allá."
                hide amigo with dissolve
                hide amiga with dissolve
                "Nos regresamos a nuestros lugares."
                "Se termina el tiempo y continúa la siguiente clase."


                # agregra quinto minijuego 
                #$ Minijuego = "Gano"
                #if juego == "gana":
                    #$ minijuegos_ganados += 1
                    #play sound "menos.mp3"
                    # $ estres -= 5
                    # $ actualizar_estado_sprite()
                    # $ renpy.restart_interaction()
                    #show amigo at center with dissolve
                    #chica "Fue fácil."
                    #amigo "Tienes razon."
                    #hide amigo with dissolve
                #$ Minijuego = "perdio"
                #elif juego == "pierde":
                    #$ minijuegos_perdidos += 1
                    #play sound "mas.mp3"
                    #$ estres += 5
                    # $ actualizar_estado_sprite()
                    #$ renpy.restart_interaction()
                    #show amigo at center with dissolve
                    #chica "Soy pésima en esto."
                    #amigo "Yo también pero ya falta una."
                    #hide amigo with dissolve

                show maestra at center with dissolve
                maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
                maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
                hide maestra with dissolve
                "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
                chica "Salió bien la verdad."
                show amigo at center with dissolve
                amigo "Sí tienes razón este fin será inolvidable. "   
                hide amigo with dissolve
                "Veo entrar al maestro Carlos dando inicio la última clase."
                show maestro at center with dissolve
                maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
                hide maestro with dissolve
                # agregra sexto minijuego 
                #$ Minijuego = "Gano"
                #if juego == "gana":
                    #$ minijuegos_ganados += 1
                    #play sound "menos.mp3"
                    # $ estres -= 5
                    # $ actualizar_estado_sprite()
                    # $ renpy.restart_interaction()
                    #show amigo at center with dissolve
                    #chica "Sin problemas."
                    #amigo "Pues claro."
                    #hide amigo with dissolve
                #$ Minijuego = "perdio"
                #elif juego == "pierde":
                    #$ minijuegos_perdidos += 1
                    #play sound "mas.mp3"
                    #$ estres += 5
                    # $ actualizar_estado_sprite()
                    #$ renpy.restart_interaction()
                    #show amigo at center with dissolve
                    #chica "Soy pésimo en esto."
                    #amigo "Yo también, pero al menos termino.
                    #hide amigo with dissolve

                "Termina la clase dando finalizado este día de hoy."    
                chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
                show amigo at center with dissolve
                amigo "Así es."
                chica "Muy bien entonces nos vemos Sebastián."
                amigo "Cuídate [nombre]."
                hide amigo with dissolve
                "Tomo mis cosas y me despido de Luna."
                chica "Adiós Luna."
                show amiga at center with dissolve
                amiga "Adiós [nombre] nos vemos allá entonces."
                hide amiga with dissolve
                #stop music
                scene negro with dissolve
                "Estoy ansiosa de que llegue este fin de semana." 

                "Pasa el tiempo llegando el fin de semana."

                scene parque with slideleft
                play music "parque.mp3"
                "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
                scene negro with dissolve
                misterioso "Afrontas bien las consecuencias recuerda no rendirte."
                "Te sientes confusa."
                "Bueno gracias a él todo fue mejor y resolví las cosas."
                "Ahora sólo debo concentrarme en pasarla bien con ellos."
                scene parque with slideleft
                "Me siento a esperar a Luna y Sebastián."
                "Pasa un tiempo y veo llegar a Sebastián primero."
                chica "Hola Sebastián."
                show amigo at move_in_left
                amigo "Hola [nombre]."
                amigo "¿Estás lista para pasarla bien?"
                chica "Si estoy lista."
                " Luna aparece con un material para estudiar."
                show amiga at move_in_right
                amiga "Hola amigos ¿Listos?"
                "Sebastián y [nombre]" "Si estamos listos."
                hide amiga with dissolve
                hide amigo with dissolve
                "Pasa el tiempo y Sebastián me lleva a un lugar privado."
                "Luna se nos queda viendo confusa de lo que pasa."
                chica "¿Qué pasa? "
                chica "¿Te sientes bien?"
                show amigo_triste at center with dissolve
                amigo "Sí solo que reunirnos y verla feliz me hace feliz."
                chica " Deberías decirle lo que sientes por ella."
                amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
                # Reflexión Interna
                "Escuchar a Sebastián me hace recordar mis propias dudas y temores. Entiendo lo que es sentirse insegura, y quizá, si lo apoyo, le ayude a ganar la confianza que necesita."
                "Si le doy ese empujón para que hable con Luna, podría ser lo mejor para ambos. Pero también me pregunto si debería respetar su ritmo y su espacio."
                hide amigo_triste with dissolve

            menu:
                "Darle apoyo para que se confiese.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaD1

                "Respetar sus sentimientos de preocupación.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaD2





                    
            label final_chicaD1:
                chica "Se cómo te sientes, pero es mejor decirle lo que sientes por ella veo que ella quiere que le digas eso."
                show amigo at center with dissolve
                amigo "¿Estás segura de esto?"
                chica "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo with dissolve
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at move_in_left
                amigo "Luna…"
                show amiga at move_in_right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga with dissolve
                show amiga_triste at right with dissolve

                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo with dissolve
                hide amiga_triste with dissolve
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at move_in_left
                show amiga at move_in_right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella. "
                hide amigo with dissolve
                hide amiga with dissolve
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Ayudar a tus amigos desinteresadamente te da propósito y fortalece tus lazos. No subestimes el poder de una mano amiga."
                misterioso "En la vida universitaria y más allá, no temas ofrecer tu apoyo. A veces, el simple hecho de estar presente hace una gran diferencia."
                misterioso "Nunca dudes en expresar tus emociones a quienes te importan. El camino de la amistad se nutre de la autenticidad y la empatía."
                stop music

                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label final_chicaD2:
                chica "Si es lo que sientes, te apoyaré en cualquier decisión que tomes, Sebastián."
                chica "Sé lo que se siente no poder expresarte, así que cuentas conmigo en lo que sea."
                show amigo at center with dissolve
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chica "De acuerdo."
                hide amigo with dissolve
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo."
                show amigo at move_in_left
                amigo "Volvimos."
                show amiga at move_in_right
                amiga "¿Todo bien?"
                chica "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chica "Continuemos."
                "Luna parece tranquila al pasar tiempo con Sebastián, pero  puedes notar que le hubiera gustado que él le confesara sus sentimientos."
                "Aun así, respetastes  su decisión de Sebastián."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Respetar los sentimientos de tus amigos también muestra madurez. A veces, darles espacio es el mejor apoyo."
                misterioso "Recuerda, [nombre], la verdadera fortaleza está en saber cuándo apoyar y cuándo dar un paso atrás, confiando en el proceso de los demás."
                misterioso "La universidad puede ser desafiante, pero enfrentarlo acompañado de amigos hace el camino más llevadero. No te rindas, y apóyate en quienes te rodean."
                misterioso "Confía en tus decisiones, y recuerda que la vida es un constante aprendizaje."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return








            #RChica D,D
            label NadaLD_Chica:
                "Decides no hacer nada, Sebastián parece preocupado."
                # Reflexión Interna
                "Un extraño malestar se instala en mí al ver que decidí no invitarla. Algo en mí me dice que pude haber hecho más."
                "¿Por qué no di ese paso? Quizás el miedo de interferir o simplemente de equivocarme."   
                chica "Lo siento, Sebastián."
                show amigo_triste at center with dissolve
                amigo "No te preocupes, vámonos entonces."
                hide amigo_triste with dissolve
                "¿Qué me sucede? Ver a Luna sola me recuerda a mí, y no puedo hacer nada."
                "También me quedaba sola estudiando..."
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                #stop music
                # Continuación de la Ruta
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "Gracias por acompañarme, aunque deberíamos haberla invitado."
                chica "Está bien relajarse de vez en cuando, y de verdad lo siento... no sé por qué no me animé."
                amigo "Anímate, yo soy quien debió convencerla, no tú."
                #play music "Sebastian.mp3"
                amigo "Me siento como un idiota ahora mismo."
                chica "¿Pasa algo, Sebastián?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y, aun así, pasábamos tiempo juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que algo anda mal, así que decido preguntarle."
                chica "¿Todo bien, Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna, para mí, es mi mejor amiga, pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como por mi desempeño en la escuela."
                amigo "A mi madre nunca la conocí, pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna. Me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián. Su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa, ya que trabajan todos los días y los veo muy pocas veces, así que sé lo que siente Sebastián, sobre todo el querer que estén orgullosos..."
                "Lo abrazo fuerte."
                amigo "Gracias, [nombre]. Lo necesitaba. Sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chica "Sé lo que sientes, no poder agarrar fuerzas para seguir, pero no debemos rendirnos."
                hide amigo_triste with dissolve
                #stop music
                show amigo at center with dissolve
                amigo "Mejor regresemos, nos vemos mañana."
                chica "Muy bien."
                amigo "Gracias por acompañarme. Me recuerdas mucho a ella."
                chica "¿En serio? Espero llevarme muy bien con ella entonces..."
                hide amigo with dissolve
                scene negro with dissolve
                "Sientes un dolor profundo al saber que no sufres sola, pero te sientes peor por no haber invitado a Luna."
                "Regresas a casa pensando en todo lo que pasó hoy."
                play sound "mas.mp3"
                $ estres += 20
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite()     
                # Continuar
                scene cuartonoche with slideright
                "Sientes que pudiste hacer más con Luna y te acuestas a dormir."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, el mayor desafío es enfrentar nuestros propios miedos y limitaciones, ¿verdad, [nombre]?"
                misterioso "Recuerda que la vida nos da varias oportunidades. El arrepentimiento no debe ser un peso, sino una motivación para actuar diferente la próxima vez."
                misterioso "Si sientes que pudiste hacer más, considera esta reflexión como una promesa a ti misma de intentarlo mejor en el futuro."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confusa, pero sigues pensando en Luna."
                chica "¿Enfrentar mis miedos?"
                
                if estres >= 50:
                    scene chica_estres with dissolve
                    $ actualizar_estado_sprite() 
                    chica "Me siento muy mal por no haber hecho nada por Sebastián y Luna."
                    "Esa voz me dijo que debo enfrentar mis miedos."
                else:
                    scene chica_normal with dissolve 
                    $ actualizar_estado_sprite()  
                    chica "Me siento muy mal por no haber hecho nada por Sebastián y Luna, pero al menos voy bien en mis estudios."
                    "Esa voz me dijo que debo enfrentar mis miedos."

                scene cocina with slideleft
                "Te preparas un desayuno con mayor esfuerzo para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"

                menu:
                    "Tomar Tren":
                        jump Tren13
                    "Tomar Autobús":
                        jump Autobus13  

            label Tren13:
                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Es el más rápido."  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
                jump Dia_chicaDD

            label Autobus13:
                if transporte == "tren":  
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El tren es rápido, pero aún tengo tiempo para llegar."  
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "Bueno, aunque es más lento, es el más económico."
                jump Dia_chicaDD








        label Dia_chicaDD:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "No es hora de pensar en eso debo de dar lo mejor de mí. "
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon with slideleft 
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chica "Hola Sebastián."
            show amigo_preocupado at center with vpunch
            amigo "Hola [nombre] ¿te sientes bien?"
            chica "Si estoy bien."
            hide amigo_preocupado with dissolve
            "Miro como los 2 estamos mejor que ayer, pero decidí contarle mi pasado."
            chica "Sobre lo de ayer yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chica "No quisiera que entre tú y Luna tengan problemas."
            show amigo at center with dissolve
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chica "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chica "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chica "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien esta vez iremos los 2 pero yo le diré que te veo un poco desanimada."
            chica "De acuerdo."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra with dissolve

            # agregra cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "fue facil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovechamos el tiempo para ir a hablar con luna."
            chica "Hola Luna."
            show amiga at move_in_left
            amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
            chica "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
            show amigo at move_in_right
            amigo "Como en los viejos tiempos."
            amiga "Claro encantada de ir con ustedes."
            hide amiga with dissolve
            show amiga_preocupada at left with vpunch
            "Luna me observa preocupada. "
            amiga "¿Estás bien [nombre]?"
            chica "Si estoy bien no te preocupes Luna."
            amiga "Si tu lo dices."
            chica "Entonces nos vemos allá."
            hide amigo with dissolve
            hide amiga_preocupada with dissolve
            "Nos regresamos a nuestros lugares."
            "Se termina el tiempo y continúa la siguiente clase."


            # agregra quinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chica "Salió bien la verdad."
            show amigo at center with dissolve
            amigo "Sí tienes razón este fin será inolvidable. "   
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro with dissolve
            # agregra sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Sin problemas."
                #amigo "Pues claro."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo with dissolve

            "Termina la clase dando finalizado este día de hoy."    
            chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo at center with dissolve
            amigo "Así es."
            chica "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chica "Adiós Luna."
            show amiga 
            amiga "Adiós [nombre] nos vemos allá entonces."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Estoy ansiosa de que llegue este fin de semana." 
            "Y sobre todo cambiar mi destino."
            "Pasa el tiempo llegando el fin de semana."

            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "No importa que decisión tomes solo se consciente. "
            "Te sientes confusa."
            "¿Ser consciente? Creo que he hecho bien en planear este día."
            "Mejor no pensar en ello y pasarla bien."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chica "Hola Sebastián."
            show amigo at move_in_left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros."    
            amigo "Vamos amiga mucho ánimo ¿vale?"
            chica "Está bien, pero sigo pensando que esto pudo cambiar al decirle desde un principio, pero estoy preocupada de cómo está ella."
            amigo "No te dejaré sola en esto."
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chica "¿Mejor?"
            amigo "Mucho mejor."
            "Luna aparece con un material para estudiar."
            show amiga at move_in_right
            amiga "Hola amigos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga with dissolve
            hide amigo with dissolve
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chica "¿Qué pasa? "
            chica "¿Te sientes bien?"
            show amigo_triste at center with dissolve
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            amigo "Te dije que todo está bien [nombre]."
            chica " Aun así quiero apoyarte Sebastián y ayudarte con Luna."
            amigo "Muchas gracias amiga, lo aprecio mucho."
            # Reflexión Interna
            "Sé lo que es tener dudas, especialmente cuando los sentimientos están involucrados. ¿Debo motivarlo a actuar o debería respetar su cautela y dejar que decida su propio camino?"
            "Quizás lo que él necesita es un empujón... o quizás sólo una amiga que entienda su silencio."
            hide amigo_triste with dissolve

            menu:
                "Darle apoyo para que se confiese.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaDD1

                "Respetar sus sentimientos de preocupación.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaDD2





                    
            label final_chicaDD1:
                chica "No pude convencerla en un principio, pero quiero ayudarte a que le confieses tus sentimientos a ella."
                show amigo at center with dissolve
                amigo "No te preocupes más por eso."
                amigo "¿Y estás segura de esto?"
                chica "Esta vez te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo with dissolve
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at move_in_left
                amigo "Luna…"
                show amiga at move_in_right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga with dissolve
                show amiga_triste at right with dissolve

                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo with dissolve
                hide amiga_triste with dissolve
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at move_in_left
                show amiga at move_in_right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella, y se siente más apoyado. "
                hide amigo with dissolve
                hide amiga with dissolve
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos, aunque tuvimos dificultades."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia."
                stop music
                hide screen barra_estres 
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, ayudar a quienes amamos es motivarlos a enfrentar sus propios temores. Lo has hecho bien."
                misterioso "No temas en expresar lo que piensas y en buscar siempre el bienestar de los demás, incluso cuando implique un riesgo."
                stop music


                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label final_chicaDD2:
                chica "No pude convencerla en un principio, pero tampoco quiero presionarte y respeto tu decisión."
                chica "Te daré el apoyo que necesites con Luna."
                show amigo at center with dissolve
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chica "De acuerdo."
                hide amigo with dissolve
                "Regresamos con Luna."
                "Volvemos con Luna Sebastián parece más calmado sabiendo que cuenta conmigo para lo que sea y me siento mejor al darle mi apoyo que no pude darle antes."
                show amigo at move_in_left
                amigo "Volvimos."
                show amiga at move_in_right
                amiga "¿Todo bien?"
                chica "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chica "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia y sobre todo respetar decisiones."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Respetar las decisiones de otros es también una forma de apoyo. La vida nos enseña que, a veces, acompañar sin presionar es el mejor camino."
                misterioso "Recuerda que no siempre se trata de tomar decisiones por los demás, sino de estar ahí cuando nos necesiten."
                stop music 

                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return
                
                



        # Ruta C        
        label cansada:
            $ cansancio = True
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction() 
            scene cuartonoche with slideright
            chica "Bueno, un libro no hará daño..."
            "Sé que debería dormir para estar en mi mejor forma mañana... pero necesito una distracción. Solo un capítulo más."
            scene negro with dissolve
            "Lees un buen libro y pierdes la noción del tiempo."
            scene cuarto with slideleft
            "Despiertas con dificultad, sintiendo el peso de tus malas decisiones."
            scene wc with slideleft
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chica_normal with dissolve
            "El cansancio es evidente. Me miro al espejo y no reconozco al reflejo. ¿Valió la pena el desvelo? Quizás esté escapando de algo..."
            chica "Creo que me emocioné un poco…"
            "*Suspiro*"
            chica "Bueno, diría que demasiado... Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina with slideleft
            "Desayunas lo primero que hallaste y vas corriendo para tomar el transporte."
            scene negro with dissolve
            #stop music
            "¿Ahora qué debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren6

                "Tomar Autobús":
                    jump Autobus6  

        label Tren6:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
            jump ChicaC

        label Autobus6:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "Bueno, aunque es más lento, es el más económico."
            jump ChicaC   

    
        #ChicaC
        label ChicaC:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "Aquí vamos de nuevo."
            scene salon with slideleft
            "Luna parece decepcionada y Sebastián se muestra pensativo."
            amiga "Bueno... supongo que estudiaré sola entonces."
            # Reflexión Interna 
            "La decepción en los ojos de Luna es evidente, y aunque Sebastián intenta animarme, siento una carga en mis hombros que no se va."
            "¿Por qué siempre evito enfrentar estos momentos de frente? Quizás temo a lo que pueda descubrir de mí misma."
            "Quería que fuéramos juntos… pero no puedo estar en dos lugares a la vez."
            "Veo cómo Luna se sienta en su lugar, intentando concentrarse en sus apuntes, pero su mirada se desvía hacia mí."
            "Hay un silencio incómodo que parece durar una eternidad."
            chica "Me siento mal por ella."
            show amigo at center with dissolve
            amigo "No te preocupes por Luna, luego hay que convencerla de que venga con nosotros."
            chica "Sí, tienes razón... aunque algo en su mirada me dice que ya la decepcioné."
            "Sebastián se queda en silencio por un momento."
            amigo "¿Dormiste bien? Te ves cansada."
            chica "No te preocupes, estaré bien... o al menos eso espero."
            hide amigo with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase. Vamos a repasar lo que vimos la clase anterior."
            hide maestro with dissolve
            "Durante la clase, el cansancio comienza a hacer mella en ti."
            "Te cuesta concentrarte, y cada palabra del profesor se siente como un peso más sobre tus hombros."
            # Agregar Minijuego 2
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # chica "Me fue muy bien."
            # $ Minijuego = "Perdió"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 10
                # $ renpy.restart_interaction()
            chica "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            amigo "¿Segura que estás bien?"
            chica "Sí, estoy bien... sólo tuve dificultades, pero la próxima vez lo haré mejor, lo prometo."
            amigo "Si tú lo dices, solo recuerda que tenemos otra clase, dormilona."
            chica "Lo sé, Sebastián... pero tú también estabas en las mismas."
            "A pesar de sus palabras de ánimo, sabes que algo en ti está cambiando."
            "Te preguntas si realmente vale la pena seguir así."
            "Veo entrar a la maestra para dar inicio a la siguiente clase."
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            chica "Bueno, a empezar con la siguiente materia."
            "Aunque siga con sueño."
            hide maestra with dissolve
            # Minijuego 3 agregar 
            # $ Minijuego = "Gano"
            # if juego == "gana":
                # $ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                # show amigo at center with dissolve
                # amigo "Muy fácil."
                # chica "Es cierto."
            # $ Minijuego = "Perdió"
            # elif juego == "pierde":
                # $ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                # $ estres += 10
                # $ renpy.restart_interaction()
            show amigo at center with dissolve
            amigo "Bueno, esta estuvo fácil, ¿a que sí, dormilona?"
            chica "Sí, y deja de decirme dormilona."
            amigo "Tranquila, está bien."
            "Sebastián y tú están en clase, pero tu mente está en otro lugar."
            "Cada palabra que Sebastián menciona sobre Luna hace que te sientas más culpable."
            amigo "Siempre he sido cercano a Luna, pero últimamente no hemos pasado tiempo juntos como antes."
            chica "Podemos quedarnos esta vez, intentar recuperarlo."
            amigo "Sí, aunque hoy hay un festival... Tal vez podamos convencerla de que venga con nosotros."
            chica "Haré lo que pueda..."
            hide amigo with dissolve
            # Reflexión Interna 
            "Sé que tengo la oportunidad de invitarla, y tal vez sea lo correcto... Pero, ¿y si prefiero quedarme en mi zona de confort?"
            "¿Estoy evitando el esfuerzo emocional por miedo, o realmente no deseo involucrarme?"
            $ estres = 30 # Eliminar después de poner minijuego
            $ renpy.restart_interaction()
            menu:
                "Convencerla de que se una.":
                    jump ConvencerlaC_Chica

                "No hacer nada.":
                    jump NadaLC_Chica
                    
            
            
            
            #Chica C
            label ConvencerlaC_Chica:
                "Estás muy cansada y estresada, pero aun así intentas convencer a Luna."
                chica "¿Luna, Sebastián y yo vamos a ir a un festival, quieres unirte?"
                show amiga at center with dissolve
                amiga "Deberías mejor descansar por hoy, pero diviértanse. Yo prefiero quedarme a repasar."
                chica "Gracias por la preocupación, te veré mañana."
                amiga "Hasta mañana."
                hide amiga with dissolve
                "Te sientes mal por no pasar tiempo con Luna y recordaste la preparatoria, donde no convivías con prácticamente nadie."
                "Veo mi vida en la prepa reflejada en ella, pues no convivía mucho con mis compañeros."
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 
                #stop music
                # Continuar Historia
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "En serio, te ves muy cansada, pero gracias por acompañarme."
                chica "Estaré bien, no te preocupes."
                #play music "Sebastian.mp3"
                amigo "Me siento como un idiota ahora mismo."
                chica "¿Te preocupa algo?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y, aun así, pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que algo está mal, así que decido preguntarle."
                chica "¿Todo bien, Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna para mí es mi mejor amiga, pues en mi hogar mi padre siempre está decepcionado, tanto por mi conducta como por mi desempeño en la escuela."
                amigo "Mi madre nunca la conocí, pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna. Me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Intento consolar a Sebastián, pues su vida es muy dura."
                # Reflexión Interna
                "Escuchar su historia me recuerda la soledad que yo misma siento en casa, con padres que apenas veo. A veces, el vacío es más profundo cuando parece que todo está bien."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias, [nombre], lo necesitaba. Sé que la escuela es importante, pero a veces no puedes reunir fuerzas para continuar."
                chica "Sé lo que se siente, no poder agarrar fuerzas para seguir, pero no debemos rendirnos."
                hide amigo_triste with dissolve
                #stop music
                show amigo at center with dissolve
                amigo "Mejor regresemos y nos vemos mañana."
                chica "Muy bien."
                amigo "Gracias por acompañarme. Me recuerdas mucho a ella, pero por ahora ve a descansar."
                chica "¿En serio? Espero llevarme muy bien con ella entonces..."
                chica "Y no te preocupes, hoy descansaré."
                hide amigo with dissolve
                scene negro with dissolve
                "Sientes un dolor profundo y no tienes ánimos de continuar, pero la vida sigue adelante."
                "Regresas a casa pensando en todo lo que pasó hoy."
                play sound "mas.mp3"
                $ estres += 20
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 

                # Continuar Reflexión
                scene cuartonoche with slideright
                # Reflexión Interna
                "Hoy me he dado cuenta de que el cansancio físico no es lo único que me afecta. El peso de mis decisiones se siente cada vez más, y no sé si estoy lista para enfrentarlo."
                "Te sientes muy cansada y te acuestas a dormir, pero no puedes dejar de pensar en Luna."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Cada paso que das tiene un impacto, [nombre]. Recuerda que no puedes cambiarlo todo en un solo día."
                misterioso "El cansancio y la frustración pueden ser tus maestros. Aprende a escuchar lo que te dicen, en lugar de evitarlos."
                misterioso "La próxima vez que tengas una decisión en tus manos, pregúntate: ¿Es esto realmente lo que quiero, o estoy evitando enfrentarme a algo más profundo?"
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confusa, pero sigues pensando en Luna."
                chica "¿Evitar algo más profundo? ¿Lo que realmente quiero?"
                
                if estres >= 50:
                    scene chica_estres with dissolve
                    $ actualizar_estado_sprite()
                    chica "Me llevo bien con Sebastián, pero ¿por qué me siento así?"
                    chica "Pensar tanto en Luna y la situación de Sebastián hace que no pueda concentrarme."
                    chica "Vamos, tú puedes con esto."
                else:
                    scene chica_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chica "Me llevo bien con Sebastián, pero ¿por qué me siento así?"
                    chica "Pensar tanto en Luna y la situación de Sebastián hace que no pueda concentrarme."
                    chica "Vamos, tú puedes con esto."

                scene cocina with slideleft
                "Con mucho esfuerzo, te preparas algo para comer."
                #stop music
                scene negro with dissolve
                "¿Qué transporte debo tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren15

                    "Tomar Autobús":
                        jump Autobus15 
        label Tren15:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Llegare temprano aunque no se que hacer..."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "así tengo mas tiempo de pensar que hare... "
             
            jump Dia_chicaC
        
        label Autobus15:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero quiero primero estar bien antes de verlos..."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Así tengo tiempo de pensar muy bien todo..."
             
            jump Dia_chicaC








        label Dia_chicaC:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "Vamos anímate debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon with slideleft
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chica "Hola Sebastián."
            show amigo_preocupado at center with vpunch
            amigo "¡¡wow!! ¿estas bien [nombre]?"
            amigo "Te veo un poco mal."
            chica "Estoy bien no te preocupes."
            amigo "Oye deberías sacarlo todo yo lo hice ayer y me sentí mejor así que puedes decirme que pasa."
            chica "Yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chica "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado with dissolve
            show amigo at center with dissolve
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chica "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chica "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chica "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo un poco mal para que no se preocupe."
            chica "Tienes razón gracias."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra with dissolve

            # agregra cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con luna mientras los observo."
            "Espero que todo esté bien entre ellos."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno jóvenes comencemos la siguiente clase."
            hide maestra with dissolve
            "Sebastián Regresa a su asiento, después le preguntare como le fue."


            # agregra quinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chica "¿Cómo te fue con ella?"
            show amigo at center with dissolve
            amigo "Aceptó así que nos veremos con ella este fin."
            chica "Me alegra oír eso."   
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro with dissolve
            # agregra sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Sin problemas."
                #amigo "Pues claro."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo with dissolve

            "Termina la clase dando finalizado este día de hoy."    
            chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo at center with dissolve
            amigo "Así es y recuerda tranquila vale."
            chica "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chica "Adiós Luna."
            show amiga at center with dissolve
            amiga "Adiós [nombre] te veré allá entonces con Sebastián."
            chica "Te veo ahí."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Me retiro a mi casa a descansar esperando el fin de semana." 

            "Pasa el tiempo llegando el fin de semana."

            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Afrontar bien las consecuencias sigue así."
            "Te sientes confusa."
            "Aun no entiendo el propósito de esa sombra."
            "No importa, hoy la pasaré bien con mis amigos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chica "Hola Sebastián."
            show amigo at move_in_left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros"
            amigo "Vamos amiga mucho ánimo ¿vale?"
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chica "¿Mejor?"
            amigo "Mucho mejor."
            " Luna aparece con un material para estudiar."
            show amiga at move_in_right
            amiga "Hola amigos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga with dissolve
            hide amigo with dissolve
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chica "¿Qué pasa? "
            chica "¿Te sientes bien?"
            show amigo_triste at center with dissolve
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            chica " Deberías decirle lo que sientes por ella."
            amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
            "La soledad no es una buena opción." 
            #Reflexión Interna
            "Sé que sería lo correcto animarlo a sincerarse con Luna, pero ¿realmente es lo que necesita ahora? A veces, la prudencia es más importante que la acción inmediata."
            
            hide amigo_triste with dissolve

            menu:
                "Darle apoyo para que se confiese.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaC1

                "Respetar sus sentimientos de preocupación.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaC2





                    
            label final_chicaC1:
                chica "Mira, la soledad no es buena y no es excusa puedes pasar más tiempo con ella estudiando juntos conociéndote más."
                chica "Es difícil Estudiar cuando uno está estresado y Solo, así que siempre es bueno tener a alguien en quien apoyarse."
                show amigo at center with dissolve
                amigo "¿Estás segura de esto?"
                chica "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo with dissolve
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at move_in_left
                amigo "Luna…"
                show amiga at move_in_right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga with dissolve
                show amiga_triste at right with dissolve

                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo with dissolve
                hide amiga_triste with dissolve
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at move_in_left
                show amiga at move_in_right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Ayudar a otros a expresar sus sentimientos requiere de gran sensibilidad."
                misterioso "No olvides, [nombre], que las relaciones se fortalecen cuando actuamos con sinceridad y cuidado."
                misterioso "Recuerda, cada palabra y cada gesto tienen peso. Las conexiones pueden ser una fortaleza o un desafío, dependiendo de cómo las manejemos."
                stop music

                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label final_chicaC2:
                chica "Si sientes eso en verdad te apoyo sea cual sea la decisión que tomes Sebastián."
                show amigo at center with dissolve
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chica "De acuerdo."
                hide amigo with dissolve
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo para lo que sea."
                show amigo at move_in_left
                amigo "Volvimos."
                show amiga at move_in_right
                amiga "¿Todo bien?"
                chica "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chica "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has mostrado respeto y comprensión, permitiendo que los sentimientos evolucionen con el tiempo."
                misterioso "A veces, ser paciente y escuchar es la mayor ayuda que puedes ofrecer."
                misterioso "No permitas que el miedo o las dudas te frenen, pero respeta el ritmo de las personas. Cada silencio tiene su valor, y cada palabra su lugar."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            #Chica Egoista
            label NadaLC_Chica:
                "Decides no hacer nada, el cansancio y la falta de energía te paralizan."
                chica "Lo siento, Sebastián... simplemente no puedo."
                show amigo_triste at center with dissolve
                amigo "No te preocupes, vámonos entonces."
                hide amigo_triste with dissolve
                # Reflexión Interna
                "Ver a Luna sola… Me hace ver mi propio reflejo. Tal vez esté proyectando mis propios miedos y fracasos en ella, pero ahora mismo no tengo la fuerza para actuar."
                "Algo en tu interior grita que actúes, pero el peso de tus malas decisiones te hunde más."
                play sound "mas.mp3"
                $ estres += 25
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 
                    #stop music
                # Continuar Historia
                scene escuela with slideleft
                show amigo at center with dissolve
                amigo "Te ves muy cansada... pero gracias por acompañarme."
                amigo "Aunque, la verdad, deberíamos haberla invitado."
                chica "Estaré bien... lo siento, Sebastián, de verdad lo siento."
                amigo "No te castigues tanto, debí ser yo quien la convenciera, no tú."
                "Mientras caminan por el festival, notas que Sebastián está más callado de lo habitual. Decides preguntarle qué le sucede."
                chica "¿Qué pasa, Sebastián?"
                #play music "Sebastian.mp3"
                "Sebastián se detiene y te mira con tristeza."
                hide amigo with dissolve
                show amigo_triste at center with dissolve
                amigo "Luna es mi mejor amiga."
                amigo "Siempre ha estado ahí para mí, incluso cuando mi padre estaba decepcionado conmigo o cuando no tenía a nadie más."
                amigo "Ella me daba fuerzas... y ahora siento que la estoy perdiendo."
                "La confesión de Sebastián te golpea como un balde de agua fría."
                "Te das cuenta de que tus acciones no solo te han afectado a ti, sino también a las personas que te rodean."
                hide amigo_triste with dissolve
                show amigo_preocupado at center with vpunch
                chica "Sebastián... no estás solo. Lo que sea que necesites, estoy aquí."
                "Lo abrazas con fuerza, sintiendo la presión de las expectativas y la culpa arremolinándose dentro de ti."
                hide amigo_preocupado with dissolve
                show amigo_triste at center with dissolve
                amigo "Gracias, [nombre]. A veces es difícil continuar, pero al menos sé que te tengo a ti."
                hide amigo_triste with dissolve
                #stop music
                scene negro with dissolve
                "La culpa te golpea más fuerte, pero resistes para que no te vean decaer."
                chica "Debo resistir, por mis amigos..."
                "Regresas a casa intentando despejar tu mente."
                play sound "mas.mp3"
                $ estres += 25
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 
                # Continuar Reflexión
                scene cuartonoche with slideright
                "Te sientes más agotada que nunca."
                "La culpa de no haber hecho más por Luna y Sebastián te pesa enormemente."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "¿Realmente crees que has tomado las mejores decisiones, [nombre]?"
                misterioso "Las elecciones que hacemos llevan consigo consecuencias, y escapar de ellas solo te llevará a enfrentarte a un mayor peso más adelante."
                misterioso "Pregúntate: ¿Estás evitando enfrentar tus miedos, o simplemente estás huyendo del dolor?"
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas con el corazón acelerado y el estrés al límite."
                "Las palabras de la voz resuenan en tu mente."
                chica "No puedo seguir así..."
                scene chica_estres with dissolve
                chica "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                chica "Pensar tanto en Luna y la situación de Sebastián hace que no pueda concentrarme."
                chica "Vamos, tú puedes con esto."
                scene cocina with slideleft
                "Apenas logras prepararte algo para comer."
                #stop music
                scene negro with dissolve
                "¿Qué transporte debería tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren17

                    "Tomar Autobús":
                        jump Autobus17  

        label Tren17:
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Llegaré temprano, aunque no sé qué hacer..."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así tengo más tiempo de pensar qué haré..."
            jump Dia_chicaCC

        label Autobus17:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero quiero primero estar bien antes de verlos..."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Así tengo tiempo de pensar muy bien todo..."
            jump Dia_chicaCC








        label Dia_chicaCC:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "No es hora de pensar en eso, debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon with slideleft
            "Miro que Sebastián aún no llega y veo a Luna estudiando. No quisiera molestarla después de que no hablé con ella ayer."
            "Después de un tiempo, veo llegar a Sebastián."
            chica "Hola, Sebastián."
            show amigo_preocupado at center with vpunch
            amigo "¡¡Wow!! ¿Estás bien, [nombre]?"
            amigo "Te veo peor que ayer."
            chica "Estoy bien, no te preocupes."
            amigo "¿Segura?"
            chica "Sí."
            amigo "Oye, deberías sacarlo todo. Yo lo hice ayer y me sentí mejor, así que puedes decirme qué pasa."
            chica "Yo también tuve problemas en la preparatoria, solo que nunca vi a alguien como mi amigo hasta ahora."
            chica "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado with dissolve
            show amigo at center with dissolve
            amigo "Ya veo, no te preocupes por nosotros. Sé que he estado saliendo y, pues, no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los dos a gusto."
            chica "Entiendo, pero aun así debí apoyarte. Sé que ella es importante para ti."
            amigo "No solo eso, sin ella mi vida no tendría sentido. Cuando estoy con ella, me siento vivo."
            chica "Tengo una idea: ¿qué tal si la invitamos un fin de semana? Nos reunimos y hablan ustedes."
            amigo "No suena mal, puesto que le gustaría pasar un rato y, pues, estudiar como hacíamos antes."
            chica "Muy bien, entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo muy mal. No quiero que se preocupe."
            chica "Tienes razón. Gracias."
            hide amigo with dissolve
            "Comienza la clase."
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos."
            amigo "Anímate, todo saldrá bien."
            hide maestra with dissolve

            # Agregar cuarto minijuego
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Estuvo bien."
                #amigo "vez sí se pudo."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
            #if estres >= 100:
                #call game_over
            #else:    
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Esto es muy difícil."
                #amigo "Si."
                #hide amigo with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con Luna mientras los observo."
            "Espero que todo esté bien entre ellos. No quiero arruinar esto y estar sola otra vez."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve
            "Sebastián regresa a su asiento. Después le preguntaré cómo le fue."

            # Agregar quinto minijuego
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Estuvo bien."
                #amigo "vez sí se pudo."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Esto es muy difícil."
                #amigo "Muy cierto."
                #hide amigo with dissolve

            show maestra at center with dissolve
            maestra "Bueno, clase, estudien porque la siguiente semana será de exámenes. Estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra with dissolve
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chica "¿Cómo te fue con ella?"
            show amigo at center with dissolve
            amigo "Aceptó, así que nos veremos con ella este fin."
            chica "Me alegra oír eso."
            amigo "También noto que te ves mal. Intenta descansar para que este fin de semana sea agradable."
            chica "Lo intentaré..."
            amigo "No te esfuerces mucho."
            hide amigo with dissolve
            "Veo entrar al maestro Carlos dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase. Hoy veremos un tema nuevo. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                #$ actualizar_estado_sprite()
                # $ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "fue facil."
                #amigo "ves que sí."
                #hide amigo with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amigo at center with dissolve
                #chica "Esto es muy difícil."
                #amigo "Tienes razón, pero ya termino.""
                #hide amigo with dissolve

            "Termina la clase, dando finalizado este día."
            chica "Bueno, nos reuniremos en un parque para pasar tiempo juntos."
            show amigo at center with dissolve
            amigo "Así es. Y recuerda: tranquila, ¿vale?"
            chica "Muy bien, entonces nos vemos, Sebastián."
            amigo "Cuídate, [nombre]."
            hide amigo with dissolve
            "Tomo mis cosas y me despido de Luna."
            chica "Adiós, Luna."
            "Observo su preocupación en mi cara, pero aun así decido sonreírle."
            show amiga at center with dissolve
            amiga "Adiós, [nombre]. Te veré allá entonces con Sebastián."
            chica "Te veo ahí."
            hide amiga with dissolve
            #stop music
            scene negro with dissolve
            "Me retiro a mi casa a descansar, esperando el fin de semana." 
            "Espero que todo salga bien, la verdad."

            "Pasa el tiempo llegando el fin de semana."
            play music "parque.mp3"
            scene parque with slideleft
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Recuerda, tus decisiones te han llevado hasta aquí."
            "Te sientes confusa y abrumada."
            "Vaya, esa voz... ¿será mi conciencia?"
            "En fin, hoy solo me divertiré con mis amigos."
            scene parque with slideleft
            "Te sientas a esperar a Luna y Sebastián, sintiendo el peso de lo que está por venir."
            "Sebastián llega primero, y te saluda con su habitual energía."
            chica "Hola Sebastián."
            show amigo at move_in_left
            amigo "¡Hola [nombre]! Vamos, ánimo, amiga."
            "Intentas poner tu mejor cara, pero el dolor de cabeza te traiciona."
            amigo "Tranquila, no te esfuerces tanto."
            amigo "Todo saldrá bien."
            "Agachas la mirada, apenas esbozando una sonrisa."
            "¿Será este el camino del que hablaba esa sombra?"
            "Sebastián, preocupado, me abraza."
            amigo "Estamos contigo. No estás sola, ¿vale?"
            chica "Eso espero..."
            "Luna llega y nos observa con preocupación."
            show amiga_preocupada at right with vpunch
            amiga "¿Están bien los dos?"
            "Sebastián le da un pulgar arriba, ocultando la verdad de tu estado."
            amigo "Solo le duele la cabeza a [nombre], no es nada grave."
            "Me susurra al oído."
            amigo "Te apoyo en lo que decidas."
            chica "Gracias, Sebastián..."
            "Te das cuenta de que, aunque ellos se preocupan por ti, tú no has hecho nada por ellos."
            #Reflexión Interna
            "Mirando a mis amigos, siento una mezcla de culpa y alivio. Son lo mejor que tengo aquí, pero no estoy segura de si podré cambiar. ¿Debería darme otra oportunidad, o es mejor dejar todo atrás?"
            hide amiga_preocupada with dissolve
            hide amigo with dissolve
            

            menu:
                "Hacer un último esfuerzo":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaCC1

                "Retirarse de la Universidad.":
                    play sound "menos.mp3"
                    $ estres -= 10
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaCC2





                    
            label final_chicaCC1:
                "Agarras el mayor coraje para enmendar tus errores."
                chica "Amigos…"
                chica "Quiero empezar de nuevo, Ustedes son lo mejor que me ha pasado."
                chica "Nunca pude tener amigos en la preparatoria…"
                chica "Y ahora que los tengo a ustedes."
                "Agachas mas la cabeza y aprietas los puños fuertemente sintiendo un peso enorme"
                chica "He sido una mala amiga y ustedes han sido buenos conmigo."
                "Ambos me abrazan fuertemente"
                chica "Quiero pasarla bien con ustedes y no volverlos a decepcionar."
                show amiga_preocupada at left with vpunch
                amiga "Tranquila no nos has decepcionado y me alegra que me hayas dicho cómo te sientes."
                hide amiga_preocupada
                show amiga at move_in_left
                amiga "Gracias Sebastián por estar al pendiente de ella como siempre estuviste de mi"
                show amigo at move_in_right
                amigo "Una amistad grande jamás abandona a sus amigos en las buenas o en las malas."
                chica "Gracias amigos."
                "Sientes un peso menos, pero la culpa no se irá fácilmente."
                "Me abrazan más fuerte y correspondiendo regresando un abrazo más fuerte."
                amiga "Toda ira bien ya lo veras."
                amigo " si te apoyaremos en lo que sea."
                hide amigo with dissolve
                hide amiga with dissolve
                "Los 3 nos quedamos estudiando, aunque no me preocupaba el examen, pero si estar con mis amigos y no volver a decepcionarlos."
                "Las decisiones que tome tardaran en sanar pues lo que hice no fue bueno ahora se a que se refería esa sombra "
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Afrontar las consecuencias y enmendar los errores es un acto de valentía, [nombre]."
                misterioso "Reconocer nuestras fallas y buscar el apoyo de quienes nos importan es el primer paso para un verdadero cambio."
                misterioso "Las amistades son una fuente de fortaleza, y los errores nos hacen más sabios. Nunca olvides que siempre puedes contar con otros para ayudarte en los momentos más oscuros."
                stop music 

                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


            

            label final_chicaCC2:
                stop music
                #play music "Sebastian.mp3"
                "Con lágrimas y un fuerte dolor en el pecho, decides decirles que te vas de la universidad."
                " Sebastián y Luna me miran preocupados, la sorpresa se refleja en sus rostros."
                show amiga_preocupada at left with vpunch
                show amigo_preocupado at right with vpunch
                amigo "Amiga, no tires la toalla tan rápido."
                amigo "Todos pasamos por momentos difíciles, pero siempre hay una salida."
                amiga "[nombre], no te rindas aún."
                amiga "Tienes un futuro por delante y nosotros estamos aquí para ayudarte..."
                "Me agarro el pecho, incapaz de levantar la mirada."
                "Las palabras se me escapan, el peso de la situación me aplasta."
                "La cabeza me pesa, el estómago se revuelve, el pecho me duele."
                "Siento que las paredes se cierran y las voces en mi cabeza se vuelven ensordecedoras."
                " El pánico me paraliza."
                chica "No puedo… no puedo seguir…"
                hide amiga_preocupada with dissolve
                hide amigo_preocupado with dissolve
                show amiga_triste at left with dissolve
                show amigo_triste at right with dissolve
                "Luna y Sebastián, con expresiones tristes, se acercan y me abrazan, intentando transmitirme fuerzas."
                amigo "Respetamos tu decisión, pero por favor, regresa pronto." 
                amigo "Sabes que te estaremos esperando."
                amiga "Te extrañaremos mucho, aunque no convivimos tanto, aprecio el tiempo que pasamos juntos."
                amiga "Prométeme que cuidarás de ti y que regresarás."
                amigo " Y que no estamos enojados ni decepcionados contigo."
                amigo "Todos tenemos momentos así."
                "Con un gran esfuerzo, apenas logró responderles."
                chica "Lo prometo… haré lo mejor que pueda."
                "Me sueltan y, con una sonrisa llena de esfuerzo, me despido de ellos."
                hide amiga_triste with dissolve
                hide amigo_triste with dissolve
                show amiga at move_in_left
                show amigo at move_in_right
                "Ambos me devuelven la sonrisa, aunque se nota la tristeza en sus ojos."               
                "Sebastián y Luna" "Adios [nombre] cuidate mucho."
                hide amigo with dissolve
                hide amiga with dissolve
                "Me alejo de ellos, regresando sola a mi casa, sintiendo el vacío en cada paso."
                #stop music
                scene cuarto with slideleft
                play music "latidos.mp3"
                "Te acuestas en la cama, reflexionando sobre lo sucedido."
                chica "No pude con la presión."
                chica "Este peso es insoportable, pero no puedo huir para siempre."
                chica "Esta ansiedad es horrible."
                chica "Volveré…" 
                "Luna, Sebastián… les prometo volver."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, el peso de nuestras decisiones nos lleva a un punto de ruptura. No es una señal de debilidad, sino una oportunidad para aprender."
                misterioso "Rendirse puede parecer una derrota, pero es mejor buscar apoyo que enfrentar todo solo."
                misterioso "Recuerda que siempre puedes volver a intentarlo. Las decisiones difíciles son inevitables, pero nunca olvides que hay personas dispuestas a ayudarte, y la puerta siempre está abierta para regresar."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return


        #Decisión Luna
        label estudiar2:
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction() 
            show amigo at center with dissolve
            amigo "Como gustes."
            hide amigo with dissolve
            "Te quedaste estudiando con Luna. Fue estresante, pero al menos aprendiste."    
            show amiga at center with dissolve
            amiga "Gracias por quedarte."
            hide amiga with dissolve
            scene negro with dissolve
            "Regreso a mi casa algo cansada."
            #stop music
            #play music "cancioncuarto.mp3"
            scene cuartonoche with slideright
            "No fue tan mal para ser mi primer día."
            "¿Debería dormirme ya o leer un libro?"
            
            menu:
                "Dormir.":
                    jump descansada2

                "Jugar videojuegos.":
                    jump cansada2     

        label descansada2:
            play sound "menos.mp3"
            $ estres -= 5
            $ renpy.restart_interaction() 
            scene cuartonoche with slideright
            chica "Bueno, lo mejor será descansar para mañana y tener energía."
            scene negro with dissolve
            "Te acuestas a dormir temprano, recuperando energía para el siguiente día."
            scene cuarto with slideleft
            "Te despiertas con energía y descansada."
            scene wc with slideleft
            "Te sientes con mucha energía. ¿Qué pasará hoy?"   
            scene chica_normal with dissolve
            chica "¡Ahhh! Qué bien me siento."    
            chica "Hora de ir a la universidad."    
            scene cocina with slideleft
            "Desayunas lo primero que encontraste y vas corriendo para tomar el transporte." 
            scene negro with dissolve
            #stop music
            "¿Ahora qué debería tomar?"

            menu:
                "Tomar Tren":
                    jump Tren7

                "Tomar Autobús":
                    jump Autobus7  

        label Tren7:
            if transporte == "tren":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen  
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
                
            jump ChicaB

        label Autobus7:
            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento, es el más económico."
                
            jump ChicaB 



        #Ruta B
        label ChicaB:
            #play music "salonclase.mp3"
            scene escuela with slideleft
            "Aquí vamos de nuevo."
            scene salon with slideleft
            show amiga at center with dissolve
            amiga "¿Lista para continuar?"    
            chica "Claro que sí."
            amiga "Te ves muy concentrada. Esto va a ser muy fácil."
            chica "Sí, gracias por ayudarme a practicar."
            hide amiga with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase. Vamos a repasar lo que vimos la clase anterior."
            hide maestro with dissolve
            chica "Estoy preparada."
            #Agregar Minijuego 2
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
            chica "Eso fue fácil. Muchas gracias, Luna."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ renpy.restart_interaction()
                #chica "Esta clase fue estresante, pero logré salir adelante."
            show amiga at center with dissolve
            amiga "Sabes, estamos para apoyarnos."
            amiga "Estuviste excelente, [nombre]."
            chica "Todo gracias a ti, Luna, por ayudarme a practicar."
            amiga "Un placer. Es mejor para mí practicar con una amiga."
            hide amiga with dissolve
            "Quién sabe cómo me habría ido si no hubiera dormido temprano."
            "Oh, aquí viene la nueva maestra."
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            chica "Bueno, a empezar con la siguiente materia."
            hide maestra with dissolve
            #Minijuego 3 agregar 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
            show amiga at center with dissolve
            amiga "Bueno, bueno. Explica muy bien la maestra."
            chica "Sí, tienes razón."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ renpy.restart_interaction()
                #chica "Estuvo complicado."
            amiga "Sigo preocupada por Sebastián. Seguro tuvo problemas en la anterior."
            chica "Tienes razón. Ahora hay que convencerlo de que practique con nosotras."
            amiga "Buena suerte con eso."
            hide amiga with dissolve
            #Reflexión Interna
            "Sebastián ha estado algo distante últimamente... Siento que debería acercarme más y apoyarlo, pero me pregunto si estoy siendo demasiado insistente."
            "¿Debería tomar la iniciativa e intentar convencerlo de unirse, o simplemente respetar su espacio?"
            $ estres = 5 #Eliminar despues de poner minijuego
            $ renpy.restart_interaction()

            menu:
                "convencerlo de que se te una.":
                    jump ConvencerB_Chica

                "No hacer nada":
                    jump NadaB_Chica
            
            
            
            
            #Chica B
            label ConvencerB_Chica:
                chica "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo at center with dissolve
                amigo "Pero habrá un festival…"
                chica "Vamos hazlo por mí y por Luna."
                amigo " Está bien, el festival puede esperar."
                chica "No te arrepentirás."
                hide amigo with dissolve
                play sound "mas.mp3"
                $ estres += 5
                $ renpy.restart_interaction()
                #Continuar guion 
                "Nos quedamos con luna parecía muy feliz."
                #Reflexión Interna
                "Convencer a Sebastián de estudiar con nosotras me hace sentir un poco más confiada. Tal vez, estar aquí para mis amigos también me ayude a mantenerme enfocada y recordar que no estoy sola en esta experiencia."
                show amiga at move_in_left
                amiga "Gracias por acompañarme amigos."
                show amigo at move_in_right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto, nos va a servir mucho." 
                hide amigo with dissolve
                hide amiga with dissolve
                "Pasa el tiempo y estudiamos un rato mas con Luna."
                "Observó cómo Sebastián se retira para ir al festival, pero decidió acompañar un rato más a Luna."
                show amiga at center with dissolve
                amiga "[nombre], ¿puedo decirte algo?"
                chica " Claro amiga."
                #stop music
                #play music "Luna.mp3
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chica "Sé cómo te sientes Luna y te comprendo."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Si, me alegra que seamos amigas, tenemos algo en común."
                #Reflexión Interna
                "Ver a Luna vulnerable me hace darme cuenta de que todos llevamos una carga, incluso cuando intentamos mantenerla oculta."
                "Es fácil olvidar que cada uno enfrenta sus propias batallas, y a veces el mejor apoyo es estar ahí, escuchar y ser alguien en quien pueden confiar."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chica "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga with dissolve
                play sound "menos.mp3"
                $ estres -= 5
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche with slideright
                "Te acuestas a dormir feliz por las amistades que has hecho."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Vas por buen camino, [nombre]. Estar ahí para los demás también ayuda a fortalecer tu propio sentido de propósito."
                misterioso "Recuerda que la universidad es un momento de desafíos, pero tener amigos para apoyarse mutuamente te hará más fuerte."
                misterioso "No subestimes el impacto positivo que puedes tener en la vida de los demás. Los pequeños gestos de apoyo pueden hacer una gran diferencia."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas confusa pero calmada a la vez."
                chica "¿Qué o quién era esa voz? "
                chica "¿Buen camino?"
                scene chica_normal with dissolve
                chica "Nunca pensé estar tan calmada desde lo de la preparatoria. "
                scene cocina with slideleft
                "Te preparas un Desayuno para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren22

                    "Tomar Autobus":
                        jump Autobus22  
        label Tren22:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción"  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump Dia_chicaB
        
        label Autobus22:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump Dia_chicaB








        label Dia_chicaB:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chica "Hoy espero volver a pasar tiempo con Luna y Sebastián."
            scene salon with slideleft
            chica "Hola amigos, ¿cómo están?"
            show amiga at move_in_right
            amiga "Hola, me siento mucho mejor, gracias. Espero que tú también, [nombre]."
            show amigo at move_in_left
            amigo "Bien también, ¿y tú cómo estás, [nombre]?"
            chica "Muy bien, ¿hoy vamos a quedarnos a repasar, verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Sí, será lo mejor."
            "Empieza la clase."
            chica "¿Hoy tendremos 3 clases, verdad?"
            amiga "Según el horario, sí."
            chica "Vale, gracias, Luna."
            hide amigo with dissolve
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra with dissolve
            #agregar cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "fue facil."
                #amiga "Eso es verdad."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más. "
                #hide amiga with dissolve
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."

            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDia_chicaB

                "Quedarse callada.":
                    $ Luna = "callarse"
                    jump cDia_chicaB

        label cDia_chicaB:
            if Luna == "preguntar":
                chica "Luna, ¿cómo has estado?"
                "Decido abrazarla por lo que pasó ayer."
                show amiga at move_in_right
                amiga "Me he sentido mejor, gracias por preguntar."
                show amigo at move_in_left
                amigo "¿Aún preocupada, Luna? Eres lista y puedes con todo."
                amiga "Gracias a ambos por el apoyo."
                amiga "Sin ustedes, no sé qué haría."
                hide amiga with dissolve
                hide amigo with dissolve

            elif Luna == "callarse":
                "Te quedas callada, pero te quedas cerca de ella."
                chica "No tengo palabras ahorita, pero tienes mi apoyo, Luna."
                show amiga at move_in_right
                amiga "Gracias, amiga. Lo aprecio mucho."  
                show amigo at move_in_left
                amigo "También estoy aquí y me quedaré contigo, Luna."
                amiga "Gracias a ambos, de verdad."
                hide amiga with dissolve
                hide amigo with dissolve

            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve
            #agregar cuinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Genial muy fácil."
                #amiga "Practicando todo se logra."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más [nombre]."
                #hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Bueno, clase, estudien porque la próxima semana será de exámenes. Estos definirán su futuro."
            maestra "Su otro profesor les ayudará a reforzar los temas."
            hide maestra with dissolve
            "Nos relajamos por un momento mientras inicia la siguiente clase."
            show amigo at move_in_left
            amigo "Vaya, un fin de semana y ya tenemos exámenes."
            show amiga at move_in_right
            amiga "Lo sé, pero esto ya es la universidad. Siempre hay momentos para divertirse, pero lo más recomendable sería estudiar."
            amigo "Bueno, ya lo veremos el fin de semana."
            chica "Apuesto que será divertido. Quizá podamos reunirnos para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chica "Entonces no se diga más. Nos veremos en el parque."
            hide amigo with dissolve
            hide amiga with dissolve

            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase. Hoy veremos un tema nuevo. Espero que estén preparados."
            hide maestro with dissolve
            #agregar sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                # $ estres -= 5
                # $ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Eso estuvo difícil."
                #amiga "No te rindas  [nombre]."
                #hide amiga  with dissolve
            "Termina la clase, finalizando el día de hoy."
            chica "Bueno, nos reuniremos en un parque para pasar tiempo los dos."
            show amiga at move_in_right
            amiga "Muy bien, los veré ahí."
            show amigo at move_in_left
            amigo "Igual, nos veremos allí."
            hide amiga with dissolve
            hide amigo with dissolve
            scene cuarto with slideleft
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            #stop music
            scene negro with dissolve
            "Es la primera vez que estoy muy relajada. Estudiar con amigos es mejor que sola, ya que aprendes más."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Recuerda, vas por buen camino."
            "Te sientes confusa pero calmada."
            chica "Buen camino ¿eh?"
            "Mejor me concentro en pasarla bien con mis amigos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chica "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chica "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chica "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            #Reflexión Interna
            "Este es el tipo de situación que temía enfrentar desde que entré a la universidad. No quiero perder a mis amigos, pero también quiero hacer las cosas bien para ambos."
            "Quizás eligiendo bien ahora, pueda evitar el tipo de soledad que experimenté en la preparatoria. Tal vez puedo ser la amiga que ambos necesitan."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaB1

                "Quedarse con Luna.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaB2

            label final_chicaB1:
                show amiga at move_in_right
                show amigo at move_in_left
                #Reflexión Interna
                "Saber que convencí a Sebastián de quedarse me da una sensación de logro. Me doy cuenta de que, en lugar de separarnos, esta experiencia nos está uniendo aún más."
                chica "Sebastián, podemos dejarlo para otro fin de semana."
                chica "Hoy hay que darle todo el apoyo a Luna."
                amigo "Tienes razón, es momento de saber cuándo hay que divertirse y cuándo hay que apoyar en momentos difíciles."
                amiga "Gracias por quedarte, Sebastián."
                amiga "Y a ti, [nombre], por ayudarme."
                chica "Quiero decirles que al principio no creí que haría buenos amigos."
                chica "El miedo a quedarme sola me aterraba, pero cuando los conocí, sentí más emoción, y es más divertido estudiar con amigos."
                "Sebastián y Luna me abrazan."
                amiga "Para eso están los amigos, [nombre]."
                amigo "Así es, estamos para apoyarnos en las buenas y en las malas."
                hide amigo with dissolve
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes amiga me alegra ayudar."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    hide amiga with dissolve


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tomaste una decisión valiente al acercarte a tus amigos, [nombre]."
                misterioso "A veces, apoyar a otros requiere que nos pongamos en su lugar y reconozcamos la importancia de estar juntos en los momentos difíciles."
                misterioso "Recuerda que la amistad genuina no solo aligera las cargas de otros, sino que también te fortalece a ti."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            label final_chicaB2:
                chica "Yo prefiero quedarme a estudiar un poco más."
                "No puedo dejar a Luna sola es mejor darle mi apoyo."
                show amigo at move_in_left
                amigo "Entiendo, bueno, no importa, los veré después."
                show amiga at move_in_right
                amiga "No tienes que irte ahora puedes quedarte."
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián me susurra."
                amigo "Cuida de ella, [nombre], ¿vale? Haz la diferencia por mí vale."
                "Lo miras directamente, haciendo un gesto de afirmación."
                hide amigo with dissolve
                hide amiga with dissolve
                "Sebastián se retira dejándonos solas."
                #Reflexión Interna
                "Aunque Sebastián se fue, sé que me quedé aquí por una razón importante. Estar aquí para Luna me hace sentir que, por una vez, puedo ser alguien en quien los demás confíen."
                chica "Tranquila, Luna, tienes mi apoyo."
                chica "Después de esto lo veremos y te ayudaré, ¿vale? Debemos permanecer juntos."
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes amiga me alegra ayudar."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chica "Gracias Luna."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga with dissolve
                "Ambas nos quedamos estudiando, pero debí convencerlo para que luna estuviera mejor."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, las elecciones que hacemos nos muestran lo que realmente valoramos."
                misterioso "Quedarte y apoyar a Luna fue un acto de empatía. Recuerda que tu presencia tiene un impacto importante en aquellos que valoran tu amistad."
                misterioso "La universidad es un viaje donde aprenderás a equilibrar tus decisiones, el apoyo mutuo será clave para sobrellevar los momentos difíciles."
                stop music 
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            #Chica B,B
            label NadaB_Chica:
                "Decides no hacer nada y seguir practicando con Luna, parece preocupada aún."
                chica "Lo siento, Luna."
                show amiga_preocupada at center with vpunch
                amiga "No pasa nada, [nombre]."
                hide amiga_preocupada with dissolve
                play sound "mas.mp3"
                $ estres += 10
                $ renpy.restart_interaction()  
                # Continuar guion 
                "Me quedo con Luna mientras observo cómo Sebastián se va al festival."
                # Reflexión Interna
                "Ver a Sebastián marcharse mientras me quedo con Luna me hace sentir una mezcla de alivio y culpa. Quiero ayudarla, pero ¿habrá sido suficiente? Tal vez dejé ir una oportunidad de unirnos más los tres."
                show amiga at center with dissolve
                amiga "Gracias por quedarte, [nombre]."
                chica "A ti, Luna, por ayudarme."                
                amiga "[nombre], ¿puedo decirte algo?"
                chica "Claro, amiga."
                #stop music
                #play music "Luna.mp3"
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "De verdad lo aprecio mucho, [nombre], y gracias por estar conmigo."
                chica "Sé cómo te sientes, Luna, y te comprendo."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Sí, me alegra que seamos amigas, tenemos algo en común."
                # Reflexión Interna
                "Ver a Luna luchar contra sus propias expectativas y la soledad me recuerda que todos tenemos cargas pesadas que no siempre mostramos."
                "Quizá, en lugar de preocuparme solo por cómo me ven mis amigos, debería centrarme en cómo puedo ser una mejor amiga para ellos."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chica "Nos vemos, Luna."
                amiga "Cuídate mucho, [nombre]."
                hide amiga with dissolve
                "Me siento mal porque sé que pude haber convencido a Sebastián."
                play sound "mas.mp3"
                $ estres += 10
                $ renpy.restart_interaction()
                if estres >= 50:
                    $ actualizar_estado_sprite() 
                #continuar
                scene cuartonoche with slideright
                chica "Pude haberlo convencido."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Las personas que confían en ti son un reflejo de lo que valoras, [nombre]."
                misterioso "Tener amigos es una oportunidad y una responsabilidad. Asegúrate de responder a esa confianza siendo honesto y solidario."
                misterioso "La duda y el miedo pueden evitar que actúes, pero reconocer tus propias emociones y las de los demás es el primer paso para acercarte y hacer una verdadera diferencia."
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas con un sentimiento de culpa."
                chica "Tranquila, solo fue un sueño."
                if estres >=50:
                    scene chica_estres
                    chica "Solo fue un sueño, hoy veré que Luna esté bien."
                else:
                    scene chica_normal with dissolve
                    chica "Solo fue un sueño, hoy veré que Luna esté bien."
                scene cocina with slideleft
                "Te preparas un Desayuno para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren23

                    "Tomar Autobus":
                        jump Autobus23 
        label Tren23:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción"  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump Dia_chicaBB
        
        label Autobus23:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump Dia_chicaBB








        label Dia_chicaBB:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chica "Sé que pude haber convencido a Sebastián."
            chica "No quisiera ser responsable de que Luna se distancie de él."
            scene salon with slideleft
            "Veo a Luna aún preocupada."
            chica "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga at center with dissolve
            amiga "No te preocupes, Sebastián siempre ha sido así desde la preparatoria, así que estoy acostumbrada."
            chica "Sé que es importante estudiar, pero también es bueno salir con personas."
            chica "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar sola."
            amiga "¿Estás bien, [nombre]?"
            chica "Sí, estoy bien, gracias."
            "Veo a Sebastián saludarnos de lejos, pero no se ve feliz."
            "Hoy tendremos tres clases." 
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra with dissolve
            
            # Agregar cuarto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Salió bien."
                #amiga "Sí."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Pudo ser peor."
                #amiga "Practica más."
                #hide amiga with dissolve
                
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDia_chicaBB

                "Quedarse callada.":
                    $ Luna = "callarse"
                    jump cDia_chicaBB

        label cDia_chicaBB:
            if Luna == "preguntar":
                chica "Luna, ¿estás bien?"
                show amiga at center with dissolve
                amiga "Solo estoy preocupada, no quiero que Sebastián piense que lo dejé atrás. Él sabe mi situación."
                "Decido abrazarla fuerte."      
                chica "Todo estará bien, ya lo verás."
                amiga "Eso espero."
                hide amiga with dissolve
            elif Luna == "callarse":  
                "Un incómodo silencio nos invadió a ambas."
                "Intentas calmar a Luna."
                chica "Cualquier cosa, aquí estaré, Luna."
                show amiga at center with dissolve
                amiga "Lo sé…"  
                hide amiga with dissolve
                "Decido darle ánimo a Luna."

            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve

            # Agregar quinto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Genial, muy fácil."
                #amiga "Me alegro por ti."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Vaya, sí tuve dificultades."
                #amiga "Deberías practicar más."
                #hide amiga with dissolve
            
            show maestra
            maestra "Bueno clase, estudien porque la siguiente semana será de exámenes. Estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para reforzar lo aprendido."
            hide maestra with dissolve 
            "Nos relajamos por un momento mientras iniciaba la siguiente clase."
            "Pero notas que Luna está cada vez más desanimada."
            chica "Ánimo, Luna. Este fin de semana hay que reunirnos con Sebastián en el parque para que te animes, ¿qué te parece?"
            show amiga at center with dissolve
            amiga "No es mala idea. Gracias por preocuparte tanto por mí, [nombre]."
            chica "Entonces este fin iremos al parque."
            amiga "Muy bien."
            hide amiga with dissolve

            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien clase, hoy veremos un tema nuevo. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga with dissolve
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 5
                #$ actualizar_estado_sprite()
                #$ renpy.restart_interaction()
                #show amiga at center with dissolve
                #chica "Eso estuvo difícil."
                #amiga "Tienes mi apoyo."
                #hide amiga with dissolve
            
            "Termina la clase, finalizando el día de hoy."
            chica "Bueno, nos reuniremos en un parque para pasar tiempo los tres."
            show amiga at move_in_right
            amiga "Muy bien, los veré ahí."
            hide amiga with dissolve
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chica "Hola Sebastián, Luna y yo nos vamos a reunir este fin de semana. ¿Te unes?"
            show amigo at center with dissolve
            amigo "Claro que sí. Los veré a las dos entonces."
            hide amigo with dissolve
            "Me despido de él, regresando a mi casa."
            #stop music
            scene cuarto with slideleft
            "Al final salió bien. Espero que todo salga bien este fin de semana."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso " Ella aún confía en ti."
            "Te sientes menos culpable ya que conviviste con ambos."
            chica "¿Seguiré Dormida?"
            "No creo mejor no pensar en ello y concentrarme para pasarla bien con ellos."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chica "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chica "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chica "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Gracias por organizar esto."
            chica "Te la debo Luna."
            "Veo a Luna más tranquila que antes."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            #Reflexión Interna
            "Me encuentro entre dos personas a las que quiero ayudar, pero me siento atrapada por mis propias inseguridades."
            "¿Cómo puedo ser una buena amiga si siempre temo que mis acciones no sean suficientes? Hoy quiero hacer lo correcto, aunque no sé qué significa exactamente."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaBB1

                "Quedarse con Luna.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaBB2

            label final_chicaBB1:
                show amiga at move_in_right
                show amigo at move_in_left
                chica "Sebastián esta vez quiero decirte que te quedes con nosotras, la vez del festival no sé por qué no pude hacerlo."
                amigo "No te preocupes se lo que se siente no poder decidir."
                chica "Aun así lo siento, Luna necesita apoyo así que esta vez acompáñanos."
                amigo " Está bien y no te preocupes es hora de pasar tiempo con ustedes esta vez amigas."
                amiga "Gracias a ambos por quedarse conmigo y más en estos tiempos."
                #Reflexión Interna
                "Convencer a Sebastián de quedarse me da esperanza. Quizá por fin estoy logrando unir a mis amigos y demostrarles que pueden contar conmigo cuando más lo necesitan."
                "Los junto a los 2 para estar más juntos."
                chica "La soledad nunca es buena."
                "Sebastián y Luna" "Estamos de acuerdo contigo."
                hide amigo with dissolve
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigas."
                    hide amiga with dissolve


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos, aunque me costó trabajo."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Elegir ser un punto de unión es una decisión de fortaleza, [nombre]."
                misterioso "Cuando decides apoyar a tus amigos, también te estás apoyando a ti misma, creando un vínculo que te ayudará a superar los momentos difíciles."
                misterioso "La verdadera amistad implica tomar decisiones que beneficien al grupo. Sigue adelante con confianza y la seguridad de que no estás solo."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            label final_chicaBB2:
                "Me vuelvo a quedar sin palabras para convencerle."
                chica "Yo prefiero quedarme a estudiar un poco más."
                "Luna necesita apoyo ahora más que nunca ahora que se su pasado."
                show amigo at move_in_left
                amigo "Entiendo bien, no importa las veré después…"
                show amiga at move_in_right
                amiga "Sebastián…"
                amigo "No te preocupes es como en los viejos tiempos diviértanse los 2."
                "Sebastián me susurra."
                amigo "Si de verdad eres mi amiga cuidaras bien de ella ¿Vale?"
                "Decido abrazarlo por la culpa que cargo y le susurro también."
                chica " Lo siento no te fallare te lo prometo."
                "Sebastián corresponde el abrazo y más calmado se retira."
                hide amigo with dissolve
                #Reflexión Interna
                "Sentí que debía quedarme con Luna. Aunque no convencí a Sebastián, espero poder compensarlo con mi dedicación. A veces, ser una buena amiga es estar ahí para quien más lo necesita en ese momento."
                chica "Lo siento Luna te he vuelto a fallar."
                amiga "No te preocupes, pero me ayudaras a convivir más con el."
                chica "Te lo prometo."
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica"Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chica "Gracias amiga."
                    chica "No te fallare."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga with dissolve
                "Ambas nos quedamos estudiando."
                "Debo cumplir con estas promesas."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Elegiste quedarte con alguien que confía en ti, lo cual muestra tu empatía y determinación."
                misterioso "No siempre puedes cumplir con todos, pero dar lo mejor en cada situación es una muestra de tu crecimiento."
                misterioso "Recuerda que la amistad es una oportunidad para aprender, mejorar y equilibrar decisiones. Sigue buscando ese equilibrio, y nunca dudes de tu capacidad de impactar positivamente en la vida de los demás."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return
                



        # ChicaA       
        label cansada2:
            $ cansancio = True
            play sound "mas.mp3"
            $ estres += 5
            $ renpy.restart_interaction() 
            scene cuartonoche with slideright
            chica "Bueno, un libro no hará daño."
            scene negro with dissolve
            "Lees un buen libro y pierdes la noción del tiempo."
            scene cuarto with slideleft
            "Despiertas con dificultad, sintiendo mucho sueño."
            scene wc with slideleft
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chica_normal with dissolve
            # Reflexión Interna
            "Miro mi reflejo, apenas reconociéndome. Esto no es lo que imaginé para mí en la universidad."
            "¿Realmente vale la pena seguir así? Sacrifico descanso y salud por distracciones que solo me dejan más agotada."
            chica "Creo que me emocioné demasiado."
            "Suspiro."
            chica "Bueno, diría que demasiado, pero no hay vuelta atrás. Es hora de ir a la universidad."
            scene cocina with slideleft
            "Desayunas lo primero que encontraste y vas corriendo para tomar el transporte." 
            scene negro with dissolve
            #stop music
            "¿Ahora qué debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren8

                "Tomar Autobús":
                    jump Autobus8  

        label Tren8:

            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno, lo mejor será tomar el tren ya que el autobús fue más lento."
            
            jump ChicaA

        label Autobus8:

            if transporte == "tren": 
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento, es el más económico."
            
            jump ChicaA  
       
       
       
        #Ruta A
        label ChicaA:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            "Aquí vamos de nuevo."
            scene salon with slideleft
            show amiga at center with dissolve
            amiga "¿Lista para continuar?"    
            chica "Claro que sí."
            amiga "¿Te sientes bien? Te ves un poco cansada."     
            chica "Sí, estoy bien, no te preocupes."       
            hide amiga with dissolve
            show maestro at center with dissolve
            maestro "Muy bien, clase, vamos a repasar lo que vimos la clase anterior."
            "Oh no, tengo mucho sueño."
            hide maestro with dissolve
            # Agregar Minijuego 2
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ renpy.restart_interaction()
                #chica "Eso fue fácil, muchas gracias, Luna."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 10
                #$ renpy.restart_interaction()
            chica "Rayos, casi no me pude concentrar bien, pero gracias a Luna no fue tan mal."
            # Reflexión Interna
            "El sueño me invade y, aunque intento enfocarme, la clase se vuelve una lucha constante contra mis propios párpados."
            "¿Por qué no me detuve a descansar? Esto no solo me afecta a mí, también a Luna, que está aquí apoyándome."           
            show amiga at center with dissolve
            amiga "Vamos, anímate. No estuvo tan mal."
            chica "Bueno, si tú lo dices. Esperemos que en la siguiente vaya mejor."
            amiga "Ya verás que sí."
            hide amiga with dissolve
            "Sigo un poco cansada, pero veo que entra la maestra."
            show maestra at center with dissolve
            maestra "Buenas tardes, alumnos. Espero que su inicio de semana haya sido agradable."
            chica "Bueno, a empezar con la siguiente materia."
            hide maestra with dissolve
            # Minijuego 3 agregar 
            #$ Minijuego = "Gano"
            #if juego == "gana":
                #$ minijuegos_ganados += 1
                #play sound "menos.mp3"
                #$ estres -= 5
                #$ renpy.restart_interaction()
            show amiga at center with dissolve
            amiga "Bueno, bueno. Explica muy bien la maestra."
            chica "Sí, tienes razón."
            #$ Minijuego = "perdio"
            #elif juego == "pierde":
                #$ minijuegos_perdidos += 1
                #play sound "mas.mp3"
                #$ estres += 10
            #if estres >=50:
                #$ actualizar_estado_sprite()    
                #$ renpy.restart_interaction()
                #chica "Estuvo complicado."
            amiga "Sigo preocupada por Sebastián. Seguro tuvo problemas en la anterior."
            chica "Tienes razón, ahora hay que convencerlo de que practique con nosotros."
            amiga "Buena suerte con eso."
            hide amiga with dissolve
            $ estres = 15 # Eliminar después de poner minijuego
            $ renpy.restart_interaction()
            menu:
                "Convencerlo de que se te una.":
                    jump ConvencerA_Chica

                "No hacer nada.":
                    jump NadaA_Chica




            #Chica A
            label ConvencerA_Chica:
                chica "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo at center with dissolve
                amigo "Pero habrá un festival."
                chica "Vamos, hazlo por mí y por Luna."
                amigo "Te ves muy cansada, pero está bien, me uniré a ustedes. El festival puede esperar."
                chica "No te arrepentirás."

                # Reflexión Interna
                "Ver a Sebastián quedarse me hace pensar que tomar la iniciativa fue lo correcto. Puede que el cansancio me afecte, pero saber que estoy ayudando a mis amigos también me da energía."
                "Tal vez, si mantengo este equilibrio entre el estudio y el descanso, podré enfrentar mejor los desafíos de la universidad."

                play sound "mas.mp3"
                $ estres += 5
                $ renpy.restart_interaction()

                # Continuar guion
                "Nos quedamos con Luna, quien parecía muy feliz."
                show amiga at move_in_left
                amiga "Gracias por acompañarme, amigos."
                show amigo at move_in_right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto. Nos va a servir mucho." 
                hide amigo with dissolve
                hide amiga with dissolve
                "Pasa el tiempo y estudiamos un rato más con Luna."
                "Observo cómo Sebastián se retira para ir a lo que queda del festival, pero decido acompañar un rato más a Luna."

                show amiga at center with dissolve
                amiga "[nombre], ¿puedo decirte algo?"
                chica "Claro, amiga."
                #stop music
                #play music "Luna.mp3"
                amiga "Muchas gracias por acompañarme. Aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve

                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "De verdad lo aprecio mucho, [nombre]. Gracias por estar conmigo."
                chica "Sé cómo te sientes, Luna, y te comprendo."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Sí, me alegra que seamos amigas. Tenemos algo en común."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chica "Nos vemos, Luna."
                amiga "Cuídate mucho, [nombre]."
                hide amiga with dissolve

                play sound "menos.mp3"
                $ estres -= 5
                $ renpy.restart_interaction()

                # Continuar
                scene cuartonoche with slideright
                "Te acuestas a dormir porque te sentías muy cansada, pero a pesar de todo, el día salió bien."
                "Mientras tus ojos se cierran, tu mente repasa las últimas horas... algo se siente fuera de lugar, pero decides no pensar demasiado en ello."
                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, el esfuerzo que hacemos para apoyar a nuestros amigos nos da la fuerza que pensamos que no tenemos."
                misterioso "Recuerda que, en la universidad, tanto el apoyo mutuo como el descanso son esenciales para mantenerse firme ante los desafíos."
                misterioso "Aprende a dosificar tu energía, y nunca subestimes la importancia de rodearte de personas que te fortalezcan."
                stop music

                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Te despiertas sobresaltada y con la mente llena de preguntas, pero te das cuenta de que ya no te sientes cansada."
                chica "¿Qué habrá sido eso?"
                

                if estres >= 50:
                    scene chica_estres with dissolve 
                    $ actualizar_estado_sprite()   
                    chica "Hoy va a ser un buen día. Mejor dejar atrás esos pensamientos extraños." 
                else:    
                    scene chica_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chica "Hoy va a ser un buen día. Mejor dejar atrás esos pensamientos extraños."

                scene cocina with slideleft
                "Te preparas un desayuno para ir a la escuela."
                #stop music
                scene negro with dissolve
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren24

                    "Tomar Autobús":
                        jump Autobus24  

            label Tren24:

                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Otro día más. ¡Qué emoción!"  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Así llego más rápido."

                jump Dia_chicaA

            label Autobus24:

                if transporte == "tren":  
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El tren es rápido, pero aún tengo mucho tiempo."  
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "Aún tengo tiempo."

                jump Dia_chicaA








        label Dia_chicaA:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chica "Hoy espero volver a pasar tiempo con Luna y Sebastián."
            scene salon with slideleft
            "Veo a Luna y a Sebastián reunidos y me decido a saludarlos."
            chica "Hola amigos, ¿cómo están?"
            show amiga at move_in_right
            amiga "Hola [nombre], te ves mejor que ayer. Yo estoy bien, espero que tú también."
            show amigo at move_in_left
            amigo "Sí, opino lo mismo. Yo estoy bien también, ¿y tú cómo estás?"
            chica "Muy bien. ¿Hoy vamos a quedarnos a repasar, verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Sí, será lo mejor."
            "Empieza la clase."
            chica "¿Hoy tendremos tres clases, verdad?"
            amiga "Según el horario, sí."
            chica "Vale, gracias Luna."
            hide amigo with dissolve
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra with dissolve

            # Agregar cuarto minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Fue fácil."
            #     amiga "Eso es verdad."
            #     hide amiga with dissolve
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Vaya, sí que tuve dificultades."
            #     amiga "Deberías practicar un poco más."
            #     hide amiga with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDia_chicaA

                "Quedarse callada.":
                    $ Luna = "callarse"
                    jump cDia_chicaA

        label cDia_chicaA:
            if Luna == "preguntar":
                chica "Luna, ¿cómo has estado?"
                "Decido abrazarla por lo que pasó ayer."
                show amiga at move_in_right
                amiga "Me he sentido mejor. Gracias por preguntar."
                show amigo at move_in_left
                amigo "¿Aún preocupada, Luna? Eres lista y tú puedes con todo."
                amiga "Gracias a ambos por el apoyo."
                amiga "Sin ustedes, no sé qué haría."
                hide amiga with dissolve
                hide amigo with dissolve

            elif Luna == "callarse":
                "Te quedas callada, pero te quedas cerca de ella."
                chica "No tengo palabras ahorita, pero tienes mi apoyo, Luna."
                show amiga at move_in_right
                amiga "Gracias, lo aprecio mucho."
                show amigo at move_in_left
                amigo "También estoy aquí y me quedaré contigo, Luna."
                amiga "Gracias a ambos, de verdad."
                hide amiga with dissolve
                hide amigo with dissolve

            "Se termina el tiempo y continúa la siguiente clase."
            show maestra at center with dissolve
            maestra "Bueno, jóvenes, comencemos la siguiente clase."
            hide maestra with dissolve

            # Agregar quinto minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Genial, muy fácil."
            #     amiga "Practicando, todo se logra."
            #     hide amiga with dissolve
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Vaya, sí que tuve dificultades."
            #     amiga "Deberías practicar más, [nombre]."
            #     hide amiga with dissolve

            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at move_in_left
            amigo "Vaya, un fin de semana. No puede ser que ya tengamos exámenes."
            show amiga at move_in_right
            amiga "Lo sé, pero esto ya es la universidad. Siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno, ya lo veremos el fin de semana."
            chica "Apuesto que será divertido. Quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chica "Entonces, no se diga más, nos veremos en el parque."
            hide amigo with dissolve
            hide amiga with dissolve
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase. Hoy veremos un nuevo tema. Espero que estén preparados."
            hide maestro with dissolve

            # Agregar sexto minijuego
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Estuvo bien."
            #     amiga "Te lo dije."
            #     hide amiga with dissolve
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Eso estuvo difícil."
            #     amiga "No te rindas, [nombre]."
            #     hide amiga with dissolve

            "Termina la clase, finalizando el día de hoy."
            chica "Bueno, nos reuniremos en un parque para pasar tiempo los tres."
            show amiga at move_in_right
            amiga "Muy bien, los veré ahí."
            show amigo at move_in_left
            amigo "Igual, nos veremos allí."
            hide amiga with dissolve
            hide amigo with dissolve
            scene cuarto with slideleft
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            #stop music
            scene negro with dissolve
            "Es la primera vez que estoy muy relajada, Estudiar con amigos es mejor que sola ya que aprendes más."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Recuerda vas muy bien."
            "Te sientes confusa."
            chica "¿Otra vez?"
            "Bueno no importa debo estar concentrada."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chica "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chica "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chica "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            "Debería convencer a Sebastián que se una o me quedo sola con Luna."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaA1

                "Quedarse con Luna.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaA2

            label final_chicaA1:
                show amiga at move_in_right
                show amigo at move_in_left
                chica "Sebastián, podemos dejarlo para otro fin de semana."
                chica "Hoy hay que darle todo el apoyo a Luna."
                amigo "Tienes razón, es momento de saber cuándo hay que divertirse y cuándo hay que apoyar en momentos difíciles."
                amiga "Gracias por quedarte esta vez Sebastián."
                amiga "Y a ti, [nombre], por ayudarme."
                hide amigo with dissolve
                hide amiga with dissolve
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudar amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    hide amiga with dissolve


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos."
                #Reflexión Interna
                "Estudiar junto a Luna y Sebastián me hace sentir que estoy en el camino correcto. La compañía de amigos no solo ayuda a sobrellevar el estrés académico, sino que también aporta una paz que no se puede encontrar estudiando sola."
                "Quizás la universidad no solo sea un desafío académico, sino también una oportunidad para aprender a apoyarnos mutuamente."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has hecho buenos amigos que te apoyarán en esta etapa de tu vida. No olvides que el apoyo mutuo fortalece las amistades y también tu espíritu."
                misterioso "Aprender a equilibrar tus esfuerzos y compartirlos con personas en quienes confías es esencial en este camino."
                misterioso "Recuerda, la universidad te ofrece no solo conocimiento académico, sino también una lección sobre el valor de las relaciones y el apoyo en los momentos difíciles."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return

                

            label final_chicaA2:
                chica "Yo prefiero quedarme a estudiar un poco más."
                "Recuerdo lo que Luna me contó sobre su pasado, y sé que necesita apoyo ahora más que nunca."
                show amigo at move_in_left
                amigo "Entiendo... no importa, las veré después."
                show amiga at move_in_right
                amiga "Sebastián…"
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián se acerca y me susurra al oído."
                amigo "Cuida de ella, [nombre], ¿vale?"
                "Lo miras directamente, haciendo un gesto de afirmación, sintiendo el peso de su petición."
                hide amigo with dissolve
                hide amiga with dissolve
                "Al verlo marcharse, me quedo pensando si realmente tomé la decisión correcta."
                "Pero no quiero que Luna se sienta sola, así que dejo esos pensamientos de lado."
                chica "Tranquila, Luna, tienes mi apoyo."
                chica "Después de esto lo veremos y te ayudaré, ¿vale?"
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudar amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chica "Gracias Luna."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga with dissolve
                "Aunque me quedo con Luna para estudiar, no puedo evitar que, en el fondo de mi mente, una pequeña duda me siga preguntando por qué no convencí a Sebastián de quedarse también."
                #Reflexión Interna
                "Quedarme con Luna me da la certeza de que, a veces, priorizar a quienes nos importan es el camino correcto."
                "Quizá este pequeño gesto no cambie el mundo, pero fortalece nuestra amistad y me hace sentir en paz."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Cuidar de tus amigos cuando lo necesitan demuestra tu madurez y crecimiento."
                misterioso "Recuerda que en la vida y en la universidad, construir relaciones sólidas te ayudará a sobrellevar los momentos difíciles."
                misterioso "El bienestar emocional de las personas que nos importan puede ser un refugio en tiempos de estrés y desafíos."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return






            #Chica A,A
            label NadaA_Chica:
                "Decides no hacer nada y seguir practicando con Luna, quien parece estar preocupada aún."
                chica "Lo siento, Luna."
                show amiga_preocupada at center with vpunch
                amiga "No pasa nada, [nombre]."
                hide amiga_preocupada with dissolve
                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()

                if estres >= 50:
                    $ actualizar_estado_sprite()

                "Decides quedarte con Luna mientras observas cómo Sebastián se va al festival."
                "Te sientes realmente cansada."

                # Reflexión Interna
                "El cansancio me supera, y aunque sé que pude haber intentado convencer a Sebastián, no tuve las fuerzas para hacerlo. ¿Es este el tipo de persona en la que me estoy convirtiendo?"

                show amiga at center with dissolve
                amiga "Gracias por quedarte, [nombre]."
                chica "A ti, Luna, por ayudarme."
                amiga "[nombre], ¿puedo decirte algo?"
                chica "Claro, amiga."
                #stop music
                #play music "Luna.mp3"
                amiga "Quería agradecerte por acompañarme. Esto significa mucho para mí."
                amiga "Esto significa mucho para mí."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga with dissolve

                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste at center with dissolve
                amiga "De verdad lo aprecio mucho, [nombre]. Gracias por estar aquí."
                chica "Entiendo cómo te sientes, Luna. Aquí estoy contigo, amiga."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Sí, me alegra que seamos amigas. Tenemos algo en común."

                # Reflexión Interna
                "Luna confía en mí, y aquí estoy, sintiéndome agotada y culpable. Tal vez ella no lo sabe, pero siento que he fallado al no hacer más por nuestros amigos. ¿Por qué no puedo reaccionar?"

                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste with dissolve
                #stop music
                show amiga at center with dissolve
                chica "Nos vemos, Luna."
                amiga "Cuídate mucho, [nombre]."
                hide amiga with dissolve

                "Te sientes mal porque sabes que pudiste haber convencido a Sebastián, pero el cansancio te supera."

                # Reflexión Interna
                "Si solo hubiera tenido un poco más de energía... Quizás esto habría terminado de otra forma. Siento que esta carga de arrepentimiento se hace cada vez más pesada."

                play sound "mas.mp3"
                $ estres += 15
                $ renpy.restart_interaction()

                if estres >= 50:
                    $ actualizar_estado_sprite()

                # Continuar historia
                scene cuartonoche with slideright
                chica "Pude haberlo convencido, pero estaba muy cansada..."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."

                play music "sueñom.mp3"
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "A veces, nuestras decisiones son reflejo de nuestro estado emocional, [nombre]."
                misterioso "Cuando estamos agotados, nuestras acciones pueden parecer ajenas a nosotros, pero cada una deja una huella."
                misterioso "La próxima vez que enfrentes una decisión importante, pregúntate: ¿Es esto lo que realmente quiero, o es solo una respuesta a cómo me siento en el momento?"
                stop music
                scene cuarto with slideleft
                #play music "cancioncuarto.mp3"
                "Despiertas nerviosa."
                chica "¿Solo fue un sueño?"
                "Aún te sientes culpable, pero ya no te sientes agotada."

                if estres >= 50:
                    scene chica_estres
                    $ actualizar_estado_sprite()
                    chica "Espero que Luna esté bien..."
                else:
                    scene chica_normal with dissolve
                    $ actualizar_estado_sprite() 
                    chica "Espero que Luna esté bien."

                scene cocina with slideleft
                "Te preparas un desayuno para ir a la escuela."
                scene negro with dissolve
                #stop music  
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren25

                    "Tomar Autobús":
                        jump Autobus25

            label Tren25:
                if transporte == "tren":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Otro día más. Espero que hoy sea mejor."
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "El tren es rápido. Mejor opción para llegar pronto."
                jump Dia_chicaAA

            label Autobus25:
                if transporte == "tren":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El autobús es más lento, pero aún tengo tiempo para llegar."
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "El autobús me da tiempo para reflexionar un poco."
                jump Dia_chicaAA








        label Dia_chicaAA:
            scene escuela with slideleft
            #play music "salonclase.mp3"
            chica "Sé que pude haber convencido a Sebastián."
            chica "No quisiera ser responsable de que Luna se distancie de él."
            scene salon with slideleft
            "Veo a Luna preocupada aún."
            chica "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga at center with dissolve
            amiga "No te preocupes, [nombre]. Sebastián siempre ha sido independiente desde la preparatoria, así que estoy acostumbrada."
            chica "Sé que es importante estudiar, pero también es bueno convivir con los demás."
            chica "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Nadie debería estar sola."
            amiga "¿Estás bien, [nombre]?"
            chica "Sí, estoy bien. Gracias por preocuparte."
            "Veo a Sebastián saludarnos de lejos, pero no parece estar contento."
            "Hoy tendremos 3 clases."
            hide amiga with dissolve
            show maestra at center with dissolve
            maestra "Muy bien, alumnos. Hoy les impartiré dos clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra with dissolve

            # Reflexión interna antes del minijuego
            "El cansancio me persigue, pero sé que debo seguir adelante. Cada decisión cuenta, incluso si no lo parece."

            # Minijuego 4 (comentado):
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Salió bien."
            #     amiga "¡Te lo dije!"
            #     hide amiga with dissolve
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Esto salió fatal."
            #     amiga "¡Necesitas practicar más!"
            #     hide amiga with dissolve

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."

            menu:
                "¿Preguntar a Luna cómo está?":
                    $ Luna = "preguntar"
                    jump cDia_chicaAA

                "Quedarse callada.":
                    $ Luna = "callarse"
                    jump cDia_chicaAA

            label cDia_chicaAA:
                if Luna == "preguntar":
                    chica "Luna, ¿estás bien?"
                    show amiga at center with dissolve
                    amiga "Solo estoy preocupada. No quiero que Sebastián piense que lo dejé atrás. Él sabe mi situación."
                    "Decido abrazarla fuerte."
                    chica "Todo estará bien, ya lo verás."
                    amiga "Eso espero..."
                    hide amiga with dissolve

                elif Luna == "callarse":
                    "Un incómodo silencio nos invadió a ambas."
                    "Intento calmar a Luna."
                    chica "Cualquier cosa, aquí estaré, Luna."
                    show amiga at center with dissolve
                    amiga "Lo sé..."  
                    hide amiga with dissolve
                    "Decido darle ánimo a Luna."

                "Se termina el tiempo y continúa la siguiente clase."
                show maestra at center with dissolve
                maestra "Bueno, jóvenes, comencemos la siguiente clase."
                hide maestra with dissolve

            # Minijuego 5 (comentado):
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "¡Genial! Muy fácil."
            #     amiga "¡Me alegro por ti!"
            #     hide amiga with dissolve
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Esto fue complicado."
            #     amiga "¡Deberías practicar más!"
            #     hide amiga with dissolve

            show maestra at center with dissolve
            maestra "Bueno, clase. Estudien porque la siguiente semana será de exámenes. Esto definirá su futuro."
            maestra "Su otro profesor les enseñará el tema de una manera diferente para reforzar lo aprendido."
            hide maestra with dissolve

            "Nos relajamos por un momento mientras inicia la siguiente clase."
            "Pero noto que Luna está cada vez más desanimada."
            chica "Ánimo, Luna. Este fin de semana deberíamos reunirnos con Sebastián en el parque para animarte. ¿Qué te parece?"
            show amiga at center with dissolve
            amiga "No es mala idea. Gracias por preocuparte tanto por mí, [nombre]."
            chica "Entonces, este fin de semana iremos al parque."
            amiga "Muy bien."
            hide amiga with dissolve

            "Observo cómo Luna se ve más calmada."
            "Veo entrar al maestro Carlos, quien da inicio a la última clase."
            show maestro at center with dissolve
            maestro "Muy bien, clase. Hoy veremos un nuevo tema. Espero que estén preparados."
            hide maestro with dissolve

            # Minijuego 6 (comentado):
            # $ Minijuego = "Gano"
            # if juego == "gana":
            #     $ minijuegos_ganados += 1
            #     play sound "menos.mp3"
            #     $ estres -= 5
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "¡Estuvo bien!"
            #     amiga "¡Te lo dije!"
            #     hide amiga with dissolve
            # $ Minijuego = "perdio"
            # elif juego == "pierde":
            #     $ minijuegos_perdidos += 1
            #     play sound "mas.mp3"
            #     $ estres += 5
            # if estres >= 100:
            #     call game_over
            # else:
            #     $ actualizar_estado_sprite()
            #     $ renpy.restart_interaction()
            #     show amiga at center with dissolve
            #     chica "Eso estuvo difícil."
            #     amiga "¡No te rindas, [nombre]!"
            #     hide amiga with dissolve

            "Termina la clase, finalizando el día de hoy."
            chica "Bueno, nos reuniremos en el parque para pasar tiempo juntos."
            show amiga at move_in_right
            amiga "Muy bien, los veré allí."
            hide amiga with dissolve

            "Veo cómo Luna se va un poco mejor y decido acercarme a Sebastián."
            chica "Hola, Sebastián. Luna y yo nos vamos a reunir este fin de semana. ¿Te unes?"
            show amigo at center with dissolve
            amigo "¡Claro que sí! Los veré a las 2 entonces."
            hide amigo with dissolve

            "Me despido de él, regresando a mi casa."
            #stop music
            scene cuarto with slideleft
            "Al final, todo salió bien. Espero que el fin de semana sea perfecto."
            scene parque with slideleft
            play music "parque.mp3"
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro with dissolve
            misterioso "Ahora puedes hacer la diferencia."
            "Te sientes menos culpable, pero confusa."
            chica "¿Otra vez el?"
            "Bueno, debo estar concentrada."
            scene parque with slideleft
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at move_in_right
            chica "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chica "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chica "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Gracias por organizar esto."
            chica "Te la debo Luna."
            #Reflexión Interna
            "Me quedo al lado de Luna, pero no puedo evitar sentir un peso en el pecho. Sigo pensando en cómo pude haber intentado más, en lo fácil que sería mejorar esta situación si tan solo tuviera la energía para ello."
            "Veo a Luna más tranquila que antes."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at move_in_left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez, debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            #Reflexión Interna
            "Me encuentro en la misma encrucijada, pero esta vez debo dar un paso adelante. No puedo seguir dejando que el cansancio y la culpa me controlen. Es momento de decidir qué clase de amigo quiero ser."
            hide amiga with dissolve
            hide amigo with dissolve
            menu:
                "Convencer a Sebastián.":
                    play sound "menos.mp3"
                    $ estres -= 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaAA1

                "Quedarse con Luna.":
                    play sound "mas.mp3"
                    $ estres += 5
                    $ actualizar_estado_sprite()
                    $ renpy.restart_interaction()
                    jump final_chicaAA2

            label final_chicaAA1:
                show amiga at move_in_right
                show amigo at move_in_left
                chica "Sebastián, esta vez quiero decirte que te quedes con nosotras."
                chica "Aquella vez no pude convencerte porque me sentía mal y cansada."
                amigo "oh no lo sabía."
                amigo "Lo siento..."
                chica "No pasa nada, Sebastián."
                chica "Pero me preocupé mucho por Luna aquella vez."
                amigo " Entiendo..."
                "Ves que Sebastián finalmente decide quedarse con ustedes."
                amiga "Gracias, [nombre], por convencer a Sebastián."
                chica "No hay problema. "
                chica "Sé que te preocupa estar sola."
                hide amigo with dissolve
                hide amiga with dissolve
                "Pasan la tarde juntos, disfrutando del tiempo como amigos y estudiando. "
               
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."

                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    hide amiga with dissolve

                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos, aunque me costó trabajo."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Reconocer las propias limitaciones y aun así encontrar la fuerza para actuar es un acto de valentía, [nombre]."
                misterioso "Nunca subestimes el poder de pequeños esfuerzos, porque son esos momentos los que fortalecen las amistades."
                misterioso "Hoy, elegiste no permitir que el cansancio te definiera, y ese es un paso hacia adelante."
                stop music
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return




            label final_chicaAA2:
                "Me siento mal al no volver a convencer a Sebastián, pero con pocos ánimos respondo."
                chica "Lo siento, Sebastián."
                chica "Creo que esta vez me quedaré con Luna. "
                "No quiero que se quede sola."
                show amigo at move_in_left
                amigo "Lo entiendo, no te preocupes."
                amigo "Me reuniré con otros amigos entonces."
                show amiga at move_in_right
                amiga "Sebastián…"
                hide amigo with dissolve
                "Ves cómo Sebastián se va, dejándote con Luna."              
                amiga "Gracias por quedarte conmigo, [nombre]."
                chica "Lo haré siempre que lo necesites, Luna."
                hide amiga with dissolve
                "Pasan la tarde estudiando juntas, aunque sientes un poco de tristeza por no haber salido con Sebastián."
                "Luna parece estar un poco más tranquila, pero sabes que aún queda mucho por superar."
                "Decides tomar un descanso después de un largo día de estudio."
                if Luna == "preguntar":
                    show amiga at center with dissolve
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez Luna."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se..."
                    amiga "Es mejor ayudarnos entre nosotras."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    amiga "Así que no te sientas culpable."
                    chica "Gracias Luna."
                    chica "No te volvere a fallar."
                    hide amiga with dissolve
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "callarse":
                    show amiga at center with dissolve
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía y el apoyo que me das."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    chica "Lo mejor sera darle espacio."
                    amiga "Si tiene razón [nombre]."
                    hide amiga with dissolve
                
                "Estás satisfecho de haber apoyado a Luna, pero también sabes que aún hay retos por enfrentar."
                stop music
                hide screen barra_estres
                hide screen personaje_sprite
                play music "TonoMisteriosoFinales.mp3"
                image misteriosoo = Movie(play="trampa.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "La culpa puede ser una carga, pero también una señal de que tienes el deseo de mejorar."
                misterioso "No te castigues demasiado, en la universidad y en la vida, habrá oportunidades de redención."
                misterioso "Recuerda, [nombre], que las decisiones que tomas hoy son solo el comienzo de un camino en el que siempre podrás evolucionar."
                stop music 
                scene negro with dissolve

                play music "resultados.mp3"
                "Demo completada, pero hay otros caminos para elegir."

                "Resultados del juego:"
                "Minijuegos ganados: [minijuegos_ganados]"
                "Minijuegos perdidos: [minijuegos_perdidos]"
                "Nivel de estrés acumulado: [estres]"
                stop music

                return  
                     


return