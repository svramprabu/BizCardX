# BizcardX

BizcardX is a Python project designed to simplify the process of extracting information from business card images using the EasyOCR module. This tool allows users to effortlessly extract information from images and manipulate the data as needed. The extracted details are then displayed, and users can make edits if necessary. The project provides a user-friendly interface generated using Streamlit, making it accessible and intuitive.

## Features

- Extracts details from business card images using EasyOCR.
- Displays the extracted information in designated fields.
- Allows users to edit the displayed details.
- Presents the extracted details in both a dataframe and a sidebar for easy access.
- Provides a button to load the data into an SQLite database.
- Displays the SQLite database contents as a dataframe after loading.
- Offers an option to clear the database via a button in the sidebar.

## Installation

To use BizcardX, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/svramprabu/BizCardX
   cd BizcardX
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run BizCardX.py
   ```

## Usage

1. Upload a business card image using the provided interface.
2. The extracted details will be displayed in designated fields.
3. Edit the displayed details if necessary.
4. Use the "Load Data to Database" button to save the data into an SQLite database.
5. View the SQLite database contents in a dataframe.
6. If needed, clear the database using the "Clear Database" button in the sidebar.

## Contributors

- Ramprabu S V
<!-- - Another Contributor (if applicable) -->

## License

This project is a free to use public repository.

---

Feel free to contribute to this project or report any issues on the [GitHub repository](https://github.com/svramprabu/BizCardX). We welcome your feedback and contributions to make BizcardX even better!
