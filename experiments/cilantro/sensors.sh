#!/bin/bash

sensors -j > "/tmp/sensors.$(date +%m%d%Y%H%M%S)".json
