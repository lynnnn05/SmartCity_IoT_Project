# 🏢 HKMU Smart Campus - Edge IoT Energy Hub

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OOP](https://img.shields.io/badge/paradigm-Object--Oriented-success.svg)
![Data Structure](https://img.shields.io/badge/Data_Structure-FIFO_Queue-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green)

> **Course Project:** COMP2090SEF / 8090SEF Data Structures, Algorithms and Problem Solving  
> **Task 1:** OOP-based Application Development  

An enterprise-grade, Object-Oriented IoT energy management dashboard designed to solve real-world energy waste problems within the Hong Kong Metropolitan University (HKMU) campus. It simulates a localized Edge AI node that manages various campus devices, calculates dynamic power consumption, and executes asynchronous tasks via a FIFO Command Queue.

---

## 📑 Table of Contents
- [1. Problem Definition & Motivation](#-1-problem-definition--motivation)
- [2. Key Features](#-2-key-features)
- [3. Object-Oriented Architecture (Rubric Mapping)](#-3-object-oriented-architecture-rubric-mapping)
- [4. Repository Structure](#-4-repository-structure)
- [5. Getting Started](#-5-getting-started)
- [6. Acknowledgments & Academic Declaration](#-6-acknowledgments--academic-declaration)

---

## 📌 1. Problem Definition & Motivation
**Real-World Context:** University campuses face significant challenges in managing energy efficiency. In places like HKMU's EECS laboratories (Block E) and lecture theaters (Block A), high-power devices such as Air Conditioners and specialized measurement tools (e.g., Oscilloscopes) are frequently left running idle. Under the CLP Power (中华电力) progressive tariff structure, this leads to heavy financial burdens and unnecessary carbon emissions.

**The Solution:** This project builds a **Smart Campus IoT Edge Controller**. Instead of replacing hardware, it provides a centralized software hub utilizing OOP principles to abstract, monitor, and intelligently schedule power states for different device types, paving the way for a Green Campus (ESG) initiative.

---

## ✨ 2. Key Features
* **🔌 Polymorphic Power Analytics:** Dynamically calculates real-time power draw (W) and estimated hourly costs (HKD). The AC unit computes power based on ambient vs. target temperature differences, while lab equipment computes power based on operational modes (Active/Standby).
* **⏳ Asynchronous Task Queue (FIFO):** Incorporates core Data Structure concepts. Hardware commands are not executed instantaneously; they are wrapped as lambda functions and queued, allowing for safe, sequential batch processing.
* **🍃 One-Click Eco-Mode:** A centralized aggregation command that scans the registry and forces all active devices into a powered-down state to prevent overnight energy waste.
* **🖥️ Modern Dark-Mode GUI:** A decoupled, responsive Tkinter dashboard demonstrating professional UI/UX separation from business logic.

*(Add a screenshot of your GUI here by replacing the link below)*
> `![Dashboard Screenshot](docs/screenshot.png)`

---

## 🏗️ 3. Object-Oriented Architecture (Rubric Mapping)
This project strictly adheres to all OOP concepts introduced in the COMP2090SEF curriculum, engineered with high cohesion and low coupling.

### I. Abstraction & Inheritance
* **`CampusDevice (ABC)`**: An Abstract Base Class defining the blueprint for all hardware nodes. It enforces the implementation of the `@abstractmethod get_power_consumption()`.
* **Derived Classes**: `SmartAC` and `LabOscilloscope` inherit from `CampusDevice`, gaining baseline properties while introducing specific localized behaviors.

### II. Polymorphism
* The `calculate_total_zone_power()` method in the Hub simply iterates through registered devices calling `get_power_consumption()`. 
* **The Magic:** The Hub does not need to check the device type. The AC calculates power using `$temp\_diff * 150W$`, while the Oscilloscope returns a fixed `350W` or `15W` depending on its state.

### III. Encapsulation
* Sensitive device properties (e.g., `_device_id`, `_is_on`, `_target_temp`) are protected. They can only be accessed or modified via secure getter/setter methods (e.g., `set_temperature()`), protecting the hardware state from illegal external modifications.

### IV. Advanced Class Features
* **Class Attributes:** `total_active_devices` and `CLP_BASE_TARIFF` are shared globally across all instances.
* **Class Methods:** `@classmethod get_system_device_count()` interacts with class-level states.
* **Static Methods:** `@staticmethod validate_hkmu_room()` provides utility validation without requiring class instantiation.
* **Magic Methods:** Overridden `__str__` for elegant terminal printing, `__eq__` for preventing duplicate ID registration, and `__add__` to allow direct addition of objects (`device1 + device2`) to sum their power draw.

### V. Integration with Data Structures
* **`CommandQueue` Class:** Implements a custom First-In-First-Out (FIFO) queue utilizing an encapsulated Python list, proving the ability to merge OOP with foundational Data Structures.

---

## 📂 4. Repository Structure
The system is built upon **Modular Programming**, separating data models, engine logic, and presentation layers into distinct Python modules.

```text
📦 HKMU-Smart-Campus-Hub
 ┣ 📜 devices.py          # Core OOP hierarchy (Abstraction, Inheritance)
 ┣ 📜 hub_controller.py   # Aggregation Hub & FIFO Command Queue engine
 ┣ 📜 gui_app.py          # Decoupled Tkinter Graphical User Interface
 ┗ 📜 main.py             # Minimal system entry point