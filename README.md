# Automation-Testing
Developed an automation script using Selenium WebDriver in Python to test the responsiveness and functionality of a web-based chatbot which was developed by Krea University to answer questions related to courses offered.

The project included the following key features:

Dynamic Query Management: Loaded a set of queries from a text file and ensured the chatbot received unique questions in each iteration.

Parallel Execution: Utilized Python's ThreadPoolExecutor to run up to 10 parallel browser instances, simulating concurrent user interactions with the chatbot.

Browser Automation: Automated browser actions, including navigating to the chatbot URL, entering queries, and submitting them.

Error Handling and Logging: Implemented exception handling to capture and log any errors during execution, ensuring stability and ease of debugging.

Efficiency and Scalability: Designed to handle large sets of queries and iterations, making it suitable for stress testing and performance analysis.
