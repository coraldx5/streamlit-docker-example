#!/bin/bash
export PYTHONPATH="${PYTHONPATH}:$(dirname "$0")" 
python src/create_yml.py
streamlit run src/st_main.py --server.port 5000
