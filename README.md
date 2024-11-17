
# Guitar Tuner Application

This is a simple Python-based guitar tuner application. It captures audio input from your microphone, analyzes the sound using Fast Fourier Transform (FFT), and identifies the closest guitar note.

## Features

- Detects the frequency of the played note.
- Matches the detected frequency with standard guitar tuning (EADGBE).
- Provides feedback on how close the note is to the correct frequency.

## Prerequisites

- Python 3.x
- `numpy`
- `scipy`
- `sounddevice`

You can install the required dependencies with:

```bash
pip install numpy scipy sounddevice
```

## How to Use

1. Run the `guitar_tuner.py` script:
   ```bash
   python guitar_tuner.py
   ```

2. Follow the on-screen instructions to play a string on your guitar. The program will analyze the sound and display the detected note and frequency.

### Example Output

```
Welcome to the Guitar Tuner!
Recording...
Recording complete.
Detected Note: E2, Frequency: 82.50 Hz, Difference: 0.09 Hz
Tune another string? (y/n): y
```

## Guitar Notes

The application supports standard guitar tuning with the following notes:

| Note | Frequency (Hz) |
|------|----------------|
| E2   | 82.41          |
| A2   | 110.00         |
| D3   | 146.83         |
| G3   | 196.00         |
| B3   | 246.94         |
| E4   | 329.63         |

## Future Enhancements

- Add a graphical user interface (GUI).
- Improve frequency detection using advanced signal processing techniques.
- Support alternative tunings (e.g., Drop D, Open G).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Author

Developed by [Your Name].
