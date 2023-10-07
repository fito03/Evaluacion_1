from django.shortcuts import render

# Create your views here.
def renderIndex(request):
    return render(request, 'templatesAPP1/index.html')

def renderUsuario(request):
    return render(request, 'templatesAPP1/usuario.html')



data = {
        '1': {'titulo':'Xiaomi 12 pro 5G', 'imagen':'celu_1.png', 'precio':'$1.000.000', 'descripcion':'Fotografía profesional en tu bolsillo Descubre infinitas posibilidades para tus fotos con las 3 cámaras principales de tu equipo. Pon a prueba tu creatividad y juega con la iluminación, diferentes planos y efectos para obtener grandes resultados. La cámara gran angular toma encuadres amplios de paisajes y permite sumar más integrantes a las fotografías grupales para que nadie quede afuera.'},
        '2': {'titulo':'Xiaomi 13T', 'imagen':'celu_2.png', 'precio':'$1.200.000', 'descripcion':'El Xiaomi 13 Pro, forma parte de la serie 13 de dispositivos de la marca Xiaomi, se centra en la fotografía gracias a su colaboración con Leica. Un dispositivo que tiende un puente entre las imágenes legendarias del siglo pasado y las obras maestras modernas porque se compone de lentes profesionales, Es un dispositivo que se destaca por su forma curvada. La pantalla frontal es resistente creada con Corning Gorilla Glass Victus .'},
        '3': {'titulo':'Xiaomi Redmi A2', 'imagen':'celu_3.png', 'precio':'$1.400.000', 'descripcion':'Xiaomi Redmi A2+ 3GB 64GBEl Xiaomi Redmi A2+ es un smartphone chino con capacidad para redes 4G y doble SIM que pertenece a la serie Xiaomi Redmi, específicamente a la gama de entrada. Cuenta con una pantalla IPS de 6,52 pulgadas (16,561 cm) con resolución de 1.650 x 720 píxeles (HD) y una frecuencia de refresco de 60 Hz'},
        '4': {'titulo':'Xiaomi Mi Smart Kettle', 'imagen':'hogar_1.png', 'precio':'$49.990', 'descripcion':'Disfruta de una experiencia única y práctica con la Pava Eléctrica Xiaomi Kettle Pro en acero inoxidable y color blanco. Con una capacidad de 1.5 litros, esta jarra eléctrica te permitirá calentar agua de manera rápida y eficiente para preparar tus infusiones, mates o cafés favoritos en cualquier momento del día.'},
        '5': {'titulo':'Mi Bedside Lamp 2', 'imagen':'hogar_2.png', 'precio':'$59.990', 'descripcion':'Funciona con Apple Homekit, Siri, APP Remote Control Puedes utilizar Apple, iPad, Apple Watch, la aplicación doméstica y Siri para controlar fácilmente con toque, voz e incluso ajustes automatizados. Gran área luminosa La lámpara de noche está hecha de molde invertido de alta dificultad y diseño de canal caliente; hace que toda la lámpara se ilumine uniformemente. Crea un ambiente práctico y romántico.'},
        '6': {'titulo':'Xiaomi Smart Doorbell 3', 'imagen':'hogar_3.png', 'precio':'$84.990', 'descripcion':'Timbre Inteligente Xiaomi Smart Doorbell 3 Cada detalle en claridad nítida 2K • La imagen de mayor calidad garantiza buenos resultados de visualización. Video claro incluso en la oscuridad • Las 4 luces infrarrojas integradas de alta potencia de 940 nm permiten que las imágenes se capturen claramente incluso con poca o sin luz. Monitoreo en tiempo real • El monitoreo en tiempo real permite la activación remota del timbre y la visualización de la cámara por medio de un smartphone.'},
        '7': {'titulo':'Xiaomi Redmi Buds 4 White', 'imagen':'audio_1.png', 'precio':'$49.990', 'descripcion':'Los Audífonos Inalámbricos Xiaomi Redmi Buds 4 ofrecen una experiencia auditiva inalámbrica, con sonido claro y equilibrado. Perfectos para disfrutar de tu música y llamadas sin cables'},
        '8': {'titulo':'Audífonos Mi In-Ear Headphones Basic', 'imagen':'audio_2.png', 'precio':'$7.990', 'descripcion':'Audífonos Xiaomi Mi in ear Jack 3.5mm Los auriculares Mi In-Ear Jack 3.5mm de Xiaomi, fabricados con aleación de aluminio y diseño en metal anodizado anti huellas y anti rayaduras, más durable. Cuenta con un sistema de equilibrio de amortiguación de tercera generación que adopta la única cavidad de sonido frontal y trasera, perfectamente optimiza el rendimiento de tres frecuencias que aportan una experiencia musical más clara y detallada.'},
        '9': {'titulo':'Mi Parlante Portable Bluetooth', 'imagen':'audio_3.png', 'precio':'$29.990', 'descripcion':'Duración de la batería de 10 horas: equipada con una batería de alta capacidad de 2000 mAh, puede reproducir música hasta 10 horas cuando está completamente cargada. Batería grande, batería de larga duración, hace que la música acompañe más tiempo. Una clave para llamar: micrófono incorporado de alta sensibilidad y alta relación señal / ruido, tecnología de cancelación de eco integrada, para garantizar llamadas transparentes y claras, de modo que cada llamada sea como una comunicación cara a cara.'},
    }

