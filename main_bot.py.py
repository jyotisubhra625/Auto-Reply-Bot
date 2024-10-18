import pyautogui
import time
import pyperclip
import google.generativeai as genai

# Function to get response from Gemini model
def get_gemini_response(input_text):
    # Configure the Gemini API
    genai.configure(api_key="<API KEY>")
    
    # Define the personality for the model
    personality = "You are 'NAME' and you are talking with a person. Reply according to the data provided. The languages he can speak are English, Hindi, and Bengali, and the chats are usually in a fusion of English and Bengali or English or Hindi."
    
    # Create a GenerativeModel instance
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Combine personality with input text
    prompt = personality + " " + input_text
    
    # Generate a response
    response = model.generate_content(prompt)
    
    # Extract the generated text from the response
    generated_text = response.candidates[0].content.parts[0].text
    return generated_text

if __name__=="__main__":
    # Click on the WhatsApp window (update coordinates as necessary)
    pyautogui.click(656, 744)
    time.sleep(1)

    # Select the latest message (update coordinates as necessary)
    pyautogui.moveTo(506, 180)
    pyautogui.dragTo(1178, 693, duration=1.0, button='left')

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # Click to focus on the input area (update coordinates as necessary)
    pyautogui.click(500, 175)

    # Get the copied text
    input_text = pyperclip.paste()

    # Get the response from the Gemini model
    response_text = get_gemini_response(input_text)

    # Remove everything up to the last colon (including the colon)
    last_colon_index = response_text.rfind(':')
    if last_colon_index != -1:
        cleaned_response_text = response_text[last_colon_index + 1:].strip()  # Get text after the last colon and strip whitespace
    else:
        cleaned_response_text = response_text.strip()  # If no colon is found, just return the original text stripped of whitespace

    # Print the cleaned response (or send it back to WhatsApp)
    print(cleaned_response_text)

    # Optionally, you can send the cleaned response back to WhatsApp
    pyautogui.typewrite(cleaned_response_text)
    pyautogui.press('enter')

    # Sleep for a while before checking for new messages
    time.sleep(5)