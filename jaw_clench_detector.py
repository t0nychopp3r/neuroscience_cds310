from scipy import signal

## DETECRTORS


def detector_flavio(data):
        # notch filter to remove powerline noise
        notch_freq = 50  # set to 50 in Europe, 60 in North America
        numerator, denominator = signal.iirnotch(notch_freq, 20, 250)
        filtered_notch_data = signal.filtfilt(b=numerator, a=denominator, x=data, padtype=None)

        # bandpass filter to remove common artefacts during resting state recordings
        high_pass_freq = 1
        low_pass_freq = 35
        denom, nom = signal.iirfilter(int(3), [high_pass_freq, low_pass_freq], btype="bandpass", ftype="butter", fs=float(250), output="ba")
        filtered_bp_data = signal.filtfilt(b=denom, a=nom, x=filtered_notch_data, padtype=None)

        # filters only the jaw clenches frequencies beteween 40 and 80 Hz
        low_pass_freq = 40
        high_pass_freq = 80
        denom, nom = signal.iirfilter(int(3), [low_pass_freq, high_pass_freq], btype="bandpass", ftype="butter", fs=float(250), output="ba")
        jaw_clench_filtered = (signal.filtfilt(b=denom, a=nom, x=filtered_bp_data, padtype=None))**2 # square the signal

        # Jaw Clench Detection
        jaw_clench_detection = []
        for i in jaw_clench_filtered:
            if i > 100:
                jaw_clench_detection.append('JawClench')
            else:
                jaw_clench_detection.append('Nothing')

        return jaw_clench_detection


# Function to detect jaw clenches
# will be called in jaw_clenches.py Callback function

def detector(data):
    # get the raw eeg data
    ch1_array = data['raw_eeg']['ch1']

    #filter and Detecort
    jaw_clench_detection = detector_flavio(ch1_array)

    return jaw_clench_detection




    