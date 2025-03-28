# API Documentation Generator

This Python program, built with the Streamlit library, allows you to generate API documentation from an OpenAPI (formerly Swagger) specification in JSON format. You can either upload a JSON file or paste the JSON text directly into the application.

## Features

* **Input Flexibility:** Supports uploading a JSON file or pasting JSON text.
* **JSON Validation:** Checks if the provided input is valid JSON and displays an error message if it's not.
* **Schema Display:** Shows the uploaded or pasted JSON schema in an editable text area.
* **Dynamic Documentation Generation:** Parses the OpenAPI specification and generates human-readable documentation.
* **Organized Output:** Documents are organized by tags, making it easy to navigate different API sections.
* **Detailed Endpoint Information:** For each endpoint, it displays:
    * Path and Summary
    * HTTP Method
    * Operation ID
    * Description
    * Parameters (as a table or JSON)
    * Request Body (as JSON)
    * Responses (as JSON)
* **Expandable Sections:** Uses Streamlit expanders to keep the documentation concise and allow users to view details on demand.
* **Styled Interface:** Includes custom CSS for improved readability and visual appeal.

## How to Use

1.  **Run the application:**
    * Make sure you have Python and Streamlit installed. If not, you can install them using pip:
        ```bash
        pip install streamlit requests pandas
        ```
    * Save the Python code as a `.py` file (e.g., `api_doc_generator.py`).
    * Run the application from your terminal:
        ```bash
        streamlit run api_doc_generator.py
        ```
    * The application will open in your web browser.

2.  **Input your API Specification:**
    * The application will present you with two options: "Upload JSON File" and "Paste JSON Text".
    * **Upload JSON File:** Click on the "Browse files" button and select your OpenAPI specification file in JSON format.
    * **Paste JSON Text:** Select the "Paste JSON Text" option and paste the content of your OpenAPI specification into the provided text area.

3.  **View and Edit Schema (Optional):**
    * Once the JSON is successfully uploaded or pasted, the application will display the schema in the left column under the "Schema Data" heading.
    * You can edit the JSON directly in the text area. The application will validate the JSON as you type and display an error message if it's invalid.
    * Editing the schema here will dynamically update the generated documentation in the right column.

4.  **Explore the Documentation:**
    * The right column, under the "Documentation" heading, will display the generated API documentation.
    * The documentation is organized by the tags defined in your OpenAPI specification. Each tag will have its own section.
    * Within each tag section, you'll find a list of API endpoints associated with that tag. Each endpoint is initially collapsed within an expander.
    * Click on the expander to view the detailed information for a specific endpoint, including its method, operation ID, description, parameters, request body, and responses.

## Dependencies

* **streamlit:** For creating the web application interface.
* **requests:** Although imported, it's not directly used in the current version of the code. It might be intended for future use, such as fetching the schema from a URL.
* **pandas:** Used to display parameters in a tabular format (DataFrame) when applicable.
* **json:** For handling JSON data (loading and parsing).

## Customization

The look and feel of the application can be customized by modifying the CSS embedded within the `st.markdown` block at the beginning of the script. You can change colors, fonts, and other styles to match your preferences.

## Potential Improvements

* **Fetch from URL:** Allow users to input a URL to fetch the OpenAPI specification.
* **Authentication Support:** Handle API specifications that require authentication to access.
* **More Robust Error Handling:** Implement more specific error handling for different scenarios.
* **Search Functionality:** Add a search bar to easily find specific endpoints or information within the documentation.
* **Download Documentation:** Provide an option to download the generated documentation (e.g., as a PDF or Markdown file).
* **Schema Validation against OpenAPI Standards:** Implement more rigorous validation to ensure the provided schema adheres to OpenAPI specifications.
