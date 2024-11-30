
# AI-Powered Article to HTML Converter

This project is an AI-powered application that transforms text articles into semantically structured HTML. The HTML includes placeholders for images with detailed prompts for generation and captions, providing a complete structure for presenting articles on the web.

## Features

- Converts text articles into semantic HTML using OpenAI's API.
- Automatically identifies image placeholders with detailed `alt` attributes and captions.
- Modular, well-documented Python code.
- Error logging for debugging issues.
- Automated setup and execution using `Makefile`.

## Requirements

- Python 3.8 or higher
- OpenAI API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-article-html-converter.git
   cd ai-article-html-converter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key using the Makefile:
   ```bash
   make set-key
   ```

4. Add your input article in the `article.txt` file.

## Usage

- **Run the application:**
  ```bash
  make run
  ```

- **Clean up temporary files:**
  ```bash
  make clean
  ```

## File Structure

```
project-directory/
│
├── Makefile          # Automates key setup, execution, and cleanup
├── app.py            # Main Python application
├── .env              # Environment file containing API key
├── error_log.txt     # Log file for errors
├── requirements.txt  # Python dependencies
└── article.txt       # Input text article
```

## Example Workflow

1. Prepare the input article in `article.txt`.
2. Run the application using `make run`.
3. Find the generated HTML file in `article.html`.

### Example HTML Output:
```html
<section>
  <h2>Artificial Intelligence in Everyday Life</h2>
  <p>AI is revolutionizing how we interact with technology...</p>
  <figure>
    <img src="image_placeholder.jpg" alt="A futuristic robot assisting in a modern kitchen">
    <figcaption>An advanced AI-powered robot helping with daily cooking tasks.</figcaption>
  </figure>
</section>
```

## Error Logging

Any errors during execution are logged in `error_log.txt`. Check this file for details if something goes wrong.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any inquiries or contributions, please open an issue or submit a pull request 👌