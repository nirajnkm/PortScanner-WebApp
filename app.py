from flask import Flask, request, render_template
import socket
from ai import generate_chat_response
from scan import get_open_ports
import markdown

app = Flask(__name__)

def resolve_dns(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"Resolved IP for {hostname}: {ip}")  # Debug anchor
        return ip
    except socket.gaierror:
        print(f"Failed to resolve IP for {hostname}")  # Debug anchor
        return None

def process_open_ports(ip, start, end, threads):
    print("Scanning open ports...")  # Debug anchor
    open_ports = get_open_ports(ip, start, end, threads)
    print(f"Open ports found: {open_ports}")  # Debug anchor
    response = generate_chat_response(open_ports)
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hostname = request.form['hostname']
        print(f"Received hostname: {hostname}")  # Debug anchor
        ip = resolve_dns(hostname)
        if ip:
            start = int(request.form['start'])
            end = int(request.form['end'])
            threads = int(request.form['threads'])
            result = process_open_ports(ip, start, end, threads)
        # Convert result to Markdown format
            result_markdown = markdown.markdown(result)
            return render_template('index.html', result=result_markdown,hostname=hostname)
        else:
            return render_template('index.html', result="Invalid hostname")
    return render_template('index.html', result=None)
