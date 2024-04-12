from guardian_manager import GuardianManager
from keyboardmapping import keyboard_mapping_right
from jaw_clench_detector import detector



def callback(data):
    jaw_clench_detection = detector(data)
    if 'JawClench' in jaw_clench_detection: 
        print("*********Jaw Clench detected**********")
        keyboard_mapping_right()
    else:
        print("No Jaw Clench detected")

    #print(jaw_clench_detection)


    

gm = GuardianManager(
    device_id="EB-2D-14-92-D6-71",
    api_key="idun_2YV1BILW_T95lLajPwP2WHLqAxuYyuYheMKj-frjs7jBQz1wsbuaxSOh"
)

#gm.recordings()
gm.stream_data(callback)
#gm.disconnect_session()
#gm.stream_data_jaw(callback)