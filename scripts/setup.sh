#!/bin/bash
set -euo pipefail
echo "Setting up Log Analysis Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
