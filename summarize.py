from transformers import pipeline

# Load Hugging Face summarization pipeline once
summarizer = pipeline("summarization")

# Define a mapping of user-friendly summary lengths to max_length values
length_settings = {
    "light": (30, 10),
    "small": (60, 20),
    "medium": (120, 30),
    "large": (200, 50)
}

def summarize_text(text, length="medium"):
    if not text.strip():
        return "⚠️ No input text provided."

    # Use length setting, fallback to medium
    max_len, min_len = length_settings.get(length, (120, 30))

    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']
