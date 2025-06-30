from __future__ import print_function

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
from pyspark.sql.types import IntegerType, FloatType

# Columns of the CSV file
# App Name,App Id,Category,Rating,Rating Count,Installs,Minimum Installs,Maximum Installs,Free,Price,Currency,
# Size,Minimum Android,Developer Id,Developer Website,Developer Email,Released,Last Updated,Content Rating,
# Privacy Policy,Ad Supported,In App Purchases,Editors Choice,Scraped Time

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: PaidAppsRatings.py <filein> <fileout_topCategories> <fileout_topPaidAppsCategories> <fileout_paidAppsRatings>", file=sys.stderr)
        sys.exit(-1)

    filein = sys.argv[1]
    fileout = sys.argv[2]

    spark = SparkSession.builder.appName("PaidAppsRatings").getOrCreate()

    # Se lee el csv y se convierte a dataframe

    df = spark.read.options(delimiter=",", header=True, inferSchema=False).csv(filein)

    # Se procesa la columna "Installs"

    df = df.withColumn("Installs", regexp_replace(col("Installs"), "[+,]", ""))
    df = df.withColumn("Installs", col("Installs").cast(IntegerType()))

    # ¿Cuáles son las categorías de aplicaciones más populares en la Play Store?

    topApps = df.filter(df.App_Name != 'null')

    TopAppsCategory = topApps.select(topApps.App_Name, topApps.Category, topApps.Installs)

    TopAppsCategory = TopAppsCategory.groupBy("Category").agg({"Installs": "sum"}).withColumnRenamed("sum(Installs)", "Total_Installs")
    TopAppsCategory = TopAppsCategory.orderBy(col("Total_Installs").desc())

    fileout_1 = f"{fileout}/results_1"

    TopAppsCategory.write.option("header", True).option("delimiter", ",").csv(fileout_1)

    # ¿Qué tipo de aplicaciones de pago obtienen más descargas?

    paidApps = df.filter((df.App_Name != 'null') & (df.Rating != 'null') & (df.Free == "False"))

    TopPaidAppsCategory = paidApps.select(paidApps.App_Name, paidApps.Category, paidApps.Installs)

    TopPaidAppsCategory = TopPaidAppsCategory.groupBy("Category").agg({"Installs": "sum"}).withColumnRenamed("sum(Installs)", "Total_Installs")
    TopPaidAppsCategory= TopPaidAppsCategory.orderBy(col("Total_Installs").desc())

    fileout_2 = f"{fileout}/results_2"

    TopPaidAppsCategory.write.option("header", True).option("delimiter", ",").csv(fileout_2)

    # ¿Qué correlación existe entre las calificaciones de las aplicaciones de pago y su cantidad de descargas?

    PaidAppsRating = paidApps.select(paidApps.Rating.cast(FloatType()), paidApps.Installs)

    fileout_3 = f"{fileout}/results_3"

    PaidAppsRating.write.option("header", True).option("delimiter", ",").csv(fileout_3)
    
    spark.stop()