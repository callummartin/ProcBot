
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
import re 

variable_dictionary = {}

# Logging functionality. 
def log_entry(type, message):
    print(f"[{type}] {message}")


# Returns a driver object based on the browser requested. 
def get_web_driver(browser):

    # The get_web_driver function initialises and returns the appropriate Selenium WebDriver
    # based on the provided browser choice ('Chrome', 'Edge', or 'Firefox').
    #
    # Parameters:
    # browser (str): The browser for which the WebDriver should be initialised. It can be:
    #   - "Chrome" for Chrome WebDriver
    #   - "Edge" for Edge WebDriver
    #   - "Firefox" for Firefox WebDriver
    #   - Any other value will default to initialising the Edge WebDriver.
    #
    # Returns:
    # driver (WebDriver or None): Returns the initialised WebDriver instance for the specified browser.
    #   If an error occurs during WebDriver initialisation, it prints an error message and returns None.

    try:
        match browser:
            case "Chrome":
                driver = webdriver.Chrome()
            case "Edge":
                driver = webdriver.Edge()
            case "Firefox":
                driver = webdriver.Firefox()
            case _:
                driver = webdriver.Chrome() 
        return driver 
    except Exception as e:
        log_entry("error", f"Browser driver invokation error: {e}")
        return None


def browser_load(driver, url):

    # The browser_load function retrieves the HTML content from a specified URL 
    # using the provided Selenium WebDriver.
    #
    # Parameters:
    # driver (WebDriver): The Selenium WebDriver instance used to open the URL and retrieve the page.
    # url (str): The URL of the web page whose HTML content is to be fetched.
    #
    # Returns:
    # None: The function doesn't return a value. It simply uses the driver to navigate to a page. 

    try:
        driver.get(url)
    except Exception as e:
        log_entry("error", f"Browser load error: {e}")



def process_wait(seconds):

    # The process_wait function pauses the execution for a specified duration
    #
    # Parameters:
    # seconds (int or float): The duration (in seconds) to wait before timing out.
    #
    # Returns:
    # None: The function doesn't return a value. It simply applies a system wait.

    try:
        time.sleep(seconds)
    except Exception as e:
        log_entry("error", f"Process wait error: {e}")
    

    

def browser_wait(driver, duration):

    # The browser_wait function pauses the execution for a specified duration
    # to allow the WebDriver to wait implicitly for elements to appear on the page.
    #
    # Parameters:
    # driver (WebDriver): The Selenium WebDriver instance used to perform the implicit wait.
    # duration (int or float): The duration (in seconds) to wait before timing out.
    #
    # Returns:
    # None: The function doesn't return a value. It simply applies an implicit wait to the WebDriver. 

    try:
        driver.implicitly_wait(duration)
    except Exception as e:
        log_entry("error", f"Implicit wait error: {e}")


def browser_stop(driver):
    
    # The browser_stop function terminates the WebDriver session and closes the browser window.
    #
    # Parameters:
    # driver (WebDriver): The Selenium WebDriver instance to be stopped and the browser to be closed.
    #
    # Returns:
    # None: The function doesn't return a value. It simply stops the WebDriver and closes the browser.
    
    try:
        driver.quit()
    except Exception as e:
        log_entry("error", f"Browser quit error: {e}")


def get_element_by_id(driver, id):

    # The get_element_by_id function locates an element on the web page using its ID.
    #
    # Parameters:
    # driver (WebDriver): The Selenium WebDriver instance used to locate the element.
    # id (str): The ID attribute of the element to be located on the page.
    #
    # Returns:
    # element (WebElement or None): Returns the WebElement if the element is found. 
    #   If an error occurs or the element is not found, it prints an error message and returns None.

    try:
        element = driver.find_element(by=By.ID, value=id)
        return element 
    except Exception as e:
        log_entry("error", f"Get element by Id error: {e}")
        return None 
    

def get_element_by_name(driver, name):

    # Attempts to find a web element by its 'name' attribute.
    #
    # This function uses the provided WebDriver instance to locate an element 
    # on the webpage using the 'name' attribute. If successful, it returns 
    # the located element. In the event of an error (e.g. element not found), 
    # an error message is logged and the function returns None.
    #
    # Parameters:
    #    driver (WebDriver): The Selenium WebDriver instance used to interact with the page.
    #    name (str): The 'name' attribute of the element to be located.
    #
    # Returns:
    #    WebElement or None: The located web element if found, otherwise None.

    try:
        element = driver.find_element(by=By.NAME, value=name)
        return element
    except Exception as e:
        log_entry("error", f"Get element by name error: {e}")
        return None 
    

