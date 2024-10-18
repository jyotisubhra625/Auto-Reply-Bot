<h1>Auto-Reply-Bot</h1>

<h4>Step 1: Get the coordinates of the elements</h4>

Open the GitHub page you want to interact with.
Run the script with pyautogui.position() to get the coordinates of the elements.
Move your mouse to the position of the element you want to interact with (e.g., the text area where you want to paste the response).
Note down the coordinates displayed in the terminal or console.

<h4>Step 2: Update the coordinates in the script</h4>

Open the script and update the coordinates in the following lines:
pyautogui.click(656, 744) -> Update with the coordinates of the text area where you want to paste the response.
pyautogui.moveTo(506, 180) -> Update with the coordinates of the top-left corner of the text area where you want to select the text.
pyautogui.dragTo(1178, 693, duration=1.0, button='left') -> Update with the coordinates of the bottom-right corner of the text area where you want to select the text.
pyautogui.click(500, 175) -> Update with the coordinates of the input area where you want to focus.

<h4>Step 3: Update the script to interact with GitHub</h4>

Update the get_gemini_response function to handle the GitHub-specific input text.
Update the cleaned_response_text variable to handle any GitHub-specific formatting.

