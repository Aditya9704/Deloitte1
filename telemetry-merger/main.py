import json
from datetime import datetime

def iso_to_millis(iso_str):
    dt = datetime.fromisoformat(iso_str)
    return int(dt.timestamp() * 1000)

def unify_telemetry(data1, data2):
    result = []

    for entry in data1:
        unified_entry = {
            "device_id": entry["device_id"],
            "telemetry": []
        }
        for reading in entry["telemetry"]:
            unified_entry["telemetry"].append({
                "timestamp": iso_to_millis(reading["timestamp"]),
                "value": reading["value"]
            })
        result.append(unified_entry)

    for entry in data2:
        unified_entry = {
            "device_id": entry["device_id"],
            "telemetry": entry["telemetry"]
        }
        result.append(unified_entry)

    return result

def main():
    with open('data-1.json', 'r') as f:
        data1 = json.load(f)

    with open('data-2.json', 'r') as f:
        data2 = json.load(f)

    unified_data = unify_telemetry(data1, data2)

  
    with open('output.json', 'w') as f:
        json.dump(unified_data, f, indent=2)

    print("Unified telemetry written to output.json")

if __name__ == '__main__':
    main()
