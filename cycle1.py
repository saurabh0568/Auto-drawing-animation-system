def anima_cycle():
    import cv2
    import time

# Load the GIF file
    gif_path = "cycle.gif"
    gif = cv2.VideoCapture(gif_path)

# Check if the GIF loaded successfully
    if not gif.isOpened():
        print("Error: Could not open the GIF file.")
        exit()

# Display each frame of the GIF
    try:
        while True:
            ret, frame = gif.read()
            if not ret:
                break
            cv2.imshow("GIF Animation", frame)
            key = cv2.waitKey(200)  # Adjust delay as needed
            if key == ord('q'):  # Press 'q' to quit
                break
    except KeyboardInterrupt:
        pass  # Allow the user to stop the animation by pressing Ctrl+C

# Release the GIF and close all windows
    gif.release()
    cv2.destroyAllWindows()