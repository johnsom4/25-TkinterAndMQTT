"""
Using a Brickman (robot) as the receiver of messages.
"""

# Same as m2_fake_robot_as_mqtt_sender,
# but have the robot really do the action.
# Implement just FORWARD at speeds X and Y is enough.

import tkinter
from tkinter import ttk
import time
import mqtt_remote_method_calls as com
import m1_robot_motion_with_sensors as rb




def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid()
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid()

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid()
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid()

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid()
    forward_button['command'] = lambda: mqtt_client.send_message("rb.go",
                                                                 [left_speed_entry.get(), right_speed_entry.get()])
    root.bind('<Up>', lambda event: print("Forward key"))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid()
    left_button['command'] = lambda: print("Left button")
    root.bind('<Left>', lambda event: print("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid()
    stop_button['command'] = lambda: print("Stop button")
    root.bind('<space>', lambda event: print("Stop key"))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid()
    right_button['command'] = lambda: print("Right button")
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid()
    back_button['command'] = lambda: print("Back button")
    root.bind('<Down>', lambda event: print("Back key"))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid()
    up_button['command'] = lambda: print("Up button")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid()
    down_button['command'] = lambda: print("Down button")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid()
    q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid()
    e_button['command'] = lambda: exit()

    root.mainloop()


main()