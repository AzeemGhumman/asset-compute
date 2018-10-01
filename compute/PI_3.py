

'''

Assumption:
    Same code can run on different types of Raspberry PIs
    The rationale for creating different 'types' of compute is to capture the pinout
    Since we heavily depend on external code for low-level drivers that is specifically
    written for BBB or Raspberry PI, I dont see the need to maintain separate code
    for each type of board.

    PinOut is captured here.
    This helps in creating a readable manifest
    Also, we can add tags with each pin, e.g., GND, VCC-3, VCC-5, GPIO, other, etc.
    This mapping allows the sensors to check if the connections are made correctly
    when configuring the hardware on startup.
    e.g, a sensors can check if the GND, power and signal pin is connected to valid
    pins on the actual board.


    class PI_3:
        pin number: 23
        name: GPIO_32 (shows up in manifest)
        tags: [GPIO, reserved]

        a map!

'''
