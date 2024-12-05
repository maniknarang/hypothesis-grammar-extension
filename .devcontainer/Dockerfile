FROM ubuntu:22.04

# Update and install necessary dependencies
RUN apt-get update && apt-get install -y \
	python3-pip -y

RUN pip install hypothesis ipytest pytest black duckdb sympy coverage