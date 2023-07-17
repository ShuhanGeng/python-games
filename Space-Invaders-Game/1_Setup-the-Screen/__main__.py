import sys
import os
sys.path.append(os.path.dirname(__file__))

def main():
    if sys.version_info[0] < 3 or sys.version_info[1] < 7:
        print("Program requires python 3.7+")
        exit(1)
    try:
        import turtle
    except Exception as e:
        print(e)
        print("Failed to import turtle")
        exit(1)

    try:
        import setup_the_screen
   
    except Exception as e:
        print(e)
        print("Missing one of setup_the_screen, something_adding_later...")
        exit(1)

    setup_the_screen.display_main_menu()
    

if __name__ == "__main__":
    main()

