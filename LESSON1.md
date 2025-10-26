# Lesson 1: Electromagnetic Light Wave Characteristics

## Overview

This lesson provides a comprehensive demonstration and simulation to understand the characteristics of electromagnetic light waves, which form the foundation for understanding Optical Coherence Tomography (OCT) principles.

## Learning Objectives

By the end of this lesson, you will understand:

1. **Wave Equation**: The mathematical representation of electromagnetic waves
2. **Wavelength (λ)**: The spatial period of the wave and its relationship to color
3. **Frequency (ν)**: The temporal frequency and its relationship to wavelength
4. **Amplitude**: Wave amplitude and its relationship to intensity
5. **Phase**: Wave phase and its role in interference phenomena
6. **Speed of Light**: The fundamental relationship c = λν

## Key Concepts

### 1. The Wave Equation

Electromagnetic waves can be described by the equation:

```
E(x,t) = A sin(kx - ωt + φ)
```

Where:
- **E** = Electric field
- **A** = Amplitude (related to intensity)
- **k** = Wave number (2π/λ)
- **x** = Position
- **ω** = Angular frequency (2πν)
- **t** = Time
- **φ** = Phase

### 2. Wavelength and Color

The wavelength determines the color of visible light:
- **Violet**: 380-450 nm
- **Blue**: 450-495 nm
- **Green**: 495-570 nm
- **Yellow**: 570-590 nm
- **Orange**: 590-620 nm
- **Red**: 620-750 nm

For OCT, near-infrared wavelengths (800-1310 nm) are commonly used.

### 3. Amplitude and Intensity

The intensity of light is proportional to the square of the amplitude:

```
I ∝ A²
```

This is crucial for understanding signal strength in OCT imaging.

### 4. Phase and Interference

When two waves meet, they interfere based on their relative phase:
- **Constructive interference** (Δφ = 0): Waves add together
- **Destructive interference** (Δφ = π): Waves cancel out
- This principle is fundamental to OCT imaging

### 5. The Speed of Light

All electromagnetic waves travel at the speed of light in vacuum:

```
c = λν ≈ 3 × 10⁸ m/s
```

This relationship means:
- Shorter wavelength → Higher frequency
- Longer wavelength → Lower frequency

## Running the Demonstration

### Prerequisites

Install the required packages:

```bash
pip install -r requirements.txt
```

### Execute the Simulation

```bash
python lesson1_electromagnetic_waves.py
```

This will generate five demonstration plots:

1. **wavelength_demonstration.png**: Shows how wavelength affects wave patterns for different colors
2. **amplitude_demonstration.png**: Demonstrates the relationship between amplitude and intensity
3. **phase_demonstration.png**: Illustrates wave interference patterns
4. **propagation_demonstration.png**: Shows wave propagation over time
5. **spectrum_demonstration.png**: Displays the visible light spectrum

## Using the ElectromagneticWave Class

You can also use the provided `ElectromagneticWave` class for custom simulations:

```python
from lesson1_electromagnetic_waves import ElectromagneticWave
import numpy as np

# Create a wave representing red light
red_light = ElectromagneticWave(amplitude=1.0, wavelength=650e-9)

# Calculate electric field at different positions
x = np.linspace(0, 2e-6, 1000)  # 2 micrometers
e_field = red_light.electric_field(x, t=0)

# Get wave properties
print(f"Frequency: {red_light.frequency:.2e} Hz")
print(f"Intensity: {red_light.intensity()}")
```

## Interactive Exploration

Try modifying the code to explore:

1. **Different wavelengths**: What happens with ultraviolet or infrared light?
2. **Multiple waves**: How do three or more waves interfere?
3. **Time evolution**: Create animations showing wave propagation
4. **Different media**: How would waves behave in materials with different refractive indices?

## Relevance to OCT

Understanding these electromagnetic wave properties is essential for OCT because:

1. **Interference**: OCT uses interference between reference and sample beams
2. **Coherence**: The coherence length depends on the wavelength spectrum
3. **Resolution**: Axial resolution is related to the wavelength and bandwidth
4. **Penetration**: Different wavelengths penetrate tissues differently

## Questions for Reflection

1. Why does blue light have a higher frequency than red light?
2. What happens to the intensity when amplitude doubles?
3. How does phase difference affect the interference pattern?
4. Why is the speed of light constant for all wavelengths in vacuum?
5. Why might longer wavelengths be preferred for deeper tissue imaging in OCT?

## Next Steps

In the next lesson, we will explore:
- Coherence and coherence length
- Light sources for OCT
- The principle of interferometry
- Low-coherence interferometry basics

## Additional Resources

- Born, M., & Wolf, E. (1999). *Principles of Optics*
- Hecht, E. (2017). *Optics* (5th ed.)
- Fercher, A. F., et al. (2003). "Optical coherence tomography - principles and applications"

---

*This lesson is part of the OCT-Principle educational series*
