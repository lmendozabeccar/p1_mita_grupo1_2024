# Sistema de Evaluación Académica

Este proyecto es un sistema de evaluación académica óptimo y eficiente, diseñado para gestionar las notas de los alumnos de manera organizada. Ofrece funcionalidades clave tanto para alumnos como para profesores, adaptándose a las necesidades de ambos usuarios.

## 🚀 Características Principales

- **Autenticación**: Inicio de sesión y creación de cuentas para alumnos y profesores.
- **Gestión de Inscripciones**: Los alumnos pueden inscribirse a materias con un límite de 10 materias activas.
- **Gestión de Notas**: Los profesores pueden asignar o modificar notas asociadas a materias.
- **Cuentas de Usuario**: Creación, edición y eliminación de cuentas para alumnos y profesores.
- **Promedios Automatizados**: Cálculo eficiente de promedios utilizando recursividad.
- **Validación de Entradas**: Uso de expresiones regulares para garantizar datos correctos y seguros.

---

## 🧑‍🎓 Usuarios del Sistema

### **Alumno**
- Inscribirse a materias (máximo de 10 materias).
- Visualizar sus notas una vez cargadas.
- Recursar o abandonar materias con notas menores a 4.
- Eliminar o modificar su cuenta.

### **Profesor**
- Cargar y modificar notas para los alumnos inscritos.
- Ver todas las notas de los alumnos de una materia.
- Eliminar inscripciones de alumnos en una materia.
- Eliminar o modificar su cuenta.

---

## 🌀 CRUD (Create, Read, Update, Delete) Implementado

### **Create**
- Los alumnos pueden inscribirse en materias, añadiéndose al archivo JSON.

### **Read**
- Alumnos y profesores pueden consultar las notas cargadas.

### **Update**
- Los profesores pueden editar las notas de los alumnos.

### **Delete**
- Los alumnos pueden eliminar su cuenta.
- Los profesores pueden eliminar cuentas de alumnos o inscripciones en materias.

---

## 📂 Estructura de Archivos

- **Usuarios (archivo de texto)**: Contiene información básica de estudiantes y profesores separadas por punto y coma (Legajo, email, contraseña y nombre).
- **Datos de Materias (JSON)**: Registra las materias inscriptas y notas asociadas.

---
