from guardian_manager import GuardianManager

def callback(data):
    print(data)
    #print(data['ch1'])
    pass

gm = GuardianManager(
    device_id="D6-96-7C-C5-2E-14",
    api_key="idun_2zZuE2ImqssU8T0HnVOlkJNutPXc6q_9nAt0DpTNtrAYgcocAHhEbxoI"
)

gm.recordings()
#gm.stream_data(5, callback)
#gm.disconnect_session()
#gm.stream_data_jaw(callback)