def get_element_by_class_name(driver, class_name):

    # Attempts to find a web element by its 'class' attribute.
    #
    # This function uses the provided WebDriver instance to locate an element 
    # on the page by its 'class' attribute. If the element is found, it is 
    # returned. If an error occurs (such as the element not being found), 
    # an error message is logged and None is returned.
    #
    # Parameters:
    #    driver (WebDriver): The Selenium WebDriver instance used to interact with the page.
    #    class_name (str): The 'class' attribute of the element to be located.
    #
    # Returns:
    # 

    try:
        element = driver.find_element(by=By.CLASS_NAME, value=class_name)
        return element 
    except Exception as e:
        log_entry("error", f"Get element by class name error: {e}")
        return None 


def get_element_by_css_selector(driver, selector):

    # Attempts to find a web element using a CSS selector.
    #
    # This function uses the provided WebDriver instance to locate an element 
    # on the page via a CSS selector. If the element is located successfully, 
    # it is returned. If an error occurs, an error message is logged and None 
    # is returned.
    #
    # Parameters:
    #    driver (WebDriver): The Selenium WebDriver instance used to interact with the page.
    #    selector (str): The CSS selector used to identify the element.
    #
    # Returns:
    #    WebElement or None: The located web element if found, otherwise None.

    try:
        element = driver.find_element(by=By.CSS_SELECTOR, value=selector)
        return element 
    except Exception as e:
        log_entry("error", f"Get element by CSS selector error: {e}")
        return None 
    

def get_element_by_xpath(driver, xpath):

    # Attempts to find a web element using an XPath expression.
    #
    # This function uses the provided WebDriver instance to locate an element 
    # on the page via an XPath expression. If the element is found, it is 
    # returned. If an error occurs (e.g. element not found), an error message 
    # is logged and None is returned.
    #
    # Parameters:
    #    driver (WebDriver): The Selenium WebDriver instance used to interact with the page.
    #    xpath (str): The XPath expression used to locate the element.
    #
    # Returns:
    #    WebElement or None: The located web element if found, otherwise None.

    try:
        element = driver.find_element(by=By.XPATH, value=xpath)
        return element
    except Exception as e:
        log_entry("error", f"Get element by xpath error: {e}")
        return None 


def browser_stop_with_confirmation(driver):

    # Attempts to quit the current Selenium session.
    #
    # This function uses the provided WebDriver to quit all concurrent processes. 
    #
    # Parameters:
    #    driver (WebDriver): The Selenium WebDriver instance used to interact with the page.
    #
    # Returns:
    #    This function does not return a value. 

    # User prompt.
    print(f"Press enter to close the browser process...")
    input()

    # Quits the browser session. 
    print(f"Closing the browser.")
    browser_stop(driver)


def start_test_harness():

    # The start_test_harness function runs through a test harness process to ensure the engine is working correctly.
    #
    # Parameters:
    # None: The function does not take a parameter. 
    #
    # Returns:
    # None: The function doesn't return a value. 

    # Defines the test URL.
    test_url = "https://duckduckgo.com/"

    # Gets the browser driver. 
    print(f"Fetching browser driver.")
    browser = get_web_driver("Chrome")
    if browser is None:
        print("Unable to get the browser driver.")
        return False 
    print(browser)

    # Loads the browser and navigates to the test URL.
    print(f"Loading browser and navigating to test URL: {test_url}")
    browser_load(browser, test_url)

    # Runs test search
    search_box = get_element_by_id(browser, "searchbox_input")
    search_button = get_element_by_xpath(browser, '//*[@id="searchbox_homepage"]/div/div/div/button')
    search_box.send_keys("Lorem ipsum")
    process_wait(2)
    search_button.click()
    process_wait(2)

    # Graceful browser stop with confirmation. 
    browser_stop_with_confirmation(browser)

    return True 