def renderCelular(request,id):

    if id in data:
        return render(request, 'templatesAPP1/descripcion.html', data[id])
    if id == '0': 
        dataCelu = {}
        for i in range(1,4):
            clave_prefijo = f'{i}'
            i = str(i)
            dataCelu['categoria'] = 'Celulares'
            dataCelu[f'btn_{i}'] = f'celulares/{i}'
            dataCelu[f'titulo_{i}'] = data[clave_prefijo]['titulo']
            dataCelu[f'imagen_{i}'] = data[clave_prefijo]['imagen']
            dataCelu[f'precio_{i}'] = data[clave_prefijo]['precio']
            dataCelu[f'descripcion_{i}'] = data[clave_prefijo]['descripcion']
        return render(request, 'templatesAPP1/productos.html', dataCelu)

def renderHogar(request,id):
    if id in data:
        return render(request, 'templatesAPP1/descripcion.html', data[id])
    if id == '0':
        dataHogar = {}
        for i in range(4,7):
            x = i - 3
            clave_prefijo = f'{i}'
            i = str(i)
            dataHogar['categoria'] = 'Hogar'
            dataHogar[f'btn_{x}'] = f'hogar/{i}'
            dataHogar[f'titulo_{x}'] = data[clave_prefijo]['titulo']
            dataHogar[f'imagen_{x}'] = data[clave_prefijo]['imagen']
            dataHogar[f'precio_{x}'] = data[clave_prefijo]['precio']
            dataHogar[f'descripcion_{x}'] = data[clave_prefijo]['descripcion']
        return render(request, 'templatesAPP1/productos.html', dataHogar)

def renderAudio(request,id):
    if id in data:
        return render(request, 'templatesAPP1/descripcion.html', data[id])
    if id == '0':
        dataAudio = {}
        for i in range(7,10):
            x = i - 6
            clave_prefijo = f'{i}'
            i = str(i)
            dataAudio['categoria'] = 'Audio'
            dataAudio[f'btn_{x}'] = f'audio/{i}'
            dataAudio[f'titulo_{x}'] = data[clave_prefijo]['titulo']
            dataAudio[f'imagen_{x}'] = data[clave_prefijo]['imagen']
            dataAudio[f'precio_{x}'] = data[clave_prefijo]['precio']
            dataAudio[f'descripcion_{x}'] = data[clave_prefijo]['descripcion']
        return render(request, 'templatesAPP1/productos.html', dataAudio)


