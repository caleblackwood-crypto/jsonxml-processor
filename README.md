# JSON / XML Data Processor
Convert a structured XML ticket export into JSON, with required-field and priority validation.

```bash
python processor.py sample.xml output.json
python -m pytest -q
```
Uses Python standard library. Never process untrusted large XML files without additional XML security and size limits.
