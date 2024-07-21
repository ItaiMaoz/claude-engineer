# Project Overview: Claude-3-Sonnet Engineer Chat

## Main Components

### 1. main.py

This file contains the core implementation of the chatbot system using the Claude-3-Sonnet model. Key features include:

- **Libraries and Initializations**:
  - Uses libraries like `anthropic`, `tavily`, `PIL`, and `rich` for various functionalities.
  - Initializes Anthropic and Tavily clients for AI and search capabilities.

- **Constants**:
  - `CONTINUATION_EXIT_PHRASE`: "AUTOMODE_COMPLETE"
  - `MAX_CONTINUATION_ITERATIONS`: 25
  - Models: MAINMODEL and TOOLCHECKERMODEL (both set to "claude-3-5-sonnet-20240620")

- **Core Functions**:
  - `update_system_prompt`: Dynamically updates the system prompt based on the current mode.
  - `chat_with_claude`: Handles the main conversation logic with the AI model.
  - `execute_tool`: Manages the execution of various tools available to the AI.

- **File Operations**:
  - Functions for creating folders and files, reading, editing, and listing files.

- **Image Processing**:
  - `encode_image_to_base64`: Prepares images for AI analysis.

- **Automode Feature**:
  - Allows for autonomous operation based on user-defined goals.
  - Implements iteration tracking and goal execution.

- **Main Loop**:
  - Handles user input, including special commands for image input and automode activation.

### 2. prompts.py

This file defines the system prompts used to guide the AI's behavior:

- **BASE_SYSTEM_PROMPT**:
  - Outlines the AI's capabilities in software development.
  - Lists available tools and their use cases.
  - Provides guidelines for tool usage, error handling, and best practices.

- **AUTOMODE_SYSTEM_PROMPT**:
  - Specific instructions for automode operation.
  - Covers goal setting, execution, progress tracking, and completion criteria.

## Key Features

1. **Multi-tool Integration**: The system incorporates various tools for file manipulation, web searches, and more.
2. **Image Analysis**: Capability to process and analyze images provided by the user.
3. **Automode**: Allows for semi-autonomous operation based on user-defined goals.
4. **Dynamic Prompt Updates**: The system prompt adapts based on the current mode and iteration.
5. **Error Handling**: Implements strategies for dealing with API errors and tool execution failures.
6. **Rich Console Output**: Uses the `rich` library for enhanced console display, including syntax highlighting for diffs.

## Technical Details

- **AI Model**: Uses Claude-3-Sonnet (version 20240620) for both main interactions and tool checking.
- **API Integrations**: Anthropic API for AI capabilities, Tavily API for web searches.
- **File Editing**: Implements a diff-based approach for file modifications, showing changes clearly.
- **Conversation Management**: Maintains a conversation history for context in ongoing interactions.

## Usage Notes

- The system supports both interactive chat mode and an automode for more autonomous operations.
- Users can input images for analysis by typing 'image' and providing the image path.
- Automode can be activated with a specified number of iterations.
- The system is designed to handle a wide range of software development tasks, from project structure creation to code writing and debugging.

This overview provides a comprehensive understanding of the current state of the project, its capabilities, and key components. It can be referred to quickly get up to speed on the progress made so far.