# Function to replace each dictionary query with its value from the dictionary
def parse_var(candidate_exec_line, variable_dictionary):

        # This function processes a line of code (candidate_exec_line) and replaces any 
    # occurrences of variables within the `variable_dictionary` pattern with 
    # their corresponding values from the provided dictionary.

    # The function uses regular expressions to identify the variables written 
    # in the form of `variable_dictionary['key']`, where 'key' is a string that 
    # matches a key in the provided `variable_dictionary`.

    # Parameters:
    # candidate_exec_line (str): A string representing the line of code to be parsed. 
    # variable_dictionary (dict): A dictionary where keys represent variable names 
    # and values represent their corresponding values.

    # Returns:
    # str: The modified `candidate_exec_line` where all recognised variables are 
    # replaced with their respective values from `variable_dictionary`.

    # The function works as follows:
    # 1. A regular expression pattern is used to find occurrences of the form 
    #    `variable_dictionary['key']` in the input line.
    # 2. For each match, the function checks if the variable (`key`) exists in 
    #    the `variable_dictionary`.
    # 3. If a match is found in the dictionary, it replaces the `variable_dictionary['key']` 
    #    with the actual value of the key in the dictionary.
    # 4. The modified line is returned after all replacements have been made.

    # Regular expression to match the left side of the assignment
    regex = r"variable_dictionary\['([a-zA-Z0-9_]+)'\]"

    # Find all matches for variable_dictionary[...] pattern
    matches = re.findall(regex, candidate_exec_line)
    
    # Iterates over the matches. 
    for match in matches:

        # Check if the key exists in the dictionary.
        if match in variable_dictionary:

            # Create the replacement string
            replacement = str(variable_dictionary[match])

            # Replace the matched key with the corresponding value
            candidate_exec_line = re.sub(r"variable_dictionary\['" + re.escape(match) + r"'\]", replacement, candidate_exec_line)
    
    return candidate_exec_line


def preserve_quote_string(text):

    # This function processes a given string (`text`) by identifying any quoted 
    # strings and replacing them with placeholders, then splitting the text 
    # into components (words) while preserving the quoted strings.

    # The function works as follows:
    # 1. It identifies all quoted strings (enclosed in double quotes).
    # 2. It replaces the quoted strings in the text with placeholders.
    # 3. It splits the modified text into individual components (words).
    # 4. It then replaces the placeholders back with the original quoted strings 
    #    to restore them in their original positions.

    # Parameters:
    # text (str): A string which may contain quoted substrings that need to be 
    # preserved while splitting the text into components.

    # Returns:
    # list: A list of components (words) from the input string, with the 
    # quoted substrings restored to their original positions.

    # Regex finds quotation. 
    quote_strings = re.findall(r'"(.*?)"', text)

    # Replace the quoted strings with placeholder values. 
    for i, quote in enumerate(quote_strings):
        placeholder = f"{{{i}}}"
        text = text.replace(f'"{quote}"', placeholder)

    # Split the text by spaces. 
    components = text.split()

    # Replaces the placeholders with the original quote strings. 
    for i, quote in enumerate(quote_strings):
        components = [item.replace(f"{{{i}}}", f'"{quote}"') for item in components]

    return components


def proc_var(statement):

    # This function processes a given statement to check if it is a variable 
    # in the form of "[var]" and, if so, converts it into a dictionary query 
    # string that accesses the variable's value from `variable_dictionary`.

    # The function works as follows:
    # 1. It checks if the statement starts with the "[var]" identifier.
    # 2. If the statement is a variable (starts with "[var]"), it removes the 
    #    "[var]" identifier and constructs a string that queries the 
    #    `variable_dictionary` for the variable's value.
    # 3. If the statement does not start with "[var]", it returns the 
    #    statement as-is without modification.

    # Parameters:
    # statement (str): A string representing the statement to be processed. 
    # It is expected to be in the form of "[var]variable_name" for variables.

    # Returns:
    # str: A string which either represents a dictionary query for a variable 
    # or the original statement if it is not a variable.

    # Variables should start with [var].
    var_identifier = "[var]"

    # If this statement is a variable
    if statement.startswith(var_identifier):

        # Remove the identifier and return the dictionary query string. 
        clean_var = statement.replace(var_identifier, "")
        return f"variable_dictionary[{repr(clean_var)}]"
    else:
        return statement


