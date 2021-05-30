#!/bin/bash

echo "Le nom du fichier est: $1"

gcc "$1.c" -o "$1"

./$1
