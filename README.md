Intelligent Log Analyzer

This Python script is an asynchronous log analyzer designed to intelligently parse log files for errors and provide suggestions for resolving them. It uses the Ollama API with the mistral model to analyze the content of log files and returns insights in real-time.
Features

    Customizable Analysis Prompt: Option to provide a custom message or use the default prompt for log analysis.
    Asynchronous Processing: Runs the log analysis in the background, allowing the user to continue other tasks while waiting for results.
    Streaming Response Handling: Processes and displays the analysis results as they are received from the API.
    Error Handling: Includes error handling for API requests and JSON decoding issues.
    Easy-to-Use Command-Line Interface: Accepts input parameters for the log file path and optional custom prompt message.

Requirements

    Python 3.x
    Dependencies:
        argparse (part of the Python standard library)
        requests
        json
        threading (part of the Python standard library)
    Ollama API:
        The script assumes an Ollama API server is running locally on port 11434. Update the endpoint URL if necessary.

Installation

    Clone the repository:

git clone https://github.com/yourusername/intelligent-log-analyzer.git
cd intelligent-log-analyzer

Install the required Python libraries:

    pip install requests

Usage

Run the script from the command line:

python log_analyzer.py <file> [--message "Custom prompt message"]

Parameters:

    <file>: Path to the log file to be analyzed.
    --message: (Optional) A custom message to include in the prompt sent to the API.

How It Works

    Prompt Preparation:
        The script reads the content of the provided log file.
        A default prompt message is used unless overridden by the user with the --message flag.

    API Request:
        Sends the log content and prompt to the Ollama API endpoint using a POST request.
        The response is streamed, allowing real-time output.

    Asynchronous Analysis:
        The API request and response handling occur in a separate thread, freeing up the main program for other tasks.

    Streaming Output:
        The script decodes each line of the API’s streaming response and prints it in real-time.

    Error Handling:
        Handles common errors, including file reading issues, API request failures, and JSON decoding errors.

Example
Default Prompt

python log_analyzer.py /path/to/logfile.log

Output:

Request sent. Processing in the background...
Analysis Result:
[API response with error insights and resolution suggestions]

Custom Prompt

python log_analyzer.py /path/to/logfile.log --message "Look for memory leak issues and suggest solutions."

Output:

Request sent. Processing in the background...
Analysis Result:
[API response focused on memory leak issues]

Limitations

    Local Dependency: Requires the Ollama API server to be running locally.
    Real-Time Output: The user must wait for the response to be streamed for a complete analysis.

License

This project is licensed under the MIT License.
