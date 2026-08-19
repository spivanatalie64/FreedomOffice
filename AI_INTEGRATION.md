# FreedomAI — AI Integration Guide

FreedomOffice comes with **FreedomAI**, a built-in AI assistant powered by [opencode](https://opencode.ai). This document explains how it works, how to configure it, and how to keep everything 100% private and local.

---

## How FreedomAI Works

FreedomAI is an opencode agent that integrates directly into the FreedomOffice development workflow. When you invoke `@FreedomAI`, opencode routes your request to a configured LLM (local or cloud) and returns results inline.

```
You → @FreedomAI "write a memo about Q3 budget"
        → opencode sends prompt to local/cloud model
        → model generates document content
        → opencode returns result
        → paste into your document
```

## Configuration

FreedomAI is configured in `.opencode/opencode.json`. The default setup is configured to use a **100% local Ollama instance** (`ollama/llama3.2`), keeping all AI document generation entirely on your machine.

### Using Local LLMs (100% Private, No Internet Needed)

FreedomOffice fully supports local AI. You don't need to send data to anyone.

#### Option 1: Ollama (Recommended)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model (run this once)
ollama pull llama3.2
ollama pull mistral
ollama pull phi4

# Verify it's running
ollama serve
```

Then update `.opencode/opencode.json`:

```json
{
  "agent": {
    "FreedomAI": {
      "model": "ollama/llama3.2",
      "mode": "all",
      "description": "FreedomOffice's built-in AI assistant (local)"
    }
  }
}
```

#### Option 2: llama.cpp

```bash
# Clone and build
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make

# Download a model (GGUF format)
wget https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf

# Start the server
./server -m Llama-3.2-3B-Instruct-Q4_K_M.gguf

# Configure opencode
# model: "openai/http://localhost:8080/v1"
```

#### Option 3: Hugging Face Transformers

```bash
pip install transformers torch accelerate
# Use the huggingface provider in opencode
```

### Using Cloud AI Providers

If you prefer cloud models, opencode supports:

| Provider       | Model string                          |
|----------------|---------------------------------------|
| Anthropic      | `anthropic/claude-sonnet-4-6`         |
| OpenAI         | `openai/gpt-4o`                       |
| Google Gemini  | `google/gemini-2.0-flash`            |
| Groq           | `groq/llama3-70b-8192`               |
| Together       | `together/mistralai/Mixtral-8x22B`   |

Set your API key in your shell or `~/.opencode/auth.json`:

```bash
export ANTHROPIC_API_KEY=sk-...
```

## Privacy

**All AI processing can be 100% local.** No data ever leaves your machine when using:

- **Ollama** — runs entirely on localhost
- **llama.cpp** — local inference, no telemetry
- **Hugging Face transformers** — fully offline

This is critical for:
- Confidential documents
- Offline/air-gapped environments
- Compliance with data protection regulations (GDPR, HIPAA, etc.)

> FreedomOffice will never phone home. The AI you use is *your* choice.

## FOSS AI Stack

| Component       | Tool                            | License      |
|-----------------|---------------------------------|--------------|
| Runtime         | Ollama / llama.cpp              | MIT          |
| Models          | Llama, Mistral, Gemma, Phi      | Various OSS  |
| Embeddings      | sentence-transformers           | Apache 2.0   |
| Tokenizers      | Hugging Face tokenizers         | Apache 2.0   |
| Vector Search   | Chroma / FAISS                  | Apache 2.0   |
| Framework       | opencode                        | Apache 2.0   |

## Commands for Common AI Tasks

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# List available models
ollama list

# Pull a new model
ollama pull llama3.2:3b

# Test a model directly
ollama run llama3.2 "summarize: AI in open source office suites"

# Run llama.cpp server
./llama.cpp/server -m model.gguf --port 8080

# Run a local embedding model for RAG
ollama pull nomic-embed-text
```

## Integration with the Ribbon UI

FreedomOffice's Ribbon UI will include a **"FreedomAI" tab** that provides:

- **AI Write** — generate document content from a prompt
- **AI Analyze** — analyze selected spreadsheet data
- **AI Summarize** — summarize the current document
- **AI Translate** — translate selected text
- **AI Formula** — generate spreadsheet formulas from natural language
- **AI Present** — generate slide content from an outline

Each button calls opencode in the background with `@FreedomAI` and inserts the result into the active document.

### Example: AI Write Button

When a user clicks **AI Write** in the Ribbon:

1. A dialog asks for a prompt (e.g. "write a cover letter for a software engineer position")
2. FreedomOffice calls: `@FreedomAI write a cover letter for a software engineer position`
3. opencode returns the generated text
4. The text is inserted at the cursor position in the document

## Getting Started

```bash
# 1. Install opencode
npm install -g @opencode/cli

# 2. Navigate to FreedomOffice
cd FreedomOffice/freedomoffice-core-github

# 3. Open the project with opencode
opencode .

# 4. Invoke FreedomAI
@FreedomAI "help me write a business letter"
```

---

*FreedomAI — your privacy-respecting AI copilot for FreedomOffice.*
