# <img src="https://api.iconify.design/tabler/chart-bar.svg?color=white" width="30" align="center"> CPM Optimization Algorithm (Critical Path Method)

<div align="center">
  🌐 <strong>English</strong> | <a href="README.es.md">Español</a>
</div>

## <img src="https://api.iconify.design/tabler/device-desktop-code.svg?color=white" width="30" align="center"> About project

This project consists of the complete development of a custom mathematical engine implementing the CPM (Critical Path Method) algorithm entirely in pure Python, followed by its integration into an interactive and multilingual web application built with Streamlit. The primary goal of the platform is to bring complex project schedule optimization into a visual, fluid, and accessible environment, automating the delicate balance between execution time and associated project costs (Time-Cost Trade-off).

The application is designed to process structured data through Excel templates, handling essential project variables such as task dependencies, normal and crash durations, and both direct and indirect costs. Using this information, the algorithmic engine performs a comprehensive analysis that constructs the project network, calculates task slack values, and accurately determines the initial Critical Path.

Once the base scenario is established, the algorithm launches an advanced optimization process through the iterative crashing of critical activities. During each iteration, the system evaluates the cost slope of each reducible task to always select the most cost-efficient reduction strategy. This optimization process generates several key outputs:

- **Iterative Gantt Charts:** A visual sequence that allows users to inspect the evolution and restructuring of the project schedule phase by phase, from the normal plan to the fully crashed scenario.

- **Cost-Time Optimization Curve:** A strategic graphical representation that compares the increase in direct costs against the reduction in indirect costs, clearly revealing the optimal project duration and minimum total cost point.

- **Dependency Graph:** A visual representation of the project network that facilitates understanding of the workflow and logical task relationships.

Finally, the platform goes beyond analysis and visualization by providing automated technical documentation generation. Once the optimization process is completed, the system compiles all iterations, tables, and generated graphs into a fully structured LaTeX report. This ensures the delivery of a professional and academic-quality document ready to support strategic decision-making.

## <img src="https://api.iconify.design/tabler/sparkles-2.svg?color=white" width="30" align="center"> Main features

* **Custom Algorithmic Engine:** Fully developed in pure Python to calculate slack values, critical paths, and execute iterative task crashing (Time-Cost Trade-off).
* **Graph Analysis & Visualization:** GAutomatic generation of dependency graphs (graph theory based), iterative Gantt charts, and Cost-Time optimization curves.
* **Interactive Web Interface:** Streamlit-based application allowing users to upload Excel files and visualize calculations in real time.
* **Professional Export System:** Automatic generation of LaTeX source code containing all project tables, iterations, and optimization results.
* **Multi-language Support:** Dynamic UI with native support for both English and Spanish.

## <img src="https://api.iconify.design/tabler/rocket.svg?color=white" width="30" align="center"> Live Demo

The algorithm has been deployed as an interactive Streamlit application. You can access it here: [Algorithm CPM](https://cpm-algorithm.streamlit.app/)

## <img src="https://api.iconify.design/tabler/tool.svg?color=white" width="30" align="center"> Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-005B81?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)