# Use Python Slim Buster image
FROM python:3.10-slim-buster

LABEL maintainer="bigdeli.ali3@gmail.com"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy project files
COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

# Set working directory
WORKDIR /src

# Install Python dependencies
RUN pip install -r /requirements/development.txt
RUN pip install debugpy

# Expose port
EXPOSE 8000

# Set permissions and create directories (if needed)
# RUN chmod -R +x /scripts && \
#     mkdir -p /vol/web/static /vol/web/media && \
#     adduser --disabled-password --gecos '' djshop && \
#     chown -R djshop:djshop /vol && \
#     chmod -R 755 /vol

# Set environment variable (if needed)
# ENV PATH="/scripts:/usr/local/bin:$PATH"

# Switch to non-root user (if needed)
# USER djshop

# Run the application
CMD ["bash", "/scripts/run.sh"]

