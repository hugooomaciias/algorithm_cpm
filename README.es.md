# <img src="https://api.iconify.design/tabler/chart-bar.svg?color=white" width="30" align="center"> Algoritmo de Optimización CPM (Método del Camino Crítico)

<div align="center">
  🌐 <a href="README.md">English</a> | <strong>Español</strong>
</div>

## <img src="https://api.iconify.design/tabler/device-desktop-code.svg?color=white" width="30" align="center"> Sobre el proyecto

Este proyecto consiste en el desarrollo integral del motor matemático del algoritmo CPM (Critical Path Method) en Python puro, y su posterior integración en una aplicación web interactiva y multi-idioma construida con Streamlit. El objetivo principal de la herramienta es llevar la optimización de calendarios de proyectos complejos a un entorno visual, fluido y accesible, permitiendo automatizar el delicado equilibrio entre el tiempo de ejecución y los costes asociados (Time-Cost Trade-off).

La plataforma está diseñada para ingerir datos estructurados a través de plantillas de Excel, procesando variables de entrada fundamentales como las dependencias lógicas entre tareas, las duraciones (normales y de compresión extrema o crash) y los costes (directos e indirectos). A partir de esta información, el motor algorítmico ejecuta un análisis exhaustivo que dibuja la red del proyecto, calcula las holguras de cada nodo y determina con precisión matemática la Ruta Crítica inicial.

Una vez establecido el escenario base, el algoritmo inicia un proceso de optimización avanzada mediante la compresión iterativa de las tareas críticas, evaluando en cada paso la pendiente de coste (Slope) para seleccionar siempre la reducción más eficiente. Este procesamiento genera varios resultados clave:

- **Diagramas de Gantt iterativos:** Una secuencia visual que permite al usuario inspeccionar la evolución y reestructuración del cronograma fase por fase, desde el estado normal hasta la compresión máxima.

- **Curva de optimización Coste-Tiempo:** Una representación gráfica estratégica que cruza el aumento de los costes directos con el ahorro en costes indirectos, revelando de forma inequívoca el punto exacto (duración y coste óptimos) donde el proyecto es más rentable.

- **Grafo de dependencias:** Un mapa visual de la red de tareas que facilita la comprensión del flujo de trabajo.

Finalmente, la herramienta va más allá del cálculo y visualización, aportando un gran valor añadido en la automatización documental. Al concluir la optimización, el sistema compila todo el historial de iteraciones, tablas de datos y gráficos, exportando un informe estructurado y completo en código LaTeX. Esto garantiza la entrega de un documento de calidad académica y profesional, listo para respaldar la toma de decisiones estratégicas.

## <img src="https://api.iconify.design/tabler/sparkles-2.svg?color=white" width="30" align="center"> Características principales

* **Motor Algorítmico Propio:** Algoritmo desarrollado 100% en Python puro para calcular holguras, rutas críticas y ejecutar la compresión iterativa de tareas (*Time-Cost Trade-off*).
* **Análisis Gráfico y Visualización:** Generación de grafos de dependencias (mediante teoría de grafos), diagramas de Gantt iterativos y curvas de optimización Coste-Tiempo.
* **Interfaz Web Interactiva:** Aplicación construida con Streamlit que permite a los usuarios cargar archivos Excel y visualizar los cálculos en tiempo real.
* **Exportación Profesional:** Generación automática de código fuente en formato LaTeX con todas las tablas, iteraciones y resultados del proyecto.
* **Soporte Multi-idioma:** UI dinámica con soporte nativo para inglés y español.

## <img src="https://api.iconify.design/tabler/rocket.svg?color=white" width="30" align="center"> Cómo visualizar el proyecto

El algoritmo está desplegado con Streamlit en una aplicación. Puedes visualizarlo accediendo a [Algoritmo CPM](https://cpm-algorithm.streamlit.app/)

## <img src="https://api.iconify.design/tabler/tool.svg?color=white" width="30" align="center"> Tecnologías utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-005B81?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)