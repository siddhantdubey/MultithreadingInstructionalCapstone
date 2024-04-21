import random
import time
from faker import Faker

faker = Faker()

# List of sample user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
]

# HTTP methods and URLs
methods = ["GET", "POST"]
urls = ["/home", "/about", "/contact", "/login", "/register", "/products", "/api/data", "/api/status"]

# HTTP response codes
response_codes = [200, 404, 500, 302]

def generate_log_entry():
    ip = faker.ipv4()
    user_agent = random.choice(user_agents)
    method = random.choice(methods)
    url = random.choice(urls)
    response_code = random.choice(response_codes)
    timestamp = faker.date_time_this_year().strftime("%d/%b/%Y:%H:%M:%S +0000")
    
    log_entry = f'{ip} - - [{timestamp}] "{method} {url} HTTP/1.1" {response_code} {random.randint(200, 5000)} "{faker.url()}" "{user_agent}"'
    return log_entry

def generate_log_file(filename, entries_count):
    with open(filename, "w") as file:
        for _ in range(entries_count):
            log_entry = generate_log_entry()
            file.write(log_entry + "\n")

# Example usage: Generate a log file with 10000 entries
# To really have a big log file, you'll need about 10 million entries
generate_log_file("web_server_logs.txt", 10000)
