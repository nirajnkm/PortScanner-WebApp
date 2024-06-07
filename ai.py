import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os


def generate_chat_response(port):
    genai.configure(api_key=os.getenv("API_KEY"))
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    message = f"""**Input:** A list of open ports {port} discovered on a system (e.g., 22, 80, 443).

**System Instructions:**

1. **Respond in the following format:**
    - Title: Open Port Security Risks (List of ports)
    - For each port in the input list:
        - Subheading: Port {port}
        - Description: Briefly explain the purpose of the port and its associated service. 
        - Security Risk: Describe the potential security vulnerabilities associated with an open port, including real-world examples of exploits (if applicable).
        - Mitigation: Provide clear and concise best practices for mitigating the security risks associated with the open port.
2. **Prioritize clarity and conciseness.**
3. **Avoid technical jargon whenever possible.**

**Example:**

**Input:** 22, 80, 443

**Output:**

**Title:** Open Port Security Risks (22, 80, 443)

**Body:**

* **Port 22:**
    * Description: This port is commonly used for Secure Shell (SSH) connections, allowing remote access to the system.
    * Security Risk: An open SSH port can be targeted by brute-force attacks, where attackers attempt to guess login credentials. Hackers can exploit vulnerabilities in SSH servers to gain unauthorized access to the system. 
    * Mitigation: Use strong passwords for SSH logins and enable two-factor authentication for added security. Consider restricting SSH access to specific IP addresses. 
* **Port 80:**
    * Description: This port is used for standard HTTP traffic, which is the foundation of web browsing.
    * Security Risk: An open port 80 can be exploited to inject malicious code into websites (https://en.wikipedia.org/wiki/Cross-site_scripting), steal user data, or redirect traffic to phishing sites. 
    * Mitigation: If you are not hosting a website, consider disabling port 80. For web servers, ensure they are kept up to date with the latest security patches. 
* **Port 443:**
    * Description: This port is used for HTTPS, which is the secure version of HTTP and encrypts communication between the web browser and the server.
    * Security Risk: While HTTPS mitigates many risks, a misconfigured server or outdated SSL certificate can still be vulnerable to interception attacks. 
    * Mitigation: Use strong encryption algorithms like TLS 1.3 on your web server and keep the server software updated."""
    convo.send_message(message)
    return convo.last.text

if __name__ == "__main__":
    response = generate_chat_response(open_port)
    print(response)