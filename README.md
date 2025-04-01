# API Documentation Generator

## Overview

This Streamlit application generates API documentation from an OpenAPI specification (JSON format). It allows you to either upload a JSON file or paste the JSON content directly. The application then parses the OpenAPI schema and displays the documentation in a user-friendly format, and also generates a Docusaurus folder structure.

## Features

* **Input Flexibility**:
    * Upload an OpenAPI JSON file.
    * Paste OpenAPI JSON text.
* **Real-time Preview**: Displays the generated API documentation based on the provided OpenAPI schema.
* **Documentation Structure**:
    * Organizes documentation by tags.
    * Displays endpoints, methods, descriptions, parameters, request bodies, and responses.
* **Docusaurus Output**: Generates a Docusaurus site folder structure, ready for deployment.

## How to Use

1.  **Import API**:
    * Choose either "Upload JSON File" or "Paste JSON Text".
    * Upload your OpenAPI JSON file or paste the JSON content into the text area.
    * The application will parse the JSON and display the documentation.
2.  **View Documentation**:
    * The documentation is displayed in a structured format, organized by tags.
    * Expand each endpoint to view details such as method, operation ID, description, parameters, request body, and responses.
3.  **Docusaurus Output**:
    * The application generates a folder named `docusaurus-doc-site_YYYYMMDD_HHMMSS` (with a timestamp) in the current directory.
    * This folder contains a basic Docusaurus site structure with your API documentation in Markdown files.

## Docusaurus Integration

The application creates a Docusaurus website structure, placing your API documentation within the `docs` folder.  This allows you to quickly deploy your API documentation using Docusaurus.

## Requirements

* Python 3.6+
* Streamlit
* Docusaurus (If you intend to use the generated output)

## Installation

1.  **Install Python Dependencies:**

    ```bash
    pip install streamlit
    ```

## Running the Application

1.  **Run the Streamlit app:**

    ```bash
    streamlit run your_script_name.py
    ```

    Replace `your_script_name.py` with the name of your Python file.

2.  **Access the App:**
    Open your browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

## Generated Docusaurus Structure

The application generates the following Docusaurus folder structure:

docusaurus-doc-site_YYYYMMDD_HHMMSS/├── blog/│   └── hello-world.md├── docs/│   ├── intro.md│   ├── tag_name_1.md  (Markdown files for each tag)│   ├── tag_name_2.md│   └── ...├── docusaurus.config.js├── sidebars.js├── src/│   └── pages/│       └── index.js└── static/└── img/
* `docs/`: Contains the API documentation in Markdown files, organized by tags.
* `blog/`:  Contains a sample blog post.
* `src/pages/`: Contains the main page component.
* `static/img/`:  Folder for static images.
* `docusaurus.config.js`: Docusaurus configuration file.
* `sidebars.js`: Docusaurus sidebar configuration.

## Next Steps (Docusaurus Deployment)

1.  **Navigate to the generated folder:**

    ```bash
    cd docusaurus-doc-site_YYYYMMDD_HHMMSS
    ```

2.  **Install Docusaurus dependencies:**

    ```bash
    npm install
    ```

3.  **Start the Docusaurus server:**

    ```bash
    npm run start
    ```

4.  **Build the Docusaurus site:**

    ```bash
    npm run build
    ```

5.  **Deploy the site:**
    Follow the Docusaurus deployment instructions: https://docusaurus.io/docs/deployment

## Notes

* The application assumes that the input JSON follows the OpenAPI specification.
* The generated Docusaurus site provides a basic structure. You may need to customize it further (e.g., configure the sidebar, theme, and navigation).
* The application attempts to display parameters as a dataframe if possible, otherwise it displays them as JSON.
