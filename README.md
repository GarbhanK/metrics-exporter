# metrics-exporter
rasperry pi metrics exporter

## Export to CSV
- run `sqlite3` and open the system metrics db

```
.mode column
.mode csv

.output name_of_output_file.csv

select * from cpu;
```

## TODOs
- export to cloud DB service instead of save locally
- export more metrics e.g `psutil.net_io_counters()`
- set up terraform for managing cloud resources

