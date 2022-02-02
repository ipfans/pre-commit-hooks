#!/usr/bin/env bash

MERGE_MSG=$(grep -E "^Merge branch*" "$1")

if [ "$MERGE_MSG" != "" ]; then
    exit 0
fi

COMMIT_MSG=$(grep -E "^(fix|feat|build|chore|ci|docs|style|refactor|perf|test|misc)(\(\w+\))?\!?:\s(.*)$" "$1")

if [ "$COMMIT_MSG" = "" ]; then
    echo "Commit message should be structured as Conventional Commits spec."
    exit 1
fi

if [ ${#COMMIT_MSG} -lt 15 ]; then
    echo "Please make sure add readable meaning to commit message."
    exit 1
fi
