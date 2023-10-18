
def count_batteries_by_health(present_capacities):
    rated_capacity = 120
    healthy = exchange = failed = 0

    for capacity in present_capacities:
        soh = (capacity / rated_capacity) * 100

        if soh > 80:
            healthy += 1
        elif 63 <= soh <= 80:
            exchange += 1
        else:
            failed += 1

    return {"healthy": healthy, "exchange": exchange, "failed": failed}

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :)")

if __name__ == '__main':
    test_bucketing_by_health()
