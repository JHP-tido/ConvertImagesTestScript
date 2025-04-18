# Script para probar pillow y multiprocessing para realizar conversiones y ajuste de tamaño de imágenes.

El script hace uso del módulo pillow para la conversión y cambio de tamaño de imágenes, y el módulo de multiprocessing para 
realizar la tarea en paralelo. Esto podría ayudar a realizar la conversión y el cambio de tamaño a una mayor velocidad al repartir
cada imagen como un proceso.

Las conversiones las realiza desde un directorio superior llamado images(../images) a donde esté el script y lo almacena en un directorio 
superior llamado /opt/icons/(../opt/icons). La conversión rota la imágen 90º en el sentido contrario a las agujas de reloj, cambia el 
tamaño a 128,128, elimina las capas y deja sólo RGB y finalmente convierte a JPEG y almacena.