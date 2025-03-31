import subprocess
import re
import csv
import matplotlib.pyplot as plt

services = {
    "Django+DjangoORM": "http://localhost:8000/users",
    "Robyn+Pony": "http://localhost:8002/users",
    "FastAPI+SQLAlchemy": "http://localhost:8001/users",
    "Robyn+Tortoise": "http://localhost:8003/users",
    "Go+Gin+pgxpool": "http://localhost:8004/users"
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
    # Set the figure size before creating the plot (width: 12, height: 6)
    plt.figure(figsize=(12, 6))
    
    labels = [r["service"] for r in results]
    values = [r["rps"] for r in results]

    plt.bar(labels, values)
    plt.title("Benchmark RPS Comparison")
    plt.ylabel("Requests per Second (RPS)")
    
    # Rotate labels 45 degrees and adjust their position
    plt.xticks(rotation=45, ha='right')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    plt.savefig("benchmark_results.png", dpi=300)
    print("📊 benchmark_results.png oluşturuldu.")

if __name__ == "__main__":
    for name, url in services.items():
        run_wrk(name, url)

    write_csv()
    plot_graph()
