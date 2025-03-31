import subprocess
import re
import csv
import matplotlib.pyplot as plt

services = {
    "Django": "http://localhost:8000/users",
    "FastAPI": "http://localhost:8001/users",
    "Robyn": "http://localhost:8002/users"
}

results = []

def run_wrk(service_name, url):
    print(f"\n▶ Benchmarking {service_name}")
    result = subprocess.run(
        ["wrk", "-t4", "-c100", "-d10s", url],
        capture_output=True, text=True
    ).stdout

    match = re.search(r"Requests/sec:\s+([\d\.]+)", result)
    rps = float(match.group(1)) if match else 0.0

    print(f"🔹 {service_name}: {rps:.2f} RPS")
    results.append({"service": service_name, "rps": rps})

def write_csv():
    with open("benchmark_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["service", "rps"])
        writer.writeheader()
        writer.writerows(results)
    print("✅ benchmark_results.csv yazıldı.")

def plot_graph():
    labels = [r["service"] for r in results]
    values = [r["rps"] for r in results]

    plt.bar(labels, values)
    plt.title("Benchmark RPS Karşılaştırması")
    plt.ylabel("Requests per Second (RPS)")
    plt.savefig("benchmark_results.png")
    print("📊 benchmark_results.png oluşturuldu.")

if __name__ == "__main__":
    for name, url in services.items():
        run_wrk(name, url)

    write_csv()
    plot_graph()
