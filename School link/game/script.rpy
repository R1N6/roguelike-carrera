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
        elif estres <= 80:
            add "estres_80.png"  # Imagen para 26-50% de estrés                
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
    "¡Finalmente! Terminé la preparatoria. Ese examen de admisión para la universidad fue algo difícil. Me pregunto qué me deparará esta nueva etapa..."
    "Al día siguiente."
    "Te levantas  temprano, te espera un nuevo comienzo.  "
   
    scene cuarto
    # Mostrar la barra de estrés en la parte inferior izquierda
    show screen barra_estres

   

    # Mostrar al personaje correspondiente
    if genero == "chico":
        show chico 
        chico " *bostezo* Ya es hora de levantarme para ir mi primer día de universidad."
        chico " ¡Espero que salga todo bien."
    elif genero == "chica":
        show chica 
        chica " *bostezo* Ya es hora de levantarme para ir mi primer día de  universidad no se me vaya a ser tarde."
        chica " Espero que salga todo bien."

    
    

    

    if genero == "chico":
        scene wc
        "..."
        scene chico_normal
        chico "Espero no tener problemas como en la preparatoria."    
        chico "Me cuesta un poco socializar. "
        chico "Vamos, nuevo comienzo, nuevas personas. "
        chico "Además, pude entrar a la carrera que quería Ingeniería en computación."
        scene cocina    
        "Cualquier cosa servirá de desayuno. "
        "Hoy mis padres están lejos por temas de trabajo así que estaré solo estos días. "
    elif genero == "chica":
        scene wc
        "..."
        scene chica_normal 
        chica "Espero no tener problemas como en la preparatoria."    
        chica "Me cuesta un poco socializar. "
        chica "Vamos, nuevo comienzo, nuevas personas. "
        chica "Además, pude entrar a la carrera que quería Ingeniería en computación."
        scene cocina    
        "Cualquier cosa servirá de desayuno. "
        "Hoy mis padres están lejos por temas de trabajo así que estaré sola estos días. "




    scene negro
    "¿Debería tomar el autobús o el tren? "
    menu:
        "Tomar Tren":
            $ transporte = "tren"
            jump Tren

        "Tomar Autobus":
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
    
    # Decisión inicial
    



label universidad:
    # Aquí puedes continuar el guion para la opción de la biblioteca
    scene escuela
    
    "Pues aquí estamos, la Universidad School Link."
    "¿Qué clase de compañeros tendré? ¡Seguro que puedo hacer algún amigo!"
    "Hora de encontrar mi salón de clases."
    scene salon


