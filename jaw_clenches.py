from guardian_manager import GuardianManager
from keyboardmapping import keyboard_mapping_right


def callback(data):
    print(data)

    '''
    if 'JawClench' in data[1]: 
        print("*********Jaw Clench detected**********")
        keyboard_mapping_right()
    else:
        print("No Jaw Clench detected")

    '''
    

gm = GuardianManager(
    device_id="D6-96-7C-C5-2E-14",
    api_key="idun_2zZuE2ImqssU8T0HnVOlkJNutPXc6q_9nAt0DpTNtrAYgcocAHhEbxoI"
)

#gm.recordings()
gm.stream_data(callback)
#gm.disconnect_session()
#gm.stream_data_jaw(callback)