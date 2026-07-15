Read the Apache-style access log at `/app/access.log` and write a UTF-8 JSON report to `/app/report.json`.

The report must be a JSON object containing exactly the keys `total_requests`, `unique_ips`, and `top_path`.

1. `total_requests` must be the number of non-empty request records in `/app/access.log`.
2. `unique_ips` must be the number of distinct client IP addresses across those request records.
3. `top_path` must be the request path that occurs most frequently.
4. `/app/report.json` must contain valid JSON with exactly the three specified keys and no additional fields.