def parse_proc_line(line):

    # This function processes a single line of code (line) representing a command 
    # and translates it into an executable Python statement. 

    # The function works as follows:
    # 1. It strips any leading or trailing whitespace from the line.
    # 2. It splits the stripped line into components (elements), preserving quoted strings.
    # 3. It checks the first element (command) and constructs the corresponding executable code.
    # 4. It returns the constructed executable line of code, or `None` if the command is unrecognised.

    # Parameters:
    # line (str): A string representing a command that is to be processed and converted 
    # into executable code.

    # Returns:
    # str or None: The corresponding executable Python code based on the command, 
    # or `None` if the command is not recognised.

    # Strips out the line. 
    strip_line = line.strip()

    # Splits the stripped line into an array of its elements. 
    # strip_array = strip_line.split()
    strip_array = preserve_quote_string(strip_line)

    # Gets the command element. 
    command = strip_array[0]

    # Process determination. 
    exec_line = ""
    match command:
        case "var": 
            exec_line = f"variable_dictionary['{proc_var(strip_array[1])}'] = {proc_var(strip_array[2])}"
        case "start":
            exec_line = f"browser = get_web_driver('{proc_var(strip_array[1])}')"
        case "quit":
            exec_line = f"browser.quit()"
        case "stop":
            exec_line = f"browser_stop_with_confirmation(browser)"
        case "confirm":
            exec_line = f"input({proc_var(strip_array[1])})"
        case "goto":
            exec_line = f"browser_load(browser, {proc_var(strip_array[1])})"
        case "wait":
            exec_line = f"process_wait({proc_var(strip_array[1])})"
        case "gi":
            exec_line = f"{proc_var(strip_array[1])} = get_element_by_id(browser, {proc_var(strip_array[2])})"
        case "gn":
            exec_line = f"{proc_var(strip_array[1])} = get_element_by_name(browser, {proc_var(strip_array[2])})"
        case "gc":
            exec_line = f"{proc_var(strip_array[1])} = get_element_by_class_name(browser, {proc_var(strip_array[2])})"
        case "gs":
            exec_line = f"{proc_var(strip_array[1])} = get_element_by_css_selector(browser, {proc_var(strip_array[2])})"
        case "gx":
            exec_line = f"{proc_var(strip_array[1])} = get_element_by_xpath(browser, {proc_var(strip_array[2])})"
        case "type":
            exec_line = f"{proc_var(strip_array[1])}.send_keys({proc_var(strip_array[2])})"
        case "click":
            exec_line = f"{proc_var(strip_array[1])}.click()"
        case _:
            print(f"ERROR: Execution command parse eval is None: {command}")
            print(f"ERROR: Execution line parse: {line}")
            exec_line = None 

    return exec_line 


def parse_proc_file(file_path):

    # This function reads a file containing procedure instructions and 
    # processes each line to convert it into executable code. 

    # The function works as follows:
    # 1. It opens the specified file and reads each line sequentially.
    # 2. For each line, it checks if the line is blank or a comment (starting with "//").
    # 3. It processes valid lines into executable code using `parse_proc_line`.
    # 4. It appends the resulting executable code to a list.
    # 5. It returns the list of executable code.

    # Parameters:
    # file_path (str): The path to the procedure file to be processed.

    # Returns:
    # list: A list of executable code lines derived from the procedure file.

    # Array to store executable code. 
    execution_code = []

    # Opens the file and reads each line sequentially. 
    with open(file_path, "r") as file: 
        for line in file: 

            # If the line is blank, skip. 
            if len(line.strip()) == 0:
                 continue 
            
            # If the line is a comment line. 
            if line.startswith("//"):
                continue

            # Add the line as execution code. 
            parse_exec_line = parse_proc_line(line)
            execution_code.append(parse_exec_line) 

    return execution_code


def exec_proc_from_file(file_path):

    # This function executes a procedure file by parsing and executing 
    # each line in the file sequentially. 

    # The function works as follows:
    # 1. It reads the procedure file and determines the execution stages.
    # 2. For each stage, it parses the variables in the stage using `parse_var`.
    # 3. It then prints the parsed stage for debugging or logging purposes.
    # 4. Finally, it executes the code of each stage using the `exec` function 
    #    with the provided global and variable context.

    # Parameters:
    # file_path (str): The path to the procedure file that contains the instructions 
    # to be executed.

    # Returns:
    # None: This function does not return anything but executes code dynamically 
    # as it processes each stage in the procedure file.

    # Determines execution stages. 
    execution_stages = parse_proc_file(file_path)

    # Iterates over each stage. 
    for stage in execution_stages:

        # Performs variable parse. 
        parse_stage = parse_var(stage, variable_dictionary)
        print(f"Executing: {parse_stage}")

        # Executes stage as code. 
        exec(stage, globals(), variable_dictionary)