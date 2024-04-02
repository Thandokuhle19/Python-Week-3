# Python-Week-3
# Project Planning
_Finding Inspiration:_
 

_User Stories:_
- User stories depict small scenarios from a user's perspective.
- These stories emphasise the user's goal and motivation rather than the application itself.
- They are brief, simple, and informal, which are perfect for jotting down on index cards.
- They follow the format: "As a [user/role], I want [goal] so that [reason/benefit].
- Additional user stories can be written to delve into more specifics.
- Eg, "As a digest recipient, I want to know the weather forecat so I know how to dress."
- It is importabt to avoid overloading the application with every possible feature right from the beginning.
- The initial scope should be kept manageable, while ideas for additional features can be maintained seperately in a backlog.
- When writing user stories, focus on the user's goals and reasons, rather than specific interface details or implementation methods.
  
_Use Cases:_

- Use cases usually include a title, an actor(a user or system), and a scenario that describes how a goal is achieved.
- The scenario can be written as a paragraph or a list of steps in simple language.
- Eg, a use case may involve a digest recipient reading tweets on a specific Twitter trend, by opening email, or clicking on the trend link, and accessing the corresponding Twitter page.
- User stories and use cases capture different information.
- User stories focus on the who, what, and why of a task or goal, while use cases cover the who, what, and how of achieving the goal.

_Project Requirements:_

- It is helpful to write requirements to formally capture the capabilities and limitations of an application.
- Function requirements describe what the application should or should not do and are written as sentences starting with "the application must" or "the application".
- The requirements act as a checklist to ensure the application meets all the necessary functionalities.
- Requirements are kept at high level, omitting specific details.
- We have non-functional requirements which describes how the application should accomplish its tasks.
- Focuses on: qualities like maintainability, reliability, and usability.

_Architecture:_

- To determine what classes you will need for your Python app, you will need to select nouns from your requirements.
  
_Stube Code:_

- Stube code has provide a structure for the design and was created for the whole program using three Python modules which consists" dd_content.py, dd_email.py, and dd_gui.py.
- dd_email.py module: contains the skeleton for the daily digest email class, with placeholder methods using the pass statement.
- This allows the script to be executed without errors, even though it does not have any useful functionality.
- dd_content.py module: this module does not define a daily digest content class.
- Both the dd_email and dd_content, the if name equals the main section at the bottom of the script which can be used to add test code.
- dd_gui.py module: this module handles the graphical user interface for the email digest administrator and utilizes the TKinter module.
- The stub code provides structure for implementation, allowing for seperate development for the email class, independent content functions, and the GUI.  

# Daily Inspirational Quotes
- Now that there is a plan and the program structure is outlined, now we need to implement the code.
- In this upcoming section, four functions will be implemented in the "dd_content.py" module.
- We will be creating a "get_random_quote" function.
- To implement the "get_random_quote" function, the source of random quotes needs to be determined.
- We can use Beautiful Soup or Scrapy while web browsing. After we have explored options, a decision is made curate a persinal list of inspirational quotes.
- We can store the quotes and their authors by using different file formats like CSV, JSON, or XML.


_Weather Forecasting with OpenWeatherMap:_

- Now that we are finished with implementing the get_random_quote, we will work on implementing the next content funtion, which is get_weather_forecast.
- We will need to fetch the weather information from the internet, since the weather forecast data needs to be current.
- We can do this by the following ways:
                -  Use a Python web-scraping library: extract forecast information from a website like wether.com
                -  Search the Python Package Index for a Python library that can retrieve weather data from online source.
                -  Find an online source of weather information that provides an API we can directly call from our program.
