Data sources
============

`brain.nii.gz` is my T1. I was scanned at the Martinos Center at MGH, somehow I acquired it :)

`bet brain.nii.gz brain_stripped.nii.gz -f .6` to produce the skull-stripped image.

fast -n 3 -t 1 brain_stripped.nii.gz` to segment the skull-stripped image.

I happened to find a DTI scan.