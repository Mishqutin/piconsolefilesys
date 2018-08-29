if len(args)<2:
    print("Usage: p <pin> <1/0>")
else:
    GPIO.output(int(args[0]), int(args[1]))