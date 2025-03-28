import streamlit as st
import requests
import pandas as pd
import json
from json.decoder import JSONDecodeError

st.set_page_config(layout='wide')
st.markdown(
    """
    <style>
    .stTextArea textarea {
        background-color: #f0f8ff; /* Light blue background */
        color: #000000; /* Black text color */
    }
    .streamlit-expanderHeader {
        background-color: #e6f7ff; /* Light cyan background */
        color: #003366; /* Dark blue text color */
        font-weight: bold; /* Bold text */
        padding: 12px; /* Add padding */
        border-radius: 8px; /* Rounded corners */
        border: 1px solid #b3d9ff; /* Light blue border */
    }
    .streamlit-expanderContent {
        font-family: 'Courier New', Courier, monospace; /* Monospace font */
        font-size: 15px; /* Slightly larger font size */
        line-height: 1.8; /* Increased line height for readability */
        color: #333333; /* Dark gray text color */
        background-color: #f9f9f9; /* Light gray background */
        padding: 15px; /* Add padding */
        border-left: 4px solid #b3d9ff; /* Left border for emphasis */
    }
    </style>
    """,
    unsafe_allow_html=True,
    )


def upload_json():
    topbar = st.container(border=True)
    topbar.header("Import API")
    
    with topbar:
        # st.subheader('Connection details')
        # Option to upload a file or paste text
        input_method = topbar.radio("Choose input method:", ("Upload JSON File", "Paste JSON Text"))

        json_data = None
        error_message = None

        if input_method == "Upload JSON File":
            uploaded_file = topbar.file_uploader("Upload a JSON file", type=["json"])
            if uploaded_file is not None:
                try:
                    json_data = json.load(uploaded_file)
                    topbar.success("JSON file uploaded successfully!")
                    # topbar.json(json_data)  # Optionally display the parsed JSON
                except JSONDecodeError as e:
                    error_message = f"Invalid JSON format in file: {e}"
                except Exception as e:
                    error_message = f"An error occurred while reading the file: {e}"
        elif input_method == "Paste JSON Text":
            json_text = topbar.text_area("Paste your JSON text here:", height=300)
            if json_text:
                try:
                    json_data = json.loads(json_text)
                    topbar.success("JSON text parsed successfully!")
                    # topbar.json(json_data)  # Optionally display the parsed JSON
                except JSONDecodeError as e:
                    error_message = f"Invalid JSON format in pasted text: {e}"
                except Exception as e:
                    error_message = f"An error occurred while parsing the text: {e}"

        if error_message:
            topbar.error("Error processing JSON:")
            topbar.error(error_message)
        elif json_data is None:
            topbar.info("Please upload a JSON file or paste JSON text.")

    return json_data

def populate_structure(data):
    

    json_data = schema_col.text_area("Edit JSON:", value=json.dumps(data, indent=4), height=600)

    try:
        edited_json = json.loads(json_data)
        schema_col.success("Valid JSON!")
        populate_doc(edited_json)
        # schema_col.write("Parsed JSON:")
        # schema_col.json(edited_json)
    except json.JSONDecodeError:
        schema_col.error("Invalid JSON!")

def populate_doc(data):

    
    doc_col.write(data["info"].get("description",[]))

    tag_data = data.get("tags",[])

    
    for tag in tag_data:
        tag_name = tag["name"]
        tag_con =  doc_col.container(border=True)
        tag_con.subheader(tag_name)
        
        if "description" in tag:
            tag_con.write(tag["description"]) 
        if "externalDocs" in tag:
                tag_con.markdown(f"[{tag['externalDocs']['description']}]({tag['externalDocs']['url']})")         

        path_data = data.get("paths",[])
        for path in path_data:
            methods = path_data[path]
            

            for method, path_details in methods.items():
                
                tags = path_details.get("tags", [])
                if tag_name in tags:
                    with tag_con.expander(path + " " + path_details.get("summary", "No summary available"), expanded=False):
                        st.subheader("Method")
                       
                        st.write(method)
                        st.markdown("**Operation ID**")
                        st.markdown(path_details.get("operationId"))
                        st.subheader("Description")
                        st.markdown(path_details.get("description", "No description available"))
                        if path_details.get("parameters"):
                            st.subheader("Parameters")

                            parameters = path_details.get("parameters")
                            if isinstance(parameters, list):
                                try:
                                    st.dataframe(parameters)
                                except Exception as e:
                                    st.error(f"Error displaying parameters as JSON: {e}")
                            else:
                                st.json(parameters)
                        if path_details.get("requestBody"):
                            st.subheader("Request Body")
                            st.json(path_details.get("requestBody"))  
                        if path_details.get("responses"):
                            st.subheader("Response")
                            st.json(path_details.get("responses"))    
                          
                        
                        

                    
                
        # st.write(path[1].get["tags",[]])


if __name__ == "__main__":
    st.title("API Documentation Generator")
    schema_data = upload_json()
    
    if schema_data:
        schema_col, doc_col = st.columns(2, border=True)
        schema_col.header("Schema Data", divider=True)
        doc_col.header("Documentation", divider=True)
        populate_structure(schema_data)


    
    
        
    
 