if genero == "chico":
        
        chico "Este es mi salón."    
        chico "Bueno me sentaré aquí.   "
        desconocido "Hola, ¿cómo estás? "
        chico "Hola, bien y tu ¿cómo estás?"
        show amiga at left
        desconocido "Bien también, Soy Luna."
        chico "Un gusto yo soy  [nombre]."
        "Espero ser su amigo."
        amiga "El gusto es mío. "
        "A lo lejos veo a un chico acercándose. "
        desconocido "Qué onda."
        amiga "Hola Sebastián, ¿elegiste la misma carrera?"
        show amigo at right
        amigo "Sí, eso parece, ¿Y tú como te llamas?"
        chico "[nombre]"
        amigo " te ves pálido ¿estás bien?"
        chico "Si estoy bien."
        hide amigo
        hide amiga 
        "Debo controlarme, sé que es difícil para mí socializar, pero está saliendo bien."
        $ estres = 20
        $ renpy.restart_interaction()
        explicacion "De aquí en adelante las decisiones que tomes afectarán a tu barra de estrés."
        explicacion "Recuerda mantenerla baja si sube al límite perderás la partida. "
        explicacion "Un estrés muy alto puede ocasionar que aumente la dificultad de los minijuegos."
        explicacion "Así que cuida tu barra de estrés."
        "Veo entrando al maestro al salón de clases mientras todos se quedan callados."
        show maestro
        maestro "Buenos días alumnos, soy el profesor Carlos y yo les impartiré la materia de Redes. "
        maestro "Empezaremos viendo la primera sesión."
        hide maestro
        chico "Bueno aquí vamos."
        chico "Espero no tener dificultades."

        #agregar minijuego
         
        #if juego == "gana":
        chico "Eso estuvo facil"
        #elif juego == "pierde":
            #chico "¡uuff! Menos mal no me fue tan mal."
        chico "Debería practicar para mejorar en la siguiente."
        show amigo at right
        amigo "Oye [nombre] ¿quieres acompañarnos al billar?"
        show amiga at left
        amiga "No lo sé… creo que deberíamos repasar un poco para la siguiente clase, [nombre]."
        hide amigo
        hide amiga 
        explicacion "Esta es la primera decisión que puede afectar tu barra de estrés."
        explicacion "Recuerdo no llenarla."
        $ estres = 20
        $ renpy.restart_interaction()


        menu:
            "Claro, vámonos al billar":
                jump billar

            "Me quedaré a repasar con Luna":
                jump Estudiar 



        # Desicion Sebastián 
        label billar:
            show amigo
            amigo "Bien dicho [nombre], ¡vamos!"
            $ estres = 15
            $ renpy.restart_interaction()
            scene negro
            "Vas al billar con Sebastián." 
            "Fue divertido, pero una pequeña voz en tu cabeza te dice que mañana pagarás el precio." 
            "Regreso a mi casa algo cansado."
            scene cuartonoche
            chico "Fue un buen primer día."
            "¿Debería dormirme ya? o ¿juego videojuegos un rato?"
        menu:
            "Dormir.":
                jump descansado

            "Jugar video juegos.":
                jump cansado     



        # Ruta D
        label descansado:
            $ estres = 5
            $ renpy.restart_interaction()
            scene cuartonoche
            chico "Bueno lo mejor será descansar para mañana tener energía."
            scene negro
            "Te acuestas a dormir temprano recuperando energía para el siguiente día."
            scene cuarto
            "Te despiertas con energía y descansado."
            scene wc
            "Te sientes con mucha energía de ver que pasara hoy."   
            scene chico_normal
            chico "¡aahhh! Que bien me siento."    
            chico "Hora de ir a la Universidad."    
            scene cocina
            "Desayunas lo primero que encuentras y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren2

                "Tomar Autobus":
                    jump Autobus2  
            label Tren2:
        
            
                if transporte == "tren":  
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Es el más rápido."  
                elif transporte == "autobus":
                    image treen = Movie(play="Tren.webm", size=(1920, 1080))
                    show treen
                    "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
                
        
                 
                jump RutaD
            
            label Autobus2:

                if transporte == "tren": 
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus 
                    "El tren es rápido, pero aún tengo tiempo para llegar."  
                elif transporte == "autobus":
                    image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                    show aautobus
                    "Bueno, aunque es más lento es el más económico."
                 
                jump RutaD   



        #Ruta D
        label RutaD:    
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            chico "Parece que Luna no está muy convencida."
            show amigo
            amigo "No te preocupes, hablaremos con ella después para que se una a nosotros. "
            chico "Sí, creo que es lo mejor."
            amigo "Bueno es hora de ver cómo nos va seguro nos va bien."
            chico "Espero que todo salga bien."
            hide amigo
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro
            #Agregar segundo minijuego

            #if juego == "gana":
                #chico "Me fue muy bien"
            #elif juego == "pierde":
            chico "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            show amigo
            amigo "No estuvo mal después de todo."
            chico "Sí, me siento aliviado de que haya terminado bien.."
            amigo "pasemos a la siguiente materia."
            chico "seguro que en esta nos va todavía mejor."
            chico "si tú lo dices."
            hide amigo
            "Nunca había tenido la oportunidad de salir con un amigo."
            "Siempre solía volver solo a casa."
            "Veo que llega la maestra, Sebastián se le nota preocupado ¿será que le gusta Luna?"
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable. "
            "después le pregunto ahora a poner atención."
            hide maestra

            #Minijuego 3 agregar 

            #if juego == "gana":
                #show amigo
                #amigo "Muy facil"
                #chico "Es cierto"
            #elif juego == "pierde":
            show amigo
            amigo "esto no estuvo tan mal."
            chico "sí, tienes razón."
            chico "Oye Sebastián te veo preocupado ¿todo bien?"
            amigo "Me preocupo porque Luna siempre ha sido mi amiga y no quisiera que se quedara sola."
            "Tenía razón si le gusta."
            chico "podemos quedarnos esta vez."
            amigo "si, aunque hoy habrá un festival podemos convencerla de que venga con nosotros y ya después practicamos con ella. "
            chico "veré que puedo hacer."
            hide amigo
            $ estres = 20
            $ renpy.restart_interaction()
            menu:
                "convercerla de que se una.":
                    jump ConvencerlaD

                "No hacer nada.":
                    jump NadaLD



            #Ruta D
            label ConvencerlaD:
                chico "¿Luna, Sebastián y yo vamos a ir a un festival quieres unirte?"
                show amiga
                amiga "Yo les recomendaría quedarse a estudiar, pero prefiero quedarme a repasar, pero diviértanse."
                chico "Gracias por la preocupación, te veré mañana."
                amiga "Hasta mañana."
                hide amiga 
                "Bueno lo intente, pero espero mañana estar con ella pues no me gusta que esté sola me recuerda a mí en la preparatoria."
                $ estres = 30
                $ renpy.restart_interaction()
                #Continuacion de Ruta
                scene escuela
                show amigo
                amigo "Gracias por acompañarme."
                chico "Está bien relajarse de vez en cuando."
                amigo "No sé por qué, pero me siento como un tonto ahora mismo."
                chico "¿Qué te preocupa?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que hay algo mal así que decido preguntarle."
                chico "¿Todo bien Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna para mi es mi mejor amiga pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "Mi madre nunca la conocí pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián, su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces así que sé lo que siente Sebastián."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias [nombre] lo necesitaba sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chico "Sé lo que se siente, no poder agarrar fuerzas para seguir, pero debemos continuar adelante."
                hide amigo_triste
                show amigo
                amigo "Mejor regresemos y nos vemos mañana."
                chico "Muy bien."
                hide amigo
                scene negro
                "Sientes un dolor profundo al saber que no sufres solo."
                "regresas a casa pensando en todo lo que pasó hoy."
                $ estres = 45
                $ renpy.restart_interaction()
                #Siguiente Día 
                scene cuartonoche
                "Intento dormir, pero mi mente no deja de pensar en Luna."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tranquilo vale, en la vida hay ciertas decisiones que tomamos, pero lo mejor es afrontar las consecuencias que reprimirlas [nombre]."
                chico "Es cierto en la preparatoria cometí más errores esto lo puedo resolver."
                misterioso "Exacto tú puedes con todo, afronta las consecuencias y te sentirás mejor."
                scene cuarto
                "Despiertas confuso, pero sigues pensando en luna."
                chico "¿Afrontar consecuencias?"
                scene chico_normal
                chico "Vamos anímate Sebastián está bien yo también puedo estarlo resolveré esta situación con Luna."
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren10

                    "Tomar Autobus":
                        jump Autobus10  
        label Tren10:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
             
            jump DiaD
        
        label Autobus10:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
             
            jump DiaD








        label DiaD:
            scene escuela
            "Vamos anímate debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo
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
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Muy facil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovechamos el tiempo para ir a hablar con luna."
            chico "Hola Luna."
            show amiga at left
            amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
            chico "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
            show amigo at right
            amigo "Como en los viejos tiempos."
            amiga "Claro encantada de ir con ustedes."
            chico "Entonces nos vemos allá."
            hide amigo
            hide amiga
            "Nos regresamos a nuestros lugares."
            "Se termina el tiempo y continúa la siguiente clase."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "Salió bien la verdad."
            show amigo
            amigo "Sí tienes razón este fin será inolvidable. "   
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Sin problemas."
                #amigo "Pues claro."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            show amiga 
            amiga "Adiós [nombre] nos vemos allá entonces."
            hide amiga 
            scene negro
            "Estoy ansioso de que llegue este fin de semana." 

            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Afrontas bien las consecuencias recuerda no rendirte."
            "Te sientes confuso."
            "Bueno gracias a él todo fue mejor y resolví las cosas."
            "Ahora sólo debo concentrarme en pasarla bien con ellos."
            scene parque 
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chico "Hola Sebastián."
            show amigo at left
            amigo "Hola [nombre]."
            amigo "¿Estás listo para pasarla bien?"
            chico "Si estoy listo."
            " Luna aparece con un material para estudiar."
            show amiga at right
            amiga "Hola chicos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga
            hide amigo 
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chico "¿Qué pasa? "
            chico "¿Te sientes bien?"
            show amigo_triste 
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            chico " Deberías decirle lo que sientes por ella."
            amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
            "Comprendo su situación pues se como se siente no estar seguro de una decisión."
            "Debería darle apoyo para que se confiese o respeto su sentimiento de preocupación."
            hide amigo_triste

            menu:
                "Darle apoyo para que se confiese.":
                    jump finalD1

                "Respetar sus sentimientos de preocupación.":
                    jump finalD2





                    
            label finalD1:
                chico "Se cómo te sientes, pero es mejor decirle lo que sientes por ella veo que ella quiere que le digas eso."
                show amigo 
                amigo "¿Estás seguro de esto?"
                chico "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo 
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at left
                amigo "Luna…"
                show amiga at right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga 
                show amiga_triste at right
                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo
                hide amiga_triste
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at left
                show amiga at right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella. "
                hide amigo
                hide amiga 
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Ayudar a tus amigos desinteresadamente no solo es lo correcto, sino que también te hace sentir mejor."
                misterioso "Recuerda, en la vida, cualquier decisión que tomes traerá consecuencias, pero siempre habrá soluciones."
                misterioso "Nunca temas ofrecer tu ayuda o expresar tus sentimientos, especialmente en la universidad."
                misterioso "Solo elige bien con quién compartir tus emociones."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label finalD2:
                chico "Si es lo que sientes, te apoyaré en cualquier decisión que tomes, Sebastián."
                chico "Sé lo que se siente no poder expresarte, así que cuentas conmigo en lo que sea."
                show amigo 
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chico "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo."
                show amigo at left 
                amigo "Volvimos."
                show amiga at right
                amiga "¿Todo bien?"
                chico "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chico "Continuemos."
                "Luna parece tranquila al pasar tiempo con Sebastián, pero  puedes notar que le hubiera gustado que él le confesara sus sentimientos."
                "Aun así, respetastes  su decisión de Sebastián."
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "No deberías guardarte nada, si te sientes mal, buscar ayuda en quienes te rodean es valiente."
                misterioso "Has afrontado esta situación con madurez."
                misterioso "Apoyaste y respetaste los sentimientos de Sebastián, pero recuerda que siempre podemos hacer un poco más por aquellos que nos importan."
                misterioso "La universidad es un desafío importante en la vida, no intentes superarlo solo."
                misterioso "Busca siempre la compañía de amigos y nunca te rindas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return

            

            














            #Ruta D,D
            label NadaLD:
                "Decides no hacer nada, Sebastián parece preocupado."   
                chico " Lo siento Sebastián."
                show amigo_triste
                amigo "no te preocupes vámonos entonces."
                hide amigo_triste
                "¿Qué me sucede? Ver a Luna sola me recuerda a mí y no puedo hacer nada."
                $ estres = 35
                $ renpy.restart_interaction()
                #Continuacion de Ruta
                scene escuela
                show amigo
                amigo " Gracias por acompañarme, aunque deberíamos haberla invitado."
                chico "Está bien relajarse de vez en cuando y de verdad lo siento no sé porque no me anime."
                amigo "Anímate yo soy quien debió convencerla, no tú."
                amigo "Me siento como un idiota ahora mismo."
                chico "¿Por qué lo dices?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que hay algo mal así que decido preguntarle."
                chico "¿Todo bien Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna para mi es mi mejor amiga pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "Mi madre nunca la conocí pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián, su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces así que sé lo que siente Sebastián."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias [nombre] lo necesitaba sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chico "Sé lo que se siente, no poder agarrar fuerzas para seguir, pero debemos continuar adelante."
                hide amigo_triste
                show amigo
                amigo "Mejor regresemos y nos vemos mañana."
                chico "Muy bien."
                hide amigo
                scene negro
                "Sientes un dolor profundo al saber que no sufres solo, pero te sientes más mal de no haber invitado a Luna."
                "regresas a casa pensando en todo lo que pasó hoy."
                $ estres = 55
                $ renpy.restart_interaction()
                #continuar 
                scene cuartonoche
                "Sientes que pudiste hacer más con Luna y te acuestas a dormir."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "¿Sientes que pudiste hacer más? "
                misterioso "Hay decisiones que se nos complican en la vida, pero no te sientas mal."
                chico "Pero puede haber hecho algo, aunque no la haya convencido debí intentarlo."
                misterioso "Aun puedes cambiar tu destino [nombre]."
                scene cuarto
                "Despiertas confuso, pero sigues pensando en luna."
                chico "¿Cambiar mi destino?"
                scene chico_estres
                chico "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                "Esa sombra me dijo que puedo cambiar mi destino."
                scene cocina
                "Te preparas un Desayuno con mayor esfuerzo para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren12

                    "Tomar Autobus":
                        jump Autobus12  
        label Tren12:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
             
            jump DiaDD
        
        label Autobus12:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
             
            jump DiaDD








        label DiaDD:
            scene escuela
            "No es hora de pensar en eso debo de dar lo mejor de mí. "
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo_preocupado
            amigo "Hola [nombre] ¿te sientes bien?"
            chico "Si estoy bien."
            hide amigo_preocupado
            "Miro como los 2 estamos mejor que ayer, pero decidí contarle mi pasado."
            chico "Sobre lo de ayer yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            show amigo
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chico "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chico "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chico "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien esta vez iremos los 2 pero yo le diré que te veo un poco desanimado."
            chico "De acuerdo."
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "fue facil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovechamos el tiempo para ir a hablar con luna."
            chico "Hola Luna."
            show amiga at left
            amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
            chico "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
            show amigo at right
            amigo "Como en los viejos tiempos."
            amiga "Claro encantada de ir con ustedes."
            hide amiga
            show amiga_preocupada at left
            "Luna me observa preocupada "
            amiga "¿Estás bien [nombre]?"
            chico "Si estoy bien no te preocupes Luna."
            amiga "Si tu lo dices."
            chico "Entonces nos vemos allá."
            hide amigo
            hide amiga_preocupada
            "Nos regresamos a nuestros lugares."
            "Se termina el tiempo y continúa la siguiente clase."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "Salió bien la verdad."
            show amigo
            amigo "Sí tienes razón este fin será inolvidable. "   
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Sin problemas."
                #amigo "Pues claro."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            show amiga 
            amiga "Adiós [nombre] nos vemos allá entonces."
            hide amiga 
            scene negro
            "Estoy ansioso de que llegue este fin de semana." 
            "Y sobre todo cambiar mi destino."
            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "No importa que decisión tomes solo se consciente. "
            "Te sientes confuso."
            "¿Ser consciente? Creo que he hecho bien en planear este día."
            "Mejor no pensar en ello y pasarla bien."
            scene parque 
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chico "Hola Sebastián."
            show amigo at left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros."    
            amigo "Vamos amigo mucho ánimo ¿vale?"
            chico "Está bien, pero sigo pensando que esto pudo cambiar al decirle desde un principio, pero estoy preocupado de cómo está ella."
            amigo "No te dejaré solo en esto."
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chico "¿Mejor?"
            amigo "Mucho mejor."
            "Luna aparece con un material para estudiar."
            show amiga at right
            amiga "Hola chicos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga
            hide amigo 
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chico "¿Qué pasa? "
            chico "¿Te sientes bien?"
            show amigo_triste 
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            amigo "Te dije que todo está bien [nombre]."
            chico " Aun así quiero apoyarte Sebastián y ayudarte con Luna."
            amigo "Muchas gracias amigo."
            "Debería darle apoyo para que se confiese o respeto su sentimiento de preocupación."
            hide amigo_triste

            menu:
                "Darle apoyo para que se confiese.":
                    jump finalDD1

                "Respetar sus sentimientos de preocupación.":
                    jump finalDD2





                    
            label finalDD1:
                chico "No pude convencerla en un principio, pero quiero ayudarte a que le confieses tus sentimientos a ella."
                show amigo 
                amigo "No te preocupes más por eso."
                amigo "¿Y estás seguro de esto?"
                chico "Esta vez te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo 
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at left
                amigo "Luna…"
                show amiga at right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga 
                show amiga_triste at right
                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo
                hide amiga_triste
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at left
                show amiga at right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella, y se siente más apoyado. "
                hide amigo
                hide amiga 
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos, aunque tuvimos dificultades."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has logrado hacer la diferencia en comparación con decisiones pasadas, y las has enfrentado con valor."
                misterioso "Cualquiera sea la decisión que tomes en tu vida, recuerda que siempre habrá consecuencias, pero también soluciones."
                misterioso "Nunca temas ofrecer tu ayuda o expresar tus sentimientos, especialmente en la universidad."
                misterioso "Solo elige bien con quién compartir tus emociones."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label finalDD2:
                chico "No pude convencerla en un principio, pero tampoco quiero presionarte y respeto tu decisión."
                chico "Te daré el apoyo que necesites con Luna."
                show amigo 
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chico "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Volvemos con Luna Sebastián parece más calmado sabiendo que cuenta conmigo para lo que sea y me siento mejor al darle mi apoyo que no pude darle antes."
                show amigo at left 
                amigo "Volvimos."
                show amiga at right
                amiga "¿Todo bien?"
                chico "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chico "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia y sobre todo respetar decisiones."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Respetaste los sentimientos de Sebastián, y aunque no siempre podemos ofrecer apoyo al principio, siempre habrá oportunidades para hacerlo."
                misterioso "Cualquiera sea la decisión que tomes, siempre habrá consecuencias, pero también soluciones."
                misterioso "Nunca temas ayudar o expresar tus sentimientos, especialmente en la universidad."
                misterioso "Recuerda que nunca estás solo, elige bien con quién abrirte emocionalmente."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


                







        # Ruta C        
        label cansado:
            $ estres = 10
            $ renpy.restart_interaction()
            scene cuartonoche
            chico "Bueno, una partida no hará daño..."
            scene negro
            "juegas unas cuantas partidas y pierdes la noción del tiempo."
            scene cuarto
            "Despiertas con dificultad, sintiendo el peso de tus malas decisiones."
            scene wc 
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chico_normal
            "Te miras al espejo, tratando de reconocer a la persona reflejada."
            chico "Creo que me sobrepasé un poco…"
            "Suspiro."
            chico "Bueno, diría que demasiado... Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina
            "Desayunas lo primero que te hallaste y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren3

                "Tomar Autobus":
                    jump Autobus3  
        label Tren3:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
             
            jump RutaC
        
        label Autobus3:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
             
            jump RutaC   
       
       
       
        #Ruta C
        label RutaC:
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            "Luna parece decepcionada y Sebastián se muestra pensativo."
            amiga "Bueno... supongo que estudiaré sola entonces."
            "Puedo ver la decepción en sus ojos." 
            "Quería que fuéramos juntos… pero no puedo estar en dos lugares a la vez."
            " Veo como Luna se sienta en su lugar, intentando concentrarse en sus apuntes, pero su mirada se desvía hacia mí."
            "Hay un silencio incómodo que parece durar una eternidad."
            chico "Me siento mal por ella."
            show amigo
            amigo "No te preocupes por Luna, luego hay que convencerla de que venga con nosotros."
            chico "Sí, tienes razón... aunque algo en su mirada me dice que ya la decepcioné."
            "Sebastián se queda en silencio por un momento"
            amigo "¿Dormiste bien? Te ves cansado. "
            chico "No te preocupes, estaré bien... o al menos eso espero."
            hide amigo
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro 
            "Durante la clase, el cansancio comienza a hacer mella en ti."
            "Te cuesta concentrarte y cada palabra del profesor se siente como un peso más sobre tus hombros."
            #Agregar Minijuego 2
            #if juego == "gana":
                #chico "Me fue muy bien"
            #elif juego == "pierde":
            chico "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            amigo "¿Seguro que estás bien?"
            chico "Sí, estoy bien... sólo tuve dificultades, pero la próxima vez lo haré mejor, lo prometo."
            amigo "si tú lo dices solo recuerda que tenemos otra clase, dormilón."
            chico "Lo sé, Sebastián... pero tú también estabas en las mismas."
            "A pesar de sus palabras de ánimo, sabes que algo en ti está cambiando."
            "Te preguntas si realmente vale la pena seguir así."
            "Veo entrar a la maestra para dar inicio la siguiente clase."
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable. "
            chico "bueno a empezar con la siguiente materia."
            "Aunque sigo con sueño."

            hide maestra

            #Minijuego 3 agregar 

            #if juego == "gana":
                #show amigo
                #amigo "Muy facil"
                #chico "Es cierto"
            #elif juego == "pierde":
            show amigo
            amigo "bueno esta estuvo fácil ¿a que si dormilón?"
            chico "sí y deja de decirme dormilón."
            amigo "Tranquilo está bien."
            "Sebastián y tú están en clase, pero tu mente está en otro lugar."
            "Cada palabra que Sebastián menciona sobre Luna hace que te sientas más culpable."
            amigo "Siempre he sido cercano a Luna, pero últimamente no hemos pasado tiempo juntos como antes."
            chico "Podemos quedarnos esta vez, intentar recuperarlo."
            amigo "Sí, aunque hoy hay un festival... Tal vez podamos convencerla de que venga con nosotros."
            chico "Haré lo que pueda..."
            hide amigo
            $ estres = 30
            $ renpy.restart_interaction()
            menu:
                "convercerla de que se una.":
                    jump ConvencerlaC

                "No hacer nada.":
                    jump NadaLC
            
            
            
            #Ruta C
            label ConvencerlaC:
                "Estás muy cansado y estresado, pero aun así intentas convencer a Luna."
                chico "¿Luna, Sebastián y yo vamos a ir a un festival quieres unirte?"
                show amiga
                amiga "Deberías mejor descansar por hoy, pero diviértanse yo prefiero quedarme a repasar."
                chico "Gracias por la preocupación, te veré mañana."
                amiga "Hasta mañana."
                hide amiga 
                "Te sientes mal por no pasar tiempo con Luna y recordaste la preparatoria donde no convivías con prácticamente nadie."
                "veo mi vida en la prepa reflejada en ella pues no convivía mucho con mis compañeros. "
                $ estres = 45
                $ renpy.restart_interaction()
                #Continuar Historia
                scene escuela
                show amigo
                amigo " En serio te ves muy cansado, pero gracias por acompañarme. "
                chico "Estaré bien no te preocupes. "
                amigo "Me siento como un idiota ahora mismo."
                chico "¿Por qué lo dices?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que hay algo mal así que decido preguntarle."
                chico "¿Todo bien Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna para mi es mi mejor amiga pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "Mi madre nunca la conocí pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Intentó consolar a Sebastián pues su vida es muy dura. "
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces así que sé lo que siente Sebastián."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias [nombre] lo necesitaba sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chico "Sé lo que se siente, no poder agarrar fuerzas para seguir, pero debemos continuar adelante."
                hide amigo_triste
                show amigo
                amigo "Mejor regresemos y nos vemos mañana."
                chico "Muy bien."
                hide amigo
                scene negro
                "Sientes un dolor profundo y no sientes ánimos de continuar, pero la vida sigue adelante."
                "regresas a casa pensando en todo lo que pasó hoy."
                $ estres = 65
                $ renpy.restart_interaction()
                scene cuartonoche
                "te sientes muy cansado y te acuestas a dormir, pero no puedes de dejar de pensar en Luna."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tranquilo vale, en la vida hay ciertas decisiones que tomamos, pero lo mejor es afrontar las consecuencias que reprimirlas [nombre]."
                chico "Pero ¿cómo afrontarlas?"
                misterioso "En la vida, aunque queramos no podemos hacer todo en un día, pero siempre sé consciente de tus acciones."
                scene cuarto
                "Despiertas confuso, pero sigues pensando en luna."
                chico "¿Afrontar consecuencias?"
                scene chico_estres
                chico "Me llevo bien con Sebastián, pero porque me siento asi."
                chico "Pensar tanto en la Luna y la situación de Sebastián hace que no pueda concentrarme."
                chico "Vamos tú puedes con esto."
                scene cocina
                "Muy apenas te preparas algo para comer."
                scene negro
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
            scene escuela
            "Vamos anímate debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo_preocupado
            amigo "¡¡wow!! ¿estas bien [nombre]?"
            amigo "Te veo un poco mal."
            chico "Estoy bien no te preocupes."
            amigo "Oye deberías sacarlo todo yo lo hice ayer y me sentí mejor así que puedes decirme que pasa."
            chico "Yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado
            show amigo
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chico "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chico "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chico "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo un poco mal para que no se preocupe."
            chico "Tienes razón gracias."
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con luna mientras los observo."
            "Espero que todo esté bien entre ellos."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase."
            hide maestra
            "Sebastián Regresa a su asiento, después le preguntare como le fue."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "¿Cómo te fue con ella?"
            show amigo
            amigo "Aceptó así que nos veremos con ella este fin."
            chico "Me alegra oír eso."   
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Sin problemas."
                #amigo "Pues claro."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es y recuerda tranquilo vale."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            show amiga 
            amiga "Adiós [nombre] te veré allá entonces con Sebastián."
            chico "Te veo ahí."
            hide amiga 
            scene negro
            "Me retiro a mi casa a descansar esperando el fin de semana." 

            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Afrontar bien las consecuencias sigue así."
            "Te sientes confuso."
            "Aun no entiendo el propósito de esa sombra."
            "No importa, hoy la pasaré bien con mis amigos."
            scene parque 
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chico "Hola Sebastián."
            show amigo at left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros"
            amigo "Vamos amigo mucho ánimo ¿vale?"
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chico "¿Mejor?"
            amigo "Mucho mejor."
            " Luna aparece con un material para estudiar."
            show amiga at right
            amiga "Hola chicos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga
            hide amigo 
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chico "¿Qué pasa? "
            chico "¿Te sientes bien?"
            show amigo_triste 
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            chico " Deberías decirle lo que sientes por ella."
            amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
            "La soledad no es una buena opción." 
            "Debería darle apoyo para que se confiese o respeto su sentimiento de preocupación."
            hide amigo_triste

            menu:
                "Darle apoyo para que se confiese.":
                    jump finalC1

                "Respetar sus sentimientos de preocupación.":
                    jump finalC2





                    
            label finalC1:
                chico "Mira, la soledad no es buena y no es excusa puedes pasar más tiempo con ella estudiando juntos conociéndote más."
                chico "Es difícil Estudiar cuando uno está estresado y Solo, así que siempre es bueno tener a alguien en quien apoyarse."
                show amigo 
                amigo "¿Estás seguro de esto?"
                chico "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo 
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at left
                amigo "Luna…"
                show amiga at right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga 
                show amiga_triste at right
                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo
                hide amiga_triste
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at left
                show amiga at right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                hide amigo
                hide amiga 
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Hoy has sido testigo de un momento crucial."
                misterioso "Alentar a alguien a expresar sus sentimientos puede llevar a una conexión más profunda y genuina."
                misterioso "Pero recuerda, cada palabra tiene peso, y las emociones son delicadas."
                misterioso "Has ayudado a fortalecer un vínculo, pero asegúrate de que tus intenciones sean siempre sinceras."
                misterioso "Los lazos que formamos pueden ser nuestra mayor fortaleza o nuestra mayor debilidad."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label finalC2:
                chico "Si sientes eso en verdad te apoyo sea cual sea la decisión que tomes Sebastián."
                show amigo 
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chico "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo para lo que sea."
                show amigo at left 
                amigo "Volvimos."
                show amiga at right
                amiga "¿Todo bien?"
                chico "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chico "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Elegir el momento adecuado para hablar puede ser tan importante como las palabras mismas."
                misterioso "Has demostrado respeto por los sentimientos de los demás, comprendiendo que no siempre es necesario forzar las cosas."
                misterioso "A veces, el silencio puede ser una forma de sabiduría, permitiendo que las relaciones crezcan a su propio ritmo."
                misterioso "Pero recuerda, el miedo a lo desconocido no debe impedirnos avanzar. "
                misterioso "Cada oportunidad perdida puede convertirse en una pregunta sin respuesta."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return






            #Ruta Egoista
            label NadaLC:
                "Decides no hacer nada, el cansancio y la falta de energía te paralizan."
                chico "Lo siento, Sebastián... simplemente no puedo."
                show amigo_triste
                amigo "No te preocupes, vámonos entonces."
                hide amigo_triste
                "Ves a Luna sola, y en ella solo veo un reflejo de mí mismo." 
                "Algo en tu interior grita que actúes, pero el peso de tus malas decisiones te hunde más."
                $ estres = 55
                $ renpy.restart_interaction()
                #Continuar Historia
                scene escuela
                show amigo
                amigo "Te ves muy cansado... pero gracias por acompañarme."
                amigo " Aunque, la verdad, deberíamos haberla invitado."
                chico "Estaré bien... lo siento, Sebastián, de verdad lo siento."
                amigo "No te castigues tanto, debí ser yo quien la convenciera, no tú."
                "Mientras caminan por el festival, notas que Sebastián está más callado que de costumbre. Decides preguntarle qué le sucede."
                chico "¿Qué pasa, Sebastián?"
                "Sebastián se detiene y te mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna es mi mejor amiga. "
                amigo "Siempre ha estado ahí para mí, incluso cuando mi padre estaba decepcionado conmigo o cuando no tenía a nadie más."
                amigo "Ella me daba fuerzas... y ahora siento que la estoy perdiendo."
                "La confesión de Sebastián te golpea como un balde de agua fría."
                "Te das cuenta de que tus acciones no solo te han afectado a ti, sino también a las personas que te rodean."
                hide amigo_triste
                show amigo_preocupado
                chico "Sebastián... no estás solo. Lo que sea que necesites, estoy aquí."
                "Lo abrazas con fuerza, sintiendo la presión de las expectativas y la culpa arremolinándose dentro de ti."
                hide amigo_preocupado
                show amigo_triste
                amigo "Gracias, [nombre]. A veces es difícil continuar, pero al menos sé que te tengo a ti."
                hide amigo_triste
                scene negro
                "La culpa te golpea más fuerte pero resistes a que te observen decaer."
                "Debo resistir por mis amigos..."
                "Regresas a casa intentando despejar tu mente."
                $ estres = 80
                $ renpy.restart_interaction()
                #continuar 
                scene cuartonoche
                "Te sientes más agotado que nunca."
                "La culpa de no haber hecho más por Luna y Sebastián te pesa enormemente."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "¿Realmente crees que hiciste lo correcto?"
                misterioso "¿Este es el camino que elegiste?"
                chico "¿Quién eres?"
                chico "¿A qué te refieres?"
                misterioso "Si sigues así, deberás afrontar las consecuencias."
                scene cuarto
                "Despiertas con el corazón acelerado y el estrés a tope."
                "Las palabras de la voz resuenan en tu mente."
                chico "No puedo seguir así..."
                scene chico_estres
                chico "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                chico "Pensar tanto en Luna y la situación de Sebastián hace que no pueda concentrarme. "
                chico "Vamos tú puedes con esto."
                scene cocina
                "Muy apenas te preparas algo para comer."
                scene negro
                "¿No sé qué transporte tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren16

                    "Tomar Autobus":
                        jump Autobus16  
        label Tren16:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Llegare temprano aunque no se que hacer..."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "así tengo mas tiempo de pensar que hare... "
             
            jump DiaCC
        
        label Autobus16:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero quiero primero estar bien antes de verlos..."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Así tengo tiempo de pensar muy bien todo..."
             
            jump DiaCC








        label DiaCC:
            scene escuela
            " No es hora de pensar en eso debo de dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando, no quisiera molestarla después de que no hable con ella ayer."
            "Después de un tiempo veo llegar a Sebastián."
            chico "Hola Sebastián."
            show amigo_preocupado
            amigo "¡¡wow!! ¿estas bien [nombre]?"
            amigo "Te veo peor que ayer."
            chico "Estoy bien no te preocupes."
            amigo "¿Seguro?"
            chico "Si."
            amigo "Oye deberías sacarlo todo yo lo hice ayer y me sentí mejor así que puedes decirme que pasa."
            chico "Yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chico "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado
            show amigo
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chico "Entiendo, pero aun así debí apoyarte se que ella es importante para ti. "
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chico "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chico "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo muy mal para que no se preocupe."
            chico "Tienes razón gracias."
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos."
            amigo "Anímate todo saldrá bien."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Estuvo bien."
                #amigo "vez sí se pudo."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Esto es muy difícil."
                #amigo "Si."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con luna mientras los observo."
            "Espero que todo esté bien entre ellos, no quiero arruinar esto y estar solo otra vez."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase."
            hide maestra
            "Sebastián Regresa a su asiento, después le preguntare como le fue."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "Estuvo bien."
                #amigo "vez sí se pudo."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Esto es muy difícil."
                #amigo "Muy cierto."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chico "¿Cómo te fue con ella?"
            show amigo
            amigo "Aceptó así que nos veremos con ella este fin."
            chico "Me alegra oír eso."   
            amigo "también noto que te ves mal, intenta descansar para que este fin de semana sea agradable."
            chico "Lo intentare..."
            amigo "no te esfuerces mucho."
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chico "fue facil."
                #amigo "ves que sí."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chico "Esto es muy difícil."
                #amigo "Tienes razón, pero ya termino.""
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chico " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es y recuerda tranquilo vale."
            chico "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chico "Adiós Luna."
            "Observó su preocupación en mi cara, pero aun así decidí sonreírle."
            show amiga 
            amiga "Adiós [nombre] te veré allá entonces con Sebastián."
            chico "Te veo ahí."
            hide amiga 
            scene negro
            "Me retiro a mi casa a descansar esperando el fin de semana." 
            "Espero que todo salga bien la verdad."

            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Recuerda, tus decisiones te han llevado hasta aquí."
            "Te sientes confuso y abrumado."
            "Vaya, esa voz... ¿será mi conciencia?"
            "En fin, hoy solo me divertiré con mis amigos."
            scene parque 
            "Te sientas a esperar a Luna y Sebastián, sintiendo el peso de lo que está por venir."
            "Sebastián llega primero, y te saluda con su habitual energía."
            chico "Hola Sebastián."
            show amigo at left
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
            show amiga_preocupada at right
            amiga "¿Están bien los dos?"
            "Sebastián le da un pulgar arriba, ocultando la verdad de tu estado."
            amigo "Solo le duele la cabeza a [nombre], no es nada grave."
            "Me susurra al oído."
            amigo "Te apoyo en lo que decidas."
            chico "Gracias, Sebastián..."
            "Te das cuenta de que, aunque ellos se preocupan por ti, tú no has hecho nada por ellos."
            "Ahora enfrentas la decisión final hacer un último esfuerzo o retirarte de la Universidad."
            "Los dos te observan, esperando tu respuesta."
            hide amiga_preocupada
            hide amigo 
            

            menu:
                "Hacer un último esfuerzo.":
                    jump finalCC1

                "Retirarse de la Universidad.":
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
                show amiga_preocupada at left
                amiga "Tranquilo no nos has decepcionado y me alegra que me hayas dicho cómo te sientes."
                hide amiga_preocupada
                show amiga at left
                amiga "Gracias Sebastián por estar al pendiente como siempre estuviste de mi"
                show amigo at right
                amigo "Una amistad grande jamás abandona a sus amigos en las buenas o en las malas."
                chico "Gracias amigos."
                "Sientes un peso menos, pero la culpa no se irá fácilmente."
                "Me abrazan más fuerte y correspondiendo regresando un abrazo más fuerte."
                amiga "Toda ira bien ya lo veras."
                amigo " si te apoyaremos en lo que sea."
                "Los 3 nos quedamos estudiando, aunque no me preocupaba el examen, pero si estar con mis amigos y no volver a decepcionarlos."
                "Las decisiones que tome tardaran en sanar pues lo que hice no fue bueno ahora se a que se refería esa sombra."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Aun con las consecuencias al final desiste enfrentarte a ellas."
                misterioso "No todo es caso perdido lo importante es nunca rendirse los errores nos hacen más fuerte."
                misterioso "Es bueno tener amistades en momentos difíciles pues ellos siempre te darán apoyo y más si pasan por las mismas situaciones."
                misterioso "Recuerda estar preparado para entrar a la Universidad y disfrutar de ella con amigos, espero que esto te sirva para que siempre seas consciente de tus acciones."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label finalCC2:
                "Con lágrimas y un fuerte dolor en el pecho, decides decirles que te vas de la universidad."
                " Sebastián y Luna me miran preocupados, la sorpresa se refleja en sus rostros."
                show amiga_preocupada at left
                show amigo_preocupado at right
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
                hide amiga_preocupada
                hide amigo_preocupado
                show amiga_triste at left
                show amigo_triste at right
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
                hide amiga_triste
                hide amigo_triste
                show amiga at left
                show amigo at right
                "Ambos me devuelven la sonrisa, aunque se nota la tristeza en sus ojos."               
                "Sebastián y Luna" "Adios [nombre] cuidate mucho."
                hide amigo
                hide amiga
                "Me alejo de ellos, regresando solo a mi casa, sintiendo el vacío en cada paso."
                scene cuarto
                "Te acuestas en la cama, reflexionando sobre lo sucedido."
                chico "No pude con la presión."
                chico "Este peso es insoportable, pero no puedo huir para siempre."
                chico "Esta ansiedad es horrible."
                chico "Volveré…" 
                "Luna, Sebastián… les prometo volver."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has pasado por un momento muy difícil, pero recuerda, rendirse nunca es una opción."
                misterioso "El estrés y la ansiedad pueden ser abrumadores, pero siempre es mejor buscar ayuda que enfrentarlo solo."
                misterioso "Espero que nunca tengas que tomar una decisión tan dolorosa, pero si alguna vez te encuentras en una situación así, recuerda que no estás solo."
                misterioso "Siempre hay alguien dispuesto a ayudarte."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


        #Decisión Luna
        label Estudiar:
            $ estres = 25
            $ renpy.restart_interaction()
            show amigo
            amigo "como gustes."
            hide amigo
            "Te quedaste estudiando con Luna fue estresante, pero al menos aprendiste."    
            show amiga 
            "Gracias por quedarte."
            hide amiga 
            scene negro
            "Regreso a mi casa algo cansado."
            scene cuartonoche
            "Fue un buen primer día."
            "¿Debería dormirme ya? o ¿juego videojuegos un rato?"
        menu:
            "Dormir.":
                jump descansado2

            "Jugar video juegos.":
                jump cansado2     
        # Ruta B
        label descansado2:
            $ estres = 15
            $ renpy.restart_interaction()
            scene cuartonoche
            chico "Bueno lo mejor será descansar para mañana tener energía."
            scene negro
            "Te acuestas a dormir temprano recuperando energía para el siguiente día."
            scene cuarto
            "Te despiertas con energía y descansado."
            scene wc
            "Te sientes con mucha energía de ver que pasara hoy."   
            scene chico_normal
            chico "¡aahhh! Que bien me siento."    
            chico "Hora de ir a la Universidad."    
            scene cocina
            "Desayunas lo primero que te hallaste y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren4

                "Tomar Autobus":
                    jump Autobus4  
        label Tren4:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
              
            jump RutaB
        
        label Autobus4:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
              
            jump RutaB   



        #Ruta B
        label RutaB:
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            show amiga
            amiga "¿Listo para continuar?"    
            chico "Claro que sí."
            amiga "Te ves muy concentrado esto va a ser muy fácil."
            chico "Sí, gracias por ayudarme a practicar."
            hide amiga
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro
            chico "Estoy preparado."
            #Agregar Minijuego 2
            #if juego == "gana":
            chico "Eso fue fácil muchas gracias Luna."
            #elif juego == "pierde":
                #chico "Esta clase fue estresante, pero logré salir adelante."
            show amiga
            amiga "Sabes estamos para apoyarnos."
            $ estres = 5
            $ renpy.restart_interaction()
            amiga "Estuviste excelente [nombre]."
            chico "Todo gracias a ti Luna por ayudarme a practicar."
            amiga "un placer es mejor para mi practicar con alguien. "
            hide amiga
            "quien sabe cómo me habría ido si no hubiera dormido temprano."
            "Oh, aquí viene la nueva maestra."
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable."
            chico "bueno a empezar con la siguiente materia."
            hide maestra
            #Minijuego 3 agregar 

            #if juego == "gana":
            show amiga
            amiga "Bueno, bueno explica muy bien la maestra. "
            chico "Sí, tienes razón."
            #elif juego == "pierde":
                #chico "Estuvo complicado."
            amiga "sigo preocupada por Sebastián seguro tuvo problemas en la anterior. "
            chico "tienes razón ahora hay que convencerlo de que practique con nosotros."
            amiga "Buena suerte con eso."
            hide amiga

            menu:
                "convencerlo de que se te una.":
                    jump ConvencerB

                "No hacer nada.":
                    jump NadaB
            
            
            
            
            #Ruta B
            label ConvencerB:
                chico "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo
                amigo "Pero habrá un festival…"
                chico "Vamos hazlo por mí y por Luna."
                amigo " Está bien, el festival puede esperar."
                chico "No te arrepentirás."
                hide amigo
                $ estres = 10
                $ renpy.restart_interaction()
                #Continuar Guion
                "Nos quedamos con luna parecía muy feliz."
                show amiga at left
                amiga "Gracias por acompañarme chicos."
                show amigo at right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto, nos va a servir mucho." 
                hide amigo
                hide amiga
                "Pasa el tiempo y estudiamos un rato mas con Luna."
                "Observó cómo Sebastián se retira para ir al festival, pero decidió acompañar un rato más a Luna."
                show amiga
                amiga "[nombre], ¿puedo decirte algo?"
                chico " Claro Luna."
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chico "Sé cómo te sientes Luna y te comprendo."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chico "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga 
                $ estres = 5
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche
                "Te acuestas a dormir feliz por las amistades que has hecho."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Vas por buen camino [nombre]."
                "Sientes una presencia, pero te sientes calmado."
                chico "¿Eres mi conciencia?"
                misterioso "Solo te observare, vas por buen camino."
                scene cuarto
                "Despiertas confuso pero calmado a la vez."
                chico "¿Qué o quién era esa voz? "
                chico "¿Buen camino?"
                scene chico_normal
                chico "Nunca pensé estar tan calmado desde lo de la preparatoria. "
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren18

                    "Tomar Autobus":
                        jump Autobus18  
        label Tren18:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción"  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump DiaB
        
        label Autobus18:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump DiaB








        label DiaB:
            scene escuela
            chico "Hoy espero volver a pasar tiempo con luna y Sebastián."
            scene salon
            chico "Hola amigos ¿cómo están?"
            show amiga at right 
            amiga "Hola, me siento mucho mejor, gracias. Espero que tú también, [nombre]."
            show amigo at left
            amigo "Bien también, ¿y tú cómo estás, [nombre]?"
            chico " Muy bien ¿hoy vamos a quedarnos a repasar verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Si será lo mejor."
            "Empieza la clase."
            chico "¿Hoy tendremos 3 clases verdad?"
            amiga "Según el horario sí."
            chico "Vale gracias Luna."
            hide amigo
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "fue facil."
                #amiga "Eso es verdad."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDiaB

                "Quedarse Callado.":
                    $ Luna = "Callarse"
                    jump cDiaB


            label cDiaB:
                if Luna == "preguntar":
                    chico "Luna como has estado."
                    "Decido abrazarla por lo que pasó ayer."
                    show amiga at right
                    amiga "Me he sentido mejor Gracias por preguntar."
                    show amigo at left
                    amigo "¿aún preocupada Luna?, eres lista y tú puedes con todo."
                    amiga "Gracias a ambos por el apoyo."
                    amiga "Sin ustedes no sé qué haría."
                    hide amiga
                    hide amigo




                elif Luna == "Callarse":  
                    "Te quedas callado, pero te quedas cerca de ella."
                    chico "No tengo palabras ahorita, pero tienes mi apoyo Luna."
                    show amiga at right
                    amiga "Gracias, lo aprecio mucho."  
                    show amigo at left
                    amigo "también estoy aquí y me quedaré contigo Luna."
                    amiga "Gracias a ambos de verdad."
                    hide amiga
                    hide amigo

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Genial muy fácil."
                #amiga "Practicando todo se logra."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más [nombre]."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at left
            amigo "vaya un fin de semana no puede ser que ya tengamos exámenes."
            show amiga at right
            amiga "Lo sé, pero esto ya es la Universidad, siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno ya lo veremos el fin de semana."
            chico "A puesto que será divertido quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chico "Entonces no se diga más nos veremos en el parque."
            hide amigo
            hide amiga
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Eso estuvo difícil."
                #amiga "No te rindas  [nombre]."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chico "Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amiga at right
            amiga "muy bien los veré ahí."
            show amigo at left
            amigo "igual nos veremos allí."
            hide amiga
            hide amigo
            scene cuarto
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            
            scene negro
            "Es la primera vez que estoy muy relajado, Estudiar con amigos es mejor que solo ya que aprendes más."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Recuerda, vas por buen camino."
            "Te sientes confuso pero calmado."
            chico "Buen camino ¿eh?"
            "Mejor me concentro en pasarla bien con mis amigos."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
            chico "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chico "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chico "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            "Este es mi momento para poder juntarme con los 2 y no volver a pasar lo de la preparatoria."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump finalB1

                "Quedarse con Luna.":
                    jump finalB2

            label finalB1:
                show amiga at right
                show amigo at left
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
                hide amigo
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tomaste una decisión correcta e hiciste muy buenos amigos."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estas muy preparado para entrar a la universidad y hacer buenos amigos."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            label finalB2:
                chico "Yo prefiero quedarme a estudiar un poco más."
                "No puedo dejar a Luna sola es mejor darle mi apoyo."
                show amigo at left
                amigo "Entiendo, bueno, no importa, los veré después."
                show amiga at right
                amiga "No tienes que irte ahora puedes quedarte."
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián me susurra."
                amigo "Cuida de ella, [nombre], ¿vale? Haz la diferencia por mí vale."
                "Lo miras directamente, haciendo un gesto de afirmación."
                hide amigo
                hide amiga
                "Sebastián se retira dejándonos solos a Luna y a ti."
                chico "Tranquila, Luna, tienes mi apoyo."
                chico "Después de esto lo veremos y te ayudaré, ¿vale? Debemos permanecer juntos."
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chico "Gracias Luna."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga
                "Ambos nos quedamos estudiando, pero debí convencerlo para que luna estuviera mejor."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Es bueno apoyar a un amigo, pero es mejor cuando puedes hacer más de una diferencia mientras menos estés estresado mejor manejaras los problemas."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparado para la Universidad, pero debes tener en cuenta las acciones que tomas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return













            #Ruta B,B
            label NadaB:
                "Decides no hacer nada y seguir practicando con Luna, parece preocupada aún."
                chico "Lo siento Luna."
                show amiga_preocupada
                amiga "no pasa nada [nombre]."
                hide amiga_preocupada
                $ estres = 15
                $ renpy.restart_interaction()
                #Continuar Guion
                "Me quedo con Luna mientras observo cómo Sebastián se va al festival."
                show amiga
                amiga "Gracias por quedarte, [nombre]."
                chico "A ti, Luna por ayudarme."
                amiga "[nombre], ¿puedo decirte algo?"
                chico "Claro Luna."
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chico "Sé cómo te sientes Luna y te comprendo."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chico "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga 
                "Me siento mal porque sé que pude haber convencido a Sebastián."
                $ estres = 25
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche
                chico "pude haberlo convencido."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso " Luna confía mucho en ti [nombre] no lo eches a perder."
                "Veo una sombra acechándome en el fondo. "
                chico "¿Quién eres?"
                "Veo como se desvanece dejándome con la duda."
                chico "¿Qué o quién era esa voz?"
                scene cuarto
                "Despiertas con un sentimiento de culpa."
                chico "Tranquilízate solo fue un sueño."
                scene chico_normal
                chico "Solo fue un sueño, hoy veré que Luna esté bien."
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren19

                    "Tomar Autobus":
                        jump Autobus19  
        label Tren19:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción"  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump DiaBB
        
        label Autobus19:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump DiaBB








        label DiaBB:
            scene escuela
            chico "Sé que pude haber convencido a Sebastián."
            chico "No quisiera ser responsable de que Luna se distancie de él."
            scene salon
            "Veo a Luna preocupada aún."
            chico "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga 
            amiga "No te preocupes, Sebastián siempre sale desde la preparatoria, así que estoy acostumbrada."
            chico "Sé que es importante estudiar, pero es bueno salir con personas."
            chico "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar solo."
            amiga "¿Estás bien, [nombre]?"
            chico "Si estoy bien gracias."
            "Veo a Sebastián saludarnos de lejos pero no se ve feliz."
            "Hoy tendremos 3 clases." 
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Salió bien."
                #amiga "Si."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Pudo ser peor."
                #amiga " Práctica más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDiaBB

                "Quedarse Callado.":
                    $ Luna = "Callarse"
                    jump cDiaBB


            label cDiaBB:
                if Luna == "preguntar":
                    chico "Luna ¿estás bien?"
                    show amiga 
                    amiga "Solo estoy preocupada, no quiero que Sebastián piense que lo deje atrás pues él sabe mi situación."
                    "Decido abrazarla fuerte."      
                    chico "Todo estará bien ya lo veras. "
                    amiga "Eso espero. "
                    hide amiga
                    




                elif Luna == "Callarse":  
                    "Un incómodo silencio nos invadió a ambos. "
                    "Intentas calmar a Luna."
                    chico "Cualquier cosa aquí estaré Luna."
                    show amiga 
                    amiga "Lo sé…"  
                    hide amiga
                    "Decido darle ánimo a Luna."
                    

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Genial muy fácil."
                #amiga "Me alegro por ti."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Vaya que si tuve dificultades."
                #amiga "Deberías practicar más."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            "pero notas que Luna está cada vez más desanimada."
            chico "Animo Luna este fin de semana hay que reunirnos con Sebastián en el parque para que te animes ¿qué te parece?"
            show amiga
            amiga "No es mala idea, gracias por preocuparte mucho por mi [nombre]."
            chico "Entonces este fin iremos al parque."
            amiga "Muy bien."

            hide amiga
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Eso estuvo difícil."
                #amiga "Tienes mi apoyo."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chico "Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amiga at right
            amiga "muy bien los veré ahí."
            hide amiga
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chico "Hola Sebastián, Luna y yo nos vamos a reunir este fin de semana ¿te unes?"
            show amigo
            amigo "Claro que sí los veré a los 2 entonces."
            hide amigo
            "Me despido de él regresando a mi casa."
            scene cuarto
            "Al final salió bien, espero que todo salga bien este fin de semana."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso " Ella aún confía en ti."
            "Te sientes menos culpable ya que conviviste con ambos."
            chico "¿Seguiré Dormido?"
            "No creo mejor no pensar en ello y concentrarme para pasarla bien con ellos."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
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
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump finalBB1

                "Quedarse con Luna.":
                    jump finalBB2

            label finalBB1:
                show amiga at right
                show amigo at left
                chico "Sebastián esta vez quiero decirte que te quedes con nosotros, la vez del festival no sé por qué no pude hacerlo."
                amigo "No te preocupes se lo que se siente no poder decidir."
                chico "Aun así lo siento, Luna necesita apoyo así que esta vez acompáñanos."
                amigo " Está bien y no te preocupes es hora de pasar tiempo con ustedes esta vez."
                amiga "Gracias a ambos por quedarse conmigo y más en estos tiempos."
                "Los junto a los 2 para estar más juntos."
                chico "La soledad nunca es buena."
                "Sebastián y Luna" "Estamos de acuerdo contigo."
                hide amigo
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos, aunque me costó trabajo."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Las decisiones que tomamos siempre tienen una solución, nunca hay que quedarnos aferrados a nuestro pasado."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparado para la Universidad, aunque al principio te equivoques recuerda que todo problema tiene una solución y jamás te rindas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            label finalBB2:
                "Me vuelvo a quedar sin palabras para convencerle."
                chico "Yo prefiero quedarme a estudiar un poco más."
                "Luna necesita apoyo ahora más que nunca ahora que se su pasado."
                show amigo at left
                amigo "Entiendo bien, no importa los veré después…"
                show amiga at right
                amiga "Sebastián…"
                amigo "No te preocupes es como en los viejos tiempos diviértanse los 2."
                "Sebastián me susurra."
                amigo "Si de verdad somos amigos cuidaras bien de ella ¿Vale?"
                "Decido abrazarlo por la culpa que cargo y le susurro también."
                chico " Lo siento no te fallare te lo prometo."
                "Sebastián corresponde el abrazo y más calmado se retira."
                hide amigo
                chico "Lo siento Luna te he vuelto a fallar."
                amiga "No te preocupes, pero me ayudaras a convivir más con el."
                chico "Te lo prometo."
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez Luna."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chico "Gracias Luna."
                    chico "No te fallare."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga
                "Ambos nos quedamos estudiando."
                "Debo cumplir con estas promesas."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Las decisiones que tomamos, aunque nos equivoquemos muchas veces podemos resolverlas tardarán más, pero siempre tienen solución."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Siempre que tengas dificultades con una amistad intenta resolverlo de la mejor manera pues una amistad te da más oportunidades en la vida y también nos pueden ayudar a reducir el estrés que tenemos."
                misterioso "Si entras a la universidad ten en cuenta todas las posibilidades."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return











        # Ruta A        
        label cansado2:
            $ estres = 20
            $ renpy.restart_interaction()
            scene cuartonoche
            chico "Bueno, una partida no hará ningun daño."
            scene negro
            "juegas unas cuantas partidas y pierdes la noción del tiempo."
            scene cuarto
            "Despiertas con dificultad, sintiendo mucho sueño."
            scene wc 
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chico_normal
            "Te miras al espejo, tratando de reconocer a la persona reflejada."
            chico "Creo que me sobrepasé un poco…"
            "Suspiro."
            chico "Bueno, diría que demasiado... Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina
            "Desayunas lo primero que te hallaste y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren9

                "Tomar Autobus":
                    jump Autobus9  
        label Tren9:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
              
            jump RutaA
        
        label Autobus9:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
            
            jump RutaA   
       
       
       
        #Ruta A
        label RutaA:
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            show amiga
            amiga "¿Listo para continuar?"    
            chico "Claro que sí."
            amiga "¿Te sientes bien, te ves un poco cansado?"     
            chico "Si estoy bien no te preocupes."       
            hide amiga
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro 
            "Oh no, tengo mucho sueño."
            #Agregar Minijuego 2
            #if juego == "gana":
                #chico "Eso fue fácil muchas gracias Luna."
            #elif juego == "pierde":
            chico "Rayos, casi no me pude concentrar bien, pero gracias a Luna no fue tan mal."
            $ estres = 15
            $ renpy.restart_interaction()
            show amiga
            amiga "vamos anímate no estuvo tan mal."
            chico "Bueno si tú lo dices, esperemos que en la siguiente vaya mejor."
            amiga "ya verás que sí."
            hide amiga
            "sigo un poco cansado, pero veo que entra la maestra."
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable."
            chico "bueno a empezar con la siguiente materia."
            hide maestra
            #Minijuego 3 agregar 

            #if juego == "gana":
            show amiga
            amiga "Bueno, bueno explica muy bien la maestra. "
            chico "Sí, tienes razón."
            #elif juego == "pierde":
                #chico "Estuvo complicado."
            amiga "sigo preocupada por Sebastián seguro tuvo problemas en la anterior. "
            chico "tienes razón ahora hay que convencerlo de que practique con nosotros. "
            amiga "Buena suerte con eso."
            hide amiga
            menu:
                "Convencerlo de que se te una.":
                    jump ConvencerA

                "No hacer nada.":
                    jump NadaA


            #Ruta A
            label ConvencerA:
                chico "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo
                amigo "Pero habrá un festival."   
                chico "Vamos hazlo por mí y por Luna."     
                amigo "Te ves muy cansado, pero está bien, me uniré a ustedes." 
                amigo "El festival puede esperar."
                chico "No te arrepentirás."
                hide amigo 
                $ estres = 20
                $ renpy.restart_interaction()
                #Continuar guion 
                "Nos quedamos con luna parecía muy feliz."
                show amiga at left
                amiga "Gracias por acompañarme chicos."
                show amigo at right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto, nos va a servir mucho." 
                hide amigo
                hide amiga
                "Pasa el tiempo y estudiamos un rato mas con Luna."
                "Observó como Sebastián se retira para ir con lo que quedó del festival, pero decido acompañar un rato más a Luna."
                show amiga
                amiga "[nombre], ¿puedo decirte algo?"
                chico " Claro Luna."
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chico "Sé cómo te sientes Luna y te comprendo."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chico "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga 
                $ estres = 15
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche
                "Te acuestas a dormir porque te sentías muy cansado, pero a pesar de todo, el día salió bien."
                "Mientras tus ojos se cierran, tu mente repasa las últimas horas... algo se siente fuera de lugar, pero decides no pensar demasiado en ello."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Vas muy bien [nombre]."
                "En tu sueño, una figura borrosa y oscura se hace presente, una extraña sombra se desplaza hacia ti."
                chico "¿Quién eres?"
                misterioso "Sigue por el camino que vas y no te desvíes."
                "La sombra se desvanece antes de que puedas obtener más respuestas, dejándote con una sensación de inquietud."
                scene cuarto
                " Te despiertas sobresaltado y con la mente llena de preguntas, pero te das cuenta de que ya no te sientes cansado."
                chico "¿Qué habrá sido esa cosa?  "
                " Intentas deshacerte del recuerdo del sueño, diciéndome que es mejor no pensar en ello."
                scene chico_normal
                chico "Hoy va a ser un buen día, mejor dejar atrás esos pensamientos extraños."
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren20

                    "Tomar Autobus":
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
            scene escuela
            chico "Hoy espero volver a pasar tiempo con luna y Sebastián."
            scene salon
            "Veo a Luna y a Sebastián reunidos y me decido a saludarlos."
            chico "Hola amigos ¿cómo están?"
            show amiga at right 
            amiga "Hola [nombre], te ves mejor que ayer y bien espero que tú también."
            show amigo at left
            amigo "Si opino lo mismo y también bien ¿y tú como estas?"
            chico " Muy bien ¿hoy vamos a quedarnos a repasar verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Si será lo mejor."
            "Empieza la clase."
            chico "¿Hoy tendremos 3 clases verdad?"
            amiga "Según el horario sí."
            chico "Vale gracias Luna."
            hide amigo
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "fue facil."
                #amiga "Eso es verdad."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDiaA

                "Quedarse Callado.":
                    $ Luna = "Callarse"
                    jump cDiaA


            label cDiaA:
                if Luna == "preguntar":
                    chico "Luna como has estado."
                    "Decido abrazarla por lo que pasó ayer."
                    show amiga at right
                    amiga "Me he sentido mejor Gracias por preguntar."
                    show amigo at left
                    amigo "¿aún preocupada Luna?, eres lista y tú puedes con todo."
                    amiga "Gracias a ambos por el apoyo."
                    amiga "Sin ustedes no sé qué haría."
                    hide amiga
                    hide amigo




                elif Luna == "Callarse":  
                    "Te quedas callado, pero te quedas cerca de ella."
                    chico "No tengo palabras ahorita, pero tienes mi apoyo Luna."
                    show amiga at right
                    amiga "Gracias, lo aprecio mucho."  
                    show amigo at left
                    amigo "también estoy aquí y me quedaré contigo Luna."
                    amiga "Gracias a ambos de verdad."
                    hide amiga
                    hide amigo

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Genial muy fácil."
                #amiga "Practicando todo se logra."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más [nombre]."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at left
            amigo "vaya un fin de semana no puede ser que ya tengamos exámenes."
            show amiga at right
            amiga "Lo sé, pero esto ya es la Universidad, siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno ya lo veremos el fin de semana."
            chico "A puesto que será divertido quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chico "Entonces no se diga más nos veremos en el parque."
            hide amigo
            hide amiga
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Eso estuvo difícil."
                #amiga "No te rindas  [nombre]."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chico "Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amiga at right
            amiga "muy bien los veré ahí."
            show amigo at left
            amigo "igual nos veremos allí."
            hide amiga
            hide amigo
            scene cuarto
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            
            scene negro
            "Es la primera vez que estoy muy relajado, Estudiar con amigos es mejor que solo ya que aprendes más."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Recuerda vas muy bien."
            "Te sientes confuso."
            chico "¿Otra vez?"
            "Bueno no importa debo estar concentrado."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
            chico "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chico "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chico "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump finalA1

                "Quedarse con Luna.":
                    jump finalA2

            label finalA1:
                show amiga at right
                show amigo at left
                chico "Sebastián, podemos dejarlo para otro fin de semana."
                chico "Hoy hay que darle todo el apoyo a Luna."
                amigo "Tienes razón, es momento de saber cuándo hay que divertirse y cuándo hay que apoyar en momentos difíciles."
                amiga "Gracias por quedarte esta vez Sebastián."
                amiga "Y a ti, [nombre], por ayudarme."
                hide amigo
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tomaste una decisión correcta al principio te desviaste, pero ahora sabes cuando es el momento para divertirse y cuando dedicarle tiempo al estudio."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estas muy preparado para entrar a la universidad y hacer buenos amigos."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                

            label finalA2:
                chico "Yo prefiero quedarme a estudiar un poco más."
                "Recuerdo lo que Luna me contó sobre su pasado, y sé que necesita apoyo ahora más que nunca."
                show amigo at left
                amigo "Entiendo... no importa, los veré después."
                show amiga at right
                amiga "Sebastián…"
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián se acerca y me susurra al oído."
                amigo "Cuida de ella, [nombre], ¿vale?"
                "Lo miras directamente, haciendo un gesto de afirmación, sintiendo el peso de su petición."
                hide amigo
                hide amiga
                "Al verlo marcharse, me quedo pensando si realmente tomé la decisión correcta."
                "Pero no quiero que Luna se sienta sola, así que dejo esos pensamientos de lado."
                chico "Tranquila, Luna, tienes mi apoyo."
                chico "Después de esto lo veremos y te ayudaré, ¿vale?"
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudar."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chico "Gracias Luna."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga
                "Aunque me quedo con Luna para estudiar, no puedo evitar que, en el fondo de mi mente, una pequeña duda me siga preguntando por qué no convencí a Sebastián de quedarse también."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Es bueno apoyar a un amigo, pero es mejor cuando puedes hacer más de una diferencia mientras menos estés estresado mejor manejaras los problemas."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparado para la Universidad, pero debes tener en cuenta las acciones que tomas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return    






            #Ruta A,A
            label NadaA:
                "Decides no hacer nada y seguir practicando con Luna, quien parece estar preocupada aún."
                chico "Lo siento Luna."  
                show amiga_preocupada
                amiga "no pasa nada [nombre]."
                hide amiga_preocupada
                $ estres = 30
                $ renpy.restart_interaction()
                #Continuar guion 
                "Decides quedarte con Luna mientras observas cómo Sebastián se va al festival."
                "Te sientes realmente cansado."
                show amiga
                amiga "Gracias por quedarte, [nombre]."
                chico "A ti, Luna por ayudarme."
                amiga "[nombre], ¿puedo decirte algo?"
                chico "Claro Luna."
                amiga "Quería agradecerte por acompañarme."
                amiga "Esto significa mucho para mí."
                "Ves a Luna un poco triste y decides preguntar qué le sucede. "
                chico "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre]."
                amiga "Gracias por estar aquí."
                chico "Entiendo cómo te sientes, Luna."
                chico "Estoy aquí para ti."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chico "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga 
                "Te sientes mal porque sabes que pudiste haber convencido a Sebastián, pero el cansancio te supera."
                $ estres = 45
                $ renpy.restart_interaction()
                #Continuar historia
                scene cuartonoche
                chico "pude haberlo convencido, pero estaba muy cansado..."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso " Sabes que pudiste hacer algo, ¿no crees?"
                "Veo una sombra acechándome en el fondo. "
                chico "¿Quién eres?"
                "Solo veo como me observa y se desvaneció dejándome una sensación de culpabilidad."
                scene cuarto
                " Despiertas nervioso."
                chico "¿Solo fue un sueño?"
                "Aun te sientes culpable, pero intentas deshacerte del recuerdo del sueño, diciéndote que es mejor no pensar en ello."                
                scene chico_normal
                chico "Espero que Luna esté bien. "
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren21

                    "Tomar Autobus":
                        jump Autobus21  
        label Tren21:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump DiaAA
        
        label Autobus21:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump DiaAA








        label DiaAA:
            scene escuela
            chico "Sé que pude haber convencido a Sebastián."
            chico "No quisiera ser responsable de que Luna se distancie de él."
            scene salon
            "Veo a Luna preocupada aún."
            chico "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga 
            amiga "No te preocupes [nombre], Sebastián siempre sale desde la preparatoria, así que estoy acostumbrada."
            chico "Sé que es importante estudiar, pero es bueno salir con personas."
            chico "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar solo."
            amiga "¿Estás bien, [nombre]?"
            chico "Si estoy bien gracias."
            "Veo a Sebastián saludarnos de lejos pero no se ve feliz."
            "Hoy tendremos 3 clases." 
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chico "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Salió bien."
                #amiga "Si."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Esto salió fatal."
                #amiga " Práctica más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDiaAA

                "Quedarse Callado.":
                    $ Luna = "Callarse"
                    jump cDiaAA


            label cDiaAA:
                if Luna == "preguntar":
                    chico "Luna ¿estás bien?"
                    show amiga 
                    amiga "Solo estoy preocupada, no quiero que Sebastián piense que lo deje atrás pues él sabe mi situación."
                    "Decido abrazarla fuerte."      
                    chico "Todo estará bien ya lo veras. "
                    amiga "Eso espero. "
                    hide amiga
                    




                elif Luna == "Callarse":  
                    "Un incómodo silencio nos invadió a ambos. "
                    "Intentas calmar a Luna."
                    chico "Cualquier cosa aquí estaré Luna."
                    show amiga 
                    amiga "Lo sé…"  
                    hide amiga
                    "Decido darle ánimo a Luna."
                    

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Genial muy fácil."
                #amiga "Me alegro por ti."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Vaya que si tuve dificultades."
                #amiga "Deberías practicar más."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            "pero notas que Luna está cada vez más desanimada."
            chico "Animo Luna este fin de semana hay que reunirnos con Sebastián en el parque para que te animes ¿qué te parece?"
            show amiga
            amiga "No es mala idea, gracias por preocuparte mucho por mi [nombre]."
            chico "Entonces este fin iremos al parque."
            amiga "Muy bien."

            hide amiga
            "Observó cómo Luna se veía más calmada."
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chico "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chico "Eso estuvo difícil."
                #amiga "Tienes mi apoyo."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chico "Bueno, nos reuniremos en el parque para pasar tiempo juntos."
            show amiga at right
            amiga "muy bien los veré ahí."
            hide amiga
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chico "Hola Sebastián, Luna y yo nos vamos a reunir este fin de semana ¿te unes?"
            show amigo
            amigo "Claro que sí los veré a los 2 entonces."
            hide amigo
            "Me despido de él regresando a mi casa."
            scene cuarto
            "Al final salió bien, espero que todo salga bien este fin de semana."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Ahora puedes hacer la diferencia."
            "Te sientes menos culpable, pero confuso."
            chico "¿Otra vez el?"
            "Bueno, debo estar concentrado."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
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
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chico "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez, debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump finalAA1

                "Quedarse con Luna.":
                    jump finalAA2

            label finalAA1:
                show amiga at right
                show amigo at left
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
                hide amigo
                hide amiga
                "Pasan la tarde juntos, disfrutando del tiempo como amigos y estudiando. "
               
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chico "No te preocupes me alegra ayudarte esta vez."
                    chico "Es mejor apoyarnos en momentos de estudios."
                    chico "Es malo estar solo tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."

                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    hide amiga

                "Es mejor estudiar con amigos que pasarla solo y hoy hice 2 grandes amigos, aunque me costó trabajo."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Pudiste hacer la diferencia esta vez [nombre] te desviaste a la hora de tomar en cuenta los sentimientos de Luna, pero al final lo resolviste de la mejor manera."
                misterioso "Nunca te sientas solo, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparado para la Universidad, aunque al principio te equivoques recuerda que todo problema tiene una solución."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            label finalAA2:
                "Me siento mal al no volver a convencer a Sebastián, pero con pocos ánimos respondo."
                chico "Lo siento, Sebastián."
                chico "Creo que esta vez me quedaré con Luna. "
                "No quiero que se quede sola."
                show amigo at left
                amigo "Lo entiendo, no te preocupes."
                amigo "Me reuniré con otros amigos entonces."
                show amiga at right
                amiga "Sebastián…"
                hide amigo
                "Ves cómo Sebastián se va, dejándote con Luna."              
                amiga "Gracias por quedarte conmigo, [nombre]."
                chico "Lo haré siempre que lo necesites, Luna."
                hide amiga
                "Pasan la tarde estudiando juntos, aunque sientes un poco de tristeza por no haber salido con Sebastián."
                "Luna parece estar un poco más tranquila, pero sabes que aún queda mucho por superar."
                "Decides tomar un descanso después de un largo día de estudio."
                if Luna == "preguntar":
                    show amiga
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
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía y el apoyo que me das."
                    chico "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigos."
                    amiga "Veremos a Sebastián después de repasar."
                    chico "Lo mejor sera darle espacio."
                    amiga "Si tiene razón [nombre]."
                    hide amiga
                
                "Estás satisfecho de haber apoyado a Luna, pero también sabes que aún hay retos por enfrentar."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Siempre hay que ser conscientes antes de tomar decisiones. "
                misterioso "Antes de tomar una acción piensa a futuro alejaste a Sebastián de Luna y esto siempre puede traer mal entendidos."
                misterioso "Solo se consciente y recuerda si estás a punto de entrar a la Universidad o estás en ella has buenas amistades la soledad nunca es una buena opción. "
                misterioso "Mucha suerte."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return







