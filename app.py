import os
import logging
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ArticleProcessor:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("OpenAI API key is missing.")
        self.client = OpenAI(api_key=api_key)

    def read_article(self, file_path):
        """
        Reads the content of the input file.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist.")

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Input file is empty.")
            return content

    def process_with_ai(self, article_content):
        """
        Sends the article content to OpenAI API for HTML generation.
        """
        prompt = f"""
        Transform the following article into HTML with the following requirements:
        1. Use appropriate HTML tags for structuring content (e.g., h1, h2, p, article, section).
        2. Identify at least one place in each section for an image:
           - Add <img> tags with:
             - src="image_placeholder.jpg"
             - alt attribute containing a detailed prompt for image generation
             - a caption using the <figcaption> tag
        3. Do not include CSS or JavaScript code.
        4. Do not add html, head, or body tags - only include content to place between <body> tags.

        Here is the article to transform:

        {article_content}
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert in converting text into semantic HTML code."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"Error during OpenAI API call: {e}")
            raise RuntimeError("Failed to process the article with AI.") from e

    def save_html(self, html_content, output_file):
        """
        Saves the generated HTML content to a file.
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(html_content)
        except Exception as e:
            logging.error(f"Error saving HTML file: {e}")
            raise RuntimeError("Failed to save the generated HTML content.") from e


def main():
    """
    Main execution flow for the script.
    """
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("Missing OpenAI API key. Set it in the .env file.")

        processor = ArticleProcessor(api_key)

        input_file = Path("article.txt")
        output_file = Path("article.html")

        article_content = processor.read_article(input_file)
        html_content = processor.process_with_ai(article_content)
        processor.save_html(html_content, output_file)

        print(f"Success! Generated HTML saved to {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        logging.error(e)
    except ValueError as e:
        print(f"Error: {e}")
        logging.error(e)
    except RuntimeError as e:
        print(f"Error: {e}")
        logging.error(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
