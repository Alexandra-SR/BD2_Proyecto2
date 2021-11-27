# BASE DE DATOS 2 
## Proyecto 2

## Integrantes ✒️

- Juan Pablo Lozada [IWeseI] Participación: 100%
- Alexandra Shulca [Alexandra-SR] Participación: 100%
- Alex Loja Zumaeta [aljozu] Participación: 100%

## Profesor 🦾

- Heider Sanchez Enriquez

## Asistente de docencia
- Juan Galvez Ccopa


## Introducción :dart:

**_Objetivo:_**  Entender y aplicar los algoritmos de búsqueda y recuperación de información basado en el contenido. En este proyecto nos enfocaremos en la construcción óptima de un _Índice Invertido_. En este caso usaremos un dataset de tweets, que nos permitirá encontrar los tweets más relevantes dado un término de búsqueda. 

**_Descripción del dominio:_** Usaremos una colección  de  aproximadamente [20 mil  tweets  de  Twitter] (https://onedrive.live.com/?cid=0c2923df9f1f816f&id=C2923DF9F1F816F%2150804&ithint=folder&authkey=!ANNEKv7tNdlSSQk). En donde el diccionario de términos se construyó usando el contenido del atributo “text”, y el el Id del tweet.  Existen más de 10 mil registros y por cada uno tenemos la siguiente información:

- **Id**: Número de identificación del id.
- **Date**:  Fecha de de publicación del tweet.
- **Text**: Contenido del tweet.
- **User_id**: Id del usuario que escribió el tweet.
- **User_name**: Nombre de usuario de la persona que tweeteo.
- **Location**: Desde donde fue enviado el tweet.
- **Retweeted** : Valor booleano para para identificar si fue retweeteado o no.
- **RT_text**: Contenido del retweet.
- **RT_user_id**: Id del usuario que retweeteó el tweet.
- **RT_user_name** : Nombre de usuario de la persona que retweeteó.

- **Ejemplo**:

````json
{"id": 1026814183042686976,"date": "Tue Aug 07 12:55:53 +0000 2018", "text": "RT @de_patty: Asuuuuuuu..  @Renzo_Reggiardo me da mala espina...su pasado fujimorísta qué miedo!!!y @luchocastanedap hijo de corrupto que s…", "user_id": 544008122,"user_name": "@CARLOSPUEMAPE1", "location": {}, "retweeted": true,"RT_text": "Asuuuuuuu..  @Renzo_Reggiardo me da mala espina...su pasado fujimorísta qué miedo!!!y @luchocastanedap hijo de corrupto que secunda lo del padre NI HABLAR! Más comunicore Plop!lideran las preferencias para la alcaldía de Lima, según Ipsos | RPP Noticias https://t.co/w5TnU0Dmwq", "RT_user_id": 302995560, "RT_user_name": "@de_patty"}
 
````


**_Resultados esperados:_** Se espera poder hacer inserción de registros, búsqueda por rango, búsqueda específica y eliminación de acuerdo al id.


## Comenzando 🚀

### Pre-requisitos 📋
* [Python](https://www.python.org/downloads/) 
#### Librerías
* [Json](https://docs.python.org/3/library/json.html)
* [nltk](https://www.nltk.org/)
* [collections](https://docs.python.org/3/library/collections.html)
* [emoji](https://pypi.org/project/emoji/)
* [math](https://docs.python.org/3/library/math.html)
* [re](https://docs.python.org/3/library/re.html)


### Despliegue 📦

**1.** Clonar el repositorio del proyecto.

**2.** Realizar el Build del proyecto en su IDE de preferencia.

**3.** Ejecutar el programa


## Descripción de las técnicas 

- **Preprocesamiento:** 
  - Tokenization 
  - Filtrar Stopwords 
  - Reducción de palabras (Stemming) 
- **Construcción del Índice**
  - Estructurar el índice invertido para guardar los pesos TF-IDF.  
  - Calcular  una  sola  vez  la  longitud  de  cada  documento  (norma)  y  guardarlo  para  ser 
  utilizado al momento de aplicar la similitud de coseno. 
  - Construcción del índice en memoria secundaria para grandes colecciones de datos.   
- **Consulta** 
  - La consulta es una frase en lenguaje natural.  
  - El scoring se obtiene aplicando la similitud de coseno sobre el índice invertido en 
  memoria secundaria. 
  - La función de recuperac
  ión debe retornar una lista ordenada de documentos que se 
  aproximen a la consulta. 

###  SEQUENTIAL FILE  💯

**_Sequential file_**: En este método organizamos los registros de acuerdo a un valor de sus campos, para este caso usaremos el campo **Id** como key.

- **Búsqueda:**

  1.  Abrir el archivo de datos.
  2.  Iniciar búsqueda binaria.
  3.  Ubicar el puntero a la mitad del archivo de datos.
  4.  Comparar el id del regsitro encontrado con el id del registro entrante.
  5.  Mover el puntero de acuerdo al tamaño del id hasta encontrar una coincidencia.
  6.  Se lee el registro y tenemos 3 posibilidades:  
      6.1 El registro encontrado esta en el archivo principal entonces devolvemos el registro.  
      6.2 El registro encontrado ha sido eliminado, en este caso recorremos el archivo hasta encontrar el primer registro no borrado.  
      6.3 El registro se encuentra en el archivo auxiliar.
      - Se abre el archivo auxiliar.
      - Se recorre el archivo hasta encontrar una coincidencia.
      - Si se encuentra se devuelve el registro.
      - Si no se encuentra se devuelve el registro más cercano anterior al id del regsitro buscado.
      - Se cierra el archivo auxiliar.
  7.  Se cierra el archivo principal de datos.


#### Búsqueda específica
````c++

 

````


- **Inserción:**

  1. Abrimos el archivo auxiliar.
  2. Comprobamos si hay espacio.  
     2.1 Si no hay espacio se leen todos los registros y se insertan al archivo principal.  
     2.2 Si hay espacio se busca el registro anterior en el archivo principal.  
     2.3 Se actualizan los punteros.  
     2.4 Se escribe el registro.
  3. Se cierra el archivo.

#### Inserción
````c++
 
````

- **Eliminación:**

  1. Se busca el registro que va antes del registro actual.
  2. Se actualizan los punteros del registro anterior.
  3. Se marca el registro como eliminado.
  4. Se hace update a los registros modificados.

#### Eliminación
````c++



````
- **Búsqueda por rango:**

  1. Se busca el archivo registro inicial.
  2. Se itera añadiendo los registros hasta llegar al registro final.
  3. Retorna un vector de registros.



#### Búsqueda por rango 
````c++


  
````


* **Ventajas:**
  - Al ser un arhivo ordenado la búsqueda de registros se realizará siempre en log(n).


---

###  Extendible Hashing 🔝

**_Extendible Hashing:_** El hash extensible es una estructura que se actualiza dinámicamente y que implementa un esquema de hash utilizando un directorio. El índice se utiliza para encontrar consultas donde exista un registro con una key determinada.

- **Búsqueda:**

  1. Calculamos el hash de la key que queremos buscar.
  2. Verificamos la cantidad de bits(**n**) que se usan en el directorio.
  3. Tomar los n bits de la dirección hash.
  4. Usando este índice encontrar el bucket al que pertenece el registro.
  5. Leer todos los registros en ese bucket.
  6. Recorrer los registro leídos.
  7. Retornar el registro encontrado.
  8. Cerrar el archivo.

#### Búsqueda específica
````c++
 vector<Car> search(int key) {
    Car record;
    int totalRecords, deleteNext;
    vector<Car> result;
    fstream file; 

    string bucketName= getBucket(key); 
    string bucket = bucketName +".dat";
    
    file.open(bucket, ios::binary | ios::out | ios::in );
    file.read((char *) &totalRecords, sizeof(int));
    file.read((char *) &deleteNext, sizeof(int));
    for (unsigned int i = 0; i < totalRecords; i++) {
      file.read((char *) &record, sizeof(record));
    // -1 means that the record  is not deleted
      if (record.id == key && record.deleteNext == -2)
        {result.push_back(record);}
    }
    if (result.empty()){
      cerr<<"Key not found in search "<<endl;
    }
    file.close();
    return result;
  }
````

- **Inserción:**

  1. Calculamos el hash de la key que queremos buscar.
  2. Verificamos la cantidad de bits(**n**) que se usan en el directorio.
  3. Tomar los n bits de la dirección hash.
  4. Usando este índice encontrar el bucket al que pertenece el registro.
  5. Comprobamos que la key no se encuentre en el Bucket.
  6. Tenemos dos casos:
     - El bucket aún no esta completo.
       - Insertamos el registro.
     - El bucket está completo.
       - Creamos el nuevo bucket.
       - Reinsertamos todos los registros.
       - Se crean los nuevos buckets con la nueva profundidad local.
       - Se actualiza el directorio.

#### Inserción 
````c++


````

- **Eliminación:**

  1. Calculamos el hash de la key que queremos buscar.
  2. Verificamos la cantidad de bits(**n**) que se usan en el directorio.
  3. Tomar los n bits de la dirección hash.
  4. Usando este índice encontrar el bucket al que pertenece el registro.
  5. Leer los datos del registro.
  6. Eliminar el registro.
  7. Si el bucket queda vacio, liberar la memoria.
  8. Actualizar el directorio.
  9. Leer el directorio.
     - Si existen dos buckets con pocos elementos y el mismo prefijo en la profundidad anterior se puden mezclar.
     - Crear un nuevo bucket.
     - Leer los registros de los dos buckets.
     - Liberar los dos buckets pasados.
     - Escribir los registros en el nuevo bucket.
     - Actualizamos el directorio.
     - Cerrar el directorio.

#### Eliminación 
````c++



````

* **Ventajas:**
  - Es eficaz mientras la memoria principal soporte el directorio.
  - La eficiencia se mantiene con el crecimiento del archivo de datos.
  - La cantidad de reescrituras no es tan grande.  

## Resultados Experimentales  
  
  ***Sequential File***  
  
  ![Tiempo vs Operación por registro](/Imagenes/SF_ExecutionTimes.png)  
  - Podemos observar como los tiempos de inserción aumentan cada cierta cantidad de operaciones, ya que al acabarse el espacio auxiliar los registros son escritos en memoria secundaria y ordenados de acuerdo a su key.
  - Los tiempos de búsqueda y eliminación solo aumentan cuando el registro se encuentra en el archivo auxiliar, caso contrario su tiempo de ejecución se mantiene constante.

  ***Extendible Hashing***
  
  ![Tiempo vs Operación por registro](/Imagenes/EH_ExecutionTimes.png)
  - Los tiempos de búsqueda son constantes en cualquier moment.
  - Los picos de tiempo en insertar se dan porque en algún momento se necesita hacer split de algun bucket.
  - Los tiempos altos en eliminar se dan porque se necesita hacer merge entre dos buckets con cantidad baja de registros. 


## Evidencias 🚀

* [Video](https://drive.google.com/drive/folders/1FY2bS6usvtPjwruH39Gzagi8iZs4J8BQ?usp=sharing) 

  
