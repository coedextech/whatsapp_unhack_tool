import os
import time

def main():
    print("Welcome to the WhatsApp Unhack Tool")
    print("This tool will guide you through regaining control of your WhatsApp account.")

    # Step 1: Ask for the WhatsApp number
    whatsapp_number = input("Please enter your WhatsApp number: ")

    # Step 2: Simulate the unhacking process with a loading bar
    print(f"Unhacking your WhatsApp account associated with {whatsapp_number}...")
    for i in range(1, 101):
        print(f"Loading: {i}%", end='\r')
        time.sleep(0.1)  # Simulate delay

    print("\nYour WhatsApp account has been unhacked successfully!")

if __name__ == "__main__":
    main()