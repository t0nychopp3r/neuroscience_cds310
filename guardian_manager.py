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

    def stream_data(self, duration, callback=lambda data: data):
        start_time = datetime.datetime.now()
        recording_id = self.api.start_recording(callback, filtered_stream=True, raw_stream=False)
        self.ble.start_recording(self.api.callback)
        while datetime.datetime.now() - start_time < datetime.timedelta(seconds=duration):
            pass

    def stream_data_jaw(self, callback=lambda data: data):
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
        self.api.subscribe_rt(['JAW_CLENCH'], lambda data: print(data))
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