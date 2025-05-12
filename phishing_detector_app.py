import openai
import gradio as gr

# Set API key (store securely in environment variables!)
openai.api_key = "OPEN_API_KEY"

def detect_phishing(email_text):
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert. Detect phishing indicators in this email, Respond with Yes or No."},
            {"role": "user", "content": f"Email text:\n{email_text}\n\nIs this a phishing attempt? Explain why."}
        ],
        temperature=0.3  # Less creative, more factual
    )
    return response.choices[0].message.content

# Gradio interface
interface = gr.Interface(
    fn=detect_phishing,
    inputs=gr.Textbox(lines=10, placeholder="Paste email text here..."),
    outputs=gr.Textbox(label="Analysis"),
    examples=[
        ["Urgent! Your account will be suspended. Click here: http://malicious.link"],
        ["Hi Team, please review the attached report. Regards, IT Dept."]
    ],
    title="AI Phishing Detector 🛡️"
)

interface.launch()
