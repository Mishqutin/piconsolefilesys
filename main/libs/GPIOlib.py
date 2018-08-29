if os.name=="nt":
    print("GPIO cannot run on this os.")
else:
    from RPi import GPIO
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    