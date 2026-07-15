import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_criterion_1_total_requests():
    """Success criterion 1: total_requests counts all non-empty request records."""
    report = load_report()
    assert report["total_requests"] == 6


def test_criterion_2_unique_ips():
    """Success criterion 2: unique_ips counts the distinct client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_criterion_3_top_path():
    """Success criterion 3: top_path is the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"


def test_criterion_4_json_structure():
    """Success criterion 4: report.json is valid JSON with exactly the required keys."""
    report = load_report()
    assert isinstance(report, dict)
    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }
