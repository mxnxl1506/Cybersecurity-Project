import re

def is_sql_injection_attack(request):
    """Check if a SQL injection attack is detected in the HTTP request."""
    sql_injection_patterns = [
        r';\s*(?:--|#|{--|;|/*|--!|/*!|#|//|--\|||||%|#0|%%|@)',  # SQL comment sequences
        r'(\b(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|TRUNCATE|RENAME|CALL|EXEC|INTO|FROM|WHERE|AND|OR|UNION|ORDER BY|GROUP BY|LOAD_FILE|OUTFILE|DUMPFILE)\b)'  # SQL keywords
    ]
    for pattern in sql_injection_patterns:
        if re.search(pattern, request, re.IGNORECASE):
            return True
    return False

def is_xss_attack(request):
    """Check if a Cross-Site Scripting (XSS) attack is detected in the HTTP request."""
    xss_patterns = [
        r'<\s*script\s*>|<\s*alert\s*\(|<\s*img\s*src\s*='  # XSS attack patterns
    ]
    for pattern in xss_patterns:
        if re.search(pattern, request, re.IGNORECASE):
            return True
    return False

# Example usage:
if __name__ == "__main__":
    # Simulated HTTP request (can be replaced with actual request handling logic)
    http_request = "SELECT * FROM users WHERE username = 'admin'; --"

    # Check for SQL injection attack
    if is_sql_injection_attack(http_request):
        print("Potential SQL Injection Attack Detected!")

    # Check for XSS attack
    if is_xss_attack(http_request):
        print("Potential Cross-Site Scripting (XSS) Attack Detected!")
