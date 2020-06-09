# tarea5_pruebas_software
Código para el trabajo con aws rekognition y python.
Para su uso lo primero que se debe hacer es cargar las imagenes dentro de la carpeta imagenes en su Bucket S3 en AWS.
Una vez que tenga las imagenes cargadas en su bucket, debe modificar el archivo "imagenes.txt" el cual posee la siguiente estructura:
linea 1: Nombre de su bucket creado en AWS
linea 2: Nombre de la imagen que utilizará como imagen de control. Por ejemplo: imagen_control.png
linea 3: El nombre de las imagenes que se desean analizar separadas por una coma. Por ejemplo: imagen1.jpg,imagen2.jpg,imagen3.jpg,imagen4.png (Estos deben ser todos en una sola linea)

una vez que cargo las imagenes a su bucket y modificó el archivo imagenes.txt, abra una terminal dentro de la carpeta donde tiene el programa y ejecute:
python tarea5.py
Al momento de hacer funcionar el programa leerá los datos entregados en el archivo y ejecutará los tests en el orden que se escribieron dentro del archivo, retornando true o false
en caso que las palabras de la imagen de control se encuentren dentro de la imagen de test.