# Division Chica
elif genero == "chica":
        
        chica "Este es mi salón."    
        chica "Bueno me sentaré aquí.   "
        desconocido "Hola, ¿cómo estás? "
        chica "Hola, bien ¿y tú cómo estás?"
        show amiga at left
        desconocido "Bien también, Soy Luna."
        chica "Un placer me llamo [nombre]."
        "Espero ser su amiga."
        amiga "El gusto es mío. "
        "A lo lejos veo a un chico acercándose. "
        desconocido "Hola."
        amiga "Hola Sebastián, ¿elegiste la misma carrera?"
        show amigo at right
        amigo "Si eso parece, ¿Y tú cómo te llamas?"
        chica "Hola, me llamo [nombre] mucho gusto."
        amigo "El gusto es mío, te ves pálida ¿estás bien?"
        chica "Si estoy bien."
        hide amigo
        hide amiga 
        "Debo controlarme, sé que es difícil para mí socializar, pero está saliendo bien."
        $ estres = 20
        $ renpy.restart_interaction()
        explicacion "De aquí en adelante las decisiones que tomes afectaran a tu barra de estrés."
        explicacion "Recuerda mantenerla baja si sube al límite perderás la partida."
        explicacion "Un estrés muy alto puede ocasionar que aumente la dificultad de los minijuegos."
        explicacion "Así que cuida tu barra de estrés."
        "Veo entrando al maestro al salón de clases mientras todos se quedan callados."
        show maestro
        maestro "Buenos días alumnos, soy el profesor Carlos y yo les impartiré la materia de Redes. "
        maestro "Empezaremos viendo la primera sesión."
        hide maestro
        chica "Bueno aquí vamos. "
        chica "Espero no tener dificultades."

        #agregar minijuego 

        #if juego == "gana":
        chica "Eso estuvo facil"
        #elif juego == "pierde":
            #chica "¡uuff! Menos mal no me fue tan mal."
        chica "pero, deberia practicar para mejorar en la siguiente clase."
        show amigo at right
        amigo "Oye [nombre] ¿quieres acompañarnos al billar?"
        show amiga at left
        amiga "No lo sé… creo que deberíamos repasar un poco para la siguiente clase, [nombre]."
        hide amigo
        hide amiga 
        explicacion "Esta es la primera decisión que puede afectar tu barra de estrés."
        explicacion "Recuerdo no llenarla."
        $ estres = 20
        $ renpy.restart_interaction()
        menu:
            "Claro, vámonos al billar":
                jump billar2

            "Me quedaré a repasar con Luna":
                jump Estudiar2 



        # Desicion Sebastián 
        label billar2:
            show amigo
            amigo "Bien dicho [nombre], ¡vamos!"
            $ estres = 15
            $ renpy.restart_interaction()
            hide amigo 
            scene negro
            "Vas al billar con Sebastián." 
            "Fue divertido, pero una pequeña voz en tu cabeza te dice que mañana pagarás el precio." 
            "Regreso a mi casa algo cansada."
            scene cuartonoche
            chica "fue un buen primer día."
            "¿Debería dormirme ya? o ¿Leer un libro?"
        menu:
            "Dormir.":
                jump descansada

            "Leer libro.":
                jump cansada     



        # ChicaD
        label descansada:
            $ estres = 5
            $ renpy.restart_interaction()            
            scene cuartonoche
            chica "Bueno lo mejor será descansar para mañana tener energía."
            scene negro
            "Te acuestas a dormir temprano recuperando energía para el siguiente día."
            scene cuarto
            "Te despiertas con energía y descansada."
            scene wc
            "Te sientes con mucha energía de ver que pasara hoy."   
            scene chica_normal
            chica "¡aahhh! Que bien me siento."    
            chica "Hora de ir a la Universidad."    
            scene cocina
            "Desayunas lo primero que encuentras y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren5

                "Tomar Autobus":
                    jump Autobus5  
        label Tren5:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
              
            jump ChicaD
        
        label Autobus5:

            if transporte == "tren": 
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
              
            jump ChicaD  



        #Chica D
        label ChicaD:    
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            chica "Parece que Luna no está muy convencida."
            show amigo
            amigo "No te preocupes, hablaremos con ella después para que se una a nosotros. "
            chica "Sí, creo que es lo mejor."
            amigo "Bueno es hora de ver cómo nos va seguro nos va bien."
            chica "Espero que todo salga bien."
            hide amigo
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro
            #Agregar segundo minijuego

            #if juego == "gana":
                #chica "Me fue muy bien"
            #elif juego == "pierde":
            chica "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            show amigo
            amigo "No estuvo mal después de todo."
            chica "Sí, me siento aliviado de que haya terminado bien.."
            amigo "pasemos a la siguiente materia."
            chica "seguro que en esta nos va todavía mejor."
            chica "si tú lo dices."
            hide amigo
            "Nunca había tenido la oportunidad de salir con un amigo."
            "Siempre solía volver sola a casa."
            "Veo que llega la maestra, Sebastián se le nota preocupado ¿será que le gusta Luna?"
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable. "
            "después le pregunto ahora a poner atención."
            hide maestra

            #Minijuego 3 agregar 

            #if juego == "gana":
                #show amigo
                #amigo "Muy facil."
                #chica "Es cierto."
            #elif juego == "pierde":
            show amigo 
            amigo "esto no estuvo tan mal."
            chica "sí, tienes razón."
            chica "Oye Sebastián te veo preocupado ¿todo bien?"
            amigo "Me preocupo porque Luna siempre ha sido mi amiga y no quisiera que se quedara sola."
            "El instinto no me falla aun."
            chica "podemos quedarnos esta vez."
            amigo "si, aunque hoy habrá un festival podemos convencerla de que venga con nosotros y ya después practicamos con ella. "
            chica "veré que puedo hacer."
            hide amigo
            $ estres = 20
            $ renpy.restart_interaction()
            menu:
                "convercerla de que se una.":
                    jump ConvencerlaD_Chica

                "No hacer nada.":
                    jump NadaLD_Chica



            #Chica D
            label ConvencerlaD_Chica:
                chica "¿Luna, Sebastián y yo vamos a ir a un festival quieres unirte?"
                show amiga
                amiga "Yo les recomendaría quedarse a estudiar, pero prefiero quedarme a repasar, pero diviértanse."
                chica "Gracias por la preocupación, espero verte mañana amiga."
                amiga "Hasta mañana amiga."
                hide amiga 
                "Bueno lo intente, pero espero mañana estar con ella pues no me gusta que esté sola me recuerda a mí en la preparatoria."
                "También me quedaba sola estudiando..."
                $ estres = 30
                $ renpy.restart_interaction()
                #Continuacion de Ruta
                scene escuela
                show amigo
                amigo "Gracias por acompañarme."
                chica "Está bien relajarse de vez en cuando."
                amigo "No sé por qué, pero me siento como un tonto ahora mismo."
                chica "¿Te preocupa algo?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que hay algo mal así que decido preguntarle."
                chica "¿Todo bien Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna para mi es mi mejor amiga pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "Mi madre nunca la conocí pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián, su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces así que sé lo que siente Sebastián sobre todo que estén orgullosos..."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias [nombre] lo necesitaba sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chica "Sé lo que sientes, no poder agarrar fuerzas para seguir, pero no debemos rendirnos."
                hide amigo_triste
                show amigo
                amigo "Mejor regresemos y nos vemos mañana."
                chica "Muy bien."
                amigo "Gracias por acompañarme me recuerdas mucho a ella."
                chica "¿Enserio?, espero llevarme muy bien con ella entonces."
                hide amigo
                scene negro
                "Sientes un dolor profundo al saber que no sufres sola."
                "regresas a casa pensando en todo lo que pasó hoy."
                $ estres = 45
                $ renpy.restart_interaction()
                scene cuartonoche
                "Intento dormir, pero mi mente no deja de pensar en Luna."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tranquila vale, en la vida hay ciertas decisiones que tomamos, pero lo mejor es afrontar las consecuencias que reprimirlas [nombre]."
                chica "Es cierto en la preparatoria cometí más errores esto lo puedo resolver."
                misterioso "Exacto tú puedes con todo, afronta las consecuencias y te sentirás mejor."
                scene cuarto
                "Despiertas confusa, pero sigues pensando en luna."
                chica "¿Afrontar consecuencias?"
                scene chica_normal
                chica "Vamos anímate, Sebastián está bien yo también puedo estarlo resolveré esta situación con Luna."
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
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
                scene escuela
                "Vamos anímate debo dar lo mejor de mí."
                "No debo rendirme ahora que por fin entré a la Universidad."
                scene salon
                "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
                "Después de un tiempo veo llegar a Sebastián."
                chica "Hola Sebastián."
                show amigo
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
                hide amigo
                "Comienza la clase."
                show maestra 
                maestra "Muy bien Alumnos hoy les impartiré 2 clases."
                maestra "Vamos a ver el tema de hoy."
                chica "Aquí vamos."
                amigo "Podemos con esto."
                hide maestra 

                # agregra cuarto minijuego 
                #if juego == "gana":
                    #show amigo
                    #chica "Muy facil."
                    #amigo "Tienes razon."
                    #hide amigo
                #elif juego == "pierde":
                    #show amigo 
                    #chica "Soy pésima en esto."
                    #amigo "Yo también."
                    #hide amigo

                "Termina la primera clase, pero la maestra nos da un tiempo libre."
                "Aprovechamos el tiempo para ir a hablar con luna."
                chica "Hola Luna."
                show amiga at left
                amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
                chica "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
                show amigo at right
                amigo "Como en los viejos tiempos."
                amiga "Claro encantada de ir con ustedes."
                chica "Entonces nos vemos allá."
                hide amigo
                hide amiga
                "Nos regresamos a nuestros lugares."
                "Se termina el tiempo y continúa la siguiente clase."


                # agregra quinto minijuego 
                #if juego == "gana":
                    #show amigo
                    #chica "Fue fácil."
                    #amigo "Tienes razon."
                    #hide amigo
                #elif juego == "pierde":
                    #show amigo 
                    #chica "Soy pésima en esto."
                    #amigo "Yo también pero ya falta una."
                    #hide amigo

                show maestra 
                maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
                maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
                hide maestra
                "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
                chica "Salió bien la verdad."
                show amigo
                amigo "Sí tienes razón este fin será inolvidable. "   
                hide amigo
                "Veo entrar al maestro Carlos dando inicio la última clase."
                show maestro
                maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
                hide maestro 
                # agregra sexto minijuego 
                #if juego == "gana":
                    #show amigo
                    #chica "Sin problemas."
                    #amigo "Pues claro."
                    #hide amigo
                #elif juego == "pierde":
                    #show amigo 
                    #chica "Soy pésimo en esto."
                    #amigo "Yo también, pero al menos termino.
                    #hide amigo

                "Termina la clase dando finalizado este día de hoy."    
                chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
                show amigo
                amigo "Así es."
                chica "Muy bien entonces nos vemos Sebastián."
                amigo "Cuídate [nombre]."
                hide amigo
                "Tomo mis cosas y me despido de Luna."
                chica "Adiós Luna."
                show amiga 
                amiga "Adiós [nombre] nos vemos allá entonces."
                hide amiga 
                scene negro
                "Estoy ansiosa de que llegue este fin de semana." 

                "Pasa el tiempo llegando el fin de semana."

                scene parque
                "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
                scene negro
                misterioso "Afrontas bien las consecuencias recuerda no rendirte."
                "Te sientes confusa."
                "Bueno gracias a él todo fue mejor y resolví las cosas."
                "Ahora sólo debo concentrarme en pasarla bien con ellos."
                scene parque 
                "Me siento a esperar a Luna y Sebastián."
                "Pasa un tiempo y veo llegar a Sebastián primero."
                chica "Hola Sebastián."
                show amigo at left
                amigo "Hola [nombre]."
                amigo "¿Estás lista para pasarla bien?"
                chica "Si estoy lista."
                " Luna aparece con un material para estudiar."
                show amiga at right
                amiga "Hola amigos ¿Listos?"
                "Sebastián y [nombre]" "Si estamos listos."
                hide amiga
                hide amigo 
                "Pasa el tiempo y Sebastián me lleva a un lugar privado."
                "Luna se nos queda viendo confusa de lo que pasa."
                chica "¿Qué pasa? "
                chica "¿Te sientes bien?"
                show amigo_triste 
                amigo "Sí solo que reunirnos y verla feliz me hace feliz."
                chica " Deberías decirle lo que sientes por ella."
                amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
                "Comprendo su situación pues se como se siente no estar seguro de una decisión."
                "Debería darle apoyo para que se confiese o respeto su sentimiento de preocupación."
                hide amigo_triste

            menu:
                "Darle apoyo para que se confiese.":
                    jump final_chicaD1

                "Respetar sus sentimientos de preocupación.":
                    jump final_chicaD2





                    
            label final_chicaD1:
                chica "Se cómo te sientes, pero es mejor decirle lo que sientes por ella veo que ella quiere que le digas eso."
                show amigo 
                amigo "¿Estás segura de esto?"
                chica "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo 
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at left
                amigo "Luna…"
                show amiga at right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga 
                show amiga_triste at right
                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo
                hide amiga_triste
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at left
                show amiga at right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella. "
                hide amigo
                hide amiga 
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Ayudar a tus amigos desinteresadamente no solo es lo correcto, sino que también te hace sentir mejor."
                misterioso "Recuerda, en la vida, cualquier decisión que tomes traerá consecuencias, pero siempre habrá soluciones."
                misterioso "Nunca temas ofrecer tu ayuda o expresar tus sentimientos, especialmente en la universidad."
                misterioso "Solo elige bien con quién compartir tus emociones."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label final_chicaD2:
                chica "Si es lo que sientes, te apoyaré en cualquier decisión que tomes, Sebastián."
                chica "Sé lo que se siente no poder expresarte, así que cuentas conmigo en lo que sea."
                show amigo 
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chica "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo."
                show amigo at left 
                amigo "Volvimos."
                show amiga at right
                amiga "¿Todo bien?"
                chica "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chica "Continuemos."
                "Luna parece tranquila al pasar tiempo con Sebastián, pero  puedes notar que le hubiera gustado que él le confesara sus sentimientos."
                "Aun así, respetastes  su decisión de Sebastián."
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "No deberías guardarte nada, si te sientes mal, buscar ayuda en quienes te rodean es valiente."
                misterioso "Has afrontado esta situación con madurez."
                misterioso "Apoyaste y respetaste los sentimientos de Sebastián, pero recuerda que siempre podemos hacer un poco más por aquellos que nos importan."
                misterioso "La universidad es un desafío importante en la vida, no intentes superarlo solo."
                misterioso "Busca siempre la compañía de amigos y nunca te rindas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return








            #RChica D,D
            label NadaLD_Chica:
                "Decides no hacer nada, Sebastián parece preocupado."   
                chica " Lo siento Sebastián."
                show amigo_triste
                amigo "no te preocupes vámonos entonces."
                hide amigo_triste
                "¿Qué me sucede? Ver a Luna sola me recuerda a mí y no puedo hacer nada"
                "También me quedaba sola estudiando..."
                $ estres = 35
                $ renpy.restart_interaction()
                #Continuacion de Ruta
                scene escuela
                show amigo
                amigo "Gracias por acompañarme, aunque deberíamos haberla invitado."
                chica "Está bien relajarse de vez en cuando y de verdad lo siento no sé porque no me anime."
                amigo "Anímate yo soy quien debió convencerla, no tú."
                amigo "Me siento como un idiota ahora mismo."
                chica "¿Pasa algo Sebastián?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que hay algo mal así que decido preguntarle."
                chica "¿Todo bien Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna para mi es mi mejor amiga pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "Mi madre nunca la conocí pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Hago lo posible por consolar a Sebastián, su vida parece estar llena de dificultades."
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces así que sé lo que siente Sebastián sobre todo que estén orgullosos..."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias [nombre] lo necesitaba sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chica "Sé lo que sientes, no poder agarrar fuerzas para seguir, pero no debemos rendirnos."
                hide amigo_triste
                show amigo
                amigo "Mejor regresemos y nos vemos mañana."
                chica "Muy bien."
                amigo "Gracias por acompañarme me recuerdas mucho a ella."
                chica "¿Enserio?, espero llevarme muy bien con ella entonces..."
                hide amigo
                scene negro
                "Sientes un dolor profundo al saber que no sufres sola, pero te sientes más mal de no haber invitado a Luna."
                "regresas a casa pensando en todo lo que pasó hoy."
                $ estres = 55
                $ renpy.restart_interaction()
                $continuar
                scene cuartonoche
                "Sientes que pudiste hacer más con Luna y te acuestas a dormir."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "¿Sientes que pudiste hacer más? "
                misterioso "Hay decisiones que se nos complican en la vida, pero no te sientas mal."
                chica "Pero puede haber hecho algo, aunque no la haya convencido debí intentarlo."
                misterioso "Aun puedes cambiar tu destino [nombre]."
                scene cuarto
                "Despiertas confusa, pero sigues pensando en luna."
                chica "¿Cambiar mi destino?"
                scene chica_estres
                chica "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                "Esa sombra me dijo que puedo cambiar mi destino."
                scene cocina
                "Te preparas un Desayuno con mayor esfuerzo para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren13

                    "Tomar Autobus":
                        jump Autobus13  
        label Tren13:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
             
            jump Dia_chicaDD
        
        label Autobus13:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
             
            jump Dia_chicaDD








        label Dia_chicaDD:
            scene escuela
            "No es hora de pensar en eso debo de dar lo mejor de mí. "
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            Chica "Hola Sebastián."
            show amigo_preocupado
            amigo "Hola [nombre] ¿te sientes bien?"
            chica "Si estoy bien."
            hide amigo_preocupado
            "Miro como los 2 estamos mejor que ayer, pero decidí contarle mi pasado."
            chica "Sobre lo de ayer yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chica "No quisiera que entre tú y Luna tengan problemas."
            show amigo
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chica "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chica "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chica "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien esta vez iremos los 2 pero yo le diré que te veo un poco desanimada."
            chica "De acuerdo."
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "fue facil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovechamos el tiempo para ir a hablar con luna."
            chica "Hola Luna."
            show amiga at left
            amiga "Hola [nombre] y Sebastián ¿Qué ocurre?"
            chica "Queremos invitarte este fin de semana para pasarla juntos y estudiar en el parque."
            show amigo at right
            amigo "Como en los viejos tiempos."
            amiga "Claro encantada de ir con ustedes."
            hide amiga
            show amiga_preocupada at left
            "Luna me observa preocupada. "
            amiga "¿Estás bien [nombre]?"
            chica "Si estoy bien no te preocupes Luna."
            amiga "Si tu lo dices."
            chica "Entonces nos vemos allá."
            hide amigo
            hide amiga_preocupada
            "Nos regresamos a nuestros lugares."
            "Se termina el tiempo y continúa la siguiente clase."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chica "Salió bien la verdad."
            show amigo
            amigo "Sí tienes razón este fin será inolvidable. "   
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Sin problemas."
                #amigo "Pues claro."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es."
            chica "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chica "Adiós Luna."
            show amiga 
            amiga "Adiós [nombre] nos vemos allá entonces."
            hide amiga 
            scene negro
            "Estoy ansiosa de que llegue este fin de semana." 
            "Y sobre todo cambiar mi destino."
            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "No importa que decisión tomes solo se consciente. "
            "Te sientes confusa."
            "¿Ser consciente? Creo que he hecho bien en planear este día."
            "Mejor no pensar en ello y pasarla bien."
            scene parque 
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chica "Hola Sebastián."
            show amigo at left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros."    
            amigo "Vamos amiga mucho ánimo ¿vale?"
            chica "Está bien, pero sigo pensando que esto pudo cambiar al decirle desde un principio, pero estoy preocupada de cómo está ella."
            amigo "No te dejaré sola en esto."
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chica "¿Mejor?"
            amigo "Mucho mejor."
            "Luna aparece con un material para estudiar."
            show amiga at right
            amiga "Hola amigos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga
            hide amigo 
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chica "¿Qué pasa? "
            chica "¿Te sientes bien?"
            show amigo_triste 
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            amigo "Te dije que todo está bien [nombre]."
            chica " Aun así quiero apoyarte Sebastián y ayudarte con Luna."
            amigo "Muchas gracias amiga, lo aprecio mucho."
            "Debería darle apoyo para que se confiese o respeto su sentimiento de preocupación."
            hide amigo_triste

            menu:
                "Darle apoyo para que se confiese.":
                    jump final_chicaDD1

                "Respetar sus sentimientos de preocupación.":
                    jump final_chicaDD2





                    
            label final_chicaDD1:
                chica "No pude convencerla en un principio, pero quiero ayudarte a que le confieses tus sentimientos a ella."
                show amigo 
                amigo "No te preocupes más por eso."
                amigo "¿Y estás segura de esto?"
                chica "Esta vez te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo 
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at left
                amigo "Luna…"
                show amiga at right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga 
                show amiga_triste at right
                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo
                hide amiga_triste
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at left
                show amiga at right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                "Sebastián también se ve más calmado y feliz de haber confesado sus sentimientos por ella, y se siente más apoyado. "
                hide amigo
                hide amiga 
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos, aunque tuvimos dificultades."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has logrado hacer la diferencia en comparación con decisiones pasadas, y las has enfrentado con valor."
                misterioso "Cualquiera sea la decisión que tomes en tu vida, recuerda que siempre habrá consecuencias, pero también soluciones."
                misterioso "Nunca temas ofrecer tu ayuda o expresar tus sentimientos, especialmente en la universidad."
                misterioso "Solo elige bien con quién compartir tus emociones."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label final_chicaDD2:
                chica "No pude convencerla en un principio, pero tampoco quiero presionarte y respeto tu decisión."
                chica "Te daré el apoyo que necesites con Luna."
                show amigo 
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chica "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Volvemos con Luna Sebastián parece más calmado sabiendo que cuenta conmigo para lo que sea y me siento mejor al darle mi apoyo que no pude darle antes."
                show amigo at left 
                amigo "Volvimos."
                show amiga at right
                amiga "¿Todo bien?"
                chica "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chica "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Al principio no pude ayudar, pero siempre tenemos oportunidades de hacer la diferencia y sobre todo respetar decisiones."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Respetaste los sentimientos de Sebastián, y aunque no siempre podemos ofrecer apoyo al principio, siempre habrá oportunidades para hacerlo."
                misterioso "Cualquiera sea la decisión que tomes, siempre habrá consecuencias, pero también soluciones."
                misterioso "Nunca temas ayudar o expresar tus sentimientos, especialmente en la universidad."
                misterioso "Recuerda que nunca estás solo, elige bien con quién abrirte emocionalmente."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return
                
                



        # Ruta C        
        label cansada:
            $ estres = 10
            $ renpy.restart_interaction() 
            scene cuartonoche
            chica "Bueno, un libro no hara daño..."
            scene negro
            "Lees un buen libro y pierdes la noción del tiempo."
            scene cuarto
            "Despiertas con dificultad, sintiendo el peso de tus malas decisiones."
            scene wc 
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chica_normal
            "Te miras al espejo, tratando de reconocer a la persona reflejada."
            chica "Creo que me emocione un poco…"
            "*Suspiro*"
            chica "Bueno, diría que demasiado... Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina
            "Desayunas lo primero que te hallaste y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren6

                "Tomar Autobus":
                    jump Autobus6  
        label Tren6:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
            
    
              
            jump ChicaC
        
        label Autobus6:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "Bueno, aunque es más lento es el más económico."
              
            jump ChicaC   
       
       
       
        #ChicaC
        label ChicaC:
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            "Luna parece decepcionada y Sebastián se muestra pensativo."
            amiga "Bueno... supongo que estudiaré sola entonces."
            " Puedo ver la decepción en sus ojos." 
            "Quería que fuéramos juntos… pero no puedo estar en dos lugares a la vez."
            " Veo como Luna se sienta en su lugar, intentando concentrarse en sus apuntes, pero su mirada se desvía hacia mí."
            "Hay un silencio incómodo que parece durar una eternidad."
            chica "Me siento mal por ella."
            show amigo
            amigo "No te preocupes por Luna, luego hay que convencerla de que venga con nosotros."
            chica "Sí, tienes razón... aunque algo en su mirada me dice que ya la decepcioné."
            "Sebastián se queda en silencio por un momento."
            amigo "¿Dormiste bien? Te ves cansada. "
            chica "No te preocupes, estaré bien... o al menos eso espero."
            hide amigo
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro 
            "Durante la clase, el cansancio comienza a hacer mella en ti."
            "Te cuesta concentrarte y cada palabra del profesor se siente como un peso más sobre tus hombros."
            #Agregar Minijuego 2
            #if juego == "gana":
                #chica "Me fue muy bien"
            #elif juego == "pierde":
            chica "Esta clase fue estresante, pero logré salir adelante."
            "Termina la primera clase e inicia la segunda."
            amigo "¿Seguro que estás bien?"
            chica "Sí, estoy bien... sólo tuve dificultades, pero la próxima vez lo haré mejor, lo prometo."
            amigo "si tú lo dices solo recuerda que tenemos otra clase, dormilona."
            chica "Lo sé, Sebastián... pero tú también estabas en las mismas."
            "A pesar de sus palabras de ánimo, sabes que algo en ti está cambiando."
            "Te preguntas si realmente vale la pena seguir así."
            "Veo entrar a la maestra para dar inicio la siguiente clase."
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable. "
            chica "bueno a empezar con la siguiente materia."
            "Aunque siga con sueño."

            hide maestra

            #Minijuego 3 agregar 

            #if juego == "gana":
                #show amigo
                #amigo "Muy facil"
                #chica "Es cierto"
            #elif juego == "pierde":
            show amigo
            amigo "bueno esta estuvo fácil ¿a que si dormilona?"
            chica "sí y deja de decirme dormilona."
            amigo "Tranquila está bien."
            "Sebastián y tú están en clase, pero tu mente está en otro lugar."
            "Cada palabra que Sebastián menciona sobre Luna hace que te sientas más culpable."
            amigo "Siempre he sido cercano a Luna, pero últimamente no hemos pasado tiempo juntos como antes."
            chica "Podemos quedarnos esta vez, intentar recuperarlo."
            amigo "Sí, aunque hoy hay un festival... Tal vez podamos convencerla de que venga con nosotros."
            chica "Haré lo que pueda..."
            hide amigo
            $ estres = 30
            $ renpy.restart_interaction()
            menu:
                "convercerla de que se una.":
                    jump ConvencerlaC_Chica

                "No hacer nada.":
                    jump NadaLC_Chica
            
            
            
            #Chica C
            label ConvencerlaC_Chica:
                "Estás muy cansada y estresada, pero aun así intentas convencer a Luna."
                chica "¿Luna, Sebastián y yo vamos a ir a un festival quieres unirte?"
                show amiga
                amiga "Deberías mejor descansar por hoy, pero diviértanse yo prefiero quedarme a repasar."
                chica "Gracias por la preocupación, te veré mañana."
                amiga "Hasta mañana."
                hide amiga 
                "Te sientes mal por no pasar tiempo con Luna y recordaste la preparatoria donde no convivías con prácticamente nadie."
                "veo mi vida en la prepa reflejada en ella pues no convivía mucho con mis compañeros. "
                $ estres = 45
                $ renpy.restart_interaction()
                #Continuar Historia
                scene escuela
                show amigo
                amigo " En serio te ves muy cansada, pero gracias por acompañarme. "
                chica "Estaré bien no te preocupes. "
                amigo "Me siento como un idiota ahora mismo."
                chica "¿Te preocupa algo?"
                amigo "Luna y yo siempre convivíamos, aunque ella estaba más concentrada en el estudio y aun así pasábamos tiempos juntos."
                "No conozco mucho a Sebastián, pero por su expresión sé que hay algo mal así que decido preguntarle."
                chica "¿Todo bien Sebastián?"
                "Sebastián se detiene y me mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna para mi es mi mejor amiga pues en mi hogar mi padre siempre está decepcionado tanto por mi conducta como mi desarrollo en la escuela."
                amigo "Mi madre nunca la conocí pues cuando nací tuvo problemas, pero aquí sigo."
                amigo "He sido fuerte gracias a Luna me gustaría invitarla a salir algún día y volver a pasar tiempo con ella."
                "Intentó consolar a Sebastián pues su vida es muy dura. "
                "Mis padres tampoco están en casa ya que trabajan todos los días y los veo muy pocas veces así que sé lo que siente Sebastián sobre todo que estén orgullosos..."
                "Abrazo fuerte a Sebastián."
                amigo "Gracias [nombre] lo necesitaba sé que la escuela es importante, pero uno a veces no puede agarrar fuerzas para continuar."
                chica "Sé lo que se siente, no poder agarrar fuerzas para seguir, pero no debemos rendirnos."
                hide amigo_triste
                show amigo
                amigo "Mejor regresemos y nos vemos mañana."
                chica "Muy bien."
                amigo "Gracias por acompañarme me recuerdas mucho a ella, pero por ahora ve a descansar."
                chica "¿Enserio?, espero llevarme muy bien con ella entonces..."
                chica "Y no te preocupes hoy descansaré."
                hide amigo
                scene negro
                "Sientes un dolor profundo y no sientes ánimos de continuar, pero la vida sigue adelante."
                "regresas a casa pensando en todo lo que pasó hoy."
                $ estres = 65
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche
                "te sientes muy cansada y te acuestas a dormir, pero no puedes de dejar de pensar en Luna."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tranquilo vale, en la vida hay ciertas decisiones que tomamos, pero lo mejor es afrontar las consecuencias que reprimirlas [nombre]."
                chica "Pero ¿cómo afrontarlas?"
                misterioso "En la vida, aunque queramos no podemos hacer todo en un día, pero siempre sé consciente de tus acciones."
                scene cuarto
                "Despiertas confusa, pero sigues pensando en luna."
                chica "¿Afrontar consecuencias?"
                scene chica_estres
                chica "Me llevo bien con Sebastián, pero porque me siento asi."
                chica "Pensar tanto en la Luna y la situación de Sebastián hace que no pueda concentrarme."
                chica "Vamos tú puedes con esto."
                scene cocina
                "Muy apenas te preparas algo para comer."
                scene negro
                "¿No sé qué transporte tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren15

                    "Tomar Autobus":
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
            scene escuela
            "Vamos anímate debo dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando no quisiera molestarla."
            "Después de un tiempo veo llegar a Sebastián."
            chica "Hola Sebastián."
            show amigo_preocupado
            amigo "¡¡wow!! ¿estas bien [nombre]?"
            amigo "Te veo un poco mal."
            chica "Estoy bien no te preocupes."
            amigo "Oye deberías sacarlo todo yo lo hice ayer y me sentí mejor así que puedes decirme que pasa."
            chica "Yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chica "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado
            show amigo
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chica "Entonces ella te gusta verdad."
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chica "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chica "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo un poco mal para que no se preocupe."
            chica "Tienes razón gracias."
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos."
            amigo "Podemos con esto."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Soy pésimo en esto."
                #amigo "Yo también."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con luna mientras los observo."
            "Espero que todo esté bien entre ellos."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase."
            hide maestra
            "Sebastián Regresa a su asiento, después le preguntare como le fue."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Fue fácil."
                #amigo "Tienes razon."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Soy pésimo en esto."
                #amigo "Yo también pero ya falta una."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chica "¿Cómo te fue con ella?"
            show amigo
            amigo "Aceptó así que nos veremos con ella este fin."
            chica "Me alegra oír eso."   
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Sin problemas."
                #amigo "Pues claro."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Soy pésimo en esto."
                #amigo "Yo también, pero al menos termino.
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es y recuerda tranquila vale."
            chica "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chica "Adiós Luna."
            show amiga 
            amiga "Adiós [nombre] te veré allá entonces con Sebastián."
            chica "Te veo ahí."
            hide amiga 
            scene negro
            "Me retiro a mi casa a descansar esperando el fin de semana." 

            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Afrontar bien las consecuencias sigue así."
            "Te sientes confusa."
            "Aun no entiendo el propósito de esa sombra."
            "No importa, hoy la pasaré bien con mis amigos."
            scene parque 
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Sebastián primero."
            chica "Hola Sebastián."
            show amigo at left
            amigo "Hola [nombre]."
            "Sebastián me da palmadas en los hombros"
            amigo "Vamos amiga mucho ánimo ¿vale?"
            "Respiro hondo y decido poner mi mejor cara antes de que aparezca Luna."
            chica "¿Mejor?"
            amigo "Mucho mejor."
            " Luna aparece con un material para estudiar."
            show amiga at right
            amiga "Hola amigos ¿Listos?"
            "Sebastián y [nombre]" "Si estamos listos"
            hide amiga
            hide amigo 
            "Pasa el tiempo y Sebastián me lleva a un lugar privado."
            "Luna se nos queda viendo confusa de lo que pasa."
            chica "¿Qué pasa? "
            chica "¿Te sientes bien?"
            show amigo_triste 
            amigo "Sí solo que reunirnos y verla feliz me hace feliz."
            chica " Deberías decirle lo que sientes por ella."
            amigo "No estoy muy seguro además no quiero estorbar en sus estudios."
            "La soledad no es una buena opción." 
            "Debería darle apoyo para que se confiese o respeto su sentimiento de preocupación."
            hide amigo_triste

            menu:
                "Darle apoyo para que se confiese.":
                    jump final_chicaC1

                "Respetar sus sentimientos de preocupación.":
                    jump final_chicaC2





                    
            label final_chicaC1:
                chica "Mira, la soledad no es buena y no es excusa puedes pasar más tiempo con ella estudiando juntos conociéndote más."
                chica "Es difícil Estudiar cuando uno está estresado y Solo, así que siempre es bueno tener a alguien en quien apoyarse."
                show amigo 
                amigo "¿Estás segura de esto?"
                chica "Te apoyaré en todo momento como lo hiciste conmigo."
                amigo "Está bien."
                hide amigo 
                "Empujó a Sebastián con Luna y le levantó el pulgar dándole ánimos."
                show amigo at left
                amigo "Luna…"
                show amiga at right
                amiga "¿Si Sebastián?"
                amigo "Nunca te lo había dicho, pero eres importante en mi vida y quiero pasar más tiempo contigo."
                hide amiga 
                show amiga_triste at right
                amiga "Tú también eres importante para mí Sebastián."
                amiga "Eres mi mejor amigo desde la preparatoria."
                hide amigo
                hide amiga_triste
                "Luna y Sebastián se abrazan y siento la tranquilidad de haber ayudado a mis amigos."
                "Me llaman para que me acerque a ellos."
                show amigo at left
                show amiga at right
                "Luna y Sebastián" "Vamos [nombre] sigamos estudiando."
                "Luna se ve más feliz, su expresión muestra que siempre quiso escuchar esas palabras de Sebastián y que ella también pudo expresarse."
                hide amigo
                hide amiga 
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                "Ayudarte a ti mismo es bueno, pero ayudar a otros es mucho mejor ya que sientes que haces mucho la diferencia."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Hoy has sido testigo de un momento crucial."
                misterioso "Alentar a alguien a expresar sus sentimientos puede llevar a una conexión más profunda y genuina."
                misterioso "Pero recuerda, cada palabra tiene peso, y las emociones son delicadas."
                misterioso "Has ayudado a fortalecer un vínculo, pero asegúrate de que tus intenciones sean siempre sinceras."
                misterioso "Los lazos que formamos pueden ser nuestra mayor fortaleza o nuestra mayor debilidad."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label final_chicaC2:
                chica "Si sientes eso en verdad te apoyo sea cual sea la decisión que tomes Sebastián."
                show amigo 
                amigo "Gracias [nombre] sé que cuento contigo."
                amigo "Regresemos con Luna."
                chica "De acuerdo."
                hide amigo
                "Regresamos con Luna."
                "Sebastián parece más calmado sabiendo que cuenta con mi apoyo para lo que sea."
                show amigo at left 
                amigo "Volvimos."
                show amiga at right
                amiga "¿Todo bien?"
                chica "Si, solo resolvimos una duda que teníamos, no queríamos presionarte."
                amiga "¡oh! ¿y la resolvieron?"
                amigo "Así es."
                "Sebastián se tranquiliza más al saber que cuenta con mi apoyo."
                amiga "Bueno, continuemos estudiando."
                chica "Continuemos."
                "Luna parecía más calmada al poder pasar más tiempo con Sebastián, pero siento que le hubiera gustado más que le confesara lo que siente por ella, pero respeto la decisión de Sebastián."
                "Los 3 nos quedamos estudiando para el examen el cual todos aprobamos, aunque tuvimos dificultades."
                " Siempre hay que respetar los sentimientos de los demás, pero sí podemos hacer la diferencia o dar apoyo vale la pena el riesgo y más si son nuestros amigos y nos apoyan."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Elegir el momento adecuado para hablar puede ser tan importante como las palabras mismas."
                misterioso "Has demostrado respeto por los sentimientos de los demás, comprendiendo que no siempre es necesario forzar las cosas."
                misterioso "A veces, el silencio puede ser una forma de sabiduría, permitiendo que las relaciones crezcan a su propio ritmo."
                misterioso "Pero recuerda, el miedo a lo desconocido no debe impedirnos avanzar. "
                misterioso "Cada oportunidad perdida puede convertirse en una pregunta sin respuesta."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            #Chica Egoista
            label NadaLC_Chica:
                "Decides no hacer nada, el cansancio y la falta de energía te paralizan."
                chica "Lo siento, Sebastián... simplemente no puedo."
                show amigo_triste
                amigo "No te preocupes, vámonos entonces."
                hide amigo_triste
                "Ves a Luna sola, y en ella solo veo un reflejo de mí mismo. Algo en tu interior grita que actúes, pero el peso de tus malas decisiones te hunde más."
                $ estres = 55
                $ renpy.restart_interaction()
                #Continuar Historia
                scene escuela
                show amigo
                amigo "Te ves muy cansada... pero gracias por acompañarme."
                amigo " Aunque, la verdad, deberíamos haberla invitado."
                chica "Estaré bien... lo siento, Sebastián, de verdad lo siento."
                amigo "No te castigues tanto, debí ser yo quien la convenciera, no tú."
                "Mientras caminan por el festival, notas que Sebastián está más callado que de costumbre. Decides preguntarle qué le sucede."
                chica "¿Qué pasa, Sebastián?"
                "Sebastián se detiene y te mira con tristeza."
                hide amigo
                show amigo_triste
                amigo "Luna es mi mejor amiga. "
                amigo "Siempre ha estado ahí para mí, incluso cuando mi padre estaba decepcionado conmigo o cuando no tenía a nadie más."
                amigo "Ella me daba fuerzas... y ahora siento que la estoy perdiendo."
                "La confesión de Sebastián te golpea como un balde de agua fría."
                "Te das cuenta de que tus acciones no solo te han afectado a ti, sino también a las personas que te rodean."
                hide amigo_triste
                show amigo_preocupado
                chica "Sebastián... no estás solo. Lo que sea que necesites, estoy aquí."
                "Lo abrazas con fuerza, sintiendo la presión de las expectativas y la culpa arremolinándose dentro de ti."
                hide amigo_preocupado
                show amigo_triste
                amigo "Gracias, [nombre]. A veces es difícil continuar, pero al menos sé que te tengo a ti."
                hide amigo_triste
                scene negro
                "La culpa te golpea más fuerte pero resistes a que te observen decaer."
                "Debo resistir por mis amigos..."
                "Regresas a casa intentando despejar tu mente."
                $ estres = 80
                $ renpy.restart_interaction()
                #continuar 
                scene cuartonoche
                "Te sientes más agotada que nunca."
                "La culpa de no haber hecho más por Luna y Sebastián te pesa enormemente."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "¿Realmente crees que hiciste lo correcto?"
                misterioso "¿Este es el camino que elegiste?"
                chica "¿Quién eres?"
                chica "¿A qué te refieres?"
                misterioso "Si sigues así, deberás afrontar las consecuencias."
                scene cuarto
                "Despiertas con el corazón acelerado y el estrés a tope."
                "Las palabras de la voz resuenan en tu mente."
                chica "No puedo seguir así..."
                scene chica_estres
                chica "Me siento muy mal de no haber hecho nada por Sebastián y Luna."
                chica "Pensar tanto en Luna y la situación de Sebastián hace que no pueda concentrarme. "
                chica "Vamos tú puedes con esto."
                scene cocina
                "Muy apenas te preparas algo para comer."
                scene negro
                "¿No sé qué transporte tomar hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren17

                    "Tomar Autobus":
                        jump Autobus17  
        label Tren17:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Llegare temprano aunque no se que hacer..."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "así tengo mas tiempo de pensar que hare... "
             
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
            scene escuela
            " No es hora de pensar en eso debo de dar lo mejor de mí."
            "No debo rendirme ahora que por fin entré a la Universidad."
            scene salon
            "Miro que Sebastián aún no llega y veo a Luna estudiando, no quisiera molestarla después de que no hable con ella ayer."
            "Después de un tiempo veo llegar a Sebastián."
            chica "Hola Sebastián."
            show amigo_preocupado
            amigo "¡¡wow!! ¿estas bien [nombre]?"
            amigo "Te veo peor que ayer."
            chica "Estoy bien no te preocupes."
            amigo "¿Segura?"
            chica "Si."
            amigo "Oye deberías sacarlo todo yo lo hice ayer y me sentí mejor así que puedes decirme que pasa."
            chica "Yo también tuve problemas en la preparatoria solo que yo nunca vi a alguien como mi amigo hasta ahora."
            chica "No quisiera que entre tú y Luna tengan problemas."
            hide amigo_preocupado
            show amigo
            amigo "Ya veo, no te preocupes por nosotros sé que he estado saliendo y pues no me quedo con ella, pero así éramos siempre en la preparatoria."
            amigo "Pero nos reuníamos los fines de semana para pasarla los 2 a gusto."
            chica "Entiendo, pero aun así debí apoyarte se que ella es importante para ti. "
            amigo "No solo eso, sin ella mi vida no tendría sentido pues cuando estoy con ella me siento vivo."
            chica "Tengo una idea, qué tal si la invitamos un fin de semana nos reunimos y hablan ustedes."
            amigo "No suena mala idea puesto que le gustaría pasar un rato y pues estudiar cómo hacíamos ella y yo."
            chica "muy bien entonces terminando hay que decirle."
            amigo "Me parece bien, aunque yo le voy a decir porque te sigues viendo muy mal para que no se preocupe."
            chica "Tienes razón gracias."
            hide amigo
            "Comienza la clase."
            show maestra 
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos."
            amigo "Anímate todo saldrá bien."
            hide maestra 

            # agregra cuarto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Estuvo bien."
                #amigo "vez sí se pudo."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Esto es muy difícil."
                #amigo "Si."
                #hide amigo

            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Sebastián aprovecha el tiempo para ir a hablar con luna mientras los observo."
            "Espero que todo esté bien entre ellos, no quiero arruinar esto y estar sola otra vez."
            "Se termina el tiempo y continúa la siguiente clase."
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase."
            hide maestra
            "Sebastián Regresa a su asiento, después le preguntare como le fue."


            # agregra quinto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "Estuvo bien."
                #amigo "vez sí se pudo."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Esto es muy difícil."
                #amigo "Muy cierto."
                #hide amigo

            show maestra 
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase." 
            chica "¿Cómo te fue con ella?"
            show amigo
            amigo "Aceptó así que nos veremos con ella este fin."
            chica "Me alegra oír eso."   
            amigo "también noto que te ves mal, intenta descansar para que este fin de semana sea agradable."
            chica "Lo intentare..."
            amigo "no te esfuerces mucho."
            hide amigo
            "Veo entrar al maestro Carlos dando inicio la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro 
            # agregra sexto minijuego 
            #if juego == "gana":
                #show amigo
                #chica "fue facil."
                #amigo "ves que sí."
                #hide amigo
            #elif juego == "pierde":
                #show amigo 
                #chica "Esto es muy difícil."
                #amigo "Tienes razón, pero ya termino.""
                #hide amigo

            "Termina la clase dando finalizado este día de hoy."    
            chica " Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amigo
            amigo "Así es y recuerda tranquila vale."
            chica "Muy bien entonces nos vemos Sebastián."
            amigo "Cuídate [nombre]."
            hide amigo
            "Tomo mis cosas y me despido de Luna."
            chica "Adiós Luna."
            "Observó su preocupación en mi cara, pero aun así decidí sonreírle."
            show amiga 
            amiga "Adiós [nombre] te veré allá entonces con Sebastián."
            chica "Te veo ahí."
            hide amiga 
            scene negro
            "Me retiro a mi casa a descansar esperando el fin de semana." 
            "Espero que todo salga bien la verdad."

            "Pasa el tiempo llegando el fin de semana."

            scene parque
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Recuerda, tus decisiones te han llevado hasta aquí."
            "Te sientes confusa y abrumada."
            "Vaya, esa voz... ¿será mi conciencia?"
            "En fin, hoy solo me divertiré con mis amigos."
            scene parque 
            "Te sientas a esperar a Luna y Sebastián, sintiendo el peso de lo que está por venir."
            "Sebastián llega primero, y te saluda con su habitual energía."
            chica "Hola Sebastián."
            show amigo at left
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
            show amiga_preocupada at right
            amiga "¿Están bien los dos?"
            "Sebastián le da un pulgar arriba, ocultando la verdad de tu estado."
            amigo "Solo le duele la cabeza a [nombre], no es nada grave."
            "Me susurra al oído."
            amigo "Te apoyo en lo que decidas."
            chica "Gracias, Sebastián..."
            "Te das cuenta de que, aunque ellos se preocupan por ti, tú no has hecho nada por ellos."
            "Ahora enfrentas la decisión final hacer un último esfuerzo o retirarte de la Universidad."
            "Los dos te observan, esperando tu respuesta."
            hide amiga_preocupada
            hide amigo 
            

            menu:
                "Hacer un último esfuerzo":
                    jump final_chicaCC1

                "Retirarse de la Universidad.":
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
                show amiga_preocupada at left
                amiga "Tranquila no nos has decepcionado y me alegra que me hayas dicho cómo te sientes."
                hide amiga_preocupada
                show amiga at left
                amiga "Gracias Sebastián por estar al pendiente de ella como siempre estuviste de mi"
                show amigo at right
                amigo "Una amistad grande jamás abandona a sus amigos en las buenas o en las malas."
                chica "Gracias amigos."
                "Sientes un peso menos, pero la culpa no se irá fácilmente."
                "Me abrazan más fuerte y correspondiendo regresando un abrazo más fuerte."
                amiga "Toda ira bien ya lo veras."
                amigo " si te apoyaremos en lo que sea."
                "Los 3 nos quedamos estudiando, aunque no me preocupaba el examen, pero si estar con mis amigos y no volver a decepcionarlos."
                "Las decisiones que tome tardaran en sanar pues lo que hice no fue bueno ahora se a que se refería esa sombra "
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Aun con las consecuencias al final desiste enfrentarte a ellas."
                misterioso "No todo es caso perdido lo importante es nunca rendirse los errores nos hacen más fuerte."
                misterioso "Es bueno tener amistades en momentos difíciles pues ellos siempre te darán apoyo y más si pasan por las mismas situaciones."
                misterioso "Recuerda estar preparada para entrar a la Universidad y disfrutar de ella con amigos, espero que esto te sirva para que siempre seas consciente de tus acciones."


                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


            

            label final_chicaCC2:
                "Con lágrimas y un fuerte dolor en el pecho, decides decirles que te vas de la universidad."
                " Sebastián y Luna me miran preocupados, la sorpresa se refleja en sus rostros."
                show amiga_preocupada at left
                show amigo_preocupado at right
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
                hide amiga_preocupada
                hide amigo_preocupado
                show amiga_triste at left
                show amigo_triste at right
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
                hide amiga_triste
                hide amigo_triste
                show amiga at left
                show amigo at right
                "Ambos me devuelven la sonrisa, aunque se nota la tristeza en sus ojos."               
                "Sebastián y Luna" "Adios [nombre] cuidate mucho."
                hide amigo
                hide amiga
                "Me alejo de ellos, regresando sola a mi casa, sintiendo el vacío en cada paso."
                scene cuarto
                "Te acuestas en la cama, reflexionando sobre lo sucedido."
                chica "No pude con la presión."
                chica "Este peso es insoportable, pero no puedo huir para siempre."
                chica "Esta ansiedad es horrible."
                chica "Volveré…" 
                "Luna, Sebastián… les prometo volver."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Has pasado por un momento muy difícil, pero recuerda, rendirse nunca es una opción."
                misterioso "El estrés y la ansiedad pueden ser abrumadores, pero siempre es mejor buscar ayuda que enfrentarlo sola."
                misterioso "Espero que nunca tengas que tomar una decisión tan dolorosa, pero si alguna vez te encuentras en una situación así, recuerda que no estás sola."
                misterioso "Siempre hay alguien dispuesto a ayudarte. "

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return


        #Decisión Luna
        label Estudiar2:
            $ estres = 25
            $ renpy.restart_interaction() 
            show amigo
            amigo "como gustes."
            hide amigo
            "Te quedaste estudiando con Luna fue estresante, pero al menos aprendiste."    
            show amiga 
            "Gracias por quedarte."
            hide amiga 
            scene negro
            "Regreso a mi casa algo cansada."
            scene cuartonoche
            "No fue tan mal para ser mi primer día."
            "¿Debería dormirme ya? o ¿Leer un libro?"
        menu:
            "Dormir.":
                jump descansada2

            "Jugar video juegos.":
                jump cansada2     
        # ChicaB
        label descansada2:
            $ estres = 15
            $ renpy.restart_interaction() 
            scene cuartonoche
            chica "Bueno lo mejor será descansar para mañana tener energía."
            scene negro
            "Te acuestas a dormir temprano recuperando energía para el siguiente día."
            scene cuarto
            "Te despiertas con energía y descansada."
            scene wc
            "Te sientes con mucha energía de ver que pasara hoy"   
            scene chica_normal
            chica "¡aahhh! Que bien me siento."    
            chica "Hora de ir a la Universidad."    
            scene cocina
            "Desayunas lo primero que te hallaste y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren7

                "Tomar Autobus":
                    jump Autobus7  
        label Tren7:
       
        
            if transporte == "tren":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen  
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
            
            jump ChicaB
        
        label Autobus7:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
             
            jump ChicaB  



        #Ruta B
        label ChicaB:
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            show amiga
            amiga "¿Lista para continuar?"    
            chica "Claro que sí."
            amiga "Te ves muy concentrada esto va a ser muy fácil."
            chica "Sí, gracias por ayudarme a practicar."
            hide amiga
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            hide maestro
            chica "Estoy preparada."
            #Agregar Minijuego 2
            #if juego == "gana":
            chica "Eso fue fácil muchas gracias Luna."
            #elif juego == "pierde":
                #chica "Esta clase fue estresante, pero logré salir adelante."
            show amiga
            amiga "Sabes estamos para apoyarnos."
            $ estres = 5
            $ renpy.restart_interaction()
            amiga "Estuviste excelente [nombre]."
            chica "Todo gracias a ti Luna por ayudarme a practicar."
            amiga "un placer es mejor para mi practicar con una amiga. "
            hide amiga
            "quien sabe cómo me habría ido si no hubiera dormido temprano."
            "Oh, aquí viene la nueva maestra."
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable."
            chica "bueno a empezar con la siguiente materia."
            hide maestra
            #Minijuego 3 agregar 

            #if juego == "gana":
            show amiga
            amiga "Bueno, bueno explica muy bien la maestra. "
            chica "Sí, tienes razón."
            #elif juego == "pierde":
                #chica "Estuvo complicado."
            amiga "sigo preocupada por Sebastián seguro tuvo problemas en la anterior. "
            chica "tienes razón ahora hay que convencerlo de que practique con nosotras."
            amiga "Buena suerte con eso."
            hide amiga

            menu:
                "convencerlo de que se te una.":
                    jump ConvencerB_Chica

                "No hacer nada":
                    jump NadaB_Chica
            
            
            
            
            #Chica B
            label ConvencerB_Chica:
                chica "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo
                amigo "Pero habrá un festival…"
                chica "Vamos hazlo por mí y por Luna."
                amigo " Está bien, el festival puede esperar."
                chica "No te arrepentirás."
                hide amigo
                $ estres = 10
                $ renpy.restart_interaction()
                #Continuar guion 
                "Nos quedamos con luna parecía muy feliz."
                show amiga at left
                amiga "Gracias por acompañarme amigos."
                show amigo at right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto, nos va a servir mucho." 
                hide amigo
                hide amiga
                "Pasa el tiempo y estudiamos un rato mas con Luna."
                "Observó cómo Sebastián se retira para ir al festival, pero decidió acompañar un rato más a Luna."
                show amiga
                amiga "[nombre], ¿puedo decirte algo?"
                chica " Claro amiga."
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chica "Sé cómo te sientes Luna y te comprendo."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Si, me alegra que seamos amigas, tenemos algo en común."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chica "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga
                $ estres = 5
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche
                "Te acuestas a dormir feliz por las amistades que has hecho."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Vas por buen camino [nombre]."
                "Sientes una presencia, pero te sientes calmada."
                chica "¿Eres mi conciencia?"
                misterioso "Solo te observare, vas por buen camino."
                scene cuarto
                "Despiertas confusa pero calmada a la vez."
                chica "¿Qué o quién era esa voz? "
                chica "¿Buen camino?"
                scene chica_normal
                chica "Nunca pensé estar tan calmada desde lo de la preparatoria. "
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
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
            scene escuela
            chica "Hoy espero volver a pasar tiempo con luna y Sebastián."
            scene salon
            chica "Hola amigos ¿cómo están?"
            show amiga at right 
            amiga "Hola, me siento mucho mejor, gracias. Espero que tú también, [nombre]."
            show amigo at left
            amigo "Bien también, ¿y tú cómo estás, [nombre]?"
            chica " Muy bien ¿hoy vamos a quedarnos a repasar verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Si será lo mejor."
            "Empieza la clase."
            chica "¿Hoy tendremos 3 clases verdad?"
            amiga "Según el horario sí."
            chica "Vale gracias Luna."
            hide amigo
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "fue facil."
                #amiga "Eso es verdad."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDia_chicaB

                "Quedarse Callada.":
                    $ Luna = "Callarse"
                    jump cDia_chicaB


            label cDia_chicaB:
                if Luna == "preguntar":
                    chica "Luna como has estado."
                    "Decido abrazarla por lo que pasó ayer."
                    show amiga at right
                    amiga "Me he sentido mejor Gracias por preguntar."
                    show amigo at left
                    amigo "¿aún preocupada Luna?, eres lista y tú puedes con todo."
                    amiga "Gracias a ambos por el apoyo."
                    amiga "Sin ustedes no sé qué haría."
                    hide amiga
                    hide amigo




                elif Luna == "Callarse":  
                    "Te quedas callada, pero te quedas cerca de ella."
                    chica "No tengo palabras ahorita, pero tienes mi apoyo Luna."
                    show amiga at right
                    amiga "Gracias amiga, lo aprecio mucho."  
                    show amigo at left
                    amigo "también estoy aquí y me quedaré contigo Luna."
                    amiga "Gracias a ambos de verdad."
                    hide amiga
                    hide amigo

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Genial muy fácil."
                #amiga "Practicando todo se logra."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más [nombre]."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at left
            amigo "vaya un fin de semana no puede ser que ya tengamos exámenes."
            show amiga at right
            amiga "Lo sé, pero esto ya es la Universidad, siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno ya lo veremos el fin de semana."
            chica "A puesto que será divertido quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chica "Entonces no se diga más nos veremos en el parque."
            hide amigo
            hide amiga
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Eso estuvo difícil."
                #amiga "No te rindas  [nombre]."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chica "Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amiga at right
            amiga "muy bien los veré ahí."
            show amigo at left
            amigo "igual nos veremos allí."
            hide amiga
            hide amigo
            scene cuarto
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            
            scene negro
            "Es la primera vez que estoy muy relajada, Estudiar con amigos es mejor que sola ya que aprendes más."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Recuerda, vas por buen camino."
            "Te sientes confusa pero calmada."
            chica "Buen camino ¿eh?"
            "Mejor me concentro en pasarla bien con mis amigos."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
            chica "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chica "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chica "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            "Este es mi momento para poder juntarme con los 2 y no volver a pasar lo de la preparatoria."
            "Debería convencer a Sebastián que se una o me quedo sola con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump final_chicaB1

                "Quedarse con Luna.":
                    jump final_chicaB2

            label final_chicaB1:
                show amiga at right
                show amigo at left
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
                hide amigo
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes amiga me alegra ayudar."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    hide amiga


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tomaste una decisión correcta e hiciste muy buenos amigos."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estas muy preparada para entrar a la universidad y hacer buenos amigos."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            label final_chicaB2:
                chica "Yo prefiero quedarme a estudiar un poco más."
                "No puedo dejar a Luna sola es mejor darle mi apoyo."
                show amigo at left
                amigo "Entiendo, bueno, no importa, los veré después."
                show amiga at right
                amiga "No tienes que irte ahora puedes quedarte."
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián me susurra."
                amigo "Cuida de ella, [nombre], ¿vale? Haz la diferencia por mí vale."
                "Lo miras directamente, haciendo un gesto de afirmación."
                hide amigo
                hide amiga
                "Sebastián se retira dejándonos solas."
                chica "Tranquila, Luna, tienes mi apoyo."
                chica "Después de esto lo veremos y te ayudaré, ¿vale? Debemos permanecer juntos."
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes amiga me alegra ayudar."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotros."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chica "Gracias Luna."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga
                "Ambas nos quedamos estudiando, pero debí convencerlo para que luna estuviera mejor."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Es bueno apoyar a un amigo, pero es mejor cuando puedes hacer más de una diferencia mientras menos estés estresada mejor manejaras los problemas."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparada para la Universidad, pero debes tener en cuenta las acciones que tomas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            #Chica B,B
            label NadaB_Chica:
                "Decides no hacer nada y seguir practicando con Luna, parece preocupada aún."
                chica "Lo siento Luna."
                show amiga_preocupada
                amiga "no pasa nada [nombre]."
                hide amiga_preocupada
                $ estres = 15
                $ renpy.restart_interaction()  
                #Continuar guion 
                "Me quedo con Luna mientras observo cómo Sebastián se va al festival."
                show amiga 
                amiga "Gracias por quedarte, [nombre]."
                chica "A ti, Luna por ayudarme."                
                amiga "[nombre], ¿puedo decirte algo?"
                chica " Claro amiga."
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chica "Sé cómo te sientes Luna y te comprendo."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Si, me alegra que seamos amigas, tenemos algo en común."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chica "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga
                "Me siento mal porque sé que pude haber convencido a Sebastián."
                $ estres = 25
                $ renpy.restart_interaction()  
                #continuar
                scene cuartonoche
                chica "pude haberlo convencido."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso " Luna confía mucho en ti [nombre] no lo eches a perder."
                "Veo una sombra acechándome en el fondo. "
                chica "¿Quién eres?"
                "Veo como se desvanece dejándome con la duda."
                chica "¿Qué o quién era esa voz?"
                scene cuarto
                "Despiertas con un sentimiento de culpa."
                chica "Tranquila solo fue un sueño."
                scene chica_normal
                chica "Solo fue un sueño, hoy veré que Luna esté bien."
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
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
            scene escuela
            chica "Sé que pude haber convencido a Sebastián."
            chica "No quisiera ser responsable de que Luna se distancie de él."
            scene salon
            "Veo a Luna preocupada aún."
            chica "Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga 
            amiga "No te preocupes, Sebastián siempre sale desde la preparatoria, así que estoy acostumbrada."
            chica "Sé que es importante estudiar, pero es bueno salir con personas."
            chica "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar sola."
            amiga "¿Estás bien, [nombre]?"
            chica "Si estoy bien gracias."
            "Veo a Sebastián saludarnos de lejos pero no se ve feliz."
            "Hoy tendremos 3 clases." 
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Salió bien."
                #amiga "Si."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Pudo ser peor."
                #amiga " Práctica más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDia_chicaBB

                "Quedarse Callada.":
                    $ Luna = "Callarse"
                    jump cDia_chicaBB


            label cDia_chicaBB:
                if Luna == "preguntar":
                    chica "Luna ¿estás bien?"
                    show amiga 
                    amiga "Solo estoy preocupada, no quiero que Sebastián piense que lo deje atrás pues él sabe mi situación."
                    "Decido abrazarla fuerte."      
                    chica "Todo estará bien ya lo veras. "
                    amiga "Eso espero. "
                    hide amiga
                    




                elif Luna == "Callarse":  
                    "Un incómodo silencio nos invadió a ambas. "
                    "Intentas calmar a Luna."
                    chica "Cualquier cosa aquí estaré Luna."
                    show amiga 
                    amiga "Lo sé…"  
                    hide amiga
                    "Decido darle ánimo a Luna."
                    

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Genial muy fácil."
                #amiga "Me alegro por ti."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Vaya que si tuve dificultades."
                #amiga "Deberías practicar más."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            "pero notas que Luna está cada vez más desanimada."
            chica "Animo Luna este fin de semana hay que reunirnos con Sebastián en el parque para que te animes ¿qué te parece?"
            show amiga
            amiga "No es mala idea, gracias por preocuparte mucho por mi [nombre]."
            chica "Entonces este fin iremos al parque."
            amiga "Muy bien."

            hide amiga
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Eso estuvo difícil."
                #amiga "Tienes mi apoyo."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chica "Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amiga at right
            amiga "muy bien los veré ahí."
            hide amiga
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chica "Hola Sebastián, Luna y yo nos vamos a reunir este fin de semana ¿te unes?"
            show amigo
            amigo "Claro que sí los veré a las 2 entonces."
            hide amigo
            "Me despido de él regresando a mi casa."
            scene cuarto
            "Al final salió bien, espero que todo salga bien este fin de semana."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso " Ella aún confía en ti."
            "Te sientes menos culpable ya que conviviste con ambos."
            chica "¿Seguiré Dormida?"
            "No creo mejor no pensar en ello y concentrarme para pasarla bien con ellos."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
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
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            "Debería convencer a Sebastián que se una o me quedo sola con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump final_chicaBB1

                "Quedarse con Luna.":
                    jump final_chicaBB2

            label final_chicaBB1:
                show amiga at right
                show amigo at left
                chica "Sebastián esta vez quiero decirte que te quedes con nosotras, la vez del festival no sé por qué no pude hacerlo."
                amigo "No te preocupes se lo que se siente no poder decidir."
                chica "Aun así lo siento, Luna necesita apoyo así que esta vez acompáñanos."
                amigo " Está bien y no te preocupes es hora de pasar tiempo con ustedes esta vez amigas."
                amiga "Gracias a ambos por quedarse conmigo y más en estos tiempos."
                "Los junto a los 2 para estar más juntos."
                chica "La soledad nunca es buena."
                "Sebastián y Luna" "Estamos de acuerdo contigo."
                hide amigo
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son los amigas."
                    hide amiga


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos, aunque me costó trabajo."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Las decisiones que tomamos siempre tienen una solución, nunca hay que quedarnos aferrados a nuestro pasado."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparada para la Universidad, aunque al principio te equivoques recuerda que todo problema tiene una solución y jamás te rindas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            label final_chicaBB2:
                "Me vuelvo a quedar sin palabras para convencerle."
                chica "Yo prefiero quedarme a estudiar un poco más."
                "Luna necesita apoyo ahora más que nunca ahora que se su pasado."
                show amigo at left
                amigo "Entiendo bien, no importa las veré después…"
                show amiga at right
                amiga "Sebastián…"
                amigo "No te preocupes es como en los viejos tiempos diviértanse los 2."
                "Sebastián me susurra."
                amigo "Si de verdad eres mi amiga cuidaras bien de ella ¿Vale?"
                "Decido abrazarlo por la culpa que cargo y le susurro también."
                chica " Lo siento no te fallare te lo prometo."
                "Sebastián corresponde el abrazo y más calmado se retira."
                hide amigo
                chica "Lo siento Luna te he vuelto a fallar."
                amiga "No te preocupes, pero me ayudaras a convivir más con el."
                chica "Te lo prometo."
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica"Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chica "Gracias amiga."
                    chica "No te fallare."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga
                "Ambas nos quedamos estudiando."
                "Debo cumplir con estas promesas."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Las decisiones que tomamos, aunque nos equivoquemos muchas veces podemos resolverlas tardarán más, pero siempre tienen solución."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Siempre que tengas dificultades con una amistad intenta resolverlo de la mejor manera pues una amistad te da más oportunidades en la vida y también nos pueden ayudar a reducir el estrés que tenemos."
                misterioso "Si entras a la universidad ten en cuenta todas las posibilidades."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return
                



        # ChicaA       
        label cansada2:
            $ estres = 20
            $ renpy.restart_interaction() 
            scene cuartonoche
            chica "Bueno, un libro no hara daño."
            scene negro
            "Lees un buen libro y pierdes la noción del tiempo."
            scene cuarto
            "Despiertas con dificultad, sintiendo mucho sueño."
            scene wc 
            "Apenas puedes abrir los ojos, el cansancio te consume."
            scene chica_normal
            "Te miras al espejo, tratando de reconocer a la persona reflejada."
            chica "Creo que me emocione mucho."
            "Suspiro."
            chica "Bueno, diría que demasiado, Pero no hay vuelta atrás, es hora de ir a la universidad."
            scene cocina
            "Desayunas lo primero que encontraste y vas corriendo para tomar el transporte. " 
            scene negro
            "¿Ahora que debería tomar?"
            menu:
                "Tomar Tren":
                    jump Tren8

                "Tomar Autobus":
                    jump Autobus8  
        label Tren8:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Es el más rápido."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Bueno lo mejor será tomar el tren ya que el autobús fue mas lento. "
              
            jump ChicaA
        
        label Autobus8:

            if transporte == "tren": 
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus 
                "El tren es rápido, pero aún tengo tiempo para llegar  ."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Bueno, aunque es más lento es el más económico."
              
            jump ChicaA   
       
       
       
        #Ruta A
        label ChicaA:
            scene escuela
            "Aquí vamos de nuevo."
            scene salon
            show amiga
            amiga "¿Lista para continuar?"    
            chica "Claro que sí."
            amiga "¿Te sientes bien, te ves un poco cansada?"     
            chica "Si estoy bien no te preocupes."       
            hide amiga
            show maestro
            maestro "Muy bien clase vamos a repasar lo que vimos la clase anterior."
            "Oh no, tengo mucho sueño."
            hide maestro
            #Agregar Minijuego 2
            #if juego == "gana":
                #chica "Eso fue fácil muchas gracias Luna."
            #elif juego == "pierde":
            chica "Rayos, casi no me pude concentrar bien, pero gracias a Luna no fue tan mal."
            $ estres = 15
            $ renpy.restart_interaction()
            show amiga
            amiga "vamos anímate no estuvo tan mal."
            chica "Bueno si tú lo dices, esperemos que en la siguiente vaya mejor."
            amiga "ya verás que sí."
            hide amiga
            "sigo un poco cansado, pero veo que entra la maestra."
            show maestra
            maestra "Buenas tardes alumnos, espero que su inicio de semana haya sido agradable."
            chica "bueno a empezar con la siguiente materia."
            hide maestra
            #Minijuego 3 agregar 

            #if juego == "gana":
            show amiga
            amiga "Bueno, bueno explica muy bien la maestra. "
            chica "Sí, tienes razón."
            #elif juego == "pierde":
                #chica "Estuvo complicado."
            amiga "sigo preocupada por Sebastián seguro tuvo problemas en la anterior. "
            chica "tienes razón ahora hay que convencerlo de que practique con nosotros. "
            amiga "Buena suerte con eso."
            hide amiga
            menu:
                "Convencerlo de que se te una.":
                    jump ConvencerA_Chica

                "No hacer nada.":
                    jump NadaA_Chica




            #Chica A
            label ConvencerA_Chica:
                chica "Oye, Sebastián, ¿por qué no te nos unes hoy para practicar la materia?"
                show amigo
                amigo "Pero habrá un festival."   
                chica "Vamos hazlo por mí y por Luna."     
                amigo "Te ves muy cansado, pero está bien, me uniré a ustedes. El festival puede esperar."
                chica "No te arrepentirás."
                $ estres = 20
                $ renpy.restart_interaction()
                #Continuar guion
                "Nos quedamos con luna parecía muy feliz."
                show amiga at left
                amiga "Gracias por acompañarme amigos."
                show amigo at right
                "Sebastián y [nombre]" "A ti, Luna, por ayudarnos con esto, nos va a servir mucho." 
                hide amigo
                hide amiga
                "Pasa el tiempo y estudiamos un rato mas con Luna."
                "Observó como Sebastián se retira para ir con lo que quedó del festival, pero decido acompañar un rato más a Luna."
                show amiga
                amiga "[nombre], ¿puedo decirte algo?"
                chica " Claro amiga."
                amiga "Muchas gracias por acompañarme, aprecio mucho esto."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre] y gracias por estar conmigo."
                chica "Sé cómo te sientes Luna y te comprendo."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Si, me alegra que seamos amigas, tenemos algo en común."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chica "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga
                $ estres = 15
                $ renpy.restart_interaction()
                #continuar
                scene cuartonoche
                "Te acuestas a dormir porque te sentías muy cansada, pero a pesar de todo, el día salió bien."
                "Mientras tus ojos se cierran, tu mente repasa las últimas horas... algo se siente fuera de lugar, pero decides no pensar demasiado en ello."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Vas muy bien [nombre]."
                "En tu sueño, una figura borrosa y oscura se hace presente, una extraña sombra se desplaza hacia ti."
                chica "¿Quién eres?"
                misterioso "Sigue por el camino que vas y no te desvíes."
                "La sombra se desvanece antes de que puedas obtener más respuestas, dejándote con una sensación de inquietud."
                scene cuarto
                " Te despiertas sobresaltada y con la mente llena de preguntas, pero te das cuenta de que ya no te sientes cansada."
                chica "¿Qué habrá sido esa cosa?  "
                " Intentas deshacerte del recuerdo del sueño, diciéndome que es mejor no pensar en ello."
                scene chica_normal
                chica "Hoy va a ser un buen día, mejor dejar atrás esos pensamientos extraños."
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren24

                    "Tomar Autobus":
                        jump Autobus24  
        label Tren24:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump Dia_chicaA
        
        label Autobus24:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump Dia_chicaA








        label Dia_chicaA:
            scene escuela
            chica "Hoy espero volver a pasar tiempo con luna y Sebastián."
            scene salon
            "Veo a Luna y a Sebastián reunidos y me decido a saludarlos."
            chica "Hola amigos ¿cómo están?"
            show amiga at right 
            amiga "Hola [nombre], te ves mejor que ayer y bien espero que tú también."
            show amigo at left
            amigo "Si opino lo mismo y también bien ¿y tú como estas?"
            chica " Muy bien ¿hoy vamos a quedarnos a repasar verdad?"
            amiga "Claro, muy pronto tendremos un examen."
            amigo "Si será lo mejor."
            "Empieza la clase."
            chica "¿Hoy tendremos 3 clases verdad?"
            amiga "Según el horario sí."
            chica "Vale gracias Luna."
            hide amigo
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            amigo "Juntos podemos con esto."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "fue facil."
                #amiga "Eso es verdad."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDia_chicaA

                "Quedarse Callada.":
                    $ Luna = "Callarse"
                    jump cDia_chicaA


            label cDia_chicaA:
                if Luna == "preguntar":
                    chica "Luna como has estado."
                    "Decido abrazarla por lo que pasó ayer."
                    show amiga at right
                    amiga "Me he sentido mejor Gracias por preguntar."
                    show amigo at left
                    amigo "¿aún preocupada Luna?, eres lista y tú puedes con todo."
                    amiga "Gracias a ambos por el apoyo."
                    amiga "Sin ustedes no sé qué haría."
                    hide amiga
                    hide amigo




                elif Luna == "Callarse":  
                    "Te quedas callado, pero te quedas cerca de ella."
                    chica "No tengo palabras ahorita, pero tienes mi apoyo Luna."
                    show amiga at right
                    amiga "Gracias, lo aprecio mucho."  
                    show amigo at left
                    amigo "también estoy aquí y me quedaré contigo Luna."
                    amiga "Gracias a ambos de verdad."
                    hide amiga
                    hide amigo

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Genial muy fácil."
                #amiga "Practicando todo se logra."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Vaya que si tuve dificultades."
                #amiga " Deberías practicar un poco más [nombre]."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            show amigo at left
            amigo "vaya un fin de semana no puede ser que ya tengamos exámenes."
            show amiga at right
            amiga "Lo sé, pero esto ya es la Universidad, siempre hay momentos para divertirse, pero lo más recomendable sería estudiar para pasar los exámenes."
            amigo "Bueno ya lo veremos el fin de semana."
            chica "A puesto que será divertido quizá nos podamos reunir para estudiar y divertirnos."
            amiga "Eso suena a una excelente idea."
            amigo "Opino lo mismo."
            chica "Entonces no se diga más nos veremos en el parque."
            hide amigo
            hide amiga
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Eso estuvo difícil."
                #amiga "No te rindas  [nombre]."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chica "Bueno nos reuniremos en un parque para pasar tiempo los 2."
            show amiga at right
            amiga "muy bien los veré ahí."
            show amigo at left
            amigo "igual nos veremos allí."
            hide amiga
            hide amigo
            scene cuarto
            "Regresamos todos a nuestras casas para pasar un buen fin de semana."
            
            scene negro
            "Es la primera vez que estoy muy relajada, Estudiar con amigos es mejor que sola ya que aprendes más."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Recuerda vas muy bien."
            "Te sientes confusa."
            chica "¿Otra vez?"
            "Bueno no importa debo estar concentrada."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
            chica "Hola luna."
            amiga "Hola [nombre]."
            amiga "veo que aún no llega Sebastián."
            chica "Sí yo creo que no tarda en llegar, veo que trajiste material para estudiar."
            amiga "Si, es para estudiar para el examen."
            chica "Perfecto esperemos a Sebastián para poder estudiar juntos."
            amiga "Está bien."
            "Llega Sebastián y comenzamos estudiando los 3."
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola pero tampoco conozco los sentimientos de Sebastián."
            "Debería convencer a Sebastián que se una o me quedo sola con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump final_chicaA1

                "Quedarse con Luna.":
                    jump final_chicaA2

            label final_chicaA1:
                show amiga at right
                show amigo at left
                chica "Sebastián, podemos dejarlo para otro fin de semana."
                chica "Hoy hay que darle todo el apoyo a Luna."
                amigo "Tienes razón, es momento de saber cuándo hay que divertirse y cuándo hay que apoyar en momentos difíciles."
                amiga "Gracias por quedarte esta vez Sebastián."
                amiga "Y a ti, [nombre], por ayudarme."
                hide amigo
                hide amiga
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudar amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    hide amiga


                "Los tres nos quedamos estudiando para el examen, el cual todos aprobamos."
                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Tomaste una decisión correcta al principio te desviaste, pero ahora sabes cuando es el momento para divertirse y cuando dedicarle tiempo al estudio."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estas muy preparada para entrar a la universidad y hacer buenos amigos."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                

            label final_chicaA2:
                chica "Yo prefiero quedarme a estudiar un poco más."
                "Recuerdo lo que Luna me contó sobre su pasado, y sé que necesita apoyo ahora más que nunca."
                show amigo at left
                amigo "Entiendo... no importa, las veré después."
                show amiga at right
                amiga "Sebastián…"
                amigo "No te preocupes, es como en los viejos tiempos."
                "Sebastián se acerca y me susurra al oído."
                amigo "Cuida de ella, [nombre], ¿vale?"
                "Lo miras directamente, haciendo un gesto de afirmación, sintiendo el peso de su petición."
                hide amigo
                hide amiga
                "Al verlo marcharse, me quedo pensando si realmente tomé la decisión correcta."
                "Pero no quiero que Luna se sienta sola, así que dejo esos pensamientos de lado."
                chica "Tranquila, Luna, tienes mi apoyo."
                chica "Después de esto lo veremos y te ayudaré, ¿vale?"
                amiga "Gracias [nombre]."
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudar amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    amiga "Aunque no este sebastián el aprecia que me apoyes."
                    chica "Gracias Luna."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    hide amiga
                "Aunque me quedo con Luna para estudiar, no puedo evitar que, en el fondo de mi mente, una pequeña duda me siga preguntando por qué no convencí a Sebastián de quedarse también."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Es bueno apoyar a un amigo, pero es mejor cuando puedes hacer más de una diferencia mientras menos estés estresado mejor manejaras los problemas."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparada para la Universidad, pero debes tener en cuenta las acciones que tomas."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return






            #Chica A,A
            label NadaA_Chica:
                "Decides no hacer nada y seguir practicando con Luna, quien parece estar preocupada aún."
                chica "Lo siento Luna."  
                show amiga_preocupada
                amiga "no pasa nada [nombre]."
                hide amiga_preocupada
                $ estres = 30
                $ renpy.restart_interaction()  
                #Continuar guion
                "Decides quedarte con Luna mientras observas cómo Sebastián se va al festival."
                "Te sientes realmente cansada."
                show amiga 
                amiga "Gracias por quedarte, [nombre]."
                chica "A ti, Luna por ayudarme."                
                amiga "[nombre], ¿puedo decirte algo?"
                chica " Claro amiga."
                amiga "Quería agradecerte por acompañarme."
                amiga "Esto significa mucho para mí."
                "Veo a Luna un poco triste, así que decido preguntar qué le sucede."
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre]."
                amiga "Gracias por estar aquí."
                chica "Entiendo cómo te sientes, Luna."
                chica "Aquí estoy contigo amiga."
                chica "Mis padres también siempre quieren que sea perfecta."
                amiga "¿De verdad?"
                chica "Si, me alegra que seamos amigas, tenemos algo en común."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chica "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga
                "Te sientes mal porque sabes que pudiste haber convencido a Sebastián, pero el cansancio te supera."
                $ estres = 45
                $ renpy.restart_interaction() 
                #Continuar guion 
                "Decides quedarte con Luna mientras observas cómo Sebastián se va al festival."
                "Te sientes realmente cansado."
                show amiga
                amiga "Gracias por quedarte, [nombre]."
                chica "A ti, Luna por ayudarme."
                amiga "[nombre], ¿puedo decirte algo?"
                chica "Claro Luna."
                amiga "Quería agradecerte por acompañarme."
                amiga "Esto significa mucho para mí."
                "Ves a Luna un poco triste y decides preguntar qué le sucede. "
                chica "¿Estás bien, Luna?"
                amiga "Sí, es solo que siempre me he sentido sola."
                amiga "Aunque en la preparatoria estaba con Sebastián, no pude convivir mucho."
                amiga "Mis padres esperan que sea perfecta, sin margen de error."
                hide amiga
                "Observas cómo comienza a llorar, por lo que decides abrazarla."
                show amiga_triste
                amiga "de verdad lo aprecio mucho [nombre]."
                amiga "Gracias por estar aquí."
                chica "Entiendo cómo te sientes, Luna."
                chica "Estoy aquí para ti."
                "Secas sus lágrimas y te despides de ella, regresando a casa."
                hide amiga_triste
                show amiga
                chica "nos vemos Luna."
                amiga "Cuidate mucho [nombre]."
                hide amiga 
                "Te sientes mal porque sabes que pudiste haber convencido a Sebastián, pero el cansancio te supera."
                $ estres = 45
                $ renpy.restart_interaction()
                #Continuar historia
                scene cuartonoche
                chica "pude haberlo convencido, pero estaba muy cansada..."
                "Te acuestas a dormir, aunque con dificultades por no haber hecho nada."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso " Sabes que pudiste hacer algo, ¿no crees?"
                "Veo una sombra acechándome en el fondo. "
                chica "¿Quién eres?"
                "Solo veo como me observa y se desvaneció dejándome una sensación de culpabilidad."
                scene cuarto
                " Despiertas nerviosa."
                chica "¿Solo fue un sueño?"
                "Aun te sientes culpable, pero intentas deshacerte del recuerdo del sueño, diciéndote que es mejor no pensar en ello."                
                scene chica_normal
                chica "Espero que Luna esté bien. "
                scene cocina
                "Te preparas un Desayuno para ir a la escuela."
                scene negro
                "¿Qué transporte tomo hoy?"
                menu:
                    "Tomar Tren":
                        jump Tren25

                    "Tomar Autobus":
                        jump Autobus25  
        label Tren25:
       
        
            if transporte == "tren":  
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Otro día mas que emoción."  
            elif transporte == "autobus":
                image treen = Movie(play="Tren.webm", size=(1920, 1080))
                show treen
                "Así llego mas rapido."
             
            jump Dia_chicaAA
        
        label Autobus25:

            if transporte == "tren":  
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "El tren es rápido, pero aun tengo mucho tiempo."  
            elif transporte == "autobus":
                image aautobus = Movie(play="Autobus.webm", size=(1920, 1080))
                show aautobus
                "Aun tengo tiempo."
             
            jump Dia_chicaAA








        label Dia_chicaAA:
            scene escuela
            chica "Sé que pude haber convencido a Sebastián."
            chica "No quisiera ser responsable de que Luna se distancie de él."
            scene salon
            "Veo a Luna preocupada aún."
            chica"Luna, realmente quiero disculparme por no haber hecho nada."
            show amiga 
            amiga "No te preocupes [nombre], Sebastián siempre sale desde la preparatoria, así que estoy acostumbrada."
            chica "Sé que es importante estudiar, pero es bueno salir con personas."
            chica "No toda la vida será solo estudiar, Luna."
            "Esta situación me pone mal, pero haré lo que pueda por ella."
            "Uno nunca debe estar sola."
            amiga "¿Estás bien, [nombre]?"
            chica "Si estoy bien gracias."
            "Veo a Sebastián saludarnos de lejos pero no se ve feliz."
            "Hoy tendremos 3 clases." 
            hide amiga
            show maestra
            maestra "Muy bien Alumnos hoy les impartiré 2 clases."
            maestra "Vamos a ver el tema de hoy."
            chica "Aquí vamos de nuevo."
            amiga "Vamos allá."
            hide maestra
            #agregar cuarto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Salió bien."
                #amiga "Si."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Esto salió fatal."
                #amiga " Práctica más. "
                #hide amiga
            "Termina la primera clase, pero la maestra nos da un tiempo libre."
            "Aprovecho el tiempo para hablar con Luna."
            menu:
                "¿Preguntar a luna como esta?":
                    $ Luna = "preguntar"
                    jump cDia_chicaAA

                "Quedarse Callada.":
                    $ Luna = "Callarse"
                    jump cDia_chicaAA


            label cDia_chicaAA:
                if Luna == "preguntar":
                    chica "Luna ¿estás bien?"
                    show amiga 
                    amiga "Solo estoy preocupada, no quiero que Sebastián piense que lo deje atrás pues él sabe mi situación."
                    "Decido abrazarla fuerte."      
                    chica "Todo estará bien ya lo veras. "
                    amiga "Eso espero. "
                    hide amiga
                    




                elif Luna == "Callarse":  
                    "Un incómodo silencio nos invadió a ambas. "
                    "Intentas calmar a Luna."
                    chica "Cualquier cosa aquí estaré Luna."
                    show amiga 
                    amiga "Lo sé…"  
                    hide amiga
                    "Decido darle ánimo a Luna."
                    

            "Se termina el tiempo y continúa la siguiente clase."   
            show maestra
            maestra "Bueno jóvenes comencemos la siguiente clase." 
            hide maestra
            #agregar cuinto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Genial muy fácil."
                #amiga "Me alegro por ti."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Vaya que si tuve dificultades."
                #amiga "Deberías practicar más."
                #hide amiga 
            show maestra
            maestra " Bueno clase, estudien porque la siguiente semana será de exámenes pues estos definirán su futuro."
            maestra "Su otro profesor les enseñará mejor el tema de una manera diferente para que refuercen."
            hide maestra  
            "Nos relajamos por un momento en lo que iniciaba la siguiente clase."
            "pero notas que Luna está cada vez más desanimada."
            chica "Animo Luna este fin de semana hay que reunirnos con Sebastián en el parque para que te animes ¿qué te parece?"
            show amiga
            amiga "No es mala idea, gracias por preocuparte mucho por mi [nombre]."
            chica "Entonces este fin iremos al parque."
            amiga "Muy bien."

            hide amiga
            "Observó cómo Luna se veía más calmada."
            "Ves entrar al maestro Carlos, dando inicio a la última clase."
            show maestro
            maestro "Muy bien clase hoy veremos nuevo tema espero que estén preparados."
            hide maestro
            #agregar sexto minijuego 
            #if juego == "gana":
                #show amiga
                #chica "Estuvo bien."
                #amiga "Te lo dije."
                #hide amiga
            #elif juego == "pierde":
                #show amiga 
                #chica "Eso estuvo difícil."
                #amiga "Tienes mi apoyo."
                #hide amiga 
            "Termina la clase, finalizando el día de hoy."
            chica "Bueno, nos reuniremos en el parque para pasar tiempo juntos."
            show amiga at right
            amiga "muy bien los veré ahí."
            hide amiga
            "Ves cómo Luna se va un poco mejor y decides acercarte a Sebastián."
            chica "Hola Sebastián, Luna y yo nos vamos a reunir este fin de semana ¿te unes?"
            show amigo
            amiga "Claro que sí los veré a las 2 entonces."
            hide amigo
            "Me despido de él regresando a mi casa."
            scene cuarto
            "Al final salió bien, espero que todo salga bien este fin de semana."
            scene parque 
            "Comienza el fin de semana donde por fin me reuniré con Luna y Sebastián."
            scene negro
            misterioso "Ahora puedes hacer la diferencia."
            "Te sientes menos culpable, pero confusa."
            chica "¿Otra vez el?"
            "Bueno, debo estar concentrada."
            scene parque
            "Me siento a esperar a Luna y Sebastián."
            "Pasa un tiempo y veo llegar a Luna primero."
            show amiga at right
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
            show amigo at left
            "Pasa un tiempo después de estudiar."
            amigo "Es bueno estudiar con ustedes, aunque quisiera aprovechar el resto del día para pasarla con ustedes chicas ¿Qué opinan?"
            amiga "Yo quisiera estudiar un poco más para el examen."
            amigo "¿Tú qué opinas [nombre]?"
            chica "¿Yo?"
            "¿Qué debo hacer?"
            "Luna se ha sentido mal y no quiero dejarla sola, además ya le falle una vez, debo pensarlo bien, pero tampoco conozco los sentimientos de Sebastián."
            "Esta vez quiero convivir con ambos, no quiero herir los sentimientos de ambos."
            "Debería convencer a Sebastián que se una o me quedo solo con Luna."
            hide amiga
            hide amigo
            menu:
                "Convencer a Sebastián.":
                    jump final_chicaAA1

                "Quedarse con Luna.":
                    jump final_chciaAA2

            label final_chicaAA1:
                show amiga at right
                show amigo at left
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
                hide amigo
                hide amiga
                "Pasan la tarde juntos, disfrutando del tiempo como amigos y estudiando. "
               
                if Luna == "preguntar":
                    show amiga
                    amiga "[nombre], Gracias por todo el apoyo que me diste espero poder compensarlo algún  día."
                    chica "No te preocupes me alegra ayudarte esta vez amiga."
                    chica "Es mejor apoyarnos en momentos de estudios."
                    chica "Es malo estar sola tanto en la vida como en los estudios."
                    amiga "Lo se."
                    amiga "Es mejor ayudarnos entre nosotras."
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."

                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía ."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    hide amiga

                "Es mejor estudiar con amigos que pasarla sola y hoy hice 2 grandes amigos, aunque me costó trabajo."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Pudiste hacer la diferencia esta vez [nombre] te desviaste a la hora de tomar en cuenta los sentimientos de Luna, pero al final lo resolviste de la mejor manera."
                misterioso "Nunca te sientas sola, siempre busca ayuda y más en momentos de Universidad."
                misterioso "Puedo decir que estás preparada para la Universidad, aunque al principio te equivoques recuerda que todo problema tiene una solución."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return




            label final_chicaAA2:
                "Me siento mal al no volver a convencer a Sebastián, pero con pocos ánimos respondo."
                chica "Lo siento, Sebastián."
                chica "Creo que esta vez me quedaré con Luna. "
                "No quiero que se quede sola."
                show amigo at left
                amigo "Lo entiendo, no te preocupes."
                amigo "Me reuniré con otros amigos entonces."
                show amiga at right
                amiga "Sebastián…"
                hide amigo
                "Ves cómo Sebastián se va, dejándote con Luna."              
                amiga "Gracias por quedarte conmigo, [nombre]."
                chica "Lo haré siempre que lo necesites, Luna."
                hide amiga
                "Pasan la tarde estudiando juntas, aunque sientes un poco de tristeza por no haber salido con Sebastián."
                "Luna parece estar un poco más tranquila, pero sabes que aún queda mucho por superar."
                "Decides tomar un descanso después de un largo día de estudio."
                if Luna == "preguntar":
                    show amiga
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
                    hide amiga
                    "Luna me abraza y siento mucha paz con su abrazo."
                elif Luna == "Callarse":
                    show amiga
                    amiga "Se que me querías decir algo [nombre]."
                    amiga "Solo quiero decirte lo mucho que aprecio tu compañía y el apoyo que me das."
                    chica "Yo también aprecio tu compañía  y el apoyo que me has dado."
                    amiga "para eso son las amigas."
                    amiga "Veremos a Sebastián después de repasar."
                    chica "Lo mejor sera darle espacio."
                    amiga "Si tiene razón [nombre]."
                    hide amiga
                
                "Estás satisfecho de haber apoyado a Luna, pero también sabes que aún hay retos por enfrentar."
                image misteriosoo = Movie(play="sueño.webm", size=(1920, 1080))
                show misteriosoo
                misterioso "Siempre hay que ser conscientes antes de tomar decisiones. "
                misterioso "Antes de tomar una acción piensa a futuro alejaste a Sebastián de Luna y esto siempre puede traer mal entendidos."
                misterioso "Solo se consciente y recuerda si estás a punto de entrar a la Universidad o estás en ella has buenas amistades la soledad nunca es una buena opción. "
                misterioso "Mucha suerte."

                scene negro

                "Demo completada, pero hay otros caminos para elegir."

                return  
                     


return