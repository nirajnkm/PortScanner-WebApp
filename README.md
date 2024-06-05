# Port Scanner

## Overview

This project is a comprehensive port scanner application that allows users to scan open ports on a given hostname. The application includes a web-based interface built using Flask, Python scripts for port scanning, and integration with an AI service to generate security reports. 

## Features

- **Port Scanning**: Scans a range of ports on a given hostname to identify open ports.
- **Web Interface**: User-friendly web interface to input scan parameters and view results.
- **DNS Resolution**: Resolves hostnames to IP addresses.
- **Multi-threading**: Efficiently scans ports using multiple threads.
- **AI Integration**: Generates security reports using Google's Generative AI.

## Installation

### Prerequisites

- Python 3.x
- Google Generative AI API key (for AI integration)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/nirajnkm/PortScanner-WebApp.git
    cd PortScanner-WebApp
    ```
    
2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add your Google Generative AI API key:

    ```env
    API_KEY=your_google_generative_ai_api_key
    ```

4. **Run the Application**

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## Usage

### Web Interface

1. **Open the Web Interface**

    Navigate to `http://127.0.0.1:5000/` in your web browser.

2. **Input Scan Parameters**

    - **Hostname**: Enter the hostname to scan.
    - **Start Port**: Enter the starting port number.
    - **End Port**: Enter the ending port number.
    - **Number of Threads**: Enter the number of threads for scanning.

3. **Submit the Form**

    Click the "Scan Ports" button to start the scan. The results will be displayed on the same page.

## Project Structure

```
port-scanner/
│
├── app.py              # Main Flask application
├── scan.py             # Port scanning logic
├── ai.py               # AI integration for generating reports
├── requirements.txt    # Project dependencies
└── templates/
    └── index.html      # HTML template for the web interface

```

## Contribution

Contributions are welcome! Please fork the repository and create a pull request with your changes.

