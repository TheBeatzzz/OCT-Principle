# OCT-Principle

Educational repository for learning Optical Coherence Tomography (OCT) principles through demonstrations and simulations.

## About

This repository provides a structured series of lessons to understand the fundamental principles of Optical Coherence Tomography, starting from basic electromagnetic wave theory and progressing to advanced OCT concepts.

## Lessons

### [Lesson 1: Electromagnetic Light Wave Characteristics](LESSON1.md)

Demonstration and simulation to understand the characteristics of electromagnetic light waves.

**Topics covered:**
- Wave equation and propagation
- Wavelength and frequency relationships
- Amplitude and intensity
- Phase and interference
- The electromagnetic spectrum
- Relevance to OCT imaging

**Quick start:**
```bash
pip install -r requirements.txt
python lesson1_electromagnetic_waves.py
```
Interactive teaching materials for the Basic Principles of Optical Coherence Tomography (OCT).

## Overview

This repository contains educational materials, primarily Google Colab-compatible Jupyter notebooks, that teach the fundamental principles of Optical Coherence Tomography through an interactive approach that alternates between theoretical explanations and hands-on simulations.

## Contents

- **OCT_Principles_Interactive_Tutorial.ipynb** - Main interactive tutorial with alternating theory and simulations covering:
  - Low-coherence interferometry basics
  - Michelson interferometer operation
  - Coherence length and resolution
  - A-scan and B-scan image formation
  - Interactive exercises

## Getting Started

### Option 1: Google Colab (Recommended)

Click the badge below to open the notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TheBeatzzz/OCT-Principle/blob/main/OCT_Principles_Interactive_Tutorial.ipynb)

No installation required! Just click and start learning.

### Option 2: Local Jupyter Notebook

1. Clone this repository:
   ```bash
   git clone https://github.com/TheBeatzzz/OCT-Principle.git
   cd OCT-Principle
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter:
   ```bash
   jupyter notebook OCT_Principles_Interactive_Tutorial.ipynb
   ```

## Features

- **Alternating Theory & Simulation**: Each theoretical concept is immediately followed by an interactive simulation
- **Progressive Learning**: Concepts build upon each other from basic to advanced
- **Visual Demonstrations**: High-quality plots and visualizations
- **Interactive Exercises**: Hands-on parameter exploration
- **Clinical Context**: Real-world applications and examples

## Topics Covered

1. **Optical Coherence Tomography Fundamentals**
   - What is OCT?
   - Low-coherence interferometry
   - Clinical applications

2. **Coherence Length**
   - High vs. low coherence light
   - Effect on interference patterns
   - Simulation comparison

3. **Michelson Interferometer**
   - Basic setup and operation
   - Mathematical formulation
   - Multi-layer tissue simulation

4. **Axial Resolution**
   - Resolution formula and factors
   - Bandwidth effects
   - Interactive resolution comparison

5. **2D OCT Imaging**
   - A-scan to B-scan conversion
   - Image formation process
   - Synthetic B-scan generation

## Requirements

- Python 3.7+
- NumPy
- Matplotlib
- IPython

Install all dependencies:
```bash
pip install -r requirements.txt
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
- SciPy
- IPython/Jupyter

See `requirements.txt` for specific versions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

Educational materials designed to make OCT principles accessible to students, researchers, and practitioners in biomedical optics and medical imaging.
