import ezcadapi  # Assuming ezcadapi is the library provided for interfacing with EzCad

def initialize_ezcad():
    """Initializes the EzCad software."""
    ezcadapi.Initialize()
    if not ezcadapi.IsInitialized():
        print("EzCad initialization failed.")
        return False
    print("EzCad successfully initialized.")
    return True

def load_marking_file(filepath):
    """Loads a marking file into EzCad."""
    if ezcadapi.LoadFile(filepath):
        print(f"File {filepath} loaded successfully.")
    else:
        print(f"Failed to load file {filepath}.")

def set_marking_parameters(power, speed):
    """Sets laser marking parameters such as power and speed."""
    ezcadapi.SetPower(power)
    ezcadapi.SetSpeed(speed)
    print(f"Marking parameters set: Power={power}, Speed={speed}")

def start_marking():
    """Starts the marking process."""
    if ezcadapi.Mark():
        print("Marking started successfully.")
    else:
        print("Failed to start marking.")

def main():
    if not initialize_ezcad():
        return
    
    filepath = "C:\\path\\to\\your\\marking\\file.lxf"
    load_marking_file(filepath)
    
    # Example parameters: power=70, speed=200
    set_marking_parameters(power=70, speed=200)
    
    start_marking()

if __name__ == "__main__":
    main()
