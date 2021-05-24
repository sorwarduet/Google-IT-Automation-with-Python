#!/bin/bash

for file in *.HIM; do
    name=$(basename "$file" .HIM)
    mv "$file" "name.html"
done