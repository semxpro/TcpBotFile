# locked file — do not edit
import base64, zlib, lzma, gzip, time, sys, datetime
import traceback
import os
import json

# ড্যাশবোর্ডের Environment Variables থেকে UID এবং Password স্বয়ংক্রিয়ভাবে uid-pass-svr.json ফাইলে লেখার কোড
try:
    _env_data = {
        "uid": os.getenv('FF_UID', ''),
        "pass": os.getenv('FF_PASSWORD', ''),
        "region": os.getenv('FF_REGION', 'BD')
    }
    with open('uid-pass-svr.json', 'w') as _f:
        json.dump(_env_data, _f, indent=4)
except Exception as _e:
    print(f"⚠️ Failed to write env vars to uid-pass-svr.json: {_e}")

try:
    import faulthandler; faulthandler.enable()
except Exception:
    pass

PAYLOAD    = "==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"
EXPIRE_TS  = 1794162600.0
EXPIRE_STR = "2026-11-09 00:00:00"

# --- expiry check ---
_now = time.time()
if _now > EXPIRE_TS:
    print("=" * 50)
    print("❌ This file has EXPIRED.")
    print(f"   Expired at : {EXPIRE_STR}")
    print(f"   Current    : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    sys.exit(1)

_remaining = int(EXPIRE_TS - _now)
_h, _rem = divmod(_remaining, 3600)
_m, _s = divmod(_rem, 60)
print(f"⏳ Time remaining: {_h}h {_m}m {_s}s")

# --- decode source (portable across Python versions) ---
try:
    _z = base64.b64decode(PAYLOAD[::-1])
    _l = zlib.decompress(_z)
    _g = lzma.decompress(_l)
    _src = gzip.decompress(_g)
except Exception as e:
    print(f"❌ Failed to decode payload: {e}")
    sys.exit(3)

# --- execute ---
_globals = {"__name__": "__main__", "__file__": "easy.py"}
try:
    exec(compile(_src, "easy.py", "exec"), _globals)
except SystemExit:
    raise
except Exception:
    traceback.print_exc()
    sys.exit(4)
