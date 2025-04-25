# Use Python 3.12 slim base
FROM python:3.12-slim

# Create a non-root user
RUN useradd -ms /bin/bash gameuser

# Set working directory
WORKDIR /app

# Install required system dependencies for pygame, X11, and PulseAudio
RUN apt-get update && apt-get install -y \
    xvfb \
    libx11-dev \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libsmpeg-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# Copy project files into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set environment variables for X11 and PulseAudio
ENV DISPLAY=:99
ENV XDG_RUNTIME_DIR=/tmp/runtime-$USER

# Switch to the non-root user
USER gameuser

# Start PulseAudio and Xvfb, then run the game
CMD ["sh", "-c", "pulseaudio --start && Xvfb :99 -screen 0 800x600x16 & python src/main.py"]