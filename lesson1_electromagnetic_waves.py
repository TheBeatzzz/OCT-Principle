"""
Lesson 1: Demonstration and Simulation of Electromagnetic Light Wave Characteristics

This lesson demonstrates the fundamental characteristics of electromagnetic waves,
specifically focusing on light waves which are essential for understanding OCT principles.

Key Concepts:
1. Wave equation and propagation
2. Amplitude - intensity of the wave
3. Wavelength (λ) - distance between wave peaks
4. Frequency (ν) - oscillations per unit time
5. Phase - position in the wave cycle
6. Speed of light (c) relationship: c = λν
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


class ElectromagneticWave:
    """
    A class to represent and simulate electromagnetic waves.
    
    Attributes:
        amplitude (float): Wave amplitude (related to intensity)
        wavelength (float): Wavelength in meters
        frequency (float): Frequency in Hz
        phase (float): Initial phase offset in radians
        speed (float): Wave propagation speed (default: speed of light)
    """
    
    def __init__(self, amplitude=1.0, wavelength=600e-9, phase=0, speed=3e8):
        """
        Initialize an electromagnetic wave.
        
        Args:
            amplitude: Wave amplitude (default 1.0)
            wavelength: Wavelength in meters (default 600nm - orange light)
            phase: Initial phase in radians (default 0)
            speed: Wave speed in m/s (default speed of light)
        """
        self.amplitude = amplitude
        self.wavelength = wavelength
        self.phase = phase
        self.speed = speed
        self.frequency = self.speed / self.wavelength
        self.angular_frequency = 2 * np.pi * self.frequency
        self.wave_number = 2 * np.pi / self.wavelength
    
    def electric_field(self, x, t=0):
        """
        Calculate the electric field at position x and time t.
        
        E(x,t) = A * sin(kx - ωt + φ)
        where:
            A = amplitude
            k = wave number (2π/λ)
            ω = angular frequency (2πν)
            φ = phase
        
        Args:
            x: Position(s) in meters (can be array)
            t: Time in seconds (default 0)
        
        Returns:
            Electric field value(s)
        """
        return self.amplitude * np.sin(
            self.wave_number * x - self.angular_frequency * t + self.phase
        )
    
    def intensity(self):
        """
        Calculate the intensity of the wave.
        Intensity is proportional to the square of the amplitude.
        
        Returns:
            Relative intensity
        """
        return self.amplitude ** 2
    
    def __repr__(self):
        return (f"ElectromagneticWave(amplitude={self.amplitude}, "
                f"wavelength={self.wavelength*1e9:.1f}nm, "
                f"frequency={self.frequency:.2e}Hz)")


def demonstrate_wavelength():
    """
    Demonstrate how wavelength affects the wave pattern.
    Shows three waves with different wavelengths (different colors of light).
    """
    print("=" * 60)
    print("DEMONSTRATION 1: Effect of Wavelength")
    print("=" * 60)
    
    # Create waves representing different colors
    red_wave = ElectromagneticWave(amplitude=1.0, wavelength=700e-9)  # Red light
    green_wave = ElectromagneticWave(amplitude=1.0, wavelength=550e-9)  # Green light
    blue_wave = ElectromagneticWave(amplitude=1.0, wavelength=450e-9)  # Blue light
    
    # Position array
    x = np.linspace(0, 3e-6, 1000)  # 3 micrometers
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(x * 1e9, red_wave.electric_field(x), 'r-', label=f'Red ({red_wave.wavelength*1e9:.0f} nm)', linewidth=2)
    ax.plot(x * 1e9, green_wave.electric_field(x), 'g-', label=f'Green ({green_wave.wavelength*1e9:.0f} nm)', linewidth=2)
    ax.plot(x * 1e9, blue_wave.electric_field(x), 'b-', label=f'Blue ({blue_wave.wavelength*1e9:.0f} nm)', linewidth=2)
    
    ax.set_xlabel('Position (nm)', fontsize=12)
    ax.set_ylabel('Electric Field Amplitude', fontsize=12)
    ax.set_title('Electromagnetic Waves with Different Wavelengths', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('wavelength_demonstration.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'wavelength_demonstration.png'")
    print(f"\nRed light:   λ = {red_wave.wavelength*1e9:.1f} nm, ν = {red_wave.frequency:.2e} Hz")
    print(f"Green light: λ = {green_wave.wavelength*1e9:.1f} nm, ν = {green_wave.frequency:.2e} Hz")
    print(f"Blue light:  λ = {blue_wave.wavelength*1e9:.1f} nm, ν = {blue_wave.frequency:.2e} Hz")
    print("\nNote: Shorter wavelength → Higher frequency (c = λν)")
    plt.close()


def demonstrate_amplitude():
    """
    Demonstrate how amplitude affects wave intensity.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION 2: Effect of Amplitude (Intensity)")
    print("=" * 60)
    
    # Create waves with different amplitudes
    weak_wave = ElectromagneticWave(amplitude=0.3, wavelength=600e-9)
    medium_wave = ElectromagneticWave(amplitude=0.7, wavelength=600e-9)
    strong_wave = ElectromagneticWave(amplitude=1.0, wavelength=600e-9)
    
    x = np.linspace(0, 3e-6, 1000)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Plot electric fields
    ax1.plot(x * 1e9, weak_wave.electric_field(x), 'b-', 
             label=f'Low intensity (A={weak_wave.amplitude})', linewidth=2, alpha=0.6)
    ax1.plot(x * 1e9, medium_wave.electric_field(x), 'g-', 
             label=f'Medium intensity (A={medium_wave.amplitude})', linewidth=2, alpha=0.7)
    ax1.plot(x * 1e9, strong_wave.electric_field(x), 'r-', 
             label=f'High intensity (A={strong_wave.amplitude})', linewidth=2)
    
    ax1.set_xlabel('Position (nm)', fontsize=12)
    ax1.set_ylabel('Electric Field Amplitude', fontsize=12)
    ax1.set_title('Electromagnetic Waves with Different Amplitudes', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Plot intensities
    waves = [weak_wave, medium_wave, strong_wave]
    labels = ['Low', 'Medium', 'High']
    intensities = [w.intensity() for w in waves]
    colors = ['blue', 'green', 'red']
    
    ax2.bar(labels, intensities, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Relative Intensity (I ∝ A²)', fontsize=12)
    ax2.set_title('Wave Intensity vs Amplitude', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    for i, (label, intensity) in enumerate(zip(labels, intensities)):
        ax2.text(i, intensity + 0.02, f'{intensity:.2f}', 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('amplitude_demonstration.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'amplitude_demonstration.png'")
    print(f"\nIntensity is proportional to amplitude squared (I ∝ A²)")
    for wave, label in zip(waves, labels):
        print(f"{label:6s}: A = {wave.amplitude:.1f}, I = {wave.intensity():.2f}")
    plt.close()


def demonstrate_phase():
    """
    Demonstrate the effect of phase on wave interference.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION 3: Phase and Wave Interference")
    print("=" * 60)
    
    # Create waves with different phases
    wave1 = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=0)
    wave2_inphase = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=0)
    wave2_outphase = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=np.pi)
    wave2_quarter = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=np.pi/2)
    
    x = np.linspace(0, 3e-6, 1000)
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # Constructive interference (in phase)
    e1 = wave1.electric_field(x)
    e2_in = wave2_inphase.electric_field(x)
    axes[0].plot(x * 1e9, e1, 'b--', label='Wave 1 (φ=0)', linewidth=1.5, alpha=0.6)
    axes[0].plot(x * 1e9, e2_in, 'r--', label='Wave 2 (φ=0)', linewidth=1.5, alpha=0.6)
    axes[0].plot(x * 1e9, e1 + e2_in, 'purple', label='Sum (Constructive)', linewidth=2.5)
    axes[0].set_ylabel('Amplitude', fontsize=11)
    axes[0].set_title('Constructive Interference (Phase difference = 0)', 
                      fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)
    
    # Destructive interference (out of phase)
    e2_out = wave2_outphase.electric_field(x)
    axes[1].plot(x * 1e9, e1, 'b--', label='Wave 1 (φ=0)', linewidth=1.5, alpha=0.6)
    axes[1].plot(x * 1e9, e2_out, 'r--', label='Wave 2 (φ=π)', linewidth=1.5, alpha=0.6)
    axes[1].plot(x * 1e9, e1 + e2_out, 'green', label='Sum (Destructive)', linewidth=2.5)
    axes[1].set_ylabel('Amplitude', fontsize=11)
    axes[1].set_title('Destructive Interference (Phase difference = π)', 
                      fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)
    
    # Partial interference (quarter phase)
    e2_quarter = wave2_quarter.electric_field(x)
    axes[2].plot(x * 1e9, e1, 'b--', label='Wave 1 (φ=0)', linewidth=1.5, alpha=0.6)
    axes[2].plot(x * 1e9, e2_quarter, 'r--', label='Wave 2 (φ=π/2)', linewidth=1.5, alpha=0.6)
    axes[2].plot(x * 1e9, e1 + e2_quarter, 'orange', label='Sum (Partial)', linewidth=2.5)
    axes[2].set_xlabel('Position (nm)', fontsize=11)
    axes[2].set_ylabel('Amplitude', fontsize=11)
    axes[2].set_title('Partial Interference (Phase difference = π/2)', 
                      fontsize=12, fontweight='bold')
    axes[2].legend(fontsize=9)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('phase_demonstration.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'phase_demonstration.png'")
    print("\nPhase relationships:")
    print("  • In phase (Δφ = 0):   Constructive interference → Maximum amplitude")
    print("  • Out of phase (Δφ = π): Destructive interference → Cancellation")
    print("  • Quarter phase (Δφ = π/2): Partial interference")
    plt.close()


def demonstrate_wave_propagation():
    """
    Demonstrate wave propagation over time (creates animation frames).
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION 4: Wave Propagation")
    print("=" * 60)
    
    wave = ElectromagneticWave(amplitude=1.0, wavelength=600e-9)
    
    x = np.linspace(0, 3e-6, 1000)
    time_steps = [0, 0.5e-15, 1.0e-15, 1.5e-15]  # femtoseconds
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    for i, t in enumerate(time_steps):
        e_field = wave.electric_field(x, t)
        axes[i].plot(x * 1e9, e_field, 'b-', linewidth=2)
        axes[i].set_xlabel('Position (nm)', fontsize=10)
        axes[i].set_ylabel('Electric Field', fontsize=10)
        axes[i].set_title(f'Time = {t*1e15:.1f} femtoseconds', fontsize=11, fontweight='bold')
        axes[i].set_ylim([-1.5, 1.5])
        axes[i].grid(True, alpha=0.3)
        axes[i].axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    
    plt.suptitle('Electromagnetic Wave Propagation Over Time', 
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('propagation_demonstration.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'propagation_demonstration.png'")
    print(f"\nWave properties:")
    print(f"  • Speed of light: c = {wave.speed:.2e} m/s")
    print(f"  • Wavelength: λ = {wave.wavelength*1e9:.1f} nm")
    print(f"  • Frequency: ν = {wave.frequency:.2e} Hz")
    print(f"  • Period: T = 1/ν = {1/wave.frequency:.2e} s")
    plt.close()


def demonstrate_spectrum():
    """
    Demonstrate the electromagnetic spectrum with focus on visible light.
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION 5: Electromagnetic Spectrum")
    print("=" * 60)
    
    # Define spectrum regions
    spectrum_data = {
        'Violet': (380, 450, 'violet'),
        'Blue': (450, 495, 'blue'),
        'Green': (495, 570, 'green'),
        'Yellow': (570, 590, 'yellow'),
        'Orange': (590, 620, 'orange'),
        'Red': (620, 750, 'red')
    }
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))
    
    # Plot visible spectrum
    for name, (start, end, color) in spectrum_data.items():
        ax1.axvspan(start, end, alpha=0.7, color=color, label=f'{name} ({start}-{end} nm)')
    
    ax1.set_xlabel('Wavelength (nm)', fontsize=12)
    ax1.set_ylabel('Visible Light', fontsize=12)
    ax1.set_title('Visible Light Spectrum', fontsize=14, fontweight='bold')
    ax1.set_xlim(350, 780)
    ax1.set_ylim(0, 1)
    ax1.set_yticks([])
    ax1.legend(loc='upper right', fontsize=9, ncol=3)
    ax1.grid(True, alpha=0.3, axis='x')
    
    # Plot frequency vs wavelength for visible light
    wavelengths = np.linspace(380e-9, 750e-9, 100)
    frequencies = 3e8 / wavelengths
    
    ax2.plot(wavelengths * 1e9, frequencies / 1e14, 'k-', linewidth=2)
    ax2.fill_between(wavelengths * 1e9, frequencies / 1e14, alpha=0.3)
    ax2.set_xlabel('Wavelength (nm)', fontsize=12)
    ax2.set_ylabel('Frequency (×10¹⁴ Hz)', fontsize=12)
    ax2.set_title('Wavelength-Frequency Relationship (c = λν)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.invert_xaxis()  # Invert to show increasing frequency
    
    plt.tight_layout()
    plt.savefig('spectrum_demonstration.png', dpi=150, bbox_inches='tight')
    print("✓ Plot saved as 'spectrum_demonstration.png'")
    print("\nVisible light spectrum:")
    for name, (start, end, _) in spectrum_data.items():
        mid_wl = (start + end) / 2 * 1e-9
        freq = 3e8 / mid_wl
        print(f"  {name:8s}: {start:3d}-{end:3d} nm  (ν ≈ {freq:.2e} Hz)")
    plt.close()


def run_all_demonstrations():
    """
    Run all demonstrations in sequence.
    """
    print("\n" + "=" * 60)
    print("LESSON 1: ELECTROMAGNETIC LIGHT WAVE CHARACTERISTICS")
    print("Demonstration and Simulation")
    print("=" * 60)
    print("\nThis lesson will create 5 demonstrations showing:")
    print("1. Effect of wavelength on wave patterns")
    print("2. Effect of amplitude on intensity")
    print("3. Phase relationships and interference")
    print("4. Wave propagation over time")
    print("5. Electromagnetic spectrum\n")
    
    try:
        demonstrate_wavelength()
        demonstrate_amplitude()
        demonstrate_phase()
        demonstrate_wave_propagation()
        demonstrate_spectrum()
        
        print("\n" + "=" * 60)
        print("ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("\nGenerated files:")
        print("  • wavelength_demonstration.png")
        print("  • amplitude_demonstration.png")
        print("  • phase_demonstration.png")
        print("  • propagation_demonstration.png")
        print("  • spectrum_demonstration.png")
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Run all demonstrations
    run_all_demonstrations()
    
    # Example: Create custom wave
    print("\n" + "=" * 60)
    print("EXAMPLE: Creating Custom Electromagnetic Waves")
    print("=" * 60)
    
    # Near-infrared light (OCT typically uses ~1310 nm or ~800 nm)
    oct_wave = ElectromagneticWave(amplitude=1.0, wavelength=1310e-9)
    print(f"\nOCT Light Source: {oct_wave}")
    print(f"Frequency: {oct_wave.frequency:.2e} Hz")
    print(f"Photon Energy: {6.626e-34 * oct_wave.frequency / 1.602e-19:.3f} eV")
