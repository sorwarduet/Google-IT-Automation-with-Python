#!/bin/bash

if grep "127.0.0.0" /etc/hosts; then
  echo "Everything Ok"
else
  echo "127.0.0.0 is not in /etc/hosts"
fi