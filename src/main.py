def bake_cookies_updated(batch_size, max_batches=None):
    total_cookies = 0
    batch_count = 0

    # While loop with max_batches as None (makes it infinite)
    while max_batches is None or batch_count < max_batches:
        total_cookies += batch_size
        yield total_cookies
        batch_count += 1

# Step 2: Create a generator object with no limit
unlimited_cookie_batches_updated = bake_cookies_updated(batch_size=5, max_batches=None)

# Step 3: Use next() to retrieve batches of cookies (no limit imposed)
print(f"Batch 1: {next(unlimited_cookie_batches_updated)} cookies")
print(f"Batch 2: {next(unlimited_cookie_batches_updated)} cookies")
print(f"Batch 3: {next(unlimited_cookie_batches_updated)} cookies")
print(f"Batch 4: {next(unlimited_cookie_batches_updated)} cookies")

# Expected output:
# Batch 1: 5 cookies
# Batch 2: 10 cookies
# Batch 3: 15 cookies
# Batch 4: 20 cookies