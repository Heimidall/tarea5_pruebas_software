#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import logging
def obtener_data(photo, bucket,tol):
    logging.info("Analizando la foto {}".format(photo))
    client=boto3.client('rekognition')
    data=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    palabras = []
    for text in data['TextDetections']:
        if(text['Type'] == "WORD" and text['Confidence'] >= tol):
            palabras.append((text['DetectedText'])) 
            logging.info("La palabra detectada es: {} con confidence {}".format(text['DetectedText'],text['Confidence']))
    logging.info("El set de palabras obtenidos es: {}".format(palabras))
    return palabras

def main():
    f = open("imagenes.txt","r")
    bucket_name = f.readline().rstrip()
    imagen_control = f.readline().rstrip()
    imagenes = f.readline().split(",")
    #print(bucket_name, imagen_control,imagenes)
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    
    tolerancia = 97
    text_control = obtener_data(imagen_control,bucket_name, tolerancia)
    logging.info("El set de palabras utilizado como control es: {}".format(text_control))
    for imagen in imagenes:
        new_text = obtener_data(str(imagen),bucket_name, tolerancia)
        logging.info("Se compara el set de control {} con el de la imagen {}".format(text_control, new_text))
        if(set(text_control).issubset(set(new_text))):
            print("True")
            logging.info("True")
            logging.info("La imagen de control esta contenida dentro de la imagen de test")
        else:
            print("False")
            logging.info("False")
            logging.info("La imagen de control no esta contenida dentro de la imagen de test")
    return None



if __name__ == "__main__":
    main()