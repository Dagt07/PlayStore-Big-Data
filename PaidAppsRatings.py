from __future__ import print_function

import sys
from pyspark.sql import SparkSession

# Columns of the CSV file
# App Name,App Id,Category,Rating,Rating Count,Installs,Minimum Installs,Maximum Installs,Free,Price,Currency,
# Size,Minimum Android,Developer Id,Developer Website,Developer Email,Released,Last Updated,Content Rating,
# Privacy Policy,Ad Supported,In App Purchases,Editors Choice,Scraped Time

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: PaidAppsRatings.py <filein> <fileout>", file=sys.stderr)
        sys.exit(-1)

    filein = sys.argv[1]
    fileout = sys.argv[2]
    
    # Example:
    # in pyspark shell start with:
    #   filein = "hdfs://cm:9000/uhadoop/shared/imdb/imdb-ratings-two.tsv"
    #   fileout = "hdfs://cm:9000/uhadoop2023/<user>/series-avg-two-py/"
    # and continue line-by-line from here

    spark = SparkSession.builder.appName("PaidAppsRatings").getOrCreate()

    input = spark.read.text(filein).rdd.map(lambda r: r[0])
    # to dump an RDD like input to the pyspark shell, use
    #   input.collect()
    # make sure not to do this for a large RDD

    lines = input.map(lambda line: line.split(","))

    # Here we filter the lines to only include those that have a valid App Name and Rating and are marked as not free
    paidApps = lines.filter(lambda line: not (line[0] == 'null') and not (line[3] == 'null') and not line[8])

    # We create a new RDD where each element is a tuple of (App Name, Rating, Rating Count, Free)
    PaidAppsRating = paidApps.map(lambda line: (line[0], line[3], line[4], line[8]))

    PaidAppsRating.saveAsTextFile(fileout)

    spark.stop()