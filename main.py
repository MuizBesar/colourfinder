import pyautogui

def get_color():
    # Get the current position of the mouse cursor
    x, y = pyautogui.position()

    # Get the pixel color at the mouse position
    pixel_color = pyautogui.pixel(x, y)

    # Convert RGB values to hexadecimal
    hex_color = '#{:02x}{:02x}{:02x}'.format(pixel_color[0], pixel_color[1], pixel_color[2])

    # Return the hexadecimal color
    return hex_color

# Main program loop
while True:
    input("Press Enter to capture color or 'q' to quit...")
    user_input = input()

    if user_input == 'q':
        break

    color = get_color()
    print(f"Captured color: {color}")
