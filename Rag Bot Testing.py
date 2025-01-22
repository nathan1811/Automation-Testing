from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from concurrent.futures import ThreadPoolExecutor

# Setting up Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Load questions from Questions.txt and ignore every even line
questions_file = "C:/Users/natha/Downloads/Questions.txt"  # Path to the Question.txt file
with open(questions_file, "r") as f:
    questions = [line.strip() for i, line in enumerate(f.readlines()) if i % 2 == 0 and line.strip()]

def perform_search():
    """Perform a search on the chatbot with unique queries."""
    print("Starting the browser...")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get("http://16.170.246.137:8501/")  # URL of the chatbot
    time.sleep(3)

    # To ensure unique questions are asked during the 5 iterations
    shuffled_questions = random.sample(questions, min(len(questions), 5))  # Get 5 unique questions

    try:
        for search_query in shuffled_questions:  # Iterate over the unique questions
            print(f"Searching for: {search_query}")

            # Find the text box
            search = driver.find_element(By.XPATH, "//textarea[@aria-label='Enter your queries here: ']")
            time.sleep(2)  # Small delay to avoid unloaded page

            # Enter the query
            search.send_keys(search_query)
            time.sleep(1) # Small delay to ensure the question is filled in to the textbox before Enter key is pressed

            # Press Enter to submit
            search.send_keys(Keys.ENTER)
            time.sleep(8)  # Allow time for chatbot results

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser after 5 attempts
        driver.quit()
        print("Browser closed.")

# Repeat the process 10 times
for iteration in range(10):
    print(f"\n### Iteration {iteration + 1} of 10 ###\n")

    # Run 5 parallel instances for this iteration
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(perform_search) for i in range(10)]

    # Wait for a short delay before the next iteration
    time.sleep(5)

print("All iterations completed.")
