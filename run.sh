#!/bin/sh

echo "######################"
echo "###Commit Message : $1"
echo "######################"

git status

echo ""

git add .

echo ""

git commit -m "$1"

echo ""

git push -u origin

echo ""
