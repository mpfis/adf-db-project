# Databricks notebook source
dbutils.widgets.text("param1", "","")

# COMMAND ----------

print("hello!")

# COMMAND ----------

dbutils.notebook.exit(dbutils.widgets.get("param1"))

# COMMAND ----------

