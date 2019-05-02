#!/bin/bash
date=`date`
git add .
git commit -m "$date"
git push origin master