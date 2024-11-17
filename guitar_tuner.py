
import numpy as np
import sounddevice as sd
from scipy.signal import find_peaks

# Constants
SAMPLE_RATE = 44100  # Sampling rate in Hz (CD quality)
DURATION = 2  # Duration of audio capture in seconds

# Guitar string frequencies (Standard Tuning: EADGBE)
NOTE_FREQUENCIES = {
    "E2": 82.41,
    "A2": 110.00,
    "D3": 146.83,
    "G3": 196.00,
    "B3": 246.94,
    "E4": 329.63,
}

def record_audio(duration, sample_rate):
    """Records audio from the default microphone.

    :param duration: The length of the audio recording in seconds.
    :param sample_rate: The sample rate of the audio recording (Hz).
    :return: A numpy array of the recorded audio samples.
    """
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete.")
    return audio_data.flatten()

def perform_fft(audio_data, sample_rate):
    """Performs Fast Fourier Transform (FFT) on the audio data to find frequency components.

    :param audio_data: The recorded audio data as a numpy array.
    :param sample_rate: The sample rate of the audio recording (Hz).
    :return: Arrays of frequencies and their corresponding magnitudes.
    """
    n = len(audio_data)
    fft_result = np.fft.fft(audio_data)
    fft_magnitudes = np.abs(fft_result[:n // 2])
    frequencies = np.fft.fftfreq(n, 1 / sample_rate)[:n // 2]
    return frequencies, fft_magnitudes

def detect_peak_frequency(frequencies, magnitudes):
    """Detects the dominant frequency in the audio signal using peak detection.

    :param frequencies: Array of frequencies from the FFT.
    :param magnitudes: Array of magnitudes corresponding to the frequencies.
    :return: The frequency with the highest magnitude.
    """
    peak_indices, _ = find_peaks(magnitudes, height=0)
    if len(peak_indices) == 0:
        return None
    peak_freq = frequencies[peak_indices[np.argmax(magnitudes[peak_indices])]]
    return peak_freq

def match_note_frequency(frequency):
    """Matches the detected frequency to the nearest guitar note.

    :param frequency: The detected frequency in Hz.
    :return: The name of the closest guitar note and the difference in Hz.
    """
    if frequency is None:
        return "No sound detected", None

    closest_note = min(NOTE_FREQUENCIES, key=lambda note: abs(NOTE_FREQUENCIES[note] - frequency))
    freq_difference = frequency - NOTE_FREQUENCIES[closest_note]
    return closest_note, freq_difference

def main():
    """Main function to run the guitar tuner. Records audio, processes it, and matches the detected
    frequency to the closest guitar note.
    """
    print("Welcome to the Guitar Tuner!")
    while True:
        # Record audio
        audio_data = record_audio(DURATION, SAMPLE_RATE)

        # Perform FFT
        frequencies, magnitudes = perform_fft(audio_data, SAMPLE_RATE)

        # Detect peak frequency
        peak_frequency = detect_peak_frequency(frequencies, magnitudes)

        # Match frequency to the closest guitar note
        note, difference = match_note_frequency(peak_frequency)

        if difference is not None:
            print(f"Detected Note: {note}, Frequency: {peak_frequency:.2f} Hz, Difference: {difference:.2f} Hz")
        else:
            print("No valid peak detected. Please try again.")

        # Prompt user to continue or exit
        user_input = input("Tune another string? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
