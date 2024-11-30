# Variables
API_KEY_FILE = .env
INPUT_FILE = article.txt
OUTPUT_FILE = article.html

# Define commands
run:
	@echo "Running the application..."
	@python3 app.py

set-key:
	@if [ -z "$(API_KEY)" ]; then \
		read -p "Enter your OpenAI API Key: " API_KEY_INPUT; \
		echo "OPENAI_API_KEY=$$API_KEY_INPUT" > $(API_KEY_FILE); \
		echo "API key saved to $(API_KEY_FILE)."; \
	else \
		echo "API key is already set."; \
	fi

clean:
	@echo "Cleaning up temporary files..."
	@rm -f $(OUTPUT_FILE) $(API_KEY_FILE)
	@echo "Cleanup complete."

help:
	@echo "Available commands:"
	@echo "  make run       - Run the application"
	@echo "  make set-key   - Set the OpenAI API key"
	@echo "  make clean     - Remove generated files and API key"
