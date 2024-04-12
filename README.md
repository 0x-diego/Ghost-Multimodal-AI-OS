# GHOST: A Multimodal AI OS

## Introduction
**GHOST** is an operating system that integrates multimodal AI models to allow user interaction with Linux systems through local processing. The project aims to bring advanced AI capabilities directly to your computer, providing a intuitive way to control your system with various input modalities including voice, text, and image recognition.

## Features
- **Voice Commands:** Execute system commands via voice inputs.
- **File manipulation:** Read and write files using text or voice messages.
- **Text Analysis:** Read kernel messages, files content, commands output, etc..
- **Local Processing:** No internet required. Privacy enhaced.

**more is coming soon.**


## Installation

### Prerequisites
- A Linux-based system
- Conda package manager (Miniconda or Anaconda)

### Setup
Clone the repository and set up the Conda environment:
```bash
git clone https://github.com/0x-diego/Ghost-Multimodal-AI-OS
cd Ghost-Multimodal-AI-OS

# Create the Conda environment
conda env create -f environment.yaml

# Activate the environment
conda activate ghost-env
```

## Usage

Start the server by running:
```bash
python3 ghost
```
Ghost use a HTTP Server (flask). You can send a post request to the "inference" route.

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"prompt":"Create a file with a hello world message."}' \
  http://localhost:5000/inference

```

## Current state
GHOST development is currently paused as my GPU can only run a 2.7 billion parameters model (like phi2) which is not powerful enough xd.
this will change in the near future. 

## Contributing
If you would like to contribute to GHOST, please fork the repository and submit a pull request. 
