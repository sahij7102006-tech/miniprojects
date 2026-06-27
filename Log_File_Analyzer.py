#Log File Analyzer — Reads a server log file, uses regex to extract error codes, timestamps, and IPs; generator to process line-by-line for large files; summary report saved to output file.by using Inheritance, polymorphism, decorators, regex, generators in python
import re
from collections import Counter

# Decorator for logging analysis
def analysis_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.\n")
        return result
    return wrapper


# Base Class
class LogAnalyzer:

    def __init__(self, filename):
        self.filename = filename

    # Generator: Read file line by line
    def read_logs(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print("Log file not found.")

    def analyze(self):
        pass


# Child Class (Polymorphism)
class ServerLogAnalyzer(LogAnalyzer):

    @analysis_logger
    def analyze(self):

        ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
        error_pattern = r"ERROR\s*(\d+)"
        timestamp_pattern = (
            r"\d{4}-\d{2}-\d{2}\s"
            r"\d{2}:\d{2}:\d{2}"
        )

        ips = []
        error_codes = []
        timestamps = []

        # Generator processing
        for line in self.read_logs():

            ip = re.search(ip_pattern, line)
            error = re.search(error_pattern, line)
            timestamp = re.search(timestamp_pattern, line)

            if ip:
                ips.append(ip.group())

            if error:
                error_codes.append(error.group(1))

            if timestamp:
                timestamps.append(timestamp.group())

        return {
            "ips": ips,
            "errors": error_codes,
            "timestamps": timestamps
        }


# Report Generator
class ReportManager:

    @analysis_logger
    def save_report(self, data, output_file):

        error_summary = Counter(data["errors"])
        ip_summary = Counter(data["ips"])

        with open(output_file, "w") as file:

            file.write("===== LOG ANALYSIS REPORT =====\n\n")

            file.write("Total Log Entries: ")
            file.write(str(len(data["timestamps"])))
            file.write("\n\n")

            file.write("Error Code Summary:\n")
            for code, count in error_summary.items():
                file.write(
                    f"ERROR {code}: {count} occurrence(s)\n"
                )

            file.write("\nTop IP Addresses:\n")
            for ip, count in ip_summary.items():
                file.write(
                    f"{ip}: {count} request(s)\n"
                )

            file.write("\nTimestamps:\n")
            for ts in data["timestamps"]:
                file.write(ts + "\n")

        print("Report saved to", output_file)


# Main Program
log_file = "server.log"
output_file = "report.txt"

analyzer = ServerLogAnalyzer(log_file)
report_manager = ReportManager()

data = analyzer.analyze()

if data:
    report_manager.save_report(data, output_file)
