def heritage_food_validator():
    # Database: Mapping States to Heritage Dishes
    heritage_data = {
        "punjab": "Sarson da Saag & Makki di Roti",
        "telangana": "Hyderabadi Biryani",
        "bihar": "Litti Chokha",
        "west bengal": "Rosogolla & Macher Jhol",
        "gujarat": "Dhokla & Thepla",
        "rajasthan": "Dal Baati Churma",
        "tamil nadu": "Masala Dosa & Idli Sambar",
        "maharashtra": "Misal Pav & Puran Poli",
        "kerala": "Appam with Ishtu",
        "karnataka": "Bisi Bele Bath"
    }

    print("--- 🏛️ Welcome to the Desi Heritage Food Validator ---")
    state_input = input("Enter the State name: ").strip().lower()

    # Validation Logic
    if state_input in heritage_data:
        print(f"\n✅ SUCCESS: {state_input.title()} is a verified heritage region.")
        print(f"👉 Famous Dish: {heritage_data[state_input]}")
    else:
        print(f"\n❌ ALERT: '{state_input.title()}' is not in our heritage database yet.")

if __name__ == "__main__":
    heritage_food_validator()
  
