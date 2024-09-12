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


screen barra_estres:
    frame:
        align (0.02, 0.98)  # Ajusta la posición de la barra (0.02, 0.98) es cerca de la esquina inferior izquierda
        
        # Cambiar la imagen de la barra de estrés según el nivel de estrés
        if estres <= 0:
            add "estres_0.png"  # Imagen para 0-25% de estrés
        elif estres <= 5:
            add "estres_5.png"  # Imagen para 26-50% de estrés 
        elif estres <= 10:
            add "estres_10.png"  # Imagen para 26-50% de estrés    
        elif estres <= 15:
            add "estres_15.png"  # Imagen para 26-50% de estrés    
        elif estres <= 20:
            add "estres_20.png"  # Imagen para 26-50% de estrés      
        elif estres <= 25:
            add "estres_25.png"  # Imagen para 26-50% de estrés                
        elif estres <= 45:
            add "estres_45.png"  # Imagen para 26-50% de estrés                          
        elif estres <= 55:
            add "estres_55.png"  # Imagen para 26-50% de estrés
        elif estres <= 65:
            add "estres_65.png"  # Imagen para 51-75% de estrés
        elif estres <= 85:
            add "estres_85.png"  # Imagen para 26-50% de estrés                
        else:
            add "estres_100.png"  # Imagen para 76-100% de estrés

#ajustar video            
define config.screen_width = 1920
define config.screen_height = 1080       

label start:
    # Pantalla de selección de género
    menu:
        "Chico":
            $ genero = "chico"
            $ personaje = "Protagonista"
            jump elegir_nombre
        "Chica":
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
    "Por fin he terminado la preparatoria y aprobé el examen de admisión para la universidad, solo espero no tener dificultades…"
    "Al día siguiente"
    "Te levantas al siguiente día temprano, pues te espera un nuevo comienzo. "
   
    scene cuarto
    # Mostrar la barra de estrés en la parte inferior izquierda
    show screen barra_estres

   

    # Mostrar al personaje correspondiente
    if genero == "chico":
        show chico 
        chico " ¡Aahh! Ya es hora de levantarse para ir a la universidad."
        chico " ¡Espero que salga todo bien en mi primer día."
    elif genero == "chica":
        show chica 
        chica " ¡Aahh! Ya es hora de levantarse para ir a la universidad no se me vaya a ser tarde."
        chica " Espero que salga todo bien en mi primer día."

    # Continuar la historia
    

    scene WC

    if genero == "chico":
        scene chico_normal
        chico "¡uuhh! Espero no tener problemas como en la preparatoria."    
        chico "Me cuesta mucho trabajo Socializar. "
        chico "Vamos es tu primer día tú puedes. "
        chico "Además, entraste a la carrera que querías Ingeniería en computación."
    elif genero == "chica":
        scene chica_normal 
        chica "¡uuhh! Espero no tener problemas como en la preparatoria."    
        chica "Me cuesta mucho trabajo Socializar. "
        chica "Vamos es tu primer día tú puedes. "
        chica "Además, entraste a la carrera que querías Ingeniería en computación."


    scene cocina    
    "Solo desayuno cualquier cosa y me voy. "
    "Hoy mis padres están lejos por temas de trabajo asi que estaré solo estos días. "

    scene negro
    "¿Debería tomar el autobús o el tren? "
    menu:
        "Tomar Tren":
            jump Tren

        "Tomar Autobus":
            jump Autobus    


    label Tren:
       
        play movie "Tren.webm"  
        "El tren es rápido y llega directo a la universidad."  
 
        stop movie  
        jump universidad
        
    label Autobus:
        play movie "Autobus.webm" 
        "El autobús es más económico y hace varias paradas."
        stop movie
        jump universidad
    
    # Decisión inicial
    



label universidad:
    # Aquí puedes continuar el guion para la opción de la biblioteca
    scene escuela
    "Pues aquí estamos, La universidad School Link."
    "Espero poder adaptarme bien y hacer nuevos amigos."
    "Bueno, es hora de encontrar mi salón de clases."
    scene salon

if genero == "chico":
        
        chico "Bueno parece que aquí es."    
        chico "Bueno me sentare aquí.   "
        desconocido "Hola, ¿cómo estás? "
        
        "¡mmhh! Esa chica me está hablando."
        chico "Hola, bien y tu ¿cómo estás?"
        show amiga at left
        desconocido "Bien también, Soy Luna María, pero me puedes decir solo Luna. "
        chico "Un gusto yo soy  [nombre]."
        "Espero ser su amigo."
        amiga "El gusto es mío. "
        "A lo lejos veo a un chico acercándose. "
        desconocido "Hola, ¿interrumpo algo?"
        amiga "Hola Sebastián veo que tú también entraste a la carrera."
        show amigo at right
        amigo "Si eso parece, ¿quíen es el chico nuevo?"
        chico "Hola, me llamo [nombre] un placer."
        amigo "El gusto es mío, te ves pálido ¿estas bien?"
        chico "Si estoy bien."
        hide amigo
        hide amiga 
        "Debo controlarme, sé que es difícil para mí socializar, pero está saliendo bien."
        $ estres = 20
        $ renpy.restart_interaction()
        explicacion "De aquí en adelante las decisiones que tomes afectaran a tu barra de estrés."
        explicacion "Recuerda mantenerla baja si sube al límite perderás la partida. "
        explicacion "Así que cuida tu barra de estrés."
        "Veo entrando al maestro al salón de clases mientras todos se quedan callados."
        show maestro
        maestro "Buenos días alumnos, soy el profesor Carlos y yo les impartiré la materia de computación. "
        maestro "Empezaremos viendo la primera sesión."



elif genero == "chica":
        
        chica "Bueno parece que aquí es."    
        chica "Bueno me sentare aquí.   "
        desconocido "Hola, ¿cómo estás? "
        
        "¡vaya! Esa chica me está hablando."
        chica "Hola, bien y tu ¿cómo estás?"
        show amiga at left
        desconocido "Bien también, Soy Luna María, pero me puedes decir solo Luna. "
        chica "Un placer me llamo [nombre]."
        "Espero ser su amiga."
        amiga "El gusto es mío. "
        "A lo lejos veo a un chico acercándose. "
        desconocido "Hola, ¿interrumpo algo?"
        amiga "Hola Sebastián veo que tú también entraste a la carrera."
        show amigo at right
        amigo "Si eso parece, ¿quíen es la chica nueva?."
        chica "Hola, me llamo [nombre] mucho gusto."
        amigo "El gusto es mío, te ves pálida ¿estas bien?"
        chica "Si estoy bien."
        hide amigo
        hide amiga 
        "Debo controlarme, sé que es difícil para mí socializar, pero está saliendo bien."
        $ estres = 20
        $ renpy.restart_interaction()
        explicacion "De aquí en adelante las decisiones que tomes afectaran a tu barra de estrés."
        explicacion "Recuerda mantenerla baja si sube al límite perderás la partida. "
        explicacion "Así que cuida tu barra de estrés."
        "Veo entrando al maestro al salón de clases mientras todos se quedan callados."
        show maestro
        maestro "Buenos días alumnos, soy el profesor Carlos y yo les impartiré la materia de computación. "
        maestro "Empezaremos viendo la primera sesión."
return