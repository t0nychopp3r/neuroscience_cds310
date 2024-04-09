from idun_guardian_sdk import GuardianBLE, GuardianAPI
from datetime import datetime, timezone, timedelta
import time
import datetime

class GuardianManager:
    def __init__(self, device_id, api_key):
        self.ble = GuardianBLE()
        self.api = GuardianAPI(device_id, api_key)
        self.files = []

    def check_battery(self):
        print(f"Battery: {self.ble.get_battery()}%")

    def check_impedance(self):
        self.ble.start_impedance(lambda data: print(f"{data}\thOhm"))
        time.sleep(10)
        self.ble.stop_impedance()

    def stream_data(self, callback):
        data = self.api.get_recordings()    
        ongoing_recording_id = None
        # Überprüfen, ob 'status' == 'ONGOING' für jedes Element in den Daten
        for entry in data:
            if entry.get('status', {}).get('status') == 'ONGOING':
                ongoing_recording_id = entry['recordingID']
                self.api.stop_recording(ongoing_recording_id)
        recording_id = self.api.start_recording(callback, filtered_stream=True, raw_stream=True)
        self.ble.start_recording(self.api.callback)
        while True:
            pass

    def stream_data_jaw(self, callback):
        data = self.api.get_recordings()    
        ongoing_recording_id = None
        # Überprüfen, ob 'status' == 'ONGOING' für jedes Element in den Daten
        for entry in data:
            if entry.get('status', {}).get('status') == 'ONGOING':
                ongoing_recording_id = entry['recordingID']
                self.api.stop_recording(ongoing_recording_id)
        #self.ble.stop_recording()
        recording_id = self.api.start_recording(None, filtered_stream=True, raw_stream=False)
        self.ble.start_recording(self.api.callback)
        self.api.subscribe_rt(['JAW_CLENCH'], callback)
        while True:
            pass

    def disconnect_session(self):
        self.api.stop_recording()
        self.ble.stop_recording()
        self.ble._disconnect()
        print("Disconnected")

    def recordings(self):
        recorings = self.api.get_recordings()
        return print(recorings)
    

# Return Raw Data

# {'deviceID': 'D6-96-7C-C5-2E-14', 'bp_filter_eeg': None, 'raw_eeg': {'ch1': [-187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447, -187500.02235174447], 'timestamp': [1712674109.344, 1712674109.348, 1712674109.352, 1712674109.3560002, 1712674109.3600001, 1712674109.364, 1712674109.368, 1712674109.3720002, 1712674109.3760002, 1712674109.38, 1712674109.384, 1712674109.388, 1712674109.3920002, 1712674109.3960001, 1712674109.4, 1712674109.404, 1712674109.408, 1712674109.4120002, 1712674109.4160001, 1712674109.42]}}