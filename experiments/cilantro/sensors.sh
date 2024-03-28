#!/bin/bash

mkdir -p /users/$(whoami)/sensors
sensors -j > "/users/$(whoami)/sensors/sensors.$(date +%m%d%Y%H%M%S)".json
