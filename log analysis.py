import argparse
import requests
import json
import threading

def analyze_log_async(file_path, custom_message=None):
    # Default prompt message
    default_message = "Hi please, take a look at this log content and find error lines if any. If possible, give some clues on how to resolve these issues."
    prompt_message = custom_message if custom_message else default_message

    # Read the log file
    with open(file_path, 'r') as file:
        log_content = file.read()

    # Prepare the data to be sent to the Ollama API
    payload = {
        "model": "mistral",
        "prompt": f"{log_content} \n\n {prompt_message}"
    }

    def analyze_in_background(payload):
        try:
            # Send the content to Ollama API and handle streaming response
            response = requests.post(
                "http://localhost:11434/api/generate",  # Ollama API endpoint
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                stream=True
            )

            # Check if the request was successful
            if response.status_code == 200:
                print("Analysis Result:")
                for line in response.iter_lines():
                    if line:
                        try:
                            decoded_line = line.decode('utf-8')
                            json_response = json.loads(decoded_line)
                            print(json_response.get("response", ""), end='', flush=True)
                            if json_response.get("done"):
                                break
                        except json.JSONDecodeError as e:
                            print(f"\nError decoding JSON: {e}")
                print()  # Ensure the final output ends with a newline
            else:
                print(f"Failed to analyze log file. Status code: {response.status_code}")
                print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error during the request: {e}")

    # Start the analysis in a separate thread
    thread = threading.Thread(target=analyze_in_background, args=(payload,))
    thread.start()
    print("Request sent. Processing in the background...")

def main():
    parser = argparse.ArgumentParser(description="Intelligent Log Analyzer")
    parser.add_argument('file', type=str, help='Path to the log file')
    parser.add_argument('--message', type=str, help='Custom message to include in the prompt', default=None)

    args = parser.parse_args()
    analyze_log_async(args.file, args.message)

if __name__ == "__main__":
    main()
