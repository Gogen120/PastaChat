#!/usr/bin/env bash
#
# Удаляет рекурсивно в всех папках __pycache__ фолдеры и *.pyc/*.pyo файлы
#


find . -regex '.*\(__pycache__\|\.py[co]\)' -delete
