FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
        && rm -rf /var/lib/apt/lists/*

        # Copy project files
        COPY pyproject.toml .
        COPY src/ src/

        # Install the package
        RUN pip install --no-cache-dir -e .

        # Create output directory
        RUN mkdir -p output

        # Run the crew
        CMD ["python", "src/cleya_marketing_crew/main.py"]
