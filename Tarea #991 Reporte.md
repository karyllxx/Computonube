

# Evaluación de Desempeño y Configuración de Infraestructura

## Introducción

Este documento presenta los resultados de pruebas realizadas sobre una arquitectura diseñada para garantizar estabilidad y rendimiento bajo diferentes condiciones de carga. Se analiza la configuración implementada y su efectividad en la gestión de tráfico y procesamiento de datos.

---

## Diseño de la Infraestructura

La configuración implementada incluye múltiples instancias con mecanismos de distribución de carga y redundancia, asegurando disponibilidad y escalabilidad. Los componentes clave son:

- **Servicios distribuidos en múltiples nodos**, optimizando la respuesta bajo demanda.
- **Balanceadores de carga** para distribuir tráfico de manera eficiente.
- **Pruebas de rendimiento** enfocadas en tiempos de respuesta y estabilidad.

---

## Evaluación y Resultados

Se llevaron a cabo distintas pruebas para medir el desempeño de la infraestructura. A continuación, se presentan los resultados más relevantes.

### Prueba 1: Análisis de tiempos de respuesta en nodo principal (Puerto 80)
- Tiempo total registrado: **18.538 segundos**
- Peticiones procesadas por segundo: **13.49 req/s**
- Latencia promedio: **74.15 ms**
- Latencia máxima: **3848 ms**

### Prueba 2: Evaluación de tráfico en nodo secundario (Puerto 8080)
- Tiempo total registrado: **7.794 segundos**
- Peticiones procesadas por segundo: **32.07 req/s**
- Latencia promedio: **249.424 ms**
- Latencia máxima: **769 ms**

![1](https://github.com/user-attachments/assets/3d891144-8c07-45d8-88be-59957dba96fa)



![2](https://github.com/user-attachments/assets/0c8193f4-c2ac-4e48-ad94-5be462db83ca)

### 📷 Prueba 3: Distribución de carga en múltiples nodos con Siege

**Nodo principal (Puerto 80):**  
- Transacciones exitosas: **970**
- Tiempo medio de respuesta: **0.54 segundos**
- Tasa de transacción: **32.67 trans/s**

**Nodo secundario (Puerto 8080):**  
- Transacciones exitosas: **1015**
- Tiempo medio de respuesta: **0.54 segundos**
- Tasa de transacción: **32.68 trans/s**

---

## Conclusiones

Los resultados obtenidos indican un rendimiento estable con tiempos de respuesta eficientes y adecuada distribución de carga entre los nodos. Se identifican oportunidades de ajuste en algunos parámetros para mejorar aún más la resiliencia del sistema ante cargas concurrentes.

Este informe sirve como base para futuras optimizaciones y garantiza que la infraestructura cumple con los requisitos de disponibilidad y rendimiento.

![3](https://github.com/user-attachments/assets/90d03277-28f6-4b8c-8c2b-8039d0cbec18)

🚀📊
