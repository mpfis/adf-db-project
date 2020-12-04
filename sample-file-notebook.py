# Databricks notebook source
dbutils.widgets.text("param1", "","")

# COMMAND ----------

print("hello!")
print("more changes")

# COMMAND ----------

dbutils.notebook.exit(dbutils.widgets.get("param1"))

# COMMAND ----------

