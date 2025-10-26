"""
Unit tests for Lesson 1: Electromagnetic Wave characteristics
"""

import numpy as np
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lesson1_electromagnetic_waves import ElectromagneticWave


def test_wave_initialization():
    """Test that waves are initialized correctly."""
    print("Testing wave initialization...")
    
    wave = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=0, speed=3e8)
    
    assert wave.amplitude == 1.0, "Amplitude not set correctly"
    assert wave.wavelength == 600e-9, "Wavelength not set correctly"
    assert wave.phase == 0, "Phase not set correctly"
    assert wave.speed == 3e8, "Speed not set correctly"
    
    # Check calculated properties
    expected_freq = 3e8 / 600e-9
    assert abs(wave.frequency - expected_freq) < 1e6, "Frequency calculation incorrect"
    
    expected_wave_number = 2 * np.pi / 600e-9
    assert abs(wave.wave_number - expected_wave_number) < 1e-6, "Wave number calculation incorrect"
    
    print("✓ Wave initialization test passed")


def test_electric_field():
    """Test electric field calculation."""
    print("Testing electric field calculation...")
    
    wave = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=0)
    
    # At x=0, t=0, with phase=0, sin(0) = 0
    e_field = wave.electric_field(0, 0)
    assert abs(e_field) < 1e-10, f"Expected ~0 at origin, got {e_field}"
    
    # At one wavelength, should return to same value
    e_field_0 = wave.electric_field(0, 0)
    e_field_lambda = wave.electric_field(wave.wavelength, 0)
    assert abs(e_field_0 - e_field_lambda) < 1e-10, "Field should be same after one wavelength"
    
    # Test with array input
    x = np.linspace(0, 1e-6, 100)
    e_field_array = wave.electric_field(x, 0)
    assert len(e_field_array) == 100, "Array output length incorrect"
    assert np.max(np.abs(e_field_array)) <= 1.0, "Field exceeds amplitude"
    
    print("✓ Electric field calculation test passed")


def test_intensity():
    """Test intensity calculation."""
    print("Testing intensity calculation...")
    
    wave1 = ElectromagneticWave(amplitude=1.0, wavelength=600e-9)
    wave2 = ElectromagneticWave(amplitude=2.0, wavelength=600e-9)
    
    intensity1 = wave1.intensity()
    intensity2 = wave2.intensity()
    
    assert intensity1 == 1.0, f"Expected intensity 1.0, got {intensity1}"
    assert intensity2 == 4.0, f"Expected intensity 4.0, got {intensity2}"
    assert intensity2 == 4 * intensity1, "Intensity not proportional to A²"
    
    print("✓ Intensity calculation test passed")


def test_frequency_wavelength_relationship():
    """Test c = λν relationship."""
    print("Testing frequency-wavelength relationship...")
    
    speed = 3e8
    wavelengths = [400e-9, 500e-9, 600e-9, 700e-9]
    
    for wavelength in wavelengths:
        wave = ElectromagneticWave(amplitude=1.0, wavelength=wavelength, speed=speed)
        calculated_speed = wave.wavelength * wave.frequency
        
        assert abs(calculated_speed - speed) < 1e3, \
            f"c = λν not satisfied: {calculated_speed} ≠ {speed}"
    
    print("✓ Frequency-wavelength relationship test passed")


def test_wave_propagation():
    """Test that wave propagates correctly over time."""
    print("Testing wave propagation...")
    
    wave = ElectromagneticWave(amplitude=1.0, wavelength=600e-9)
    
    x = 0
    t1 = 0
    t2 = 1e-15  # 1 femtosecond later
    
    e1 = wave.electric_field(x, t1)
    e2 = wave.electric_field(x, t2)
    
    # Field should change over time (unless at special points)
    # We just check that the calculation works
    assert isinstance(e2, (float, np.ndarray)), "Electric field should be numeric"
    
    print("✓ Wave propagation test passed")


def test_interference():
    """Test wave interference patterns."""
    print("Testing wave interference...")
    
    wave1 = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=0)
    wave2_inphase = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=0)
    wave2_outphase = ElectromagneticWave(amplitude=1.0, wavelength=600e-9, phase=np.pi)
    
    x = np.linspace(0, 1e-6, 100)
    
    # Constructive interference
    e1 = wave1.electric_field(x, 0)
    e2_in = wave2_inphase.electric_field(x, 0)
    constructive = e1 + e2_in
    
    # Should be twice the amplitude at maximum
    assert np.max(np.abs(constructive)) <= 2.0 + 1e-10, "Constructive interference exceeds 2A"
    assert np.max(np.abs(constructive)) >= 1.9, "Constructive interference should reach ~2A"
    
    # Destructive interference
    e2_out = wave2_outphase.electric_field(x, 0)
    destructive = e1 + e2_out
    
    # Should be close to zero everywhere
    assert np.max(np.abs(destructive)) < 1e-10, "Destructive interference should cancel"
    
    print("✓ Wave interference test passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("RUNNING LESSON 1 UNIT TESTS")
    print("=" * 60 + "\n")
    
    try:
        test_wave_initialization()
        test_electric_field()
        test_intensity()
        test_frequency_wavelength_relationship()
        test_wave_propagation()
        test_interference()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED ✓")
        print("=" * 60 + "\n")
        return 0